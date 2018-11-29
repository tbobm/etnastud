from rest_framework import viewsets

from tane.models import Student
from tane.serializers import StudentSerializer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
