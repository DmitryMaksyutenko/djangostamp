# -*- coding: utf-8 -*-
import os

from src.settings import (BaseSettings,
                          DataBaseSettings)
from src.errors import SecretFileDoesntExist
from definitions import (LAYOUT_PATH,
                         SECRET_FILE_NAME)


class TestBaseSettings:

    def test_no_file(self):
        settings = BaseSettings()
        try:
            settings.setup()
        except SecretFileDoesntExist as error:
            assert isinstance(error, SecretFileDoesntExist)

    def test_setup(self, tmp_path):
        tmp_file_path = tmp_path / "TestPath"
        tmp_file_path.mkdir()
        tmp_file = tmp_file_path / SECRET_FILE_NAME
        tmp_file.write_text("SECRET_KEY=\n")
        size_before = tmp_file.stat().st_size
        os.environ[LAYOUT_PATH] = str(tmp_file.parent)
        settings = BaseSettings()
        settings.setup()
        size_after = tmp_file.stat().st_size
        assert not(size_before == size_after)


class TestDataBaseSettings:

    def test_no_file(self):
        db_settings = DataBaseSettings({})
        try:
            db_settings.setup()
        except SecretFileDoesntExist as error:
            assert isinstance(error, SecretFileDoesntExist)

    def test_setup(self, tmp_path):
        dict_for_compare = {
                "dbms": "postgresql",
                "host": "localhost",
                "database": "dvdrental",
                "username": "test_role",
                "password": "0000",
                "port": "5432"
                }
        db_settings = DataBaseSettings(dict_for_compare)
        tmp_file_path = tmp_path / "TestPath"
        tmp_file_path.mkdir()
        tmp_file = tmp_file_path / SECRET_FILE_NAME
        tmp_file.write_text("DATABASE_URL=\n")
        size_before = tmp_file.stat().st_size
        os.environ[LAYOUT_PATH] = str(tmp_file.parent)
        os.environ[LAYOUT_PATH] = str(tmp_file.parent)
        db_settings.setup()
        size_after = tmp_file.stat().st_size
        file_data = tmp_file.read_text()
        assert not(size_before == size_after)
        assert file_data.find(dict_for_compare["host"]) >= 0
        assert file_data.find(dict_for_compare["database"]) >= 0
