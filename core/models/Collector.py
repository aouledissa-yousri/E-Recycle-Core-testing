from django.db import models 
from .Citizen import Citizen


class Collector(Citizen):
    


    def setData(self, data):
        super().setData(data)