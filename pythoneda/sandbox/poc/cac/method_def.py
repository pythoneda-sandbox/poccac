# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/method_def.py

This file declares the MethodDef class.

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
import abc
from pythoneda.shared import attribute, primary_key_attribute, ValueObject
from .method_parameter import MethodParameter
from typing import Callable, List


class MethodDef(ValueObject):
    """
    Models method definitions.

    Class name: MethodDef

    Responsibilities:
        - Represent a method definition.

    Collaborators:
        - None
    """

    def __init__(
        self,
        name: str,
        returnType: str,
        doc: str,
        parameters: List[MethodParameter] = [],
        returnDoc: str = None,
        method: Callable = None,
    ):
        """
        Creates a new MethodDef instance.
        :param name: The method name.
        :type name: str
        :param returnType: The return type.
        :type returnType: str
        :param doc: The parameter documentation.
        :type doc: str
        :param defaultValue: The default value.
        :type defaultValue: str
        :param returnDoc: The documentation for the return value.
        :type returnDoc: str
        :param method: The method instance.
        :type method: Callable
        """
        super().__init__()
        self._name = name
        self._return_type = returnType
        self._doc = doc
        self._parameters = parameters
        self._return_doc = returnDoc
        self._method = method

    @classmethod
    def from_method(cls, method: Callable) -> "MethodDef":
        """
        Creates a MethodDef instance for given method.
        :param method: The method.
        :type method: function
        :return: The new MethodDef instance.
        :rtype: Callable
        """
        import inspect

        actual_method = method
        if isinstance(actual_method, property):
            actual_method = actual_method.fget

        if isinstance(actual_method, classmethod):
            actual_method = actual_method.__func__

        signature = inspect.signature(actual_method)
        return MethodDef(
            actual_method.__name__,
            signature.return_annotation,
            method.__doc__,
            "[no return doc]",
            method,
        )

    @property
    @primary_key_attribute
    def name(self) -> str:
        """
        Retrieves the parameter name.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    @primary_key_attribute
    def return_type(self) -> str:
        """
        Retrieves the return type.
        :return: The type of the value returned.
        :rtype: str
        """
        return self._return_type

    @property
    @attribute
    def doc(self) -> str:
        """
        Retrieves the parameter documentation.
        :return: Such text.
        :rtype: str
        """
        return self._doc

    @property
    @attribute
    def parameters(self) -> List[MethodParameter]:
        """
        Retrieves the parameters.
        :return: Such list.
        :rtype: List[pythoneda.sandbox.poc.cac.MethodParameter]
        """
        return self._parameters

    @property
    @attribute
    def return_doc(self) -> str:
        """
        Retrieves the documentation for the return value.
        :return: Such text.
        :rtype: str
        """
        return self._return_doc

    @property
    @attribute
    def method(self) -> Callable:
        """
        Retrieves the method instance.
        :return: Such instance.
        :rtype: Callable
        """
        return self._method

    @property
    @abc.abstractmethod
    def content(self) -> str:
        """
        Retrieves the content.
        :return: Such content.
        :rtype: str
        """
        pass


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
