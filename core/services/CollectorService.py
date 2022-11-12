from core.services import CitizenService
from core.helpers import RequestHelper
from UserManagement.models import GenericUser
from core.models import Collector
from UserManagement.models import GoogleUser
from UserManagement.Controllers import GoogleUserController, TokenController


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


    #google login 
    def googleLogin(request):
        googleUserData =  GoogleUserController.googleLogin(request)


        #seperate google account username to name and lastname 
        googleUserData["name"] = googleUserData["user"]["username"].split(" ")[0]
        googleUserData["lastname"] = googleUserData["user"]["username"].split(" ")[1]


        try: 
            collector = Collector.objects.get(user_id = TokenController.decodeToken(googleUserData["token"])["id"])

        except Collector.DoesNotExist:
            collector = Collector()

            collector.setData({
                "user" : GoogleUser.objects.get(username = googleUserData["user"]["username"]),
                "name": googleUserData["name"],
                "lastname": googleUserData["lastname"]
            })

            collector.save()

        collector.save()

        return {
            "message": "success",
            "user": collector.getData(),
            "token": googleUserData["token"]
        }  