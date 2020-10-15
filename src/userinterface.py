# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from enum import Enum

from definitions import PROMPT_TO_USER


class UIMessages(Enum):
    """Keeps all messages intended to the user."""

    MAIN = "Choose the action:\n"\
        "{} - configure project/application.\n"\
        "{} - configure databse.\n"\
        .format(PROMPT_TO_USER["action"].get("layout"),
                PROMPT_TO_USER["action"].get("database"))
    LAYOUT = "Choose the action:\n"\
        "{} - create a project for studying the Django. (minimal settings).\n"\
        "{} - create a real project. (base settings).\n"\
        "{} - create an application.\n"\
        .format(PROMPT_TO_USER["layout"].get("study"),
                PROMPT_TO_USER["layout"].get("real"),
                PROMPT_TO_USER["layout"].get("app"))

    INPUT_LINE = "------------------------->>> "

    LAYOUT_NAME = "----------------Layout name:"

    DATABASE_NAME = "---------------database name:"
    DATABASE_USER = "---------------database user:"
    DATABASE_PASS = "-----------database password:"
    DATABASE_HOST = "---------------database host:"
    DATABASE_PORT = "---------------database port:"


class Ui(metaclass=ABCMeta):
    """The base class for the UIs"""

    @abstractmethod
    def query(self):
        """The method for asking the user."""
        pass


class UiLayout(Ui):
    """The class for asking the user about layout settings."""

    def query(self):
        layout_data = dict()
        layout_data["layout"] = self._layout_choice()
        layout_data["name"] = self._layout_name()
        return layout_data

    def _layout_choice(self):
        """Determines the creation of a project or an application."""
        print(UIMessages.LAYOUT.value)
        while True:
            user_choice = input(UIMessages.INPUT_LINE.value)
            for key in PROMPT_TO_USER["layout"]:
                if user_choice in PROMPT_TO_USER["layout"][key]:
                    return user_choice

    def _layout_name(self):
        """Prompt to the user for the project name specification."""
        print(UIMessages.LAYOUT_NAME.value)
        user_choice = input(UIMessages.INPUT_LINE.value)
        return user_choice


class UiAction(Ui):
    """The class for asking user about action."""

    def query(self):
        action_dict = dict()
        action_dict["action"] = self._action()
        return action_dict

    def _action(self):
        """Prompt to the user to choose the action."""
        print(UIMessages.MAIN.value)
        while True:
            user_choice = input(UIMessages.INPUT_LINE.value)
            for key in PROMPT_TO_USER["action"]:
                if user_choice in PROMPT_TO_USER["action"][key]:
                    return user_choice


class UiDatabase(Ui):
    """The class for database set up."""
    def query(self):
        return self._setup_database_dict()

    def _setup_database_dict(self):
        """Prompt to the user to get the database settings."""
        settins_list = PROMPT_TO_USER["database"]["settings"]
        settings_dict = dict()
        for item in settins_list:
            settings_dict[item] = str(input(f"enter {item}: ")).strip()
        return settings_dict
