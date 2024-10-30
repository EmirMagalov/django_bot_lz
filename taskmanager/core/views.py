from rest_framework import status
from django.shortcuts import render,HttpResponse
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from .models import *
from rest_framework import generics,viewsets
from .serializers import PostsSerializer
def main(request):
    return HttpResponse("<h1>OK</h1>")


class PostsViewsSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if pk:
            return Posts.objects.filter(pk=pk)
        else:
            return Posts.objects.all()


    @action(methods=["get"],detail=False)
    def getuserpost(self, request):
        user_id = request.query_params.get("user_id")


        post = Posts.objects.filter(user_id=user_id)
        serializer = PostsSerializer(post, many=True)
        return Response(serializer.data)

    @action(methods=["put"], detail=False)
    def putadmin(self, request):
        message_id = request.query_params.get("message_id")

        try:
            # Получаем пост по message_id
            post = Posts.objects.get(message_id=message_id)
        except Posts.DoesNotExist:
            return Response({"detail": "Пост не найден."}, status=status.HTTP_404_NOT_FOUND)

        # Используем сериализатор для валидации и обновления
        serializer = PostsSerializer(post, data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()  # Сохраняем изменения в БД
            return Response(serializer.data)  # Возвращаем обновлённые данные
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class PostApiList(generics.ListCreateAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer
#
# class PostApiUpdate(generics.UpdateAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer
#
# class PostApiDetailViews(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer

# class PostsAPIviews(APIView):
#     def get(self,request):
#         p=Posts.objects.all().values()
#         return Response({"posts":PostsSerializer(p,many=True).data})
#
#     def post(self,request):
#         serializer=PostsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # post_new=Posts.objects.create(
#         #     title=request.data['title'],
#         #     content=request.data['content']
#         # )
#         return Response({"post":serializer.data})
#     def put(self,request,*args,**kwargs):
#         pk=kwargs.get("pk",None)
#         if not pk:
#             return Response({"error":"Put not allowed"})
#         try:
#             instance=Posts.objects.get(pk=pk)
#         except:
#             return Response({"error":"Objects not exists"})
#         serializer=PostsSerializer(data=request.data,instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

