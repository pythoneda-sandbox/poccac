# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/method_parameter.py

This file declares the MethodParameter class.

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


class MethodParameter(BaseObject):
    """
    Models method parameters.

    Class name: MethodParameter

    Responsibilities:
        - Represent a method parameter.

    Collaborators:
        - None
    """

    def __init__(
        self, name: str, parameterType: str, doc: str, defaultValue: str = None
    ):
        """
        Creates a new MethodParameter instance.
        :param name: The parameter name.
        :type name: str
        :param parameterType: The parameter type.
        :type parameterType: str
        :param doc: The parameter documentation.
        :type doc: str
        :param defaultValue: The default value.
        :type defaultValue: str
        """
        super().__init__()
        self._name = name
        self._parameter_type = parameterType
        self._doc = doc
        self._default_value = defaultValue

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
    def parameter_type(self) -> str:
        """
        Retrieves the parameter type.
        :return: The type of the parameter.
        :rtype: str
        """
        return self._parameter_type

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
    def default_value(self) -> str:
        """
        Retrieves the default value, if any.
        :return: Such value.
        :rtype: str
        """
        return self._default_value


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
