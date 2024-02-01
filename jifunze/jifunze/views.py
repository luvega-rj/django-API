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
   
@api_view(['GET','PUT' 'DELETE'])
def jifunze_detail(request, id):
  
  try:
  #pk is primary key
    jifunze = Jifunze.objects.get(pk=id) 
  except Jifunze.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)   

  
  if request.method == 'GET':
    serializer = JifunzeSerializer(jifunze)
    return Response(serializer.data)
  elif request.method == 'POST':
    pass

  elif request.method == 'DELETE':
    pass
  


 
