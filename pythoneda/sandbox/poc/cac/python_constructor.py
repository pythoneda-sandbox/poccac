# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/python_constructor.py

This file declares the PythonConstructor class.

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
from pythoneda.shared import BaseObject, primary_key_attribute


class PythonConstructor(BaseObject):
    """
    Models the Python constructors.

    Class name: PythonConstructor

    Responsibilities:
        - Represent a Python constructor.

    Collaborators:
        - None
    """

    def __init__(self, description: str):
        """
        Creates a new PythonConstructor instance.
        :param description: The description.
        :type description: str
        """
        super().__init__()
        self._description = description

    @property
    def description(self) -> str:
        """
        Retrieves the description.
        :return: The description.
        :rtype: str
        """
        return self._description

    @property
    def content(self) -> str:
        """
        Provides the constructor content.
        :return: Such content.
        :rtype: str
        """
        return f'''
def __init__(self):
    """
    {self.description}
    """
    super().__init__()'''


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
