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

from dataclasses import dataclass, field
from typing import Literal


type JsonValue = (
    str
    | int
    | float
    | bool
    | None
    | list[JsonValue]
    | dict[str, JsonValue]
)


StreamType = Literal[
    "DIRECT",
    "HLS",
]


@dataclass(frozen=True, slots=True)
class ProviderSearchResult:
    """
    A media item returned by a provider search.

    provider_item_id is private to the provider/server boundary.
    It should not normally be exposed directly to client applications.
    """

    provider_item_id: str
    title: str

    artist: str | None = None
    album: str | None = None
    thumbnail_url: str | None = None

    duration_seconds: float | None = None

    extra: dict[str, JsonValue] = field(
        default_factory=dict
    )


@dataclass(frozen=True, slots=True)
class ProviderStream:
    """
    A stream resolved by a provider.

    The provider describes the upstream media source.
    The server core decides the final playback strategy.
    """

    url: str

    mime_type: str | None = None
    expires_at_epoch: int | None = None

    headers: dict[str, str] = field(
        default_factory=dict
    )

    stream_type: StreamType = "DIRECT"

    duration_seconds: float | None = None
    content_length: int | None = None

    container: str | None = None
    codec: str | None = None
    format_id: str | None = None

    extra: dict[str, JsonValue] = field(
        default_factory=dict
    )


@dataclass(frozen=True, slots=True)
class ProviderLyrics:
    """
    Lyrics returned by a provider.
    """

    text: str
    language: str | None = None
    synced: bool = False