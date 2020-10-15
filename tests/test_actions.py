# -*- coding: utf-8 -*-
import os
import shutil
import pytest

from src.actions import LayoutAction
from src.layouts import (Study,
                         Production,
                         Application)


TEST_NAME = "TestName"


@pytest.fixture
def init_layout_action_class():
    def init(choice, name):
        return LayoutAction(choice, name)

    yield init

    shutil.rmtree(TEST_NAME)


class TestLayoutAction:

    @pytest.mark.parametrize("choice, name", [("s", TEST_NAME)])
    def test_study(self, choice, name, init_layout_action_class):
        layout = init_layout_action_class(choice, name)
        layout.execute()
        assert isinstance(layout._layout, Study)
        assert os.path.exists(TEST_NAME)
        assert os.path.isdir(TEST_NAME)
        assert os.listdir(TEST_NAME)

    @pytest.mark.parametrize("choice, name", [("r", TEST_NAME)])
    def test_real(self, choice, name, init_layout_action_class):
        layout = init_layout_action_class(choice, name)
        layout.execute()
        assert isinstance(layout._layout, Production)
        assert os.path.exists(TEST_NAME)
        assert os.path.isdir(TEST_NAME)
        assert os.listdir(TEST_NAME)

    @pytest.mark.parametrize("choice, name", [("a", TEST_NAME)])
    def test_application(self, choice, name, init_layout_action_class):
        layout = init_layout_action_class(choice, name)
        layout.execute()
        assert isinstance(layout._layout, Application)
        assert os.path.exists(TEST_NAME)
        assert os.path.isdir(TEST_NAME)
        assert os.listdir(TEST_NAME)
