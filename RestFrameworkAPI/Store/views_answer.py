from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, MultiPartParser
from Store.models import Item
from Store.serializers import ItemSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, parser_classes, permission_classes, renderer_classes
from django.contrib.auth import authenticate, login
from Store.renderers import JPEGRenderer, PNGRenderer

#Implemented 
@api_view(['GET'])
@renderer_classes([JPEGRenderer, PNGRenderer])
def get_picture(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(item)
    

# TODO 
@api_view(['GET', 'POST'])
@parser_classes([JSONParser, MultiPartParser])
def item_list(request):
    if request.method == 'GET':
        items  = Item.objects.all()
        serializer = ItemSerializer(items, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = ItemSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes([JSONParser, MultiPartParser])
def item_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = ItemSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

