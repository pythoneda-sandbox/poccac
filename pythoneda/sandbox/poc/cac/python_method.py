# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/python_method.py

This file declares the PythonMethod class.

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
from pythoneda.shared import attribute, BaseObject, primary_key_attribute
from .method_def import MethodDef


class PythonMethod(BaseObject):
    """
    Models Python methods.

    Class name: PythonMethod

    Responsibilities:
        - Represent a Python method.

    Collaborators:
        - None
    """

    def __init__(self, methodDef: MethodDef, body: str):
        """
        Creates a new PythonMethod instance.
        :param methodDef: The method definition.
        :type methodDef: pythoneda.sandbox.poc.cac.MethodDef
        :param body: The method body.
        :type body: str
        """
        super().__init__()
        self._method_def = methodDef
        self._body = body

    @property
    @primary_key_attribute
    def method_def(self) -> MethodDef:
        """
        Retrieves the method definition.
        :return: Such definition.
        :rtype: pythoneda.sandbox.poc.cac.MethodDef
        """
        return self._method_def

    @property
    @primary_key_attribute
    def body(self) -> str:
        """
        Retrieves the method body.
        :return: The content.
        :rtype: str
        """
        return self._body


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
