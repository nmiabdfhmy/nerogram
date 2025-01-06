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


class UpdatePendingJoinRequests(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.Update`.

    Details:
        - Layer: ``166``
        - ID: ``7063C3DB``

    Parameters:
        peer (:obj:`Peer <nerogram.raw.base.Peer>`):
            N/A

        requests_pending (``int`` ``32-bit``):
            N/A

        recent_requesters (List of ``int`` ``64-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "requests_pending", "recent_requesters"]

    ID = 0x7063c3db
    QUALNAME = "types.UpdatePendingJoinRequests"

    def __init__(self, *, peer: "raw.base.Peer", requests_pending: int, recent_requesters: List[int]) -> None:
        self.peer = peer  # Peer
        self.requests_pending = requests_pending  # int
        self.recent_requesters = recent_requesters  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePendingJoinRequests":
        # No flags
        
        peer = TLObject.read(b)
        
        requests_pending = Int.read(b)
        
        recent_requesters = TLObject.read(b, Long)
        
        return UpdatePendingJoinRequests(peer=peer, requests_pending=requests_pending, recent_requesters=recent_requesters)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.requests_pending))
        
        b.write(Vector(self.recent_requesters, Long))
        
        return b.getvalue()
