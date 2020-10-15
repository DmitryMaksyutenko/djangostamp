# -*- coding: utf-8 -*-
from src.userinterface import (UiLayout,
                               UiAction,
                               UiDatabase)

TEST_NAME = "TestName"


class TestUiLayout:

    def test_study_input(self, mocker):
        ui = UiLayout()
        mocker.patch("builtins.input", side_effect=["s", TEST_NAME])
        layout_data = ui.query()
        assert layout_data == {"layout": "s", "name": TEST_NAME}

    def test_production_input(self, mocker):
        ui = UiLayout()
        mocker.patch("builtins.input", side_effect=["r", TEST_NAME])
        layout_data = ui.query()
        assert layout_data == {"layout": "r", "name": TEST_NAME}

    def test_application_input(self, mocker):
        ui = UiLayout()
        mocker.patch("builtins.input", side_effect=["a", TEST_NAME])
        layout_data = ui.query()
        assert layout_data == {"layout": "a", "name": TEST_NAME}


class TestUiAction:

    def test_layout(self, mocker):
        ui = UiAction()
        mocker.patch("builtins.input", side_effect=["l"])
        action_dict = ui.query()
        assert action_dict == {"action": "l"}

    def test_database(self, mocker):
        ui = UiAction()
        mocker.patch("builtins.input", side_effect=["d"])
        action_dict = ui.query()
        assert action_dict == {"action": "d"}


class TestUiDatabase:

    tmp = {
        "dbms": "psql",
        "host": "localhost",
        "port": "5432",
        "database": "dbName",
        "username": "userName",
        "password": "123pass"
    }

    def test_query(self, mocker):
        ui = UiDatabase()
        mocker.patch("builtins.input", side_effect=[self.tmp["dbms"],
                                                    self.tmp["host"],
                                                    self.tmp["port"],
                                                    self.tmp["database"],
                                                    self.tmp["username"],
                                                    self.tmp["password"]])
        settings_dict = ui.query()
        assert settings_dict == self.tmp
