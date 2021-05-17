from .models import Students
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


# Create your views here.
class StudentViewSet(ViewSet):
    """
    API endpoint that allows users to  view student details.
    """

    def list(self, request):
        try:
            queryset = Students.objects.all().order_by('date_of_admission', 'first_name')
            serializer_data = StudentSerializer(queryset, many=True)
            return Response(serializer_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error': str(e)})
