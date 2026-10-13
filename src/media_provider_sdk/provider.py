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

from abc import ABC, abstractmethod
from typing import ClassVar, Mapping

from .capabilities import ProviderCapabilities
from .models import (
    JsonValue,
    ProviderLyrics,
    ProviderSearchResult,
    ProviderStream,
)


class MediaProvider(ABC):
    """
    Base interface implemented by all Media Provider plugins.
    """

    provider_type: ClassVar[str]

    display_name: ClassVar[str | None] = None

    def __init__(
        self,
        settings: Mapping[str, JsonValue] | None = None,
        secrets: Mapping[str, JsonValue] | None = None,
    ) -> None:
        self.settings = dict(settings or {})
        self.secrets = dict(secrets or {})

    @property
    def capabilities(self) -> ProviderCapabilities:
        """
        Capabilities supported by this provider.
        """
        return ProviderCapabilities()

    @abstractmethod
    async def search(
        self,
        query: str,
        *,
        limit: int = 20,
    ) -> list[ProviderSearchResult]:
        """
        Search media from this provider.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_stream(
        self,
        provider_item_id: str,
    ) -> ProviderStream:
        """
        Resolve a playable stream for a provider item.
        """
        raise NotImplementedError

    async def get_preview_stream(
        self,
        provider_item_id: str,
    ) -> ProviderStream:
        """
        Resolve a preview stream.

        Default behavior uses the normal stream resolver.
        Providers may override this method.
        """
        return await self.get_stream(
            provider_item_id
        )

    async def get_lyrics(
        self,
        provider_item_id: str,
    ) -> ProviderLyrics | None:
        """
        Return lyrics when supported.
        """
        return None

    async def validate_config(self) -> None:
        """
        Validate provider settings and secrets.

        Raise ProviderConfigurationError when invalid.
        """
        return None

    async def close(self) -> None:
        """
        Release resources owned by the provider.

        Providers using HTTP clients, sockets, file handles,
        pools, etc. should override this method.
        """
        return None