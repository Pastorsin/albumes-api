from interview.models import Interview
from interview.serializers import InterviewSerializer
from rest_framework import mixins, viewsets


class InterviewViewSet(viewsets.ReadOnlyModelViewSet,
                       mixins.CreateModelMixin):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer
