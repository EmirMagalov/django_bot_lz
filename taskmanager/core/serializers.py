import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *

# class PostModel:
#     def __init__(self,title,content):
#         self.title=title
#         self.content=content

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields="__all__"



# def encode():
#     model=PostModel("AJ","Content:AJ")
#     model_sr=PostsSerializer(model)
#     print(model_sr.data,type(model_sr.data),sep="\n")
#     json=JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream=io.BytesIO(b'{"title":"AJ","content":"Content:AJ"}')
#     data=JSONParser().parse(stream)
#     serializer=PostsSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)