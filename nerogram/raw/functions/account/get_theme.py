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


class GetTheme(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``3A5869EC``

    Parameters:
        format (``str``):
            N/A

        theme (:obj:`InputTheme <nerogram.raw.base.InputTheme>`):
            N/A

    Returns:
        :obj:`Theme <nerogram.raw.base.Theme>`
    """

    __slots__: List[str] = ["format", "theme"]

    ID = 0x3a5869ec
    QUALNAME = "functions.account.GetTheme"

    def __init__(self, *, format: str, theme: "raw.base.InputTheme") -> None:
        self.format = format  # string
        self.theme = theme  # InputTheme

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetTheme":
        # No flags
        
        format = String.read(b)
        
        theme = TLObject.read(b)
        
        return GetTheme(format=format, theme=theme)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.format))
        
        b.write(self.theme.write())
        
        return b.getvalue()
