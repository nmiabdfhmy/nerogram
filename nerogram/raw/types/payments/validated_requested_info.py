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


class ValidatedRequestedInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.payments.ValidatedRequestedInfo`.

    Details:
        - Layer: ``166``
        - ID: ``D1451883``

    Parameters:
        id (``str``, *optional*):
            N/A

        shipping_options (List of :obj:`ShippingOption <nerogram.raw.base.ShippingOption>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.ValidateRequestedInfo
    """

    __slots__: List[str] = ["id", "shipping_options"]

    ID = 0xd1451883
    QUALNAME = "types.payments.ValidatedRequestedInfo"

    def __init__(self, *, id: Optional[str] = None, shipping_options: Optional[List["raw.base.ShippingOption"]] = None) -> None:
        self.id = id  # flags.0?string
        self.shipping_options = shipping_options  # flags.1?Vector<ShippingOption>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ValidatedRequestedInfo":
        
        flags = Int.read(b)
        
        id = String.read(b) if flags & (1 << 0) else None
        shipping_options = TLObject.read(b) if flags & (1 << 1) else []
        
        return ValidatedRequestedInfo(id=id, shipping_options=shipping_options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.id is not None else 0
        flags |= (1 << 1) if self.shipping_options else 0
        b.write(Int(flags))
        
        if self.id is not None:
            b.write(String(self.id))
        
        if self.shipping_options is not None:
            b.write(Vector(self.shipping_options))
        
        return b.getvalue()
