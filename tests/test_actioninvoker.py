# -*- coding: utf-8 -*-
import os
import pytest

from src.actioninvoker import ActionInvoker


TEST_FILE_NAME = "TestFile"
TEST_FILE_RENAME = "TestFileRenamed"
TEST_DIRECTORY_NAME = "TestDir"
TEST_DIRECTORY_RENAME = "TestDirRenamed"


@pytest.fixture
def file_action_class():

    class CreateFileAction:

        def execute(self):
            fd = os.open(TEST_FILE_NAME, os.O_RDONLY | os.O_CREAT)
            os.close(fd)

    yield CreateFileAction

    os.remove(TEST_FILE_NAME)


@pytest.fixture
def dir_action_class():

    class CreateDirAction:

        def execute(self):
            os.mkdir(TEST_DIRECTORY_NAME)

    yield CreateDirAction

    os.rmdir(TEST_DIRECTORY_NAME)


@pytest.fixture
def rename_file_class():

    fd = os.open(TEST_FILE_NAME, os.O_RDONLY | os.O_CREAT)
    os.close(fd)

    class RenameFileAction:

        def execute(self):
            os.rename(TEST_FILE_NAME, TEST_FILE_RENAME)

    yield RenameFileAction

    os.remove(TEST_FILE_RENAME)


@pytest.fixture
def rename_dir_class():

    os.mkdir(TEST_DIRECTORY_NAME)

    class RenameDirAction:

        def execute(self):
            os.rename(TEST_DIRECTORY_NAME, TEST_DIRECTORY_RENAME)

    yield RenameDirAction

    os.rmdir(TEST_DIRECTORY_RENAME)


class TestActionInvoker:

    invoker = ActionInvoker()

    def test_invoke_action_create_file(self, file_action_class):
        self.invoker.action = file_action_class()
        self.invoker.invoke_action()
        assert os.path.exists(TEST_FILE_NAME)
        assert os.path.isfile(TEST_FILE_NAME)

    def test_invoke_action_create_directory(self, dir_action_class):
        self.invoker.action = dir_action_class()
        self.invoker.invoke_action()
        assert os.path.exists(TEST_DIRECTORY_NAME)
        assert os.path.isdir(TEST_DIRECTORY_NAME)

    def test_invoke_actin_file_renaming(self, rename_file_class):
        self.invoker.action = rename_file_class()
        self.invoker.invoke_action()
        assert os.path.exists(TEST_FILE_RENAME)

    def test_invoke_action_dir_rename(self, rename_dir_class):
        self.invoker.action = rename_dir_class()
        self.invoker.invoke_action()
        assert os.path.exists(TEST_DIRECTORY_RENAME)
