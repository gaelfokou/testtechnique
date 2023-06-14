from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from articles.models import Article
from commentaires.models import Commentaire
from commentaires.serializers import CommentaireSerializer
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated])
def index(request, pk):
    data = JSONParser().parse(request)
    data['article'] = pk
    serializer = CommentaireSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated])
def all(request, pk):
    commentaires = Commentaire.objects.filter(article=pk)
    serializer = CommentaireSerializer(commentaires, many=True)
    return JsonResponse(serializer.data, safe=False)
