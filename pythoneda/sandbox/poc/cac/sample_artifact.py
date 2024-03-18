# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/sample.py

This file declares the Sample class.

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
from pythoneda.shared import BaseObject
from pythoneda.shared.git import GitRepo
from pythoneda.shared.git.github import RepositoryAccess
from typing import List


class Sample(BaseObject):
    """
    Models the Sample abstraction.

    Class name: Sample

    Responsibilities:
        - Represent the Sample abstraction.

    Collaborators:
        - None
    """

    def __init__(self, token: str):
        """
        Creates a new Sample instance.
        :param token: The GitHub token.
        :type token: str
        """
        super().__init__()
        self._github_token = token

    @property
    def github_token(self) -> str:
        """
        Retrieves the GitHub token.
        :return: Such token.
        :rtype: str
        """
        return self._github_token

    @property
    async def git_repository(self) -> GitRepo:
        """
        Retrieves the git repository.
        :return: Such repository.
        :rtype: pythoneda.shared.git.GitRepo
        """
        return await RepositoryAccess(self.github_token).fetch(
            "pythoneda-shared-git", "shared"
        )

    async def rename_to(self, name: str) -> None:
        """
        Renames Sample to something else.
        :param name: The new name.
        :type name: str
        """
        await self._rename_myself(name)
        for component in await self.components:
            await component.rename_to(name)

    async def renamed_to(self, newName: str) -> bool:
        """
        Checks if this repository has been renamed.
        :param newName: The new name.
        :type newName: str
        :return: True if renamed.
        :rtype: bool
        """
        return True

    async def _rename_myself(self, name: str) -> None:
        """
        Renames Sample to something else.
        :param name: The new name.
        :type name: str
        """
        self.__class__.__name__ = name

    @property
    async def components(self) -> List:
        """
        Retrieves the Sample components.
        :return: Such items.
        :rtype: List
        """
        return [await self.git_repository]


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
