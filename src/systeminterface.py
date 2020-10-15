# -*- coding: utf-8 -*-
from . userinterface import (UiLayout,
                             UiAction,
                             UiDatabase)
from . actionsubsystem import ActionSubsystem
from . errors import BaseError
from definitions import PROMPT_TO_USER


class SystemInterface:
    """
    The interface provides an entry-point into the system.

    The facade that hides the system work.

    Consists of classes as attributes and delegates the execution of
    methods to the specific classes.

    Attributes:
        self.ui_action = class for prompt to user abour action.
        self.ui_layout = class for prompt to user abour layout.
        self.ui_database = class for prompt to user abour database.
        self.action_subsyst = class delegates execution for other class.
    """

    def __init__(self):
        self.ui_action = UiAction()
        self.ui_layout = UiLayout()
        self.ui_database = UiDatabase()
        self.action_subsyst = ActionSubsystem()

    def start(self):
        """Starts the execution."""
        try:
            action_dict = self.ui_action.query()
            self._action_sieve(action_dict)
        except BaseError as error:
            print(error.message)

    def _action_sieve(self, action_dict):
        if action_dict["action"] == PROMPT_TO_USER["action"]["layout"]:
            self._perform_layout_configuration()
        if action_dict["action"] == PROMPT_TO_USER["action"]["database"]:
            self._perform_database_configuration()

    def _perform_layout_configuration(self):
        layout_dict = self.ui_layout.query()
        self.action_subsyst.layout(layout_dict)
        self.action_subsyst.base_settings()

    def _perform_database_configuration(self):
        settings_dict = self.ui_database.query()
        self.action_subsyst.database_settings(settings_dict)
