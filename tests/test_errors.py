# -*- coding: utf-8 -*-
import os
import pytest

from src.errors import (LayoutNameError,
                        LayoutNameNotSpecifiedError)
from src.layouts import Study


TEST_NAME = "TestName"


class TestLayoutErrors:

    def test_name_error(self):
        os.mkdir(TEST_NAME)
        layout = Study()
        layout.root = TEST_NAME
        with pytest.raises(LayoutNameError) as err:
            layout.create_layout()
            assert isinstance(err, LayoutNameError)
        os.rmdir(TEST_NAME)

    def test_name_not_specified(self):
        layout = Study()
        with pytest.raises(LayoutNameNotSpecifiedError) as err:
            layout.create_layout()
            assert isinstance(err, LayoutNameNotSpecifiedError)
