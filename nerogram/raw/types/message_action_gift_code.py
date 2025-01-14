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


class MessageActionGiftCode(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.MessageAction`.

    Details:
        - Layer: ``166``
        - ID: ``D2CFDB0E``

    Parameters:
        months (``int`` ``32-bit``):
            N/A

        slug (``str``):
            N/A

        via_giveaway (``bool``, *optional*):
            N/A

        unclaimed (``bool``, *optional*):
            N/A

        boost_peer (:obj:`Peer <nerogram.raw.base.Peer>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["months", "slug", "via_giveaway", "unclaimed", "boost_peer"]

    ID = 0xd2cfdb0e
    QUALNAME = "types.MessageActionGiftCode"

    def __init__(self, *, months: int, slug: str, via_giveaway: Optional[bool] = None, unclaimed: Optional[bool] = None, boost_peer: "raw.base.Peer" = None) -> None:
        self.months = months  # int
        self.slug = slug  # string
        self.via_giveaway = via_giveaway  # flags.0?true
        self.unclaimed = unclaimed  # flags.2?true
        self.boost_peer = boost_peer  # flags.1?Peer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGiftCode":
        
        flags = Int.read(b)
        
        via_giveaway = True if flags & (1 << 0) else False
        unclaimed = True if flags & (1 << 2) else False
        boost_peer = TLObject.read(b) if flags & (1 << 1) else None
        
        months = Int.read(b)
        
        slug = String.read(b)
        
        return MessageActionGiftCode(months=months, slug=slug, via_giveaway=via_giveaway, unclaimed=unclaimed, boost_peer=boost_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.via_giveaway else 0
        flags |= (1 << 2) if self.unclaimed else 0
        flags |= (1 << 1) if self.boost_peer is not None else 0
        b.write(Int(flags))
        
        if self.boost_peer is not None:
            b.write(self.boost_peer.write())
        
        b.write(Int(self.months))
        
        b.write(String(self.slug))
        
        return b.getvalue()
