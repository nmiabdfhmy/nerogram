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


class ChangeStickerPosition(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``FFB6D4CA``

    Parameters:
        sticker (:obj:`InputDocument <nerogram.raw.base.InputDocument>`):
            N/A

        position (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.StickerSet <nerogram.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["sticker", "position"]

    ID = 0xffb6d4ca
    QUALNAME = "functions.stickers.ChangeStickerPosition"

    def __init__(self, *, sticker: "raw.base.InputDocument", position: int) -> None:
        self.sticker = sticker  # InputDocument
        self.position = position  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChangeStickerPosition":
        # No flags
        
        sticker = TLObject.read(b)
        
        position = Int.read(b)
        
        return ChangeStickerPosition(sticker=sticker, position=position)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.sticker.write())
        
        b.write(Int(self.position))
        
        return b.getvalue()
