from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework.parsers import JSONParser

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated])
def index(request):
    if request.method == 'GET':
        return render(request, 'articles/index.html')
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated])
def all(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
# @permission_classes([IsAuthenticated])
def show(request, pk):
    article = Article.objects.get(pk=pk)
    serializer = ArticleSerializer(article)
    context = {'data': serializer.data}
    return render(request, 'articles/show.html', context)
