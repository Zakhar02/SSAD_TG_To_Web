from django.http import JsonResponse, HttpResponseNotFound

from rest_framework.decorators import renderer_classes, api_view
from rest_framework.renderers import JSONRenderer

from backend.models import Channel



# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def get_channels(request):
#     return JsonResponse([])

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_messages(request, **kwargs):
    try:
        channel = Channel.objects.get(tg_handle=kwargs['channelId'])
        if channel.is_correct_channel():
            messages = channel.message_set.all()[:10]
            json = list(map(lambda x: {'text': x.text, 'tg_id': x.tg_id}, messages))
            return JsonResponse(json, safe=False)
        return JsonResponse([], safe=False)
    except Channel.DoesNotExist:
        # save channel to database, expect worker to check it
        # and fetch messages. For now just return empty messages
        channel = Channel(tg_handle=kwargs['channelId'])
        channel.save()
        return JsonResponse([], safe=False)