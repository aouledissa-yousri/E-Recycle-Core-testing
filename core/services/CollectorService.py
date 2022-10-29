from core.services import CitizenService
from core.helpers import RequestHelper
from UserManagement.models import GenericUser
from core.models import Citizen, Collector


class CollectorService: 
    
    @staticmethod
    def signUp(request):

        collector = Collector()
        result = CitizenService.createUserProfile("generic", request)

        if result == "Account created successfully":
            collectorData = RequestHelper.getRequestBody(request)

            collector.setData({
                "user" : GenericUser.objects.get(username = collectorData["user_profile"]["username"]),
                "name": collectorData["name"],
                "lastname": collectorData["lastname"]
            })

            collector.save()
            return "Account created successfully"
                
        return result    