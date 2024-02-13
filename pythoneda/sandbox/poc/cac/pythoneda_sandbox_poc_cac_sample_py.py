# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/pythoneda_sandbox_poc_cac_sample_py.py

This file declares the PythonedaSandoxPocCacSamplePy class.

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
from io import StringIO
from .python_default_constructor import PythonDefaultConstructor
from .python_import import PythonImport
from .method_parameter import MethodParameter
from .python_method_def import PythonMethodDef
from .python_method import PythonMethod
from pythoneda.shared import BaseObject
from stringtemplate3 import StringTemplateGroup
from typing import List


class PythonedaSandboxPocCacSamplePy(BaseObject):
    """
    Models the pythoneda/sandbox/poc/cac/sample.py file.

    Class name: PythonedaSandboxPocCacSamplePy

    Responsibilities:
        - Represent the pythoneda/sandbox/poc/cac/sample.py file.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new PythonedaSandboxPocCacSamplePy instance.
        """
        super().__init__()
        self._relative_file_path = "pythoneda/sandbox/poc/cac/sample.py"
        self._file_description = "This file defines the Sample class."
        self._copyright_preamble = """Copyright (C) 2024-today rydnr's https://github.com/pythoneda-sandbox/poccac

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
        self._imports = [PythonImport("pythoneda.shared", "BaseObject")]
        self._name = "Sample"
        self._parents = ["BaseObject"]
        self._class_description = "A class used to show the Code-as-Code approach."
        self._class_responsibilities = ["Show a sample code."]
        self._class_collaborators = []
        self._constructor = PythonDefaultConstructor(self.name)
        self._method_defs = [
            PythonMethodDef(
                "add",
                "int",
                "Adds two numbers.",
                [
                    MethodParameter("x", "int", "The first number."),
                    MethodParameter("y", "int", "The second number."),
                ],
                "The sum of the two numbers.",
            )
        ]

    @property
    def relative_file_path(self) -> str:
        """
        Retrieves the relative file path.
        :return: Such path.
        :rtype: str
        """
        return self._relative_file_path

    @property
    def file_description(self) -> str:
        """
        Retrieves the file description.
        :return: Such description.
        :rtype: str
        """
        return self._file_description

    @property
    def copyright_preamble(self) -> str:
        """
        Retrieves the copyright preamble.
        :return: Such content.
        :rtype: str
        """
        return self._copyright_preamble

    @property
    def imports(self) -> List[PythonImport]:
        """
        Retrieves the imports.
        :return: Such imports.
        :rtype: List[pythoneda.sandbox.poc.cac.python_import.PythonImport]
        """
        return self._imports

    @property
    def name(self) -> str:
        """
        Retrieves the name.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    def parents(self) -> List[str]:
        """
        Retrieves the parents.
        :return: Such parents.
        :rtype: List[str]
        """
        return self._parents

    @property
    def class_description(self) -> str:
        """
        Retrieves the class description.
        :return: Such description.
        :rtype: str
        """
        return self._class_description

    @property
    def class_responsibilities(self) -> List[str]:
        """
        Retrieves the class responsibilities.
        :return: Such responsibilities.
        :rtype: List[str]
        """
        return self._class_responsibilities

    @property
    def class_collaborators(self) -> List[str]:
        """
        Retrieves the class collaborators.
        :return: Such collaborators.
        :rtype: List[str]
        """
        return self._class_collaborators

    @property
    def constructor(self) -> PythonDefaultConstructor:
        """
        Retrieves the constructor.
        :return: Such constructor.
        :rtype: pythoneda.sandbox.poc.cac.python_default_constructor.PythonDefaultConstructor
        """
        return self._constructor

    @property
    def methods(self) -> List[PythonMethod]:
        """
        Retrieves the methods.
        :return: Such methods.
        :rtype: List[pythoneda.sandbox.poc.cac.PythonMethod]
        """
        return list(map(lambda m: self._resolve(m), self._method_defs))

    def _resolve(self, methodDef: PythonMethodDef) -> PythonMethod:
        """
        Resolves given method definition.
        :param methodDef: The method definition.
        :type methodDef: pythoneda.sandbox.poc.cac.PythonMethodDef
        """
        return PythonMethod(methodDef, "return x + y")

    @property
    def template(self) -> str:
        """
        Retrieves the template.
        :return: Such template.
        :rtype: str
        """
        return '''
//
// This file defines the template for pythoneda/sandbox/poc/cac/Sample.py
//
// Copyright (C) 2024-today rydnr's pythoneda-sandbox/poccac
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.
//
group Sample;

// editor preamble template
editor_preamble() ::= <<
# vim: set fileencoding=utf-8
>>

// imports template
// - deps: The dependencies.
imports(deps) ::= <<
<deps: { dep |<import(dep=dep)>}; separator="\n">
>>

// class template
// - inst: The Sample instance.
class(inst) ::= <<
class <inst.name>(<parents(parents=inst.parents)>):
    """
    <inst.class_description>

    Class name: <inst.name>

    Responsibilities:
        - <inst.class_responsibilities; separator="\n        - ">

    Collaborators:
        <collaborators(collaborators=inst.class_collaborators)>
    """
    <inst.constructor.content>
<if(inst.methods)>

    <methods(methods=inst.methods)><endif>
>>

collaborators(collaborators) ::= <<
<if(collaborators)><collaborators: { collaborator |- <collaborator>}; separator="\n"><else>- None<endif>
>>

// parents template
// - inst: The Sample instance.
parents(parents) ::= <<
<parents: { parent |<parent>}; separator=", ">
>>

import(dep) ::= <<
from <dep.package> import <dep.asset>
>>

// editor settings template
editor_settings() ::= <<
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
>>

// methods template
// - methods: The methods.
methods(methods) ::= <<
<methods: { method |<method.method_def.content>
    <method.body>}; separator="\n\n" >
>>

//  root template
//  - inst: The Sample instance.
root(inst) ::= <<

<editor_preamble()>
"""
<inst.relative_file_path>

<inst.file_description>

<inst.copyright_preamble>
"""
<imports(deps=inst.imports)>


<class(inst=inst)>


<editor_settings()>
>>
'''

    @property
    async def content(self) -> str:
        """
        Generates the file content.
        :return: Such content.
        :rtype: str
        """
        # Create a group from the string content
        group = StringTemplateGroup(name="Sample", file=StringIO(self.template))

        root_template = group.getInstanceOf("root")
        root_template["inst"] = self

        return str(root_template)


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
