import re

class ClientProfiles:
    def __init__(self, profiles_list):
        self.profiles = {}
        # Dynamically set each profile in the list as an attribute and store in a dictionary
        for profile in profiles_list:
            normalized_name = profile.replace("-", "_").lower()
            setattr(self, normalized_name, profile)
            browser_type = re.match(r'([a-zA-Z]+)_', normalized_name)
            if browser_type:
                browser_key = browser_type.group(1)
                if browser_key not in self.profiles:
                    self.profiles[browser_key] = []
                self.profiles[browser_key].append(profile)

        # Generate methods dynamically for each browser type found
        for browser_key in self.profiles.keys():
            self._generate_latest_version_method(browser_key)

    def _generate_latest_version_method(self, browser_key):
        # Define a new method for each browser type to get the latest version
        def latest_version_method():
            versions = self.profiles[browser_key]
            latest_version = sorted(versions, key=lambda x: [int(num) if num.isdigit() else num for num in re.split(r'(\d+)', x)])[-1]
            return latest_version
        # Set the method to the class with an appropriate name
        setattr(self, f"get_latest_{browser_key}_version", latest_version_method)