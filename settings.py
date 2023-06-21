import requests
from django.conf import settings

WOWZA_SETTINGS = getattr(settings, "WOWZA_SETTINGS", {})

WOWZA_SETTINGS.setdefault(
    "CONFIG", "krewcabapi.apps.wowza.conf.AppConfig",
)

WOWZA_SETTINGS.setdefault(
    "BASE_URL",
    f"https://api{'-sandbox' if WOWZA_SETTINGS['WSC_SANDBOX'] is True else ''}.cloud.wowza.com/api/v{WOWZA_SETTINGS['WSC_API_VERSION']}/",
)

session = requests.Session()
session.params = {'accept': 'application/json'}
