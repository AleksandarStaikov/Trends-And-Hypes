from rest_framework import viewsets

from dummyproject import models, serializers

class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerizlizer