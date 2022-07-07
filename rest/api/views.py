from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import TestSerializer
from api.models import TestModel
class TestEndpoint(APIView):
    def get(self,request,id=None):
        if id:
            try:
                query=TestModel.objects.get(id=id)
                serializer=TestSerializer(instance=query)
                return Response(serializer.data)
            except TestModel.DoesNotExist:
                return Response({"message":"This name does not exists"},status=status.HTTP_404_NOT_FOUND)
        queryset=TestModel.objects.all()
        serializer=TestSerializer(instance=queryset,many=True)
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)
    def post(self,request):
        serializer=TestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
