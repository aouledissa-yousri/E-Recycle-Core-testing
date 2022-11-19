from django.db import models
from django.utils import timezone
from .Citizen import Citizen

class Notification(models.Model):
    users = models.ManyToManyField(Citizen)
    description = models.CharField(max_length = 255, default = '')
    date = models.DateTimeField(default = timezone.now())
    checked = models.BooleanField(default=False)


    def setData(self, data):
        self.description = data["description"]
        self.date = data["date"]
        self.checked = data["checked"]
    
    def getData(self):
        return {
            "description": self.description,
            "date": self.date,
            "checked": self.checked
        }
    
    def checkNotification(self):
        self.checked = True
