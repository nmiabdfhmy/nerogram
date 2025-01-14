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


class MessageActionGameScore(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.MessageAction`.

    Details:
        - Layer: ``166``
        - ID: ``92A72876``

    Parameters:
        game_id (``int`` ``64-bit``):
            N/A

        score (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["game_id", "score"]

    ID = 0x92a72876
    QUALNAME = "types.MessageActionGameScore"

    def __init__(self, *, game_id: int, score: int) -> None:
        self.game_id = game_id  # long
        self.score = score  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGameScore":
        # No flags
        
        game_id = Long.read(b)
        
        score = Int.read(b)
        
        return MessageActionGameScore(game_id=game_id, score=score)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.game_id))
        
        b.write(Int(self.score))
        
        return b.getvalue()
