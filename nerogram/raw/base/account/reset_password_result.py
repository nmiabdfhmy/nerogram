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

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from nerogram import raw
from nerogram.raw.core import TLObject

ResetPasswordResult = Union[raw.types.account.ResetPasswordFailedWait, raw.types.account.ResetPasswordOk, raw.types.account.ResetPasswordRequestedWait]


# noinspection PyRedeclaration
class ResetPasswordResult:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 3 constructors available.

        .. currentmodule:: nerogram.raw.types

        .. autosummary::
            :nosignatures:

            account.ResetPasswordFailedWait
            account.ResetPasswordOk
            account.ResetPasswordRequestedWait

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: nerogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.ResetPassword
    """

    QUALNAME = "nerogram.raw.base.account.ResetPasswordResult"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.nerogram.org/telegram/base/reset-password-result")
