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


class EncryptedChatWaiting(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.EncryptedChat`.

    Details:
        - Layer: ``166``
        - ID: ``66B25953``

    Parameters:
        id (``int`` ``32-bit``):
            N/A

        access_hash (``int`` ``64-bit``):
            N/A

        date (``int`` ``32-bit``):
            N/A

        admin_id (``int`` ``64-bit``):
            N/A

        participant_id (``int`` ``64-bit``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.RequestEncryption
            messages.AcceptEncryption
    """

    __slots__: List[str] = ["id", "access_hash", "date", "admin_id", "participant_id"]

    ID = 0x66b25953
    QUALNAME = "types.EncryptedChatWaiting"

    def __init__(self, *, id: int, access_hash: int, date: int, admin_id: int, participant_id: int) -> None:
        self.id = id  # int
        self.access_hash = access_hash  # long
        self.date = date  # int
        self.admin_id = admin_id  # long
        self.participant_id = participant_id  # long

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EncryptedChatWaiting":
        # No flags
        
        id = Int.read(b)
        
        access_hash = Long.read(b)
        
        date = Int.read(b)
        
        admin_id = Long.read(b)
        
        participant_id = Long.read(b)
        
        return EncryptedChatWaiting(id=id, access_hash=access_hash, date=date, admin_id=admin_id, participant_id=participant_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(Int(self.date))
        
        b.write(Long(self.admin_id))
        
        b.write(Long(self.participant_id))
        
        return b.getvalue()
