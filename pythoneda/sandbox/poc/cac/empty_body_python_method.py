# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/empty_body_python_method.py

This file declares the EmptyBodyPythonMethod class.

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
from .python_method import PythonMethod
from .python_method_def import PythonMethodDef
from pythoneda.shared import primary_key_attribute


class EmptyBodyPythonMethod(PythonMethod):
    """
    An empty implementation of any Python method.

    Class name: EmptyBodyPythonMethod

    Responsibilities:
        - Represent the empty implementation of any Python method.

    Collaborators:
        - None
    """

    def __init__(self, pythonMethodDef: PythonMethodDef):
        """
        Creates a new EmptyBodyPythonMethod instance.
        :param pythonMethodDef: The method definition.
        :type pythonMethodDef: pythoneda.sandbox.poc.cac.PythonMethodDef
        """
        super().__init__(pythonMethodDef)

    @property
    @primary_key_attribute
    def body(self) -> str:
        """
        Retrieves the method body.
        :return: The content.
        :rtype: str
        """
        return "pass"


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
