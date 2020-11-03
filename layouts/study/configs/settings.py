import environ

from pathlib import Path

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

env = environ.Env(DEBUG=(bool, True))

# https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key
SECRET_KEY = env("SECRET_KEY")
# https://docs.djangoproject.com/en/3.0/ref/settings/#debug
DEBUG = env("DEBUG")
# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]
# https://docs.djangoproject.com/en/3.0/ref/settings/#root-urlconf
ROOT_URLCONF = 'configs.urls'
