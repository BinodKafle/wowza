from django.urls import path

from ..views import LiveStreamList, LiveStreamDetail, start_live_stream, \
    stop_live_stream, live_stream_state

urlpatterns = [
    path('live-streams/', LiveStreamList.as_view()),
    path('live-streams/<str:pk>/', LiveStreamDetail.as_view()),
    path('live-streams/<str:pk>/start/', start_live_stream),
    path('live-streams/<str:pk>/stop/', stop_live_stream),
    path('live-streams/<str:pk>/state/', live_stream_state)
]
