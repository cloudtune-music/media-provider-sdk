# Copyright 2026 Yilei Bi
# SPDX-License-Identifier: Apache-2.0

# Copyright 2026 Yilei Bi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .capabilities import ProviderCapabilities
from .constants import (
    PLUGIN_ENTRY_POINT_GROUP,
    PROVIDER_TYPE_PATTERN,
)
from .exceptions import (
    ProviderAuthenticationError,
    ProviderConfigurationError,
    ProviderError,
    ProviderInvalidResponseError,
    ProviderItemNotFoundError,
    ProviderPermissionError,
    ProviderRateLimitError,
    ProviderSearchError,
    ProviderStreamError,
    ProviderTimeoutError,
    ProviderUnavailableError,
    ProviderUnsupportedOperationError,
)
from .models import (
    JsonValue,
    ProviderLyrics,
    ProviderSearchResult,
    ProviderStream,
    StreamType,
)
from .provider import MediaProvider
from .version import SDK_API_VERSION, __version__


__all__ = [
    "MediaProvider",

    "ProviderCapabilities",

    "ProviderSearchResult",
    "ProviderStream",
    "ProviderLyrics",

    "StreamType",
    "JsonValue",

    "ProviderError",
    "ProviderConfigurationError",
    "ProviderAuthenticationError",
    "ProviderPermissionError",
    "ProviderItemNotFoundError",
    "ProviderSearchError",
    "ProviderStreamError",
    "ProviderTimeoutError",
    "ProviderRateLimitError",
    "ProviderUnavailableError",
    "ProviderUnsupportedOperationError",
    "ProviderInvalidResponseError",

    "PLUGIN_ENTRY_POINT_GROUP",
    "PROVIDER_TYPE_PATTERN",

    "SDK_API_VERSION",
    "__version__",
]