from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .models import AIAnalysis
from .serializers import AIASerializer

# Create your views here.

class AIAListAPI(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    serializer_class = AIASerializer 

    def get_queryset(self): 
        return AIAnalysis.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    #     return JsonResponse({
    #     'auth' : 'success'
    # }, json_dumps_params = {'ensure_ascii': True})

class AIADetailAPI(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = AIASerializer

    def get_queryset(self):
        return AIAnalysis.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # put은 update을 내보내는 메소드
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # delete은 destroy를 내보내는 메소드
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)