from django.http import JsonResponse
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer

from subscriber.models import Channel


@api_view(['GET'])
@renderer_classes(JSONRenderer)
def get_channels(request):
    return JsonResponse([])
    # channels = list(Channel.objects.all())
    # return JsonResponse(channels, safe=False)
