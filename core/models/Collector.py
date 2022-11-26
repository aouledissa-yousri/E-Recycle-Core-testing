from django.db import models 
from .Citizen import Citizen


class Collector(Citizen):
    


    def setData(self, data):
        super().setData(data)
    
    def getData(self):
        userData = super().getData()
        userData["type"] = "collector"
        return userData