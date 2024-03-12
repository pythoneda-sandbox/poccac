# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/test_sample_should.py

This file defines tests for Sample as an abstraction.

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
from pythoneda.sandbox.poc.cac import Sample
import string


@settings(deadline=None)
@given(st.text(alphabet=string.ascii_letters, min_size=1))
@pytest.mark.asyncio
async def test_TODO_rename_(name: str):
    # given
    sut = Sample(os.environ.get("GITHUB_TOKEN", None))

    # when
    await sut._rename_myself(name)

    # then
    assert await renamed(sut, name)


@settings(deadline=None)
@given(st.text(alphabet=string.ascii_letters, min_size=1))
@pytest.mark.asyncio
async def test_TODO_rename__(name):
    # given
    sut = Sample(os.environ.get("GITHUB_TOKEN", None))
    components = await sut.components

    # when
    # await sut.rename_to(name)

    # then
    assert True  # all([await renamed(c, name) for c in components])


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
