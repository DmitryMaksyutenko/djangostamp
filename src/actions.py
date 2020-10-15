# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from os import environ
from pathlib import Path
from enum import Enum

from definitions import (PROMPT_TO_USER,
                         LAYOUT_PATH)
from . layouts import (Study,
                       Production,
                       Application)
from . settings import (BaseSettings,
                        DataBaseSettings)


class Action(metaclass=ABCMeta):
    """The abstract base class for the actions."""

    @abstractmethod
    def execute(self):
        """
        Delegates the layout creation.
        Save path to the project into virtual environment.
        """
        pass


class LayoutAction(Action):
    """
    The class delegates the layout creation,
    to the particular instance of Layout class.

    Attributes:
        _choice - The layuot choiced by the user.
        _name   - The layout name entered by the user.
        _layout - The instance of a Layout.
    """

    def __init__(self, choice, name):
        self._choice = choice
        self._name = name
        self._layout = None

    def execute(self):
        if self._choice == PROMPT_TO_USER["layout"]["study"]:
            self._layout = Study(self._name)
        if self._choice == PROMPT_TO_USER["layout"]["real"]:
            self._layout = Production(self._name)
        if self._choice == PROMPT_TO_USER["layout"]["app"]:
            self._layout = Application(self._name)

        environ.setdefault(LAYOUT_PATH, self._layout.pro_path)
        self._layout.create_layout()


class SettingsAction(Action):
    """
    The class delegates the setting up to the
    particular settins class.

    Context = Describes the settings context.

    Attributes:
        _settings_obj = The settings class.
        _context = The settings context.
        _settings = The settings data.
    """

    class Context(Enum):
        BASE = "base"
        DB = "db"

    def __init__(self, context=Context.BASE, settings=None):
        self._settings_obj = None
        self._context = context
        self._settings = settings

    def execute(self):
        if self._context == self.Context.BASE:
            self._settings_obj = BaseSettings()
        if self._context == self.Context.DB:
            self._settings_obj = DataBaseSettings(self._settings)
        environ.setdefault(LAYOUT_PATH, Path().cwd().as_posix())
        self._settings_obj.setup()
