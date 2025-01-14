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


class GetPremiumGiftCodeOptions(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``2757BA54``

    Parameters:
        boost_peer (:obj:`InputPeer <nerogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        List of :obj:`PremiumGiftCodeOption <nerogram.raw.base.PremiumGiftCodeOption>`
    """

    __slots__: List[str] = ["boost_peer"]

    ID = 0x2757ba54
    QUALNAME = "functions.payments.GetPremiumGiftCodeOptions"

    def __init__(self, *, boost_peer: "raw.base.InputPeer" = None) -> None:
        self.boost_peer = boost_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPremiumGiftCodeOptions":
        
        flags = Int.read(b)
        
        boost_peer = TLObject.read(b) if flags & (1 << 0) else None
        
        return GetPremiumGiftCodeOptions(boost_peer=boost_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.boost_peer is not None else 0
        b.write(Int(flags))
        
        if self.boost_peer is not None:
            b.write(self.boost_peer.write())
        
        return b.getvalue()
