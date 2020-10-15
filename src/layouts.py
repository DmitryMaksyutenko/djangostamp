# -*- coding: utf-8 -*-
import os
import shutil
from abc import (ABCMeta,
                 abstractmethod,
                 abstractproperty)

from definitions import (ROOT_PATH,
                         PROJECT_STUDY_DIR,
                         PROJECT_PRODUCTION_DIR,
                         PROJECT_DIR,
                         APPLICATION_DIR)
from . errors import (LayoutNameError,
                      LayoutNameNotSpecifiedError)


class Layout(metaclass=ABCMeta):
    """The abstract base class for the project types."""

    @abstractmethod
    def create_layout(self):
        pass

    @abstractproperty
    @property
    def root(self):
        pass

    @abstractproperty
    @root.setter
    def root(self, root):
        pass

    @abstractproperty
    @property
    def root_path(self):
        pass

    @abstractproperty
    @root_path.setter
    def root_path(self, path):
        pass

    @abstractproperty
    @property
    def pro_path(self):
        pass


class Study(Layout):
    """Class creates the study layout.

    Attributes:
        _root - string, represents the name of the project directory.
        _path - absolute path to the project.
    """
    def __init__(self, name=""):
        self._root = name
        self._path = os.path.abspath(name)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root
        self._path = os.path.abspath(root)

    @property
    def root_path(self):
        return self._path

    @root_path.setter
    def root_path(self, path):
        self._path = path

    @property
    def pro_path(self):
        return self._path

    def create_layout(self):
        """Makes copy from stydy directory."""
        try:
            shutil.copytree(ROOT_PATH + PROJECT_STUDY_DIR, self._root)
        except FileExistsError as error:
            raise LayoutNameError(error.filename)
        except FileNotFoundError:
            raise LayoutNameNotSpecifiedError()


class Production(Layout):
    """Class creates the production layout.

    Attributes:
        _root - string, represents the name of the project directory.
        _path - absolute path to the project.
    """
    def __init__(self, name=""):
        self._root = name
        self._path = os.path.abspath(name)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root
        self._path = os.path.abspath(root)

    @property
    def root_path(self):
        return self._path

    @root_path.setter
    def root_path(self, path):
        self._path = path

    @property
    def pro_path(self):
        return self._path + "/" + self._root

    def create_layout(self):
        """Makes copy from production directory."""
        try:
            shutil.copytree(ROOT_PATH + PROJECT_PRODUCTION_DIR, self._root)
            project_name = self._root + "/" + self._root
            os.rename(self.root_path + PROJECT_DIR, project_name)
            self._path = os.path.abspath(self._root)
        except FileExistsError as error:
            raise LayoutNameError(error.filename)
        except FileNotFoundError:
            raise LayoutNameNotSpecifiedError()


class Application(Layout):
    """
    Class creates the application layout.

    Attribute:
        _root - string, represents the name of the project directory.
        _path - absolute path to the project.
    """
    def __init__(self, name=""):
        self._root = name
        self._path = os.path.abspath(name)

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        self._root = root
        self._path = os.path.abspath(root)

    @property
    def root_path(self):
        return self._path

    @root_path.setter
    def root_path(self, path):
        self._path = path

    @property
    def pro_path(self):
        return os.path.join(self._path, os.pardir)

    def create_layout(self):
        """Creates an application."""
        try:
            shutil.copytree(ROOT_PATH + APPLICATION_DIR, self.root)
        except FileExistsError as error:
            raise LayoutNameError(error.filename)
        except FileNotFoundError:
            raise LayoutNameNotSpecifiedError()
