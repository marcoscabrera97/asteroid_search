from django.shortcuts import render
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from asteroids.services.query_params_service import QueryParamsService
from asteroids.services.get_asteroids_service import GetAsteroidsService
from asteroids.serializers import WidthHeightSerializer
from rest_framework.exceptions import ParseError

query_params_service = QueryParamsService()
get_asteroids_service = GetAsteroidsService()
def index(request):
    return render(request, 'asteroid_form.html')

def asteroids_list(request):
    params = query_params_service.get_object_params(request.META['QUERY_STRING'])
    width_height_serializer = WidthHeightSerializer(data=params)
    if not width_height_serializer.is_valid(raise_exception=False):
        raise ParseError(detail="Request body malformed")
    asteroids = get_asteroids_service.get_asteroids(width_height_serializer.data['width'], width_height_serializer.data['height'])
    print(asteroids)
    return render(request, 'asteroids_list.html', {'asteroids': asteroids})
