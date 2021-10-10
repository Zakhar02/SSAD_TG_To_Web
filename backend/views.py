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
    # algorithm
    # 1) Check if channel with this id is already in the table
    # 2) If it is already there, then just fetch messages from DB and return them
    # 3) If it is absent, then insert it, fetch messages from Telegram, insert to DB and return them
    try:
        channel = Channel.objects.get(tg_handle=kwargs['channelId'])
        return JsonResponse(MESSAGES, safe=False)
    except Channel.DoesNotExist:
        channel = Channel.create_from_tg_handle(kwargs['channelId'])
        if not channel:
            return JsonResponse([], safe=False)
        channel.save()
        return JsonResponse(MESSAGES, safe=False)
        # messages = Message.create_initial_messages_for_channel(channel)

    # TODO: actually select messages from the table
    # use kwargs['channelId'] to select messages for it
    # print(kwargs['channelId'])
    return JsonResponse(MESSAGES, safe=False)