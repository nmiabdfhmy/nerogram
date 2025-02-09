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


class ChatReactionsAll(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.ChatReactions`.

    Details:
        - Layer: ``166``
        - ID: ``52928BCA``

    Parameters:
        allow_custom (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["allow_custom"]

    ID = 0x52928bca
    QUALNAME = "types.ChatReactionsAll"

    def __init__(self, *, allow_custom: Optional[bool] = None) -> None:
        self.allow_custom = allow_custom  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatReactionsAll":
        
        flags = Int.read(b)
        
        allow_custom = True if flags & (1 << 0) else False
        return ChatReactionsAll(allow_custom=allow_custom)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.allow_custom else 0
        b.write(Int(flags))
        
        return b.getvalue()
