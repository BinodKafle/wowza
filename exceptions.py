"""
Exception definitions
"""
from django.utils.encoding import force_text
from rest_framework.exceptions import APIException


class InvalidParamDict(APIException):
    """
    Class for exceptions due to the `param_dict` not being in the
    right format.
    Desired parameters for update should be passed in as a dictionary like
    the following:
    {'transcoder_type': 'transcoded'}
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 400


class InvalidParameter(APIException):
    """
    Class for exceptions due to invalid parameters.
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 400


class MissingParameter(APIException):
    """
    Class for exceptions due to missing required parameters.
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 400


class NoApiKey(APIException):
    """
    Class for exceptions due to missing API Key
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 401


class NoAccessKey(APIException):
    """
    Class for exceptions due to missing Access Key
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 401


class InvalidApiKey(APIException):
    """
    Class for exceptions due to invalid API Key
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 401


class InvalidAccessKey(APIException):
    """
    Class for exceptions due to invalid Access Key
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 401


class BadAccountStatus(APIException):
    """
    Class for exceptions due to account being in bad status
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 401


class FeatureNotEnabled(APIException):
    """
    Class for exceptions due to disabled features
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 401


class TrialExceeded(APIException):
    """
    Class for exceptions due to maxed out trial account
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 401


class RecordUnaccessible(APIException):
    """
    Class for exceptions due to unaccessible records due to
    insufficient permissions
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 403


class RecordNotFound(APIException):
    """
    Class for exceptions due to records not found
    """

    def __init__(self, error):
        self.detail = error['message']
        self.status_code = 404


class RecordDeleted(APIException):
    """
    Class for exceptions due to records being deleted
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 410


class RecordInvalid(APIException):
    """
    Class for exceptions due to invalid records
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 422


class InvalidInteraction(APIException):
    """
    Class for exceptions due to invalid interactions
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 422


class InvalidStateChange(APIException):
    """
    Class for exceptions due to invalid state changes.
    i.e. attempting to stop a stream that's not running
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 422


class ConnectionCodeNotSupported(APIException):
    """
    Class for exceptions due to connection code regeneration attempts with
    providers who do not use connection codes (i.e. akamai)
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 405


class TokenAuthBusy(APIException):
    """
    Class for exceptions due to outstanding token auth requests being processed
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 423


class GeoblockingBusy(APIException):
    """
    Class for exceptions due to outstanding geoblocking requests being processed
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 423


class LimitReached(APIException):
    """
    Class for exceptions caused by reaching the limits of the account
    """

    def __init__(self, error):
        self.detail = {'error': [force_text(error['message'])]}
        self.status_code = 409
