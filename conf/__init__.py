from django.utils.module_loading import import_string
from .app import AppConfig  # noqa: F401
from ..settings import WOWZA_SETTINGS as SETTINGS

manager = None


def get_manager(reload=False):
    global manager

    if not manager or reload is True:
        manager = import_string(SETTINGS["CONFIG"])()

    return manager


# implementing get_manager as a function allows tests to reload settings
get_manager()
