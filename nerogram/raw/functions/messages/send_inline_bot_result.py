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


class SendInlineBotResult(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``F7BC68BA``

    Parameters:
        peer (:obj:`InputPeer <nerogram.raw.base.InputPeer>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        query_id (``int`` ``64-bit``):
            N/A

        id (``str``):
            N/A

        silent (``bool``, *optional*):
            N/A

        background (``bool``, *optional*):
            N/A

        clear_draft (``bool``, *optional*):
            N/A

        hide_via (``bool``, *optional*):
            N/A

        reply_to (:obj:`InputReplyTo <nerogram.raw.base.InputReplyTo>`, *optional*):
            N/A

        schedule_date (``int`` ``32-bit``, *optional*):
            N/A

        send_as (:obj:`InputPeer <nerogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`Updates <nerogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "random_id", "query_id", "id", "silent", "background", "clear_draft", "hide_via", "reply_to", "schedule_date", "send_as"]

    ID = 0xf7bc68ba
    QUALNAME = "functions.messages.SendInlineBotResult"

    def __init__(self, *, peer: "raw.base.InputPeer", random_id: int, query_id: int, id: str, silent: Optional[bool] = None, background: Optional[bool] = None, clear_draft: Optional[bool] = None, hide_via: Optional[bool] = None, reply_to: "raw.base.InputReplyTo" = None, schedule_date: Optional[int] = None, send_as: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.random_id = random_id  # long
        self.query_id = query_id  # long
        self.id = id  # string
        self.silent = silent  # flags.5?true
        self.background = background  # flags.6?true
        self.clear_draft = clear_draft  # flags.7?true
        self.hide_via = hide_via  # flags.11?true
        self.reply_to = reply_to  # flags.0?InputReplyTo
        self.schedule_date = schedule_date  # flags.10?int
        self.send_as = send_as  # flags.13?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendInlineBotResult":
        
        flags = Int.read(b)
        
        silent = True if flags & (1 << 5) else False
        background = True if flags & (1 << 6) else False
        clear_draft = True if flags & (1 << 7) else False
        hide_via = True if flags & (1 << 11) else False
        peer = TLObject.read(b)
        
        reply_to = TLObject.read(b) if flags & (1 << 0) else None
        
        random_id = Long.read(b)
        
        query_id = Long.read(b)
        
        id = String.read(b)
        
        schedule_date = Int.read(b) if flags & (1 << 10) else None
        send_as = TLObject.read(b) if flags & (1 << 13) else None
        
        return SendInlineBotResult(peer=peer, random_id=random_id, query_id=query_id, id=id, silent=silent, background=background, clear_draft=clear_draft, hide_via=hide_via, reply_to=reply_to, schedule_date=schedule_date, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 6) if self.background else 0
        flags |= (1 << 7) if self.clear_draft else 0
        flags |= (1 << 11) if self.hide_via else 0
        flags |= (1 << 0) if self.reply_to is not None else 0
        flags |= (1 << 10) if self.schedule_date is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        b.write(Long(self.random_id))
        
        b.write(Long(self.query_id))
        
        b.write(String(self.id))
        
        if self.schedule_date is not None:
            b.write(Int(self.schedule_date))
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()
