import json

from .conf import get_manager
from .exceptions import MissingParameter, InvalidParamDict, InvalidInteraction, \
    InvalidStateChange, InvalidParameter
from .settings import session


class LiveStreams(object):

    def __init__(self,
                 base_url=get_manager().get_wowza_base_url(),
                 api_key=get_manager().get_wowza_api_key(),
                 access_key=get_manager().get_wowza_access_key()):
        self.id = id
        self.base_url = base_url
        self.headers = {
            'wsc-api-key': api_key,
            'wsc-access-key': access_key,
            'content-type': 'application/json'
        }

    def fetch(self, stream_id=None, options=None):
        """
        Used to gather info on all streams associated with an account or
        with a particular live stream.
        When called without inputting a stream_id, it'll return all streams
        associated with the account.
        Options: state, stats, thumbnail_url
        """
        if options and not stream_id:
            raise InvalidParameter({
                'message': 'When getting optional info on a stream, a \
                stream_id needs to be provided.'
            })
        path = self.base_url + 'live_streams/'
        if stream_id:
            path = path + stream_id
        if options:
            path = path + "/{}".format(options)
        response = session.get(path, headers=self.headers)
        return response.json()

    def create(self, param_dict):
        """
        Used to create a new live stream.
        Valid parameters:
            name, transcoder_type, billing_mode, broadcast_location,
            encoder, delivery_method, aspect_ratio_width, aspect_ratio_height
        """
        required_params = [
            'aspect_ratio_height', 'aspect_ratio_width', 'billing_mode',
            'broadcast_location', 'encoder', 'name', 'transcoder_type'
        ]
        for key in required_params:
            if key not in param_dict:
                raise MissingParameter({
                    'message': 'Missing parameter [{}]. Cannot create \
                     live stream.'.format(key)
                })
        param_dict = {
            'live_stream': param_dict
        }
        path = self.base_url + 'live_streams/'
        response = session.post(
            path,
            json.dumps(param_dict),
            headers=self.headers
        )
        return response.json()

    def start(self, stream_id):
        """
        Used to start a live stream
        """
        path = self.base_url + "live_streams/{}/start".format(stream_id)
        response = session.put(path, data='', headers=self.headers)
        return response.json()

    def state(self, stream_id):
        """
        Used to get the state of a live stream
        """
        path = self.base_url + "live_streams/{}/state".format(stream_id)
        response = session.get(path, data='', headers=self.headers)
        return response.json()

    def update(self, stream_id, param_dict):
        """
        Used to update a live stream.
        Expects a dictionary with key-value pairs of the parameter to change
        and the value to change it to.
        """
        if isinstance(param_dict, dict):
            param_dict = {
                'live_stream': param_dict
            }
            path = self.base_url + 'live_streams/{}'.format(stream_id)
            response = session.patch(path, json.dumps(param_dict), headers=self.headers)
            return response.json()
        else:
            raise InvalidParamDict({
                'message': 'Desired parameters for update should be passed in \
                as a dictionary with key-value pairs. \
                i.e. {\'transcoder_type\': \'transcoded\'}'
            })

    def stop(self, stream_id):
        """
        Used to stop a live stream
        """
        state = self.fetch(stream_id, 'state')['live_stream']['state']
        if state == 'started':
            path = self.base_url + "live_streams/{}/stop".format(stream_id)
            response = session.put(path, data='', headers=self.headers)
            if 'meta' in response.json():
                if response.json()['meta']['code'] == 'ERR-422-InvalidInteraction':
                    raise InvalidInteraction({
                        'message': 'Unable to stop stream. Invalid state for stopping.'
                    })
        else:
            raise InvalidStateChange({
                'message': 'Cannot stop a live stream that is not running.'
            })
        return response.json()

    def delete(self, stream_id):
        """
        Used to delete a live stream.
        """
        state = self.fetch(stream_id, 'state')['live_stream']['state']
        if state is not 'started':
            path = self.base_url + 'live_streams/{}'.format(stream_id)
            response = session.delete(path, headers=self.headers)
            return response
        else:
            raise InvalidInteraction({
                'message': 'Cannot delete a running event. Stop the event first \
                and try again.'
            })
