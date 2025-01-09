from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def gotRoutes(request):
    routes = [
        'GET /api'
        'GET /api/rooms',
        'GET /api/room/:id'
    ]
    return Response(routes)