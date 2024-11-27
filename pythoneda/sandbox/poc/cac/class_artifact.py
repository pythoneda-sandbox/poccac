# vim: set fileencoding=utf-8
"""
pythoneda/sandbox/poc/cac/class_artifact.py

This file declares the ClassArtifact class.

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
from .artifact_metadata import ArtifactMetadata
from .default_method_binding_criteria import DefaultMethodBindingCriteria
from .dependency_import import DependencyImport
from .empty_body_python_method import EmptyBodyPythonMethod
from .method_binding_criteria import MethodBindingCriteria
from .method_def import MethodDef
from .method_parameter import MethodParameter
from .official_python_method import OfficialPythonMethod
import os
from .python_import import PythonImport
from .python_import_find import PythonImportFind
from .python_method_def import PythonMethodDef
from .python_method import PythonMethod
from pythoneda.shared import BaseObject
from stringtemplate3 import StringTemplateGroup
from typing import Dict, List, Type


class ClassArtifact(BaseObject):
    """
    The artifact representation of a class.

    Class name: ClassArtifact

    Responsibilities:
        - Contain the definition for a class.

    Collaborators:
        - None
    """

    def __init__(
        self,
        name: str,
        parents: List[str],
        constructor: PythonMethod,
        methods: List[PythonMethod],
        metadata: ArtifactMetadata,
        methodBindingCriteria: MethodBindingCriteria = None,
        target: Type = None,
    ):
        """
        Creates a new Artifact instance.
        :param name: The class name.
        :type name: str
        :param parents: The parent classes.
        :type parents: List[str]
        :param constructor: The constructor definition.
        :type constructor: pythoneda.sandbox.poc.cac.PythonConstructorDef
        :param methods: The method definitions.
        :type methods: List[pythoneda.sandbox.poc.cac.PythoMethodDef]
        :param metadata: The metadata.
        :type metadata: pythoneda.sandbox.poc.cac.ArtifactMetadata
        :param methodBindingCriteria: The criteria for binding methods.
        :type methodBindingCriteria: pythoneda.sandbox.poc.cac.MethodBindingCriteria
        :param target: The target class.
        :type target: Type
        """
        super().__init__()
        self._name = name
        self._parents = parents
        self._constructor = constructor
        self._methods = methods
        self._metadata = metadata
        self._method_binding_criteria = methodBindingCriteria
        self._target = target

    @classmethod
    def has_explicit_constructor(cls, target) -> bool:
        """
        Checks if the class has an explicit constructor.
        :param target: The target class.
        :type target: Type
        :return: True if the class has an explicit constructor, False otherwise.
        :rtype: bool
        """
        import inspect

        # Retrieve the __init__ method of the class, if it exists
        init_method = getattr(cls, "__init__", None)

        if not init_method:
            return False

        # Check if the __init__ method is defined within the class itself
        return inspect.getmodule(init_method) == inspect.getmodule(cls)

    @classmethod
    def for_class(cls, target: Type) -> "ClassArtifact":
        """
        Creates a new instance for given target.
        :param target: The target class.
        :type target: Type
        """
        import inspect

        source_file = inspect.getfile(target)
        class_imports = cls.class_imports_of(target)
        metadata = ArtifactMetadata.from_dict(
            {
                "relative_file_path": source_file,
                "module_name": target.__module__,
                "author": "rydnr",
                "start_year": "2024",
                "ref_url": "https://github.com/pythoneda-sandbox/poccac",
                "class_description": "Models the Sample abstraction.",
                "class_responsibilities": "Represent the Sample abstraction.",
                "class_collaborators": "None",
                "source": inspect.getsource(target),
                "module_source": inspect.getsource(inspect.getmodule(target)),
                "class_imports": class_imports,
            }
        )

        constructor = None

        if cls.has_explicit_constructor(target):
            constructor = OfficialPythonMethod(
                MethodDef.from_method(target.__init__), target.__init__, target
            )

        methods = list(target.__dict__.items())
        methods = [
            m
            for _, m in methods
            if (inspect.isfunction(m) and not m.__name__ == "__init__")
            or isinstance(m, property)
            or isinstance(m, classmethod)
        ]
        return ClassArtifact(
            target.__name__,
            target.__bases__,
            constructor,
            [
                OfficialPythonMethod(MethodDef.from_method(m), m, target)
                for m in methods
            ],
            metadata,
            DefaultMethodBindingCriteria(),
            target,
        )

    @property
    def name(self) -> str:
        """
        Retrieves the class name.
        :return: Such name.
        :rtype: str
        """
        return self._name

    @property
    def parents(self) -> List[Type]:
        """
        Retrieves the class parents.
        :return: Such parents.
        :rtype: List[Type]
        """
        return self._parents

    @property
    def constructor(self) -> PythonMethod:
        """
        Retrieves the class constructor.
        :return: Such constructor.
        :rtype: pythoneda.sandbox.poc.cac.PythonMethod
        """
        return self._constructor

    @property
    def methods(self) -> List[PythonMethod]:
        """
        Retrieves the class methods.
        :return: Such methods.
        :rtype: List[pythoneda.sandbox.poc.cac.PythonMethod]
        """
        return self._methods

    @property
    def metadata(self) -> Dict[str, str]:
        """
        Retrieves the metadata.
        :return: Such metadata.
        :rtype: Dict[str, str]
        """
        return self._metadata

    @property
    def method_binding_criteria(self) -> MethodBindingCriteria:
        """
        Retrieves the method binding criteria.
        :return: Such criteria.
        :rtype: pythoneda.sandbox.poc.cac.MethodBindingCriteria
        """
        return self._method_binding_criteria

    @property
    def target(self) -> Type:
        """
        Retrieves the target class.
        :return: Such class.
        :rtype: Type
        """
        return self._target

    @property
    def module_name(self) -> str:
        """
        Retrieves the module name.
        :return: Such information.
        :rtype: str
        """
        result = None
        if self.target is None:
            result = self.metadata.get("module_name", lambda: "[unknown module]")
        else:
            result = self.target.__module__

        return result

    @property
    def start_year(self) -> int:
        """
        Retrieves the starting year.
        :return: Such information.
        :rtype: int
        """
        return self.metadata.start_year

    @property
    def author(self) -> str:
        """
        Retrieves the author.
        :return: Such information.
        :rtype: str
        """
        return self.metadata.author

    @property
    def ref_url(self) -> str:
        """
        Retrieves the reference url.
        :return: Such information.
        :rtype: str
        """
        return self.metadata.ref_url

    @property
    def relative_file_path(self) -> str:
        """
        Retrieves the relative file path.
        :return: Such path.
        :rtype: str
        """
        result = self.metadata.get("relative_file_path", lambda: None)
        if result is None:
            module_name = self.metadata.get("module_name", None)
            if module_name:
                result = (
                    os.path.sep.join(module_name.split("."))
                    + os.path.sep
                    + self.__class__.camel_to_snake(name)
                    + ".py"
                )
            self.metadata.set("relative_file_path", result)

        return result

    @property
    def file_description(self) -> str:
        """
        Retrieves the file description.
        :return: Such description.
        :rtype: str
        """
        return self.metadata.get(
            "file_description", f"This file defines the {self.name} class."
        )

    @property
    def copyright_preamble(self) -> str:
        """
        Retrieves the copyright preamble.
        :return: Such content.
        :rtype: str
        """
        return self.metadata.copyright_preamble

    @property
    def copyright_preamble_for_st(self) -> str:
        """
        Retrieves the copyright preamble for StringTemplate.
        :return: Such content.
        :rtype: str
        """
        return self.metadata.copyright_preamble_for_st

    @property
    def class_description(self) -> str:
        """
        Retrieves the class description.
        :return: Such description.
        :rtype: str
        """
        return self.metadata.get("class_description", lambda: "[no description]")

    @property
    def class_responsibilities(self) -> List[str]:
        """
        Retrieves the class responsibilities.
        :return: Such responsibilities.
        :rtype: List[str]
        """
        return self.metadata.get("class_responsibilities", lambda: [])

    @property
    def class_collaborators(self) -> List[str]:
        """
        Retrieves the class collaborators.
        :return: Such collaborators.
        :rtype: List[str]
        """
        return self.metadata.get("class_collaborators", lambda: [])

    @property
    def class_imports(self) -> List[PythonImport]:
        """
        Retrieves the imports.
        :return: Such imports.
        :rtype: List[pythoneda.sandbox.poc.cac.python_import.PythonImport]
        """
        return self.metadata.get("class_imports", lambda: [])

    @property
    def method_imports(self) -> List[PythonImport]:
        """
        Retrieves the method imports.
        :return: Such imports.
        :rtype: List[pythoneda.sandbox.poc.cac.python_import.PythonImport]
        """
        result = []
        for m in self.method_definitions:
            result.extend(m.type_imports)
        for m in self.methods:
            result.extend(m.imports)
        return result

    @property
    def method_definitions(self) -> List[PythonMethod]:
        """
        Retrieves the methods.
        :return: Such methods.
        :rtype: List[pythoneda.sandbox.poc.cac.PythonMethodDef]
        """
        return [m.method_def for m in self._methods]

    @property
    def template(self) -> str:
        """
        Retrieves the template.
        :return: Such template.
        :rtype: str
        """
        return f'''
//
// This file defines the template for {self.metadata["relative_file_path"]}
//
// {self.copyright_preamble_for_st}
//
group Artifact;

// editor preamble template
editor_preamble() ::= <<
# vim: set fileencoding=utf-8
>>

// imports template
// - deps: The dependencies.
imports(deps) ::= <<
<deps: {{ dep |<import(dep=dep)>}}; separator="\\n">
>>

// class template
// - inst: The Sample instance.
class(inst) ::= <<
class <inst.name>(<parents(parents=inst.parents)>):
    """
    <inst.class_description>

    Class name: <inst.name>

    Responsibilities:
        - <inst.class_responsibilities; separator="\\n        - ">

    Collaborators:
        <collaborators(collaborators=inst.class_collaborators)>
    """<if(inst.constructor)>


<inst.constructor.body><endif>
<if(inst.methods)>

<methods(methods=inst.methods)><endif>
>>

collaborators(collaborators) ::= <<
<if(collaborators)><collaborators: {{ collaborator |- <collaborator>}}; separator="\\n"><else>- None<endif>
>>

// parents template
// - inst: The Sample instance.
parents(parents) ::= <<
<parents: {{ parent |<parent.__name__>}}; separator=", ">
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
<methods: {{ method |<method.body>}}; separator="\n\n" >
>>

//  root template
//  - inst: The Artifact instance.
root(inst) ::= <<

<editor_preamble()>
"""
<inst.relative_file_path>

