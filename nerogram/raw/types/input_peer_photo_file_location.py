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


class InputPeerPhotoFileLocation(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``166``
        - ID: ``37257E99``

    Parameters:
        peer (:obj:`InputPeer <nerogram.raw.base.InputPeer>`):
            N/A

        photo_id (``int`` ``64-bit``):
            N/A

        big (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "photo_id", "big"]

    ID = 0x37257e99
    QUALNAME = "types.InputPeerPhotoFileLocation"

    def __init__(self, *, peer: "raw.base.InputPeer", photo_id: int, big: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.photo_id = photo_id  # long
        self.big = big  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputPeerPhotoFileLocation":
        
        flags = Int.read(b)
        
        big = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        photo_id = Long.read(b)
        
        return InputPeerPhotoFileLocation(peer=peer, photo_id=photo_id, big=big)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.big else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Long(self.photo_id))
        
        return b.getvalue()
