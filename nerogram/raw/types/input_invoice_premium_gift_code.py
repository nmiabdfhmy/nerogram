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


class InputInvoicePremiumGiftCode(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.InputInvoice`.

    Details:
        - Layer: ``166``
        - ID: ``98986C0D``

    Parameters:
        purpose (:obj:`InputStorePaymentPurpose <nerogram.raw.base.InputStorePaymentPurpose>`):
            N/A

        option (:obj:`PremiumGiftCodeOption <nerogram.raw.base.PremiumGiftCodeOption>`):
            N/A

    """

    __slots__: List[str] = ["purpose", "option"]

    ID = 0x98986c0d
    QUALNAME = "types.InputInvoicePremiumGiftCode"

    def __init__(self, *, purpose: "raw.base.InputStorePaymentPurpose", option: "raw.base.PremiumGiftCodeOption") -> None:
        self.purpose = purpose  # InputStorePaymentPurpose
        self.option = option  # PremiumGiftCodeOption

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputInvoicePremiumGiftCode":
        # No flags
        
        purpose = TLObject.read(b)
        
        option = TLObject.read(b)
        
        return InputInvoicePremiumGiftCode(purpose=purpose, option=option)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.purpose.write())
        
        b.write(self.option.write())
        
        return b.getvalue()
