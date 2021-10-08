from django.db import models
#existing tables in database

class Channel(models.Model): #used fore searching in frontend
    chat_name = models.CharField(max_length=40)

    def __str__(self):
        return '{}'.format(self.chat_name)

class Message(models.Model):
    chat_name = models.ForeignKey('Channel', on_delete=models.CASCADE)
    chat_id = models.BigIntegerField() #id of a channel
    content_type = models.CharField(max_length=40) #type of a message
    message_id = models.BigIntegerField() #id of a message inside a channel
    text = models.TextField() #should be separate for photos, videos, documents and so on

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.chat_name, self.chat_id,
                                           self.content_type, self.message_id, self.text)