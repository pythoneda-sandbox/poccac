# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/domain_artifact.py

This file declares the DomainArtifact class.

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
from .artifact_metadata import ArtifactMetadata
from pythoneda.shared import BaseObject
from typing import Tuple


class DomainArtifact(BaseObject):
    """
    The artifact representation of a domain.

    Class name: DomainArtifact

    Responsibilities:
        - Artifact-scope operations for a domain.

    Collaborators:
        - pythoneda.sandbox.poc.cac.ArtifactMetadata
        - pythoneda.sandbox.poc.cac.ClassArtifact
    """

    def __init__(self, name: str, metadata: ArtifactMetadata = None):
        """
        Creates a new DomainArtifact instance.
        :param name: The domain name.
        :type name: str
        :param metadata: The metadata.
        :type metadata: pythoneda.sandbox.poc.cac.ArtifactMetadata
        """
        super().__init__()
        self._name = name
        self._metadata = metadata

    @property
    def name(self) -> str:
        """
        Retrieves the domain name.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    def metadata(self) -> ArtifactMetadata:
        """
        Retrieves the metadata.
        :return: Such metadata.
        :rtype: pythoneda.sandbox.poc.cac.ArtifactMetadata
        """
        return self._metadata

    @property
    def start_year(self) -> int:
        """
        Retrieves the starting year.
        :return: Such information.
        :rtype: int
        """
        return self.metadata.start_year

    @property
    def author(self) -> str:
        """
        Retrieves the author.
        :return: Such information.
        :rtype: str
        """
        return self.metadata.author

    @property
    def ref_url(self) -> str:
        """
        Retrieves the reference url.
        :return: Such information.
        :rtype: str
        """
        return self.metadata.ref_url

    @property
    def github_organization(self) -> str:
        """
        Retrieves the github organization.
        :return: Such information.
        :rtype: str
        """
        return self.metadata.github_organization

    @property
    def github_name(self) -> str:
        """
        Retrieves the github repository name.
        :return: Such information.
        :rtype: str
        """
        return self.metadata.github_name

    @property
    def copyright_preamble(self) -> str:
        """
        Retrieves the copyright preamble.
        :return: Such content.
        :rtype: str
        """
        return self.metadata.copyright_preamble

    @property
    def copyright_preamble_for_st(self) -> str:
        """
        Retrieves the copyright preamble for StringTemplate.
        :return: Such content.
        :rtype: str
        """
        return self.metadata.copyright_preamble_for_st

    async def rename_imports(
        self,
        oldPackage: str,
        newPackage: str,
        oldAsset: str = None,
        newAsset: str = None,
    ) -> None:
        """
        Renames the matching imports.
        :param oldPackage: The old package.
        :type oldPackage: str
        :param newPackage: The new package.
        :type newPackage: str
        :param oldAsset: The old asset.
        :type oldAsset: str
        :param newAsset: The new asset.
        :type newAsset: str
        """
        pass

    async def rename(self, newName: str) -> None:
        """
        Renames the domain.
        :param newName: The new name.
        :type newName: str
        """
        from pythoneda.shared.git.github import RepositoryAccess

        await RepositoryAccess(self.metadata.github_token).rename_to(
            self.github_organization, self.github_name, newName
        )

    async def find_classes(self) -> Tuple[str, str]:
        """
        Recursively enumerates all classes defined in the domain package.
        :return: Such classes.
        :rtype: Tuple[str, str]
        """
        import pkgutil
        import inspect
        import importlib

        result = set()

        def inspect_module(module):
            for name, obj in inspect.getmembers(module, inspect.isclass):
                # Ensure the class is defined in this module (compare __module__ attribute)
                if obj.__module__ == module.__name__:
                    result.add((module.__name__, name))

            # Recursively search for submodules
            if hasattr(module, "__path__"):  # Check if module is a package
                for _, submod_name, _ in pkgutil.walk_packages(module.__path__):
                    try:
                        submod = importlib.import_module(
                            f"{module.__name__}.{submod_name}"
                        )
                        inspect_module(submod)
                    except ImportError as e:
                        print(f"Error importing module: {e}")

        package = importlib.import_module(self.metadata.package)
        inspect_module(self.metadata.package)

        return result


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
