from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, parsers
from rest_framework.response import Response

from movie.models import *
from movie.serializer import *
from cinemaapp.global_resposne import ResponseInfo
# Create your views here.

def myindex(request):
    return HttpResponse("server is running")

class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    parser_classes = [parsers.JSONParser, parsers.FormParser, parsers.MultiPartParser]
    serializer_class = MovieSerializer
    http_method_names = ['post', 'get', 'put', 'delete']
    
    def list(self, request):
        response = super(MovieViewset, self).list(request)
        
        res = ResponseInfo(response.data, 'success', 200)
        return Response(res.custom_success_payload())
    
    def retrieve(self, request, pk):
        response = super(MovieViewset, self).retrieve(request, pk)
        
        res = ResponseInfo(response.data, 'success', 200)
        return Response(res.custom_success_payload())
    
    def create(self, request):
        response = super(MovieViewset, self).create(request)

        res = ResponseInfo(response.data, "movie added sucessfully", 200)
        return Response(res.custom_success_payload())

    def update(self, request, pk):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        res = ResponseInfo(serializer.data, "movie updated sucessfully", 200)
        return Response(res.custom_success_payload())

    def destroy(self, request, pk):
        super(MovieViewset, self).destroy(request,pk)

        res = ResponseInfo({}, "movie deleted sucessfully", 200)
        return Response(res.custom_success_payload())