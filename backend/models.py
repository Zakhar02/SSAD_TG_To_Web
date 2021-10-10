from django.db import models



class Channel(models.Model):
    tg_handle = models.CharField(max_length=40)
    tg_id = models.BigIntegerField(null=True)
    is_checked = models.BooleanField(default=False)
    messages_fetched_at = models.DateTimeField(null=True)

    def is_correct_channel(self):
        return (self.is_checked and self.tg_id)

    @classmethod
    def create_from_tg_handle(cls, handle):
        tg_id = tg.get_chat_id_for_handle(handle)
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
        return '<Message {}, {}, "{}">'.format(self.channel, self.tg_id, self.text)