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


class BotCommandScopePeerUser(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.BotCommandScope`.

    Details:
        - Layer: ``166``
        - ID: ``A1321F3``

    Parameters:
        peer (:obj:`InputPeer <nerogram.raw.base.InputPeer>`):
            N/A

        user_id (:obj:`InputUser <nerogram.raw.base.InputUser>`):
            N/A

    """

    __slots__: List[str] = ["peer", "user_id"]

    ID = 0xa1321f3
    QUALNAME = "types.BotCommandScopePeerUser"

    def __init__(self, *, peer: "raw.base.InputPeer", user_id: "raw.base.InputUser") -> None:
        self.peer = peer  # InputPeer
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotCommandScopePeerUser":
        # No flags
        
        peer = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        return BotCommandScopePeerUser(peer=peer, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()
