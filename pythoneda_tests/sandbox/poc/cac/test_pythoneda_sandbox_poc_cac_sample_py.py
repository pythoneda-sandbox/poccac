# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/test_pythoneda_sandbox_poc_cac_sample_py.py

This file defines tests for PythonedaSandboxPocCacSamplePy.

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
import pytest
from pythoneda.sandbox.poc.cac import (
    DefaultMethodBindingCriteria,
    EmptyBodyPythonMethodBindingCriteria,
    PythonedaSandboxPocCacSamplePy,
)


@pytest.mark.asyncio
async def test_default_criteria():
    sut = PythonedaSandboxPocCacSamplePy(DefaultMethodBindingCriteria())

    assert sut is not None
    assert sut.relative_file_path == "pythoneda/sandbox/poc/cac/sample.py"
    expected = target_default()
    actual = await sut.content
    assert expected == actual, f"Expected:\n{expected!r}\nActual:\n{actual!r}"


@pytest.mark.asyncio
async def test_wip():
    sut = PythonedaSandboxPocCacSamplePy(EmptyBodyPythonMethodBindingCriteria())

    assert sut is not None
    assert sut.relative_file_path == "pythoneda/sandbox/poc/cac/sample.py"
    expected = target_empty()
    actual = await sut.content
    assert expected == actual, f"Expected:\n{expected!r}\nActual:\n{actual!r}"


def target_default() -> str:
    return '''
# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/sample.py

This file defines the Sample class.

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
from pythoneda.shared import BaseObject


class Sample(BaseObject):
    """
    A class used to show the Code-as-Code approach.

    Class name: Sample

    Responsibilities:
        - Show a sample code.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new Sample instance.
        """
        super().__init__()

    def add(self, x:int, y:int) -> int:
        """
        Adds two numbers.
        :param x: The first number.
        :type x: int
        :param y: The second number.
        :type y: int
        :return: The sum of the two numbers.
        :rtype: int
        """
        return x + y


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:'''


def target_empty() -> str:
    return '''
# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/sample.py

This file defines the Sample class.

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
from pythoneda.shared import BaseObject


class Sample(BaseObject):
    """
    A class used to show the Code-as-Code approach.

    Class name: Sample

    Responsibilities:
        - Show a sample code.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new Sample instance.
        """
        super().__init__()

    def add(self, x:int, y:int) -> int:
        """
        Adds two numbers.
        :param x: The first number.
        :type x: int
        :param y: The second number.
        :type y: int
        :return: The sum of the two numbers.
        :rtype: int
        """
        pass


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:'''
