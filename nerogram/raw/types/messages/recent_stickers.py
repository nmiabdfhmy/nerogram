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


class RecentStickers(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.messages.RecentStickers`.

    Details:
        - Layer: ``166``
        - ID: ``88D37C56``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        packs (List of :obj:`StickerPack <nerogram.raw.base.StickerPack>`):
            N/A

        stickers (List of :obj:`Document <nerogram.raw.base.Document>`):
            N/A

        dates (List of ``int`` ``32-bit``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetRecentStickers
    """

    __slots__: List[str] = ["hash", "packs", "stickers", "dates"]

    ID = 0x88d37c56
    QUALNAME = "types.messages.RecentStickers"

    def __init__(self, *, hash: int, packs: List["raw.base.StickerPack"], stickers: List["raw.base.Document"], dates: List[int]) -> None:
        self.hash = hash  # long
        self.packs = packs  # Vector<StickerPack>
        self.stickers = stickers  # Vector<Document>
        self.dates = dates  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RecentStickers":
        # No flags
        
        hash = Long.read(b)
        
        packs = TLObject.read(b)
        
        stickers = TLObject.read(b)
        
        dates = TLObject.read(b, Int)
        
        return RecentStickers(hash=hash, packs=packs, stickers=stickers, dates=dates)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.packs))
        
        b.write(Vector(self.stickers))
        
        b.write(Vector(self.dates, Int))
        
        return b.getvalue()
