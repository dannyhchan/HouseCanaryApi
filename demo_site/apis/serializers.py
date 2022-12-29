# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import AnswerModel

# Create a model serializer
class AnswerSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = AnswerModel
		fields = ('questionId', 'propertyId', 'answer')
