# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/add_int_int_int_python_method_def.py

This file declares the AddIntIntIntPythonMethodDef class.

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
from .method_parameter import MethodParameter
from .python_method_def import PythonMethodDef
from pythoneda.shared import primary_key_attribute


class AddIntIntIntPythonMethodDef(PythonMethodDef):
    """
    The definition of add(self, x:int, y:int) -> int: Python method.

    Class name: AddIntIntIntPythonMethodDef

    Responsibilities:
        - Represent the Python definition of the add(self, x:int, y:int) -> int: method.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new AddIntIntIntPythonMethodDef instance.
        """
        super().__init__(
            "add",
            "int",
            "Adds two numbers.",
            [
                MethodParameter("x", "int", "The first number."),
                MethodParameter("y", "int", "The second number."),
            ],
            "The sum of the two numbers.",
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
