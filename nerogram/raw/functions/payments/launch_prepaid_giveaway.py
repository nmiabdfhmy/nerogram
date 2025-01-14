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


class LaunchPrepaidGiveaway(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``5FF58F20``

    Parameters:
        peer (:obj:`InputPeer <nerogram.raw.base.InputPeer>`):
            N/A

        giveaway_id (``int`` ``64-bit``):
            N/A

        purpose (:obj:`InputStorePaymentPurpose <nerogram.raw.base.InputStorePaymentPurpose>`):
            N/A

    Returns:
        :obj:`Updates <nerogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "giveaway_id", "purpose"]

    ID = 0x5ff58f20
    QUALNAME = "functions.payments.LaunchPrepaidGiveaway"

    def __init__(self, *, peer: "raw.base.InputPeer", giveaway_id: int, purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.peer = peer  # InputPeer
        self.giveaway_id = giveaway_id  # long
        self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LaunchPrepaidGiveaway":
        # No flags
        
        peer = TLObject.read(b)
        
        giveaway_id = Long.read(b)
        
        purpose = TLObject.read(b)
        
        return LaunchPrepaidGiveaway(peer=peer, giveaway_id=giveaway_id, purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Long(self.giveaway_id))
        
        b.write(self.purpose.write())
        
        return b.getvalue()
