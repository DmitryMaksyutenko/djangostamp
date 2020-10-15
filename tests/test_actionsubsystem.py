# -*- coding: utf-8 -*-
import os
import pytest
import shutil

from src.actionsubsystem import ActionSubsystem
from definitions import (PROJECT_STUDY_DIR_PATH,
                         PROJECT_PRODUCTION_DIR_PATH,
                         APPLICATION_DIR_PATH,
                         PROJECT_DIR)
from utils import dir_cmp

TEST_NAME = "TestName"


@pytest.fixture
def init_action_subsystem_class_layout():
    def init():
        return ActionSubsystem()

    yield init

    shutil.rmtree(TEST_NAME)


class TestActionSubsystem:

    @pytest.mark.parametrize("action_dict", [{"layout": "s",
                                              "name": TEST_NAME}])
    def test_layout_study(self, action_dict,
                          init_action_subsystem_class_layout):
        subsys = init_action_subsystem_class_layout()
        subsys.layout(action_dict)
        assert os.path.exists(TEST_NAME)
        assert dir_cmp(PROJECT_STUDY_DIR_PATH, TEST_NAME)

    @pytest.mark.parametrize("action_dict", [{"layout": "r",
                                              "name": TEST_NAME}])
    def test_layout_real(self, action_dict,
                         init_action_subsystem_class_layout):
        subsys = init_action_subsystem_class_layout()
        subsys.layout(action_dict)
        os.rename(os.path.abspath(TEST_NAME) + "/" + TEST_NAME,
                  os.path.abspath(TEST_NAME) + "/" + PROJECT_DIR)
        assert os.path.exists(TEST_NAME)
        assert dir_cmp(PROJECT_PRODUCTION_DIR_PATH, TEST_NAME)

    @pytest.mark.parametrize("action_dict", [{"layout": "a",
                                              "name": TEST_NAME}])
    def test_layout_app(self, action_dict,
                        init_action_subsystem_class_layout):
        subsys = init_action_subsystem_class_layout()
        subsys.layout(action_dict)
        assert os.path.exists(TEST_NAME)
        assert dir_cmp(APPLICATION_DIR_PATH, TEST_NAME)
