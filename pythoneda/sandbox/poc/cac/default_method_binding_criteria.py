# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/default_method_binding_criteria.py

This file declares the DefaultMethodBindingCriteria class.

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
from .method_binding_criteria import MethodBindingCriteria
from .method_def import MethodDef
from .python_method import PythonMethod


class DefaultMethodBindingCriteria(MethodBindingCriteria):
    """
    Defines the default criteria for resolving method implementations.

    Class name: DefaultMethodBindingCriteria

    Responsibilities:
        - Represent the default criteria for resolving method implementations.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DefaultMethodBindingCriteria instance.
        """
        super().__init__()

    def is_satisfied_by(self, methodDef: MethodDef, method: PythonMethod) -> bool:
        """
        Determines if the given method satisfies the criteria.
        :param method: The method implementation to evaluate.
        :type method: pythoneda.sandbox.poc.cac.PythonMethod
        :return: True if the method satisfies the criteria, False otherwise.
        :rtype: bool
        """
        return method.method_def == methodDef


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
