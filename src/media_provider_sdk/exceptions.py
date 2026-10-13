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

from __future__ import annotations

from .models import JsonValue


class ProviderError(Exception):
    """
    Base exception for all provider errors.

    Provider plugins should raise ProviderError subclasses
    instead of framework-specific exceptions such as
    FastAPI HTTPException.
    """

    code = "provider_error"

    def __init__(
        self,
        message: str,
        *,
        retryable: bool = False,
        details: dict[str, JsonValue] | None = None,
    ) -> None:
        super().__init__(message)

        self.message = message
        self.retryable = retryable
        self.details = details or {}


class ProviderConfigurationError(ProviderError):
    code = "provider_configuration_error"


class ProviderAuthenticationError(ProviderError):
    code = "provider_authentication_error"


class ProviderPermissionError(ProviderError):
    code = "provider_permission_error"


class ProviderItemNotFoundError(ProviderError):
    code = "provider_item_not_found"


class ProviderSearchError(ProviderError):
    code = "provider_search_error"


class ProviderStreamError(ProviderError):
    code = "provider_stream_error"


class ProviderTimeoutError(ProviderError):
    code = "provider_timeout"

    def __init__(
        self,
        message: str = "Provider request timed out",
        *,
        details: dict[str, JsonValue] | None = None,
    ) -> None:
        super().__init__(
            message,
            retryable=True,
            details=details,
        )


class ProviderRateLimitError(ProviderError):
    code = "provider_rate_limit"

    def __init__(
        self,
        message: str = "Provider rate limit reached",
        *,
        details: dict[str, JsonValue] | None = None,
    ) -> None:
        super().__init__(
            message,
            retryable=True,
            details=details,
        )


class ProviderUnavailableError(ProviderError):
    code = "provider_unavailable"

    def __init__(
        self,
        message: str = "Provider is temporarily unavailable",
        *,
        details: dict[str, JsonValue] | None = None,
    ) -> None:
        super().__init__(
            message,
            retryable=True,
            details=details,
        )


class ProviderUnsupportedOperationError(ProviderError):
    code = "provider_unsupported_operation"


class ProviderInvalidResponseError(ProviderError):
    code = "provider_invalid_response"