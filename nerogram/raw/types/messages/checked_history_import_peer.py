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


class CheckedHistoryImportPeer(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~nerogram.raw.base.messages.CheckedHistoryImportPeer`.

    Details:
        - Layer: ``166``
        - ID: ``A24DE717``

    Parameters:
        confirm_text (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.CheckHistoryImportPeer
    """

    __slots__: List[str] = ["confirm_text"]

    ID = 0xa24de717
    QUALNAME = "types.messages.CheckedHistoryImportPeer"

    def __init__(self, *, confirm_text: str) -> None:
        self.confirm_text = confirm_text  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "CheckedHistoryImportPeer":
        # No flags
        
        confirm_text = String.read(b)
        
        return CheckedHistoryImportPeer(confirm_text=confirm_text)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.confirm_text))
        
        return b.getvalue()
