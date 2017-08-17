from django.db import models

class Data(models.Model):
    txt = models.TextField()

    def __str__(self):
        return self.txt
