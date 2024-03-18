# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/official_python_method.py

This file declares the OfficialPythonMethod class.

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
from .method_def import MethodDef
from .python_method import PythonMethod
from pythoneda.shared import primary_key_attribute
from typing import Callable


class OfficialPythonMethod(PythonMethod):
    """
    Models Python methods read directly from .py files.

    Class name: OfficialPythonMethod

    Responsibilities:
        - Represent a Python method from a .py file.

    Collaborators:
        - None
    """

    def __init__(self, methodDef: MethodDef, method: Callable):
        """
        Creates a new PythonMethod instance.
        :param methodDef: The method definition.
        :type methodDef: pythoneda.sandbox.poc.cac.MethodDef
        :param method: The method.
        :type method: Callable
        """
        super().__init__(methodDef)
        self._method = method

    @property
    def method(self) -> Callable:
        """
        Retrieves the method.
        :return: Such instance.
        :rtype: Callable
        """
        return self._method

    @property
    def body(self) -> str:
        """
        Retrieves the method body.
        :return: The content.
        :rtype: str
        """
        import inspect

        actual_method = self.method
        if isinstance(actual_method, property):
            actual_method = actual_method.fget

        if isinstance(actual_method, classmethod):
            actual_method = actual_method.__func__

        return inspect.getsource(actual_method)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
