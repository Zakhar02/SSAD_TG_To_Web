from django.http import JsonResponse
from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer

from backend.models import Channel


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_channels(request):
    return JsonResponse([])
    # channels = list(Channel.objects.all())
    # return JsonResponse(channels, safe=False)




MESSAGES = [
    { 'text': "Тестовое сообщение из канала" },
    { 'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent efficitur urna ligula, id convallis mi varius at. Morbi sagittis aliquet sapien ut pellentesque. Duis mauris eros, tempus eget lectus quis, aliquet sollicitudin ipsum. Morbi sit amet urna accumsan, eleifend massa sit amet, dignissim odio. Sed quis risus auctor, pretium diam ut, tempus quam." },
    { 'text': "Ещё одно сообщение" },
    { 'text': "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur" },
    { 'text': "Nulla lacus dui, scelerisque a congue id, feugiat sed leo. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In in libero ac nisl suscipit pellentesque eget sit amet lorem. Nunc at velit fermentum, vulputate tortor blandit, congue turpis. Pellentesque et ante euismod lacus rhoncus viverra. Phasellus finibus neque odio, vel tristique nibh suscipit sit amet. Phasellus vestibulum eget sapien sit amet porta" }
]

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_messages(request, **kwargs):
    # TODO: actually select messages from the table
    # use kwargs['channelId'] to select messages for it
    # print(kwargs['channelId'])
    return JsonResponse(MESSAGES, safe=False)