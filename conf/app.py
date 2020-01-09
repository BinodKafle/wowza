from django.core.exceptions import ImproperlyConfigured

from ..settings import WOWZA_SETTINGS as SETTINGS


class Empty(object):
    pass


class AppConfig(object):

    def __init__(self, settings=None):
        self._settings = settings or SETTINGS

    def _get_application_settings(self, settings_key, error_message):
        value = self._settings.get(settings_key, Empty)
        if value is Empty:
            raise ImproperlyConfigured(error_message)
        return value

    def get_wowza_api_key(self):
        msg = (
            "Set WOWZA_SETTINGS[\"WSC_API_KEY\"]."
        )
        return self._get_application_settings("WSC_API_KEY", msg)

    def get_wowza_access_key(self):
        msg = (
            "Set WOWZA_SETTINGS[\"WSC_ACCESS_KEY\"]."
        )
        return self._get_application_settings("WSC_ACCESS_KEY", msg)

    def get_wowza_base_url(self):
        return self._get_application_settings("BASE_URL", 'Invalid base url')
