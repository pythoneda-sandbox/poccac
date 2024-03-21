# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/python_import.py

This file declares the PythonImport class.

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
from .dependency_import import DependencyImport
from pythoneda.shared import primary_key_attribute


class PythonImport(DependencyImport):
    """
    Models Python imports.

    Class name: PythonImport

    Responsibilities:
        - Represent a Python import.

    Collaborators:
        - None
    """

    def __init__(self, package: str, asset: str = None):
        """
        Creates a new PythonImport instance.
        :param package: The import package.
        :type package: str
        :param asset: The name of the asset.
        :type asset: str
        """
        super().__init__(package)
        self._asset = asset

    @property
    @primary_key_attribute
    def asset(self) -> str:
        """
        Retrieves the asset.
        :return: The name of the asset within the package.
        :rtype: str
        """
        return self._asset

    async def rename(
        self,
        oldPackage: str,
        newPackage: str,
        oldAsset: str = None,
        newAsset: str = None,
    ):
        """
        Renames the import to a new name.
        :param oldPackage: The old package.
        :type oldPackage: str
        :param newPackage: The new package.
        :type newPackage: str
        :param oldAsset: The old asset.
        :type oldAsset: str
        :param newAsset: The new asset.
        :type newAsset: str
        """
        if self._package == oldPackage:
            self._package = newPackage
            if oldAsset and self._asset == oldAsset:
                self._asset = newAsset


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
