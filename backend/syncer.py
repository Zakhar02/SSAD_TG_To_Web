import os
import time

from backend.tg_api import TGAPI, TGError
from backend.models import Channel, Message

import django
from django.db import transaction



def check_if_channels_are_valid(tg):
    items = Channel.objects.filter(is_checked=False)[:1]
    if len(items) == 0:
        return None
    channel = items[0]
    chat_id = tg.get_chat_id_for_handle(channel.tg_handle, timeout=3)
    if chat_id:
        channel.tg_id = chat_id
        channel.is_checked = True
        print(f'learned that @{channel.tg_handle} has chat_id={chat_id}')
    # channel.is_checked = True
    channel.save()



def select_channel_for_fetch():
    # correct channel that never had its messages fetched
    items = Channel.objects.exclude(tg_id=None).filter(is_checked=True, messages_fetched_at=None)[:1]
    if len(items) != 0:
        last_message_id = 0
        return items[0], last_message_id
    
    # if all freshly added channels already had their messages fetched
    # then select one that wasn't updated for longest
    #
    # Basically it is round-robin selection
    items = Channel.objects.order_by('messages_fetched_at')[:1]
    if len(items) != 0:
        channel = items[0]
        m_items = channel.message_set.order_by('tg_id')[:1]
        last_message_id = 0
        if len(m_items) != 0:
            last_message_id = m_items[0].tg_id
        return items[0], last_message_id
    return None, None



def fetch_fresh_messages(tg):
    channel, last_message_id = select_channel_for_fetch()
    if not channel:
        return None
    
    items = tg.get_recent_messages(channel.tg_id, limit=100, from_message_id=last_message_id)
    channel.messages_fetched_at = django.utils.timezone.now()
    with transaction.atomic():
        for data in items:
            # Current saving code is very slow
            # TODO: figure out how you do bulk insert in Django
            message = Message(text=data['text'], tg_id=data['tg_id'], channel_id=channel.id)
            message.save()
            channel.message_set.add(message)
        channel.save()



def run():
    tg = TGAPI()
    tg.login()

    while True:
        try:
            check_if_channels_are_valid(tg)
            fetch_fresh_messages(tg)
            time.sleep(5)
        except TGError as e:
            print(e)
            time.sleep(1)
