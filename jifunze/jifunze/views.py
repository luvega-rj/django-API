from django.http import JsonResponse
from .models import Jifunze
from .serializers import JifunzeSerializer

#get all the jifunze drinks
#serializer them
#return json
def jifunze_list(request):

    jifunze = Jifunze.objects.all()
    serializer = JifunzeSerializer(jifunze, many=True)
    return JsonResponse({"drinks": serializer.data}, safe=False)
