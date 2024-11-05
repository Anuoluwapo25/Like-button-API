# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class ArticleLikeView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
            article.likes += 1  
            article.save() 
            serializer = ArticleSerializer(article)  
            return Response(serializer.data, status=status.HTTP_200_OK)  
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

        

class ArticleDetailView(APIView):

    def get(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
