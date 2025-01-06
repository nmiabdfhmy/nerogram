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


class MyBoosts(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.premium.MyBoosts`.

    Details:
        - Layer: ``166``
        - ID: ``9AE228E2``

    Parameters:
        my_boosts (List of :obj:`MyBoost <nerogram.raw.base.MyBoost>`):
            N/A

        chats (List of :obj:`Chat <nerogram.raw.base.Chat>`):
            N/A

        users (List of :obj:`User <nerogram.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            premium.GetMyBoosts
            premium.ApplyBoost
    """

    __slots__: List[str] = ["my_boosts", "chats", "users"]

    ID = 0x9ae228e2
    QUALNAME = "types.premium.MyBoosts"

    def __init__(self, *, my_boosts: List["raw.base.MyBoost"], chats: List["raw.base.Chat"], users: List["raw.base.User"]) -> None:
        self.my_boosts = my_boosts  # Vector<MyBoost>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MyBoosts":
        # No flags
        
        my_boosts = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return MyBoosts(my_boosts=my_boosts, chats=chats, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.my_boosts))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        return b.getvalue()
