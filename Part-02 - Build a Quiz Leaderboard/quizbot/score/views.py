from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ScoreSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db.models import F

from .models import Score

class UpdateScores(APIView):

    def post(self, request, format=None):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():

            name = serializer.validated_data['name']
            points = serializer.validated_data['points']

            if Score.objects.filter(name=name).exists():
                serializer = Score.objects.get(name=name)
                serializer.points = F('points') + points

            serializer.save()

            return Response(None, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Leaderboard(APIView):

    def get(self, request, formate=None, **kwargs):
        scores = Score.objects.all().order_by('-points')[:10]
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)