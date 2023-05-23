
# GenericApiView and Model Mixin
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import MyPermission

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    # authentication_classes=[SessionAuthentication]
    # # permission_classes=[IsAuthenticated]
    # # permission_classes=[IsAdminUser]
    # # permission_classes=[IsAuthenticatedOrReadOnly]
    # # permission_classes=[DjangoModelPermissions]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes=[MyPermission]
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    