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

from io import BytesIO

from nerogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from nerogram.raw.core import TLObject
from nerogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageActionSetChatWallPaper(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.MessageAction`.

    Details:
        - Layer: ``166``
        - ID: ``BC44A927``

    Parameters:
        wallpaper (:obj:`WallPaper <nerogram.raw.base.WallPaper>`):
            N/A

    """

    __slots__: List[str] = ["wallpaper"]

    ID = 0xbc44a927
    QUALNAME = "types.MessageActionSetChatWallPaper"

    def __init__(self, *, wallpaper: "raw.base.WallPaper") -> None:
        self.wallpaper = wallpaper  # WallPaper

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSetChatWallPaper":
        # No flags
        
        wallpaper = TLObject.read(b)
        
        return MessageActionSetChatWallPaper(wallpaper=wallpaper)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.wallpaper.write())
        
        return b.getvalue()
