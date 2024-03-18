# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/test_build_class_should.py

This file defines tests to build classes.

Copyright (C) 2024-today rydnr's https://github.com/pythoneda-sandbox/poccac

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
import asyncio
from hypothesis import given, settings
import hypothesis.strategies as st
import os
import pytest
from pythoneda.shared import BaseObject
from pythoneda.sandbox.poc.cac import (
    ClassDef,
    DefaultMethodBindingCriteria,
    PythonConstructorDef,
    PythonMethodDef,
    MethodBindingCriteria,
    MethodParameter,
)
from pythoneda.shared.git import GitRepo
import string


@settings(deadline=None)
@given(st.text(alphabet=string.ascii_letters, min_size=1))
@pytest.mark.asyncio
async def test_TODO_rename_(name: str):
    # given
    constructor_def = PythonConstructorDef(
        "Builds a new Sample instance",
        [MethodParameter("token", "str", "The github token")],
    )
    metadata = {
        "relative_file_path": "sample.py",
        "module_name": "pythoneda.sandbox.poc.cac.sample",
        "author": "rydnr",
        "start_year": "2024",
        "ref_url": "https://github.com/pythoneda-sandbox/poccac",
        "class_description": "Models the Sample abstraction.",
        "class_responsibilities": "Represent the Sample abstraction.",
        "class_collaborators": "None",
    }
    methods = []
    methods.append(
        PythonMethodDef("github_token", "str", "Retrieves the GitHub token.")
    )
    methods.append(
        PythonMethodDef("git_repository", GitRepo, "Retrieves the git repository.")
    )
    methods.append(
        PythonMethodDef(
            "rename_to",
            None,
            "Renames the class.",
            [MethodParameter("name", "str", "The new name")],
        )
    )
    methods.append(
        PythonMethodDef(
            "renamed_to",
            "bool",
            "Checks if the class was renamed.",
            [MethodParameter("newName", "str", "The new name")],
        )
    )
    methods.append(
        PythonMethodDef(
            "_rename_myself",
            None,
            "Renames Sample to something else.",
            [MethodParameter("name", "str", "The new name")],
        )
    )
    methods.append(PythonMethodDef("components", "List", "Retrieves the components."))
    sut = ClassDef(
        "Sample",
        [BaseObject],
        constructor_def,
        methods,
        metadata,
        DefaultMethodBindingCriteria(),
    )

    # when
    await sut.rename_import("pythoneda", "pinnith")

    # then
    assert await renamed(sut, name)


async def renamed(comp, newName) -> bool:
    return comp and await comp.renamed_to(newName)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
