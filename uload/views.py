from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError
from rest_framework import status, viewsets
from uload.models import UploadMedia
from uload.serializers import UloadSerializer

# Create your views here.
class UploadMediaView(viewsets.ModelViewSet):
    queryset = UploadMedia.objects.all()
    serializer_class = UloadSerializer
    parser_classes = [MultiPartParser]
    def create(self, request, format=None):
        serializer = UloadSerializer(data=request.data)
        if 'uploaded_file' not in request.data:
            raise ParseError("Empty content")
        if serializer.is_valid():
            serializer.save()

        uploaded_data = request.data['uploaded_file']
        print('Print Information: \n')
        print(str(type(uploaded_data)))
        print(uploaded_data.size)
        if uploaded_data.readable():
            print("Readable\n")
            uploaded_data.seek(0)
            content = uploaded_data.read()
            print(str(type(content)))
        return Response(status=204)
