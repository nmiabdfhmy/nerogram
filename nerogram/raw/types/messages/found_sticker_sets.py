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


class FoundStickerSets(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.messages.FoundStickerSets`.

    Details:
        - Layer: ``166``
        - ID: ``8AF09DD2``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        sets (List of :obj:`StickerSetCovered <nerogram.raw.base.StickerSetCovered>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.SearchStickerSets
    """

    __slots__: List[str] = ["hash", "sets"]

    ID = 0x8af09dd2
    QUALNAME = "types.messages.FoundStickerSets"

    def __init__(self, *, hash: int, sets: List["raw.base.StickerSetCovered"]) -> None:
        self.hash = hash  # long
        self.sets = sets  # Vector<StickerSetCovered>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FoundStickerSets":
        # No flags
        
        hash = Long.read(b)
        
        sets = TLObject.read(b)
        
        return FoundStickerSets(hash=hash, sets=sets)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.sets))
        
        return b.getvalue()
