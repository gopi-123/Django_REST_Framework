from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    # dummy data
    # person = {"name":"Dennis", "age":28}
    # Now query all the items from our database  Item
    items = Item.objects.all()

    # Now we need to serialize the data items, before we can  return them
    # many = True means, we need to serialize multiple items

    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer  = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)