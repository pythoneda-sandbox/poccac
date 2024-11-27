# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/artifact_metadata.py

This file declares the ArtifactMetadata class.

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
from typing import Any, Callable, Dict


class ArtifactMetadata(BaseObject):
    """
    The metadata common to artifacts.

    Class name: ArtifactMetadata

    Responsibilities:
        - Provide metadata.

    Collaborators:
        - None
    """

    def __init__(self, metadata: Dict[str, str]):
        """
        Creates a new ArtifactMetadata instance.
        :param metadata: The metadata.
        :type metadata: Dict[str, str]
        """
        super().__init__()
        self._metadata = metadata

    @classmethod
    def from_dict(cls, metadata: Dict[str, str]) -> "ArtifactMetadata":
        """
        Creates a new metadata instance from given dictionary.
        :param metadata: The dictionary.
        :type metadata: Dict[str,str]
        :return: The metadata instance.
        :rtype: pythoneda.sandbox.poc.cac.ArtifactMetadata
        """
        return ArtifactMetadata(metadata)

    def get(self, key: str, defaultValueFn: Callable[[], Any]) -> Any:
        """
        Retrieves a metadata entry under given key. If it's not found, it returns a default value.
        :param key: The entry key.
        :type key: str
        :param defaultValueFn: A function to retrieve the default value.
        :type defaultValue: Callable[[str],Any]
        :return: The entry value.
        :rtype: Any
        """
        result = self._metadata.get(key, None)
        if result is None:
            result = defaultValueFn()
            self._metadata[key] = result

        return result

    def set(self, key: str, value: Any):
        """
        Stores a metadata entry under given key.
        :param key: The entry key.
        :type key: str
        :param value: The value.
        :type value: Any
        """
        self._metadata[key] = value

    def _current_year(self) -> int:
        """
        Retrieves the current year.
        :return: Such information.
        :rtype: int
        """
        import datetime

        return datetime.datetime.now().year

    @property
    def start_year(self) -> int:
        """
        Retrieves the starting year.
        :return: Such information.
        :rtype: int
        """
        return self.get("start_year", self._current_year)

    @property
    def author(self) -> str:
        """
        Retrieves the author.
        :return: Such information.
        :rtype: str
        """
        return self.get("author", lambda: "[unknown author]")

    @property
    def package_name(self) -> str:
        """
        Retrieves the name of the package.
        :return: Such information.
        :rtype: str
        """
        return self.get("package_name", lambda: None)

    @property
    def github_token(self) -> str:
        """
        Retrieves the github token.
        :return: Such information.
        :rtype: str
        """
        return self.get("github_token", lambda: None)

    @property
    def ref_url(self) -> str:
        """
        Retrieves the reference url.
        :return: Such information.
        :rtype: str
        """
        return self.get("ref_url", lambda: "[unknown url]")

    @classmethod
    def extract_github_organization_from(self, url: str) -> str:
        """
        Extracts the organization name from a github url.
        :param url: Such url.
        :type url: str
        :return: The organization name.
        :rtype: str
        """
        from pythoneda.shared.git import GitRepo

        return GitRepo.extract_repo_owner_and_repo_name(url)[0]

    @classmethod
    def extract_github_name_from(self, url: str) -> str:
        """
        Extracts the repository name from a github url.
        :param url: Such url.
        :type url: str
        :return: The repository name.
        :rtype: str
        """
        from pythoneda.shared.git import GitRepo

        return GitRepo.extract_repo_owner_and_repo_name(url)[1]

    @property
    def github_organization(self) -> str:
        """
        Retrieves the github organization.
        :return: Such information.
        :rtype: str
        """
        return self.get(
            "github_organization",
            lambda: self.__class__.extract_github_organization_from(self.ref_url),
        )

    @property
    def github_name(self) -> str:
        """
        Retrieves the github repository name.
        :return: Such information.
        :rtype: str
        """
        from pythoneda.shared.git import GitRepo

        return self.get(
            "github_name",
            lambda: self.__class__.extract_github_name_from(self.ref_url),
        )

    @property
    def copyright_preamble(self) -> str:
        """
        Retrieves the copyright preamble.
        :return: Such content.
        :rtype: str
        """
        return self.get(
            "copyright_preamble",
            lambda: f"""Copyright (C) {self.start_year}-today {self.author}'s {self.ref_url}

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses.""",
        )

    @property
    def copyright_preamble_for_st(self) -> str:
        """
        Retrieves the copyright preamble for StringTemplate.
        :return: Such content.
        :rtype: str
        """
        return "\n// ".join(self.copyright_preamble.split("\n"))


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
