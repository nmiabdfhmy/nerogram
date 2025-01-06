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


class DeleteParticipantHistory(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``367544DB``

    Parameters:
        channel (:obj:`InputChannel <nerogram.raw.base.InputChannel>`):
            N/A

        participant (:obj:`InputPeer <nerogram.raw.base.InputPeer>`):
            N/A

    Returns:
        :obj:`messages.AffectedHistory <nerogram.raw.base.messages.AffectedHistory>`
    """

    __slots__: List[str] = ["channel", "participant"]

    ID = 0x367544db
    QUALNAME = "functions.channels.DeleteParticipantHistory"

    def __init__(self, *, channel: "raw.base.InputChannel", participant: "raw.base.InputPeer") -> None:
        self.channel = channel  # InputChannel
        self.participant = participant  # InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeleteParticipantHistory":
        # No flags
        
        channel = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        return DeleteParticipantHistory(channel=channel, participant=participant)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.participant.write())
        
        return b.getvalue()
