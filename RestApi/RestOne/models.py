from django.db import models

class ModelEmail(models.Model):
    toUser = models.EmailField()
    fromUser = models.EmailField()
    subjectEmail = models.CharField(max_length=264)
    bodyEmail = models.CharField(max_length=264)

    def  __str__(self):
        return str(self.subjectEmail)
