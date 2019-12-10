from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from .serializers import CollectionSerializer, ExhibitSerializer, ModuleSerializer, QuestionSerializer
from .models import Collection, Exhibit, Module, Question

class CollectionView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CollectionView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        try:
            data = Collection.objects.filter(colID = self.kwargs['cID']) 
        except KeyError:
            data = Collection.objects.filter()
        
        ser = CollectionSerializer(data, many=True)

        return JsonResponse(ser.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        #Request data
        data = JSONParser().parse(request)
        #Check to see if the entry already exists
        try:
            dataUp = Collection.objects.get(colID = data['colID'])
            if dataUp is not None:
                print("Found")
                ser = CollectionSerializer(dataUp, data = data )
                ser.is_valid()
                ser.save()
                return HttpResponse(status=200)
        except Collection.DoesNotExist:
            ser = CollectionSerializer(data = data) 

        if ser.is_valid():
            ser.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)

class ExhibitView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ExhibitView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        try:
            data = Exhibit.objects.filter(exhID = self.kwargs['eID']) 
        except KeyError:
            data = Exhibit.objects.filter()
        
        ser = ExhibitSerializer(data, many=True)

        return JsonResponse(ser.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        #Request data
        data = JSONParser().parse(request)
        #Check to see if the entry already exists
        try:
            dataUp = Exhibit.objects.get(exhID = data['exhID'])
            if dataUp is not None:
                print("Found")
                ser = ExhibitSerializer(dataUp, data = data )
                ser.is_valid()
                ser.save()
                return HttpResponse(status=200)
        except Exhibit.DoesNotExist:
            ser = ExhibitSerializer(data = data) 

        if ser.is_valid():
            ser.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)

class ModuleView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ModuleView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        try:
            data = Module.objects.filter(modID = self.kwargs['mID']) 
        except KeyError:
            data = Module.objects.filter()
        
        ser = ModuleSerializer(data, many=True)
        
        return JsonResponse(ser.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        #Request data
        data = JSONParser().parse(request)
        #Check to see if the entry already exists
        try:
            dataUp = Module.objects.get(modID = data['modID'])
            if dataUp is not None:
                print("Found")
                ser = ModuleSerializer(dataUp, data = data )
                ser.is_valid()
                ser.save()
                return HttpResponse(status=200)
        except Module.DoesNotExist:
            ser = ModuleSerializer(data = data) 

        if ser.is_valid():
            ser.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)

class QuestionView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(QuestionView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        try:
            data = Question.objects.filter(modID = self.kwargs['qID']) 
        except KeyError:
            data = Question.objects.filter()
        
        ser = ModuleSerializer(data, many=True)

        return JsonResponse(ser.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        #Request data
        data = JSONParser().parse(request)
        #Check to see if the entry already exists
        try:
            dataUp = Question.objects.get(modID = data['queID'])
            if dataUp is not None:
                print("Found")
                ser = ModuleSerializer(dataUp, data = data )
                ser.is_valid()
                ser.save()
                return HttpResponse(status=200)
        except Question.DoesNotExist:
            ser = ModuleSerializer(data = data) 

        if ser.is_valid():
            ser.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)