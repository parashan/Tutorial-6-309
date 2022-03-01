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
    pass

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
@parser_classes([JSONParser, MultiPartParser])
def item_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    pass

