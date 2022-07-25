from django.http import HttpResponseNotFound
from rest_framework import serializers
from rest_framework.views import APIView
from . import models
from rest_framework.response import Response

import random

# Create your views here.

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WordList
        fields  = ['pk','gender', 'word']


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = models.WordList.objects.all()
        random_word = random.choice(all_words)
        serialized_random_word = WordSerializer(random_word, many=False)
        return Response(serialized_random_word.data)

class NextWord(APIView):
    def get(self, request, pk, format=None):
        next_word = models.WordList.objects.filter(pk__gt=pk).first()
        if not next_word:
            return HttpResponseNotFound()
        ser_word = WordSerializer(next_word, many=False)
        return Response(ser_word.data)