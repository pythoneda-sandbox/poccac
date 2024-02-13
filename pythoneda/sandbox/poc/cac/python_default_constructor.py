# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/python_default_constructor.py

This file declares the PythonDefaultConstructor class.

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
from .python_constructor import PythonConstructor


class PythonDefaultConstructor(PythonConstructor):
    """
    Models the Python default constructor.

    Class name: PythonDefaultConstructor

    Responsibilities:
        - Represent the Python default constructor

    Collaborators:
        - None
    """

    def __init__(self, className: str):
        """
        Creates a new PythonDefaultConstructor instance.
        :param className: The class name.
        :type className: str
        """
        super().__init__(f"Creates a new {className} instance.")


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
