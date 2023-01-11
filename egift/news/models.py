from django.db import models

# Create your models here.
class news(models.Model):
    news_title = models.CharField(max_length = 50)
    news_description = models.TextField()
    news_date = models.DateField()

    class meta:
        db_table = "news"

class Event(models.Model):
    event_name = models.CharField(max_length=25)
    event_venue = models.CharField(max_length=100)
    event_pic = models.ImageField(upload_to = "event_pic")

    class meta:
        db_table = "event"

@property
def imageURL(self):
    try:
        url = self.event_pic.url
    except:
        url = ""
    return url