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


class KeyboardButtonCopy(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.KeyboardButton`.

    Details:
        - Layer: ``195``
        - ID: ``75D2698E``

    Parameters:
        text (``str``):
            N/A

        copy_text (``str``):
            N/A

    """

    __slots__: List[str] = ["text", "copy_text"]

    ID = 0x75d2698e
    QUALNAME = "types.KeyboardButtonCopy"

    def __init__(self, *, text: str, copy_text: str) -> None:
        self.text = text  # string
        self.copy_text = copy_text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "KeyboardButtonCopy":
        # No flags
        
        text = String.read(b)
        
        copy_text = String.read(b)
        
        return KeyboardButtonCopy(text=text, copy_text=copy_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.text))
        
        b.write(String(self.copy_text))
        
        return b.getvalue()
