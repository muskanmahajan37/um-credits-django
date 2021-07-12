from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import SubjectSerializer
from .models import Subject


class SubjectsView(APIView):

    def get(self, request):
        subjects = Subject.objects.all()

        serializer = SubjectSerializer(subjects, many=True)

        return Response(serializer.data,
                        status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            # code = request.data.get('code', None)
            # name = request.data.get('name', None)
            # credits = request.data.get('credits', None)
            # year = request.data.get('year', None)

            return Response(serializer.data,
                            status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_404_NOT_FOUND)
