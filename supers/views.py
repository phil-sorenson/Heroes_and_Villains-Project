
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from super_types.models import SuperType


from .models import Super
from .serializers import SuperSerializer
from rest_framework import status

from supers import serializers

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'GET':
        queryset = Super.objects.all()
        super_type = request.query_params.get('type')
        if super_type:
            queryset = queryset.filter(super_type__type = super_type)
            serializer = SuperSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            heroes = Super.objects.filter(super_type = 1)
            villains = Super.objects.filter(super_type = 2)
            heroes_serializer = SuperSerializer(heroes, many=True)
            villains_serializer = SuperSerializer(villains, many=True)
            
            custom_response_dictionary = {
                
                "Heroes":  heroes_serializer.data,
                "Villains": villains_serializer.data,
            }
            return Response(custom_response_dictionary)

     



@api_view(['GET', 'POST', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer
    


