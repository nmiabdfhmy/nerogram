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


class ActivateStealthMode(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``57BBD166``

    Parameters:
        past (``bool``, *optional*):
            N/A

        future (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <nerogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["past", "future"]

    ID = 0x57bbd166
    QUALNAME = "functions.stories.ActivateStealthMode"

    def __init__(self, *, past: Optional[bool] = None, future: Optional[bool] = None) -> None:
        self.past = past  # flags.0?true
        self.future = future  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ActivateStealthMode":
        
        flags = Int.read(b)
        
        past = True if flags & (1 << 0) else False
        future = True if flags & (1 << 1) else False
        return ActivateStealthMode(past=past, future=future)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.past else 0
        flags |= (1 << 1) if self.future else 0
        b.write(Int(flags))
        
        return b.getvalue()
