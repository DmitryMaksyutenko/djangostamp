import os
from secrets import token_urlsafe
from abc import ABCMeta, abstractmethod
from pathlib import Path
from enum import Enum

from . errors import (SecretFileDoesntExist)
from utils import insert_between
from definitions import (SECRET_FILE_NAME,
                         SECRET_TOKEN_BYTES_AMOUNT,
                         LAYOUT_PATH)


class Settings(metaclass=ABCMeta):
    """
    The base class for all types of settings.
    """
    class Target(Enum):
        SECRET_KEY = "SECRET_KEY"
        DATABASE_URL = "DATABASE_URL"

    @abstractmethod
    def setup(self):
        pass

    def _secret_file_path(self):
        """
        Returns the path to the file for set up,
        from virtual environment.
        """
        return Path(os.environ[LAYOUT_PATH] + "/configs/" + SECRET_FILE_NAME)


class BaseSettings(Settings):
    """
    The class performs set up the base files
    of the project.
    """

    def setup(self):
        path = self._secret_file_path()
        try:
            with open(path, "r+") as f:
                self._write_secret_key(f)
        except FileNotFoundError:
            raise SecretFileDoesntExist

    def _write_secret_key(self, fd):
        """Generates and writes into the file the secret key."""
        secret_key = str(token_urlsafe(SECRET_TOKEN_BYTES_AMOUNT))
        rows_list = fd.readlines()
        for i in range(len(rows_list)):
            if self.Target.SECRET_KEY.value in rows_list[i]:
                def_len = len(self.Target.SECRET_KEY.value + "=") + 1
                if len(rows_list[i]) == def_len:
                    pos = rows_list[i].find("=")
                    rows_list[i] = insert_between(rows_list[i],
                                                  secret_key,
                                                  pos)
                    fd.seek(0, os.SEEK_SET)
                    fd.writelines(rows_list)
                    return
                else:
                    return


class DataBaseSettings(Settings):
    """
    The class performs writing into the file
    an URL-like string with database connection settings.
    """
    def __init__(self, data_dict):
        self._data_dict = data_dict

    def setup(self):
        path = self._secret_file_path()
        try:
            with open(path, "r+") as f:
                self._write_database_url(f)
        except FileNotFoundError:
            raise SecretFileDoesntExist

    def _convert_dict_to_url(self):
        url_string =\
            f"{self._data_dict['dbms']}://" +\
            f"{self._data_dict['username']}:" +\
            f"{self._data_dict['password']}@" +\
            f"{self._data_dict['host']}:" +\
            f"{self._data_dict['port']}/" +\
            f"{self._data_dict['database']}"
        return url_string

    def _write_database_url(self, fd):
        """Writes into the file URL-like string."""
        rows_list = fd.readlines()
        for i in range(len(rows_list)):
            if self.Target.DATABASE_URL.value in rows_list[i]:
                pos = rows_list[i].find("=")
                rows_list[i] = insert_between(rows_list[i],
                                              self._convert_dict_to_url(),
                                              pos)
                fd.seek(0, os.SEEK_SET)
                fd.writelines(rows_list)
                return
