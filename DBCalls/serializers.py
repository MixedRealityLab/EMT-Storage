from rest_framework import serializers
from .models import Collection, Exhibit, Module, Question

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class ExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'