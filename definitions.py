# -*- coding: utf-8 -*-
import os

# djangostamp paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(ROOT_DIR)

# The possible variants of user choices.
# Used in different check clauses.
PROMPT_TO_USER = {
    "action": {
        "layout": "l",
        "database": "d"
    },
    "layout": {
        "study": "s",
        "real": "r",
        "app": "a"
    },
    "database": {
        "settings": [
            "dbms",
            "host",
            "port",
            "database",
            "username",
            "password"
        ]
    }
}

# Virtual envirinment.
LAYOUT_PATH = "LAYOUT_PATH"

# Constants
PROJECT_DIR = "/project_dir"
PROJECT_STUDY_DIR = "/layouts/study"
PROJECT_PRODUCTION_DIR = "/layouts/production"
APPLICATION_DIR = "/layouts/application"
PROJECT_STUDY_DIR_PATH = ROOT_PATH + PROJECT_STUDY_DIR
PROJECT_PRODUCTION_DIR_PATH = ROOT_PATH + PROJECT_PRODUCTION_DIR
APPLICATION_DIR_PATH = ROOT_PATH + APPLICATION_DIR

SECRET_TOKEN_BYTES_AMOUNT = 56
SECRET_FILE_NAME = ".env"
