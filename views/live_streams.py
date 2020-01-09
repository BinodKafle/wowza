from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from ..wowza import LiveStreams


class LiveStreamList(APIView):

    """
    List all live streams, or create a new live stream.
    """

    def get(self, request):
        streams = LiveStreams().fetch()
        return Response(streams, status=status.HTTP_200_OK)

    def post(self, request):
        stream = LiveStreams().create({
                'name': 'My Live Stream',
                'billing_mode': 'pay_as_you_go',
                'transcoder_type': 'transcoded',
                'broadcast_location': 'eu_germany',
                'encoder': 'wowza_gocoder',
                'aspect_ratio_width': 1080,
                'aspect_ratio_height': 1920
        })
        return Response(stream, status=status.HTTP_201_CREATED)


class LiveStreamDetail(APIView):

    """
       Retrieve, update or delete a stream instance.
    """

    def get(self, request, pk):
        stream = LiveStreams().fetch(stream_id=pk)
        return Response(stream, status=status.HTTP_200_OK)

    def put(self, request, pk):
        stream = LiveStreams().update(pk, {})
        return Response(stream, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        LiveStreams().delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def start_live_stream(request, pk):

    """
       Start a live stream.
    """

    stream = LiveStreams().start(stream_id=pk)
    return Response(stream, status=status.HTTP_200_OK)


@api_view(['PUT'])
def stop_live_stream(request, pk):

    """
       Stop a live stream.
    """

    stream = LiveStreams().stop(stream_id=pk)
    return Response(stream, status=status.HTTP_200_OK)


@api_view(['GET'])
def live_stream_state(request, pk):

    """
       Get live stream state.
    """

    stream = LiveStreams().state(stream_id=pk)
    return Response(stream, status=status.HTTP_200_OK)