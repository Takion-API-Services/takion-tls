import os
import json
import ctypes
import threading
import platform
import requests
from tasks_logger import Logger

from ..models.clients import ClientProfiles

class LibraryManager:
    _instance = None
    _lock = threading.Lock()

    def __init__(self, library_path=None, log_level="INFO"):
        self.logger = Logger(
            level=log_level, 
            formatting="{level}: {message}"
        )
        if library_path is not None:
            self.library_path = library_path
        else:
            self.library_path = "./"
        self.dependency_info = self.load_dependency_info()

    @staticmethod
    def get_machine_details() -> dict:
        system_os = platform.system().lower()
        architecture = platform.machine().lower()
        file_extension = 'dylib' if system_os == 'darwin' else 'dll' if system_os == 'windows' else 'so'
        asset_arch = 'arm64' if architecture == 'arm64' else 'amd64' if architecture in ('amd64', 'x86_64') else 'armv7'
        distro_name = None
        if system_os == 'linux':
            try:
                import distro
                distro_name = distro.id().lower()
                if distro_name in {"ubuntu", "debian"}:
                    system_os += f"-{distro_name}"
            except ImportError:
                pass
        return {
            "system_os": system_os,
            "architecture": asset_arch,
            "file_extension": file_extension,
            "distro": distro_name
        }

    def init_library(self):
        self.logger.debug("Initializing library")
        asset_details = self.load_asset()
        if asset_details:
            self.clients = ClientProfiles(asset_details.get("clients", []))
            asset_name = asset_details.get('filename')
            if not self.is_asset_downloaded(asset_name):
                if not self.download_asset(asset_details):
                    self.logger.debug("Falling back to the most recent locally available version.")
                    asset_details = self.get_most_recent_local_asset_details()
                    asset_name = asset_details.get('filename')
            full_path = os.path.join(self.library_path, "dependencies", asset_name)
            self.library = ctypes.cdll.LoadLibrary(full_path)
            self.set_function_prototypes()
            self.logger.debug("Library initialized successfully")
        else:
            self.logger.error("Failed to load asset details", failed=True)

    def load_asset(self):
        self.logger.debug("Loading asset from server")
        machine_details = self.get_machine_details()
        try:
            response = requests.post("https://tls.takionapi.tech/latest", json=machine_details)
            response.raise_for_status()
            asset_details = response.json()
            self.logger.debug("Asset loaded successfully")
            return {
                "version": asset_details["version"],
                "filename": asset_details["filename"],
                "download": asset_details["download"],
                "clients": asset_details["clients"]
            }
        except requests.RequestException as e:
            self.logger.error(f"Error loading asset: {e}", failed=True)
            return self.get_most_recent_local_asset_details()
    
    def load_dependency_info(self):
        """ Load the local JSON file that contains metadata about downloaded dependencies. """
        try:
            with open(os.path.join(self.library_path, "dependency_info.json"), "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_dependency_info(self):
        """ Save the updated dependency information back to the JSON file. """
        with open(os.path.join(self.library_path, "dependency_info.json"), "w") as file:
            json.dump(self.dependency_info, file)

    def is_asset_downloaded(self, asset_name):
        """ Check if the asset is already downloaded and available locally. """
        return os.path.exists(os.path.join(self.library_path, "dependencies", asset_name))

    def get_most_recent_local_asset_details(self):
        """ Return the most recent local asset details if available. """
        # Placeholder for logic to determine the most recent asset
        local_assets = self.dependency_info.get('filename')
        if local_assets:
            # Assuming assets are stored with version information and sorted by date or version
            return self.dependency_info
        return {}

    def download_asset(self, assets_details: dict):
        """ Download the asset from the given URL. """
        try:
            response = requests.get(assets_details.get("download"))
            response.raise_for_status()
            asset_path = os.path.join(
                self.library_path, 
                "dependencies", 
                os.path.basename(assets_details["filename"])
            )
            # Make the folder if not exists
            os.makedirs(os.path.dirname(asset_path), exist_ok=True)
            with open(asset_path, 'wb') as f:
                f.write(response.content)
            # Update local dependency info
            self.dependency_info = assets_details
            self.save_dependency_info()
            return True
        except requests.RequestException as e:
            self.logger.error(f"Error downloading asset: {e}")
            return False

    def set_function_prototypes(self):
        """ Set the ctypes function prototypes for loaded library functions. """
        self.library.request.argtypes = [ctypes.c_char_p]
        self.library.request.restype = ctypes.c_char_p
        self.library.freeMemory.argtypes = [ctypes.c_char_p]
        self.library.freeMemory.restype = ctypes.c_void_p
