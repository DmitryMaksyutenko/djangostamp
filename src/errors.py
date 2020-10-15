# -*- coding: utf-8 -*-


class BaseError(Exception):
    """Base class for djangostamp error messages."""

    def __init__(self):
        self.message = "Base Error"


class LayoutNameError(BaseError):
    """Handles FieleExistsError for application"""
    def __init__(self, file_name):
        self.message = f"File '{file_name}' already exists."


class LayoutNameNotSpecifiedError(BaseError):
    """Handles FileNotFoundError for application."""
    def __init__(self):
        self.message = "File name not specified."


class SecretFileDoesntExist(BaseError):
    """Handles FileNotFoundError for Settings classes. """
    def __init__(self):
        self.message = "There is no secret file."
