from . import tg_api

from django.db import models

class Channel(models.Model):
    tg_handle = models.CharField(max_length=40)
    tg_id = models.BigIntegerField()

    @classmethod
    def create_from_tg_handle(cls, handle):
        tg_id = tg_api.get_chat(handle)
        if not tg_id:
            return None
        # instance is not saved yet,
        # it is up to the caller to save it to database
        return cls(tg_handle=handle, tg_id=tg_id)

    def __str__(self):
        return '<Channel {} {}>'.format(self.tg_handle, self.tg_id)

class Message(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE) 
    content_type = models.CharField(max_length=40)
    tg_id = models.BigIntegerField()
    text = models.TextField()

    @classmethod
    def create_initial_messages_for_channel(cls, channel):
        pass

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.channel, self.tg_id, self.text)