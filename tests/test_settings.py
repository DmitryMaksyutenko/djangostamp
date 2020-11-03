# -*- coding: utf-8 -*-
import os
from pathlib import Path

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

    def test_setup(self, tmpdir):
        tmp_file = \
            tmpdir.mkdir("TestPath").mkdir("configs").join(SECRET_FILE_NAME)
        tmp_file.write_text("SECRET_KEY=\n", "utf-8")
        size_before = tmp_file.size()
        os.environ[LAYOUT_PATH] = str(Path(tmp_file).parent.parent)
        settings = BaseSettings()
        settings.setup()
        size_after = tmp_file.size()
        assert not(size_before == size_after)


class TestDataBaseSettings:

    def test_no_file(self):
        db_settings = DataBaseSettings({})
        try:
            db_settings.setup()
        except SecretFileDoesntExist as error:
            assert isinstance(error, SecretFileDoesntExist)

    def test_setup(self, tmpdir):
        dict_for_compare = {
                "dbms": "postgresql",
                "host": "localhost",
                "database": "dvdrental",
                "username": "test_role",
                "password": "0000",
                "port": "5432"
                }
        db_settings = DataBaseSettings(dict_for_compare)
        tmp_file = \
            tmpdir.mkdir("TestPath").mkdir("configs").join(SECRET_FILE_NAME)
        tmp_file.write_text("DATABASE_URL=\n", "utf-8")
        size_before = tmp_file.size()
        os.environ[LAYOUT_PATH] = str(Path(tmp_file).parent.parent)
        db_settings.setup()
        size_after = tmp_file.size()
        file_data = tmp_file.read_text(encoding="utf-8")
        assert not(size_before == size_after)
        assert file_data.find(dict_for_compare["host"]) >= 0
        assert file_data.find(dict_for_compare["database"]) >= 0
