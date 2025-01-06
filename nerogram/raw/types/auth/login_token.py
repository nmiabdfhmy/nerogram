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


class LoginToken(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.auth.LoginToken`.

    Details:
        - Layer: ``166``
        - ID: ``629F1980``

    Parameters:
        expires (``int`` ``32-bit``):
            N/A

        token (``bytes``):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            auth.ExportLoginToken
            auth.ImportLoginToken
    """

    __slots__: List[str] = ["expires", "token"]

    ID = 0x629f1980
    QUALNAME = "types.auth.LoginToken"

    def __init__(self, *, expires: int, token: bytes) -> None:
        self.expires = expires  # int
        self.token = token  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "LoginToken":
        # No flags
        
        expires = Int.read(b)
        
        token = Bytes.read(b)
        
        return LoginToken(expires=expires, token=token)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.expires))
        
        b.write(Bytes(self.token))
        
        return b.getvalue()
