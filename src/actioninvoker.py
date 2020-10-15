# -*- coding: utf-8 -*-


class ActionInvoker:
    """
    The class responsible for initializing the action.

    Attributes:
        _action = The particular Action class.
    """

    def __init_(self, action=None):
        self._action = action

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

    def invoke_action(self):
        """Action initialization."""
        self._action.execute()
