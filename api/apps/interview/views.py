from interview.models import Interview
from interview.serializers import InterviewSerializer
from rest_framework import viewsets


class InterviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