<inst.file_description>

<inst.copyright_preamble>
"""
<if(inst.class_imports)><imports(inst.class_imports)>

<endif>


<class(inst=inst)>

<editor_settings()>
>>
'''

    @property
    def content(self) -> str:
        """
        Generates the file content.
        :return: Such content.
        :rtype: str
        """
        # Create a group from the string content
        group = StringTemplateGroup(name="Artifact", file=StringIO(self.template))

        root_template = group.getInstanceOf("root")
        root_template["inst"] = self

        return str(root_template)

    async def rename_imports(
        self,
        oldPackage: str,
        newPackage: str,
        oldAsset: str = None,
        newAsset: str = None,
    ) -> None:
        """
        Renames the matching imports.
        :param oldPackage: The old package.
        :type oldPackage: str
        :param newPackage: The new package.
        :type newPackage: str
        :param oldAsset: The old asset.
        :type oldAsset: str
        :param newAsset: The new asset.
        :type newAsset: str
        """
        aux = self.class_imports
        aux.extend(self.method_imports)
        for imp in aux:
            await imp.rename(oldPackage, newPackage, oldAsset, newAsset)
        if any(parent.__name__ == oldAsset for parent in self.parents):
            import importlib

            new_module = importlib.import_module(newPackage)
            new_parent = getattr(new_module, newAsset)
            self._parents = [
                new_parent if parent.__name__ == oldAsset else parent
                for parent in self.parents
            ]
            if self.target:
                self._target.__bases__ = tuple(self.parents)
            else:
                self._target = type(
                    self.name, tuple(self.parents), dict(self.target.__dict__)
                )

    async def rename(self, newName: str) -> None:
        """
        Renames the class.
        :param newName: The new name.
        :type newName: str
        """
        self._name = newName
        import types

        new_module = types.ModuleType(
            self.module_name.split(".")[:-1],
            ".",
            self.__class__.camel_to_snake(newName),
        )
        #        print(self.content)
        exec(self.content, new_module.__dict__)
        self._target = getattr(new_module, newName)

    @classmethod
    def class_imports_of(cls, target: Type) -> List[DependencyImport]:
        """
        Retrieves the imports of the class.
        :param target: The target class.
        :type target: Type
        :return: The imports.
        :rtype: List[pythoneda.sandbox.poc.cac.DependencyImport]
        """
        import inspect

        module = inspect.getmodule(target)
        return PythonImportFind(inspect.getsource(module)).imports


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
