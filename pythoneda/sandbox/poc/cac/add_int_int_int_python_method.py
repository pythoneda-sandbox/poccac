# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/add_int_int_int_python_method.py

This file declares the AddIntIntIntPythonMethod class.

Copyright (C) 2024-today rydnr's pythoneda-sandbox/poccac

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from .add_int_int_int_python_method_def import AddIntIntIntPythonMethodDef
from .method_def import MethodDef
from .python_method import PythonMethod
from pythoneda.shared import primary_key_attribute


class AddIntIntIntPythonMethod(PythonMethod):
    """
    The implementation of add(self, x:int, y:int) -> int: Python method.

    Class name: AddIntIntIntPythonMethod

    Responsibilities:
        - Represent the trivial implementation of add(self, x:int, y:int) -> int: in Python.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new AddIntIntIntPythonMethod instance.
        """
        super().__init__(AddIntIntIntPythonMethodDef())

    @property
    @primary_key_attribute
    def body(self) -> str:
        """
        Retrieves the method body.
        :return: The content.
        :rtype: str
        """
        return "return x + y"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
