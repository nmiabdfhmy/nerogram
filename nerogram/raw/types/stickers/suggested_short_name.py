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


class SuggestedShortName(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.stickers.SuggestedShortName`.

    Details:
        - Layer: ``166``
        - ID: ``85FEA03F``

    Parameters:
        short_name (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            stickers.SuggestShortName
    """

    __slots__: List[str] = ["short_name"]

    ID = 0x85fea03f
    QUALNAME = "types.stickers.SuggestedShortName"

    def __init__(self, *, short_name: str) -> None:
        self.short_name = short_name  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SuggestedShortName":
        # No flags
        
        short_name = String.read(b)
        
        return SuggestedShortName(short_name=short_name)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.short_name))
        
        return b.getvalue()
