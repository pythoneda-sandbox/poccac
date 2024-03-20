# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/dependency_import.py

This file declares the DependencyImport class.

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


class DependencyImport(BaseObject):
    """
    Models imports.

    Class name: DependencyImport

    Responsibilities:
        - Represent an import.

    Collaborators:
        - None
    """

    def __init__(self, package: str):
        """
        Creates a new Import instance.
        :param package: The import package.
        :type package: str
        """
        super().__init__()
        self._package = package

    @property
    @primary_key_attribute
    def package(self) -> str:
        """
        Retrieves the package
        :return: Such package.
        :rtype: str
        """
        return self._package


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
