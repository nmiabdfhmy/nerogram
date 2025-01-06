#  Nerogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Nerogram.
#
#  Nerogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Nerogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Nerogram.  If not, see <http://www.gnu.org/licenses/>.

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from nerogram import raw
from nerogram.raw.core import TLObject

MediaArea = Union[raw.types.InputMediaAreaVenue, raw.types.MediaAreaGeoPoint, raw.types.MediaAreaSuggestedReaction, raw.types.MediaAreaVenue]


# noinspection PyRedeclaration
class MediaArea:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 4 constructors available.

        .. currentmodule:: nerogram.raw.types

        .. autosummary::
            :nosignatures:

            InputMediaAreaVenue
            MediaAreaGeoPoint
            MediaAreaSuggestedReaction
            MediaAreaVenue
    """

    QUALNAME = "nerogram.raw.base.MediaArea"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.nerogram.org/telegram/base/media-area")
