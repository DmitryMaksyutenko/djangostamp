# -*- coding: utf-8 -*-
import os
import shutil
import pytest

from utils import dir_cmp
from definitions import (PROJECT_STUDY_DIR_PATH,
                         PROJECT_PRODUCTION_DIR_PATH,
                         APPLICATION_DIR_PATH,
                         PROJECT_DIR)

from src.layouts import (Study,
                         Production,
                         Application)

TEST_LAYOUT_NAME = "TestLayout"


@pytest.fixture(scope="function")
def setup_layout():
    def _params(layout):
        return layout(TEST_LAYOUT_NAME)

    yield _params
    shutil.rmtree(TEST_LAYOUT_NAME)


class TestStudyLayout:

    layout_type = Study
    layout = None

    @pytest.fixture(autouse=True)
    def init_layout(self, setup_layout):
        self.layout = setup_layout(self.layout_type)
        self.layout.create_layout()

    def test_is_dir(self, setup_layout):
        assert os.path.isdir(self.layout.root)

    def test_as_template(self, setup_layout):
        assert dir_cmp(PROJECT_STUDY_DIR_PATH, self.layout.root_path)


class TestProductionLayout:

    layout_type = Production
    layout = None

    @pytest.fixture(autouse=True)
    def init_layout(self, setup_layout):
        self.layout = setup_layout(self.layout_type)
        self.layout.create_layout()

    def test_is_dir(self):
        assert os.path.isdir(self.layout.root)

    def test_as_template(self):
        os.rename(self.layout.root_path + "/" + self.layout.root,
                  self.layout.root_path + "/" + PROJECT_DIR)
        assert dir_cmp(PROJECT_PRODUCTION_DIR_PATH, self.layout.root_path)


class TestApplicationLayout:

    layout_type = Application
    layout = None

    @pytest.fixture(autouse=True)
    def init_layout(self, setup_layout):
        self.layout = setup_layout(self.layout_type)
        self.layout.create_layout()

    def test_is_dir(self):
        assert os.path.isdir(self.layout.root)

    def test_as_template(self):
        assert dir_cmp(APPLICATION_DIR_PATH, self.layout.root_path)
