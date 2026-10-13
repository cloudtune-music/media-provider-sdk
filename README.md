# Media Provider SDK

Python SDK for building provider plugins for Media Provider Server.

The SDK defines the stable contract between Media Provider Server and third-party
provider plugins.

A provider plugin can connect Media Provider Server to different media sources,
such as:

- Web APIs
- WebDAV
- FTP
- S3-compatible storage
- Jellyfin
- NAS services
- Custom media services
- Other media backends

Plugin developers only need this SDK.

They do **not** need to depend on Media Provider Server or Media Provider Runtime.


## Requirements

- Python 3.12+


## Installation

### From GitHub Release

Download the wheel from the GitHub Releases page and install it:

```bash
pip install media_provider_sdk-0.1.0-py3-none-any.whl