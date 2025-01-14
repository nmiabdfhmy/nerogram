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


class SavedInfo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.payments.SavedInfo`.

    Details:
        - Layer: ``166``
        - ID: ``FB8FE43C``

    Parameters:
        has_saved_credentials (``bool``, *optional*):
            N/A

        saved_info (:obj:`PaymentRequestedInfo <nerogram.raw.base.PaymentRequestedInfo>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            payments.GetSavedInfo
    """

    __slots__: List[str] = ["has_saved_credentials", "saved_info"]

    ID = 0xfb8fe43c
    QUALNAME = "types.payments.SavedInfo"

    def __init__(self, *, has_saved_credentials: Optional[bool] = None, saved_info: "raw.base.PaymentRequestedInfo" = None) -> None:
        self.has_saved_credentials = has_saved_credentials  # flags.1?true
        self.saved_info = saved_info  # flags.0?PaymentRequestedInfo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedInfo":
        
        flags = Int.read(b)
        
        has_saved_credentials = True if flags & (1 << 1) else False
        saved_info = TLObject.read(b) if flags & (1 << 0) else None
        
        return SavedInfo(has_saved_credentials=has_saved_credentials, saved_info=saved_info)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.has_saved_credentials else 0
        flags |= (1 << 0) if self.saved_info is not None else 0
        b.write(Int(flags))
        
        if self.saved_info is not None:
            b.write(self.saved_info.write())
        
        return b.getvalue()
