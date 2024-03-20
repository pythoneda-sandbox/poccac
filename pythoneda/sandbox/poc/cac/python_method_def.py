# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/python_method_def.py

This file declares the PythonMethodDef class.

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
from .method_def import MethodDef
from .method_parameter import MethodParameter
from .python_import import PythonImport
from pythoneda.shared import attribute, BaseObject, primary_key_attribute
from io import StringIO
from stringtemplate3 import StringTemplateGroup
from typing import List


class PythonMethodDef(MethodDef):
    """
    Models Python method definitions.

    Class name: PythonMethodDef

    Responsibilities:
        - Represent a Python method definition.

    Collaborators:
        - None
    """

    def __init__(
        self,
        name: str,
        returnType: str,
        doc: str,
        parameters: List[MethodParameter] = [],
        returnDoc: str = None,
        typeImports: List[PythonImport] = [],
    ):
        """
        Creates a new PythonMethodDef instance.
        :param name: The method name.
        :type name: str
        :param returnType: The return type.
        :type returnType: str
        :param doc: The parameter documentation.
        :type doc: str
        :param parameters: The method parameters.
        :type parameters: List[MethodParameter]
        :param returnDoc: The documentation of the return value.
        :type returnDoc: str
        """
        super().__init__(name, returnType, doc, parameters, returnDoc, typeImports)

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
group Method;

// parameters template
// - parameters: The method parameters.
parameters(parameters) ::= <<
<parameters: { param | <param.name>:<param.parameter_type><if(param.default_value)> = <param.default_value>}; separator=", " >
>>

// docs
// - parameters: The method parameters.
parameter_docs(parameters) ::= <<
<parameters: { param |

:param <param.name>: <param.doc>
:type <param.name>: <param.parameter_type>} >
>>

//  root template
//  - inst: The Sample instance.
root(inst) ::= <<
def <inst.name>(self<if(inst.parameters)>, <parameters(parameters=inst.parameters)><endif>)<if(inst.return_type)> -> <inst.return_type><endif>:
    """
    <inst.doc><if(inst.parameters)>
    <parameter_docs(parameters=inst.parameters)>

<endif>
    :return: <inst.return_doc>
    :rtype: <inst.return_type>
    """
>>
'''

    @property
    def content(self) -> str:
        """
        Retrieves the content.
        :return: Such content.
        :rtype: str
        """
        # Create a group from the string content
        group = StringTemplateGroup(name="Method", file=StringIO(self.template))

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
