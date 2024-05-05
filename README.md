# Takion TLS

![Takion Banner](https://takionapi.tech/banner)

[![PyPI version](https://badge.fury.io/py/takion-tls.svg)](https://badge.fury.io/py/takion-tls)
![GitHub license](https://img.shields.io/github/license/takionapi/takion-tls)

**Takion TLS** is a dynamic and customizable TLS client designed for quick sad easy integration into Python applications. It aims to address the common issues faced with existing open-source TLS clients that often lack ongoing maintenance and crucial features as well as helping our clients, in combo with our APIs, don't have to worry about antibots.

## Table of Contents
- [Takion TLS](#takion-tls)
  - [Table of Contents](#table-of-contents)
  - [Understanding TLS and Its Importance in Web Scraping and Reverse Engineering](#understanding-tls-and-its-importance-in-web-scraping-and-reverse-engineering)
    - [What is TLS?](#what-is-tls)
    - [Why is TLS Important?](#why-is-tls-important)
      - [Web Scraping](#web-scraping)
      - [Reverse Engineering](#reverse-engineering)
  - [What is Takion TLS?](#what-is-takion-tls)
    - [Why Takion TLS?](#why-takion-tls)
    - [Features](#features)
  - [Installation](#installation)
  - [Examples](#examples)
    - [Basic Usage](#basic-usage)
    - [The Dependencies installation](#the-dependencies-installation)
    - [Changing dependencies path](#changing-dependencies-path)
    - [Getting available client identifiers](#getting-available-client-identifiers)
    - [Custom details](#custom-details)
    - [Proxy support](#proxy-support)
  - [Compiling Takion TLS](#compiling-takion-tls)
    - [Setup Example](#setup-example)
  - [Contributing](#contributing)
  - [License](#license)
  - [Discover TakionAPI for Web Scraping Solutions](#discover-takionapi-for-web-scraping-solutions)
  - [Stay connected with us](#stay-connected-with-us)

## Understanding TLS and Its Importance in Web Scraping and Reverse Engineering

### What is TLS?

**TLS (Transport Layer Security)** is the successor to SSL (Secure Sockets Layer). It is a cryptographic protocol designed to provide secure communication over a computer network. TLS ensures that data transmitted between a web server and a client (such as a web browser or a scraping tool) is encrypted, which prevents eavesdropping and tampering.

### Why is TLS Important?

#### Web Scraping

Web scraping involves programmatically accessing web pages to extract data. Websites often use TLS to secure all communications between their servers and clients, which means that scraping tools must be able to handle TLS to access the content effectively. Proper handling of TLS in web scraping is crucial because:

- **Access to Content**: Many websites only serve content over HTTPS (the secure version of HTTP enabled by TLS), which requires scraping tools to correctly implement TLS to access and extract data.
- **Data Privacy**: When scraping websites, especially those that require login credentials, TLS ensures that sensitive information (like usernames and passwords) is encrypted and secure.
- **Avoiding Blocking**: Websites might block clients that cannot handle TLS as they might be perceived as outdated or non-standard, which could be a security risk.

#### Reverse Engineering

In reverse engineering, researchers or developers analyze software or network communications to understand how they work. This often involves looking at the communications between clients and servers:

- **Security Analysis**: TLS is crucial for securing communications. Understanding how TLS is implemented and configured (like which ciphers are used) can reveal vulnerabilities or misconfigurations that could lead to security breaches.
- **Protocol Analysis**: Many modern applications use proprietary protocols over TLS. Understanding TLS setups can help reverse engineers decrypt and analyze these communications to understand application behaviors or to develop compatible clients.
- **Custom Implementations and Simulations**: Reverse engineering often involves replicating server behaviors or creating fake clients for testing. Understanding TLS configurations helps ensure these implementations are accurate and can interact correctly with real servers or clients.


## What is Takion TLS?

Takion TLS is a modern library built on top of the maintained and actively developed [tls-client](https://github.com/bogdanfinn/tls-client) project. 

It is designed to automatically update and configure the TLS client based on the operating system it runs on. 

The library simplifies the integration of a TLS client into Python applications.

### Why Takion TLS?

The creation of Takion TLS was motivated by the need for a Python-compatible TLS library that is not only easy to use but also robust and feature-rich. 

Many existing libraries in the public domain suffer from lack of maintenance and do not support modern TLS features, which can hinder development and expose applications to security risks.

### Features

- **Auto Updating**: Automatically updates TLS client libraries from the latest releases of `bogdanfinn/tls-client` and loads new clients identifiers.
- **Asynchronous Support**: Compatible with async programming, making it suitable for modern Python applications.
- **Proxy Support**: Includes a simple `.update_proxy()` method for session management.
- **Custom Configuration**:
  - Custom JA3 strings and H2 settings.
  - Custom supported signature algorithms and TLS versions.
  - Custom key share curves and certificate compression algorithms.
  - Custom pseudo header order and connection flow.
  - Custom header order and client identifiers (e.g., Chrome, Firefox, Opera, Safari, iOS, iPadOS, Android).
  - Options to randomize or customize TLS extension orders.
- **Request Enhancements**:
  - Support for `requests` history and `allow_redirects`.
  - Extensive logging and error handling capabilities.

## Installation

Install Takion TLS using pip:

```bash
pip install takion-tls
```

## Examples

For practical examples on how to use Takion TLS, please refer to the `examples` directory in the project repository:

- [Basic Usage](https://github.com/Takion-API-Services/takion-tls/tree/master/examples/basic_usage.py)
- [Changing Dependencies Path](https://github.com/Takion-API-Services/takion-tls/tree/master/examples/changing_dependencies_path.py)
- [Getting Available Client Identifiers](https://github.com/Takion-API-Services/takion-tls/tree/master/examples/getting_client_identifiers.py)
- [Custom Details](https://github.com/Takion-API-Services/takion-tls/tree/master/examples/custom_details.py)
- [Proxy Support](https://github.com/Takion-API-Services/takion-tls/tree/master/examples/proxy_support.py)


### Basic Usage
```py
from takion_tls import Session

async def main():
    session = Session("chrome_124")
    # When the session is initialized for the first time in your environment,
    # the lastest available compiled client will be downloaded and loaded.

    response = await session.get("https://tls.peet.ws/api/all")
    print(response.text)
```

### The Dependencies installation
```py
from takion_tls import Session

async def main():
    # In a situation like this, when a Session object is created, ther will be a check if the dependencies
    # are downloaded and in case do it
    Session("chrome_124")
    # When creating a new session, the deoendencies library is going
    # to be shared, so you'll not have to worry about
    # downloading each time
    Session("chrome_124")
```

### Changing dependencies path
```py
from takion_tls import Session

async def main():
    Session.library_path = "./test/"
    # If you wanna change the default path where the compiled clients are stored,
    # you can do it by changing the `library_path` attribute of the Session class.

    session = Session("chrome_124")
    response = await session.get("https://tls.peet.ws/api/all")
    print(response.text)
```

### Getting available client identifiers
```py
from takion_tls import Session

async def main():
    Session()
    # You need to initialize at least once the session to download the latest compiled clients
    # before beeing able to get the available client identifiers.
    
    print(Session.clients.profiles)
    '''
    Output:

    {
        'chrome': [
            'chrome_103', ..., 'chrome_120', 'chrome_124'
        ], 
        'safari': [
            'safari_15_6_1', ... 'safari_ios_17_0'
        ], 
        'firefox': [
            'firefox_102', ... 'firefox_120', 'firefox_123'
        ], 
        ...
    }
    '''

    # By default if not passed a client Identifier or custom configurations, the lastest Chrome client will be used.
    # Some other available methods are as well
    print(Session.clients.get_latest_chrome_version) # chrome_124
    print(Session.clients.get_latest_safari_version) # safari_ios_17_0
    print(Session.clients.get_latest_firefox_version) # firefox_123
```


### Custom details
```py
from takion_tls import Session

async def main():
    session = Session(
        ja3_string="771,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513,29-23-24,0",
        h2_settings={
            "HEADER_TABLE_SIZE": 65536,
            "MAX_CONCURRENT_STREAMS": 1000,
            "INITIAL_WINDOW_SIZE": 6291456,
            "MAX_HEADER_LIST_SIZE": 262144
        },
        h2_settings_order=[
            "HEADER_TABLE_SIZE",
            "MAX_CONCURRENT_STREAMS",
            "INITIAL_WINDOW_SIZE",
            "MAX_HEADER_LIST_SIZE"
        ],
        supported_signature_algorithms=[
            "ECDSAWithP256AndSHA256",
            "PSSWithSHA256",
            "PKCS1WithSHA256",
            "ECDSAWithP384AndSHA384",
            "PSSWithSHA384",
            "PKCS1WithSHA384",
            "PSSWithSHA512",
            "PKCS1WithSHA512",
        ],
        supported_versions=["GREASE", "1.3", "1.2"],
        key_share_curves=["GREASE", "X25519"],
        cert_compression_algo="brotli",
        pseudo_header_order=[
            ":method",
            ":authority",
            ":scheme",
            ":path"
        ],
        connection_flow=15663105,
        header_order=[
            "accept",
            "user-agent",
            "accept-encoding",
            "accept-language"
        ]
    )
    
    session = Session("chrome_124")
    response = await session.get("https://tls.peet.ws/api/all")
    print(response.text)
```

### Proxy support
```py
from takion_tls import Session

async def main():
    session = Session("chrome_124")
    
    session.update_proxy("123:456")
    # Now the proxy uses 123:456 proxy
    
    session.update_proxy("123:456:999:123")
    # Now the proxy uses 123:456:999:123 proxy
    
    session.update_proxy("http://user:password@host:port")
    # Now the proxy uses http://user:password@host:port proxy
```

## Compiling Takion TLS

For optimal management and updates, it is recommended to set the library path to an external folder rather than the default `site-packages/takion-tls` when compiling a project using Takion TLS rather than adding abinary during compilation.

### Setup Example

```python
from takion_tls import Session

# Initialize the library with a custom external path
Session.library_path = "./example"
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT [License](LICENSE). See the LICENSE file for more details.


## Discover TakionAPI for Web Scraping Solutions

![Takion Banner](https://takionapi.tech/banner)

Struggling with anti-bot measures and captchas in your web scraping or automation projects? **TakionAPI** offers a powerful solution to bypass these obstacles effortlessly. Our service uses advanced AI and algorithm-based approaches, eliminating the need for browser automation. We ensure you have a fast, 24/7 solution that's always up-to-date, supporting all operating systems and browsers.

- **Bypass tough anti-bots** like Datadome, Incapsula/Imperva, Perimeter X, and more.
- **Custom modules** and services tailored to your needs.
- **Join our community** for a free trial and see the difference!

**Connect with us on [Discord](https://takionapi.tech/discord) and start your free trial today!**

## Stay connected with us
- [GlizzyKingDreko](https://github.com/glizzykingdreko)
- [Takion API](https://takionapi.tech/)
- [Takion API Free Trial](https://takionapi.tech/discord)
- [TakionAPI Docs](https://docs.takionapi.tech)