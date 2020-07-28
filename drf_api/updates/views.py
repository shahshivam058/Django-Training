from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from cpf_api.mixins import JsonResponseMixin
from django.core.serializers import serialize
import json
from .models import Update
from django.views.generic import View
from .models import Update

# Create your views here.
# def detail_view(request):
#     return render() == > # return json js object notation 
#     return HttpResponse(get_template().render({}))

# def json_example_view(request):
#     # data = Update.objects.all()
#     """
#     URI = FOR REST API
#     GET - RETRIVE DATA
#     """
#     context = {
#         'count' : 1000,
#         'content' : 'some new content'
#     }
#     return JsonResponse(context)
#     # BEFORE THIS 
#     # data = json.dumps(context)
#     # return response(data,content-type = 'applicatation/json) used in older version 

class JsonCBV(View):
    def get(self,request,*args, **kwargs):
        data =  {
        'count' : 1000,
        'content' : 'some new content'
        }
        return JsonResponse(data)

class JsonCbv2(JsonResponseMixin,View):
    def get(self,request,*args, **kwargs):
        data =  {
            'count' : 1000,
            'content' : 'some new content'
            }
        return self.render_to_response(data)    

class SerializedView(JsonResponseMixin,View):
    def get(self,request,*args, **kwargs):
        qs = Update.objects.all().serialize()
        # data =  serialize('json',qs,fields=('user','content'))
        return HttpResponse(qs,content_type='application/json')

class SerializedDetailView(JsonResponseMixin,View):
    def get(self,request,*args, **kwargs):
        qs = Update.objects.get(id=1)
        data = qs.serialize()
        # data =  serialize('json',[qs,],fields=('user','content'))
        return HttpResponse(data,content_type='application/json')