from django.http import JsonResponse
from .models import Jifunze
from .serializers import JifunzeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#introduce a decorator
@api_view(['GET', 'POST'])
def jifunze_list(request): 

#get all the jifunze drinks
#serializer them
#return json
 if request.method == 'GET':
    jifunze = Jifunze.objects.all()
    serializer = JifunzeSerializer(jifunze, many=True)
    return JsonResponse({"jifunze": serializer.data})
 
 if request.method == 'POST':
    serializer = JifunzeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
   
   
