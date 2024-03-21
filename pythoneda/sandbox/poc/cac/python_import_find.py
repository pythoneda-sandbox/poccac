# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/python_import_find.py

This file declares the PythonImportFind class.

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
import ast
from .python_import import PythonImport
from pythoneda.shared import BaseObject, primary_key_attribute
from typing import Callable, List


class PythonImportFind(ast.NodeVisitor, BaseObject):
    """
    Logic to find imports in Python source code.

    Class name: PythonImportFind

    Responsibilities:
        - Parse Python source code looking for `import` statements.

    Collaborators:
        - None
    """

    def __init__(self, source: str, methodName: str = None):
        """
        Creates a new PythonImportFind instance.
        :param source: The source code.
        :type source: str
        """
        super().__init__()
        self._source = source
        self._method_name = methodName
        self._imports = []
        self._in_target_method = False
        self._find_imports(source)

    @property
    @primary_key_attribute
    def source(self) -> str:
        """
        Retrieves the source code.
        :return: Such code.
        :rtype: str
        """
        return self._source

    @property
    @primary_key_attribute
    def method_name(self) -> str:
        """
        Retrieves the method name.
        :return: Such information.
        :rtype: str
        """
        return self._method_name

    @property
    @primary_key_attribute
    def imports(self) -> List[PythonImport]:
        """
        Retrieves the imports.
        :return: Such list.
        :rtype: List[pythoneda.sandbox.poc.cac.PythonImport]
        """
        return self._imports

    def visit_FunctionDef(self, node):
        """
        Visits a `FunctionDef` node.
        :param node: The node to visit.
        :type node: ast.FunctionDef
        """
        if self.method_name:
            self.visit_FunctionDef_with_method_name(node)
        else:
            self.generic_visit(node)

    def visit_FunctionDef_with_method_name(self, node):
        """
        Visits a `FunctionDef` node, looking for the target method.
        :param node: The node to visit.
        :type node: ast.FunctionDef
        """
        if node.name == self.method_name:
            self._in_target_method = True
            self.generic_visit(node)
            self._in_target_method = False
        else:
            # Visit other methods/functions in case of nested definitions but avoid collecting imports.
            original_in_target_method = self._in_target_method
            self._in_target_method = False
            self.generic_visit(node)
            self._in_target_method = original_in_target_method

    def visit_Import(self, node: ast.Import) -> None:
        """
        Visits an `import` statement node.
        :param node: The node to visit.
        :type node: ast.Import
        """
        if not self.method_name or self._in_target_method:
            for alias in node.names:
                self._imports.append(PythonImport(alias.name))
            self.generic_visit(node)

    def visit_ImportFrom(self, node):
        """
        Visits a `import from` node.
        :param node: The node to visit.
        :type node: ast.FunctionDef
        """
        if not self.method_name or self._in_target_method:
            module = node.module if node.module else "built-in"
            for alias in node.names:
                imported = (
                    PythonImport(module, alias.name)
                    if module != "built-in"
                    else PythonImport(alias.name)
                )
                self._imports.append(imported)
            self.generic_visit(node)

    def _find_imports(self, source: str) -> None:
        """
        Finds imports in the given source code.
        :param source: The source code.
        :type source: str
        """
        tree = ast.parse(source)
        self.visit(tree)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
