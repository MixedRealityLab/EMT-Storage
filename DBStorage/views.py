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

from .serializers import ParticipantSerializer, CollectionAnswerSerializer, GiftAnswersSerializer, GiftParticipantSerializer, StorageSettingsSerializer
from .models import Participant, CollectionAnswer, GiftAnswers, GiftParticipant, StorageSettings

class StorageSettingsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(StorageSettingsView, self).dispatch(*args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        ser = StorageSettingsSerializer(data = StorageSettings.objects.get())

        return JsonResponse(ser.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = JSONParser().parse(request)

        print(data)

        if data == "tag_removed":
            StorageSettings.objects.filter().delete()
            print("Removing Tag")
            return HttpResponse(status=201)
        elif data is not None:
            print(StorageSettings.objects.filter())
            if StorageSettings.objects.filter():
                print("Active Tag")
                return HttpResponse(status=201)
            else:
                print("No Tag active")
                newTag = StorageSettings(userID = data)
                newTag.save()
                return HttpResponse(status=201)
            
        return HttpResponse(status=400)
        

class GiftParticipantView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(GiftParticipantView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        
        try:
            data = GiftParticipant.objects.filter(parID = self.kwargs['pfID']) 
        except KeyError:
            data = GiftParticipant.objects.filter()
        print(GiftParticipant.objects.filter())
        ser = GiftParticipantSerializer(data, many=True)

        return JsonResponse(ser.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        #Request data
        data = JSONParser().parse(request)
        #Check to see if the entry already exists
        try:
            dataUp = GiftParticipant.objects.get(parID = data['parID'])
            if dataUp is not None:
                print("Found")
                ser = GiftParticipantSerializer(dataUp, data = data )
                ser.is_valid()
                ser.save()
                return HttpResponse(status=200)
        except GiftParticipant.DoesNotExist:
            ser = GiftParticipantSerializer(data = data) 

        if ser.is_valid():
            ser.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)

class GiftAnswersView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(GiftAnswersView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        try:
            data = GiftAnswers.objects.filter(parID = self.kwargs['pfID']) 
        except KeyError:
            data = GiftAnswers.objects.filter()
        
        ser = GiftAnswersSerializer(data, many=True)

        return JsonResponse(ser.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        #Request data
        data = JSONParser().parse(request)
        #Check to see if the entry already exists
        print(data)

        try:
            dataUp = GiftAnswers.objects.get(parID = data['parID'])
            if dataUp is not None:
                print("Found")
                ser = GiftAnswersSerializer(dataUp, data = data )
                ser.is_valid()
                ser.save()
                return HttpResponse(status=200)
        except GiftAnswers.DoesNotExist:
            ser = GiftAnswersSerializer(data = data) 

        if ser.is_valid():
            ser.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)


class ParticipantView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ParticipantView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        try:
            data = Participant.objects.filter(parID = self.kwargs['pID']) 
        except KeyError:
            data = Participant.objects.filter()
        
        ser = ParticipantSerializer(data, many=True)

        return JsonResponse(ser.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        #Request data
        data = JSONParser().parse(request)
        #Check to see if the entry already exists
        try:
            dataUp = Participant.objects.get(parID = data['parID'])
            if dataUp is not None:
                print("Found")
                ser = ParticipantSerializer(dataUp, data = data )
                ser.is_valid()
                ser.save()
                return HttpResponse(status=200)
        except Participant.DoesNotExist:
            ser = ParticipantSerializer(data = data) 

        if ser.is_valid():
            ser.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)

class CollectionAnswersView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CollectionAnswersView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        try:
            data = CollectionAnswer.objects.filter(colID = self.kwargs['caID']) 
        except KeyError:
            data = CollectionAnswer.objects.filter()
        
        ser = CollectionAnswerSerializer(data, many=True)

        return JsonResponse(ser.data, safe=False)
    
    def post(self, request, *args, **kwargs):
        #Request data
        data = JSONParser().parse(request)
        #Check to see if the entry already exists
        try:
            dataUp = CollectionAnswer.objects.get(colID = data['colID'])
            if dataUp is not None:
                print("Found")
                ser = CollectionAnswerSerializer(dataUp, data = data )
                ser.is_valid()
                ser.save()
                return HttpResponse(status=200)
        except CollectionAnswer.DoesNotExist:
            ser = CollectionAnswerSerializer(data = data) 

        if ser.is_valid():
            ser.save()
            return HttpResponse(status=201)
        return HttpResponse(status=400)

       