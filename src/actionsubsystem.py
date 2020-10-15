# -*- coding: utf-8 -*-
from . actioninvoker import ActionInvoker
from . actions import (LayoutAction,
                       SettingsAction)


class ActionSubsystem:
    """
    The facade, that hides the actions.

    Attribures:
        _invoker - The class that initializes the action.
    """

    def __init__(self):
        self._invoker = ActionInvoker()

    def layout(self, action_dict):
        self._invoker.action = LayoutAction(action_dict["layout"],
                                            action_dict["name"])
        self._invoke()

    def base_settings(self):
        self._invoker.action = SettingsAction()
        self._invoke()

    def database_settings(self, settings_dict):
        self._invoker.action = SettingsAction(SettingsAction.Context.DB,
                                              settings_dict)
        self._invoke()

    def _invoke(self):
        self._invoker.invoke_action()
