from core.helpers import RequestHelper
from core.models import Notification, Collector, Citizen
from UserManagement.models import User
from UserManagement.Controllers import TokenController

class NotificationService: 

    @staticmethod
    def createNotification(request):

        try:
            data = RequestHelper.getRequestBody(request)
            
            notification = Notification()
            notification.setData(data["notification"])
            return notification
        
        except KeyError:
            return "Invalid parameters"


    @staticmethod
    def addMakeRecycleRequestNotification(request):
        notification = NotificationService.createNotification(request)
        
        if notification != "Invalid parameters":
            notification.save()

            for collector in Collector.objects.all():
                notification.users.add(collector)

            return {"message": "New recycle request sent to all collectors"}
        
        return {"message": "Invalid parameters"}
    

    @staticmethod
    def addCompleteRecycleRequestNotification(request):
        notification = NotificationService.createNotification(request)
        
        try: 
            if notification != "Invalid parameters":
                notification.save()
                notification.users.add(Citizen.objects.get(user_id = User.objects.get(id = RequestHelper.getRequestBody(request)["id"])))
                return {"message": "Complete Recycle Request sent to citizen"}
            
            return {"message": "Invalid parameters"}
        
        except Citizen.DoesNotExist: 
            return {"message": "Citizen does not exist"}

    @staticmethod
    def addValidateRecycleRequestNotification(request):
        try:
            notification = NotificationService.createNotification(request)

            if notification != "Invalid parameters":
                notification.save()
                notification.users.add(Citizen.objects.get(user_id = User.objects.get(id = RequestHelper.getRequestBody(request)["id"])))
                return {"message": "Validate Recycle Request sent to citizen"}

            return {"message": "Invalid parameters"}
        
        except Citizen.DoesNotExist:
            return {"message": "Citizen does not exist"}
    

    @staticmethod
    def getNotifications(request):

        try:
            notifications = [notification for notification in Notification.objects.filter(users = Citizen.objects.get(user_id = User.objects.get(id = TokenController.decodeToken(request.headers["Token"])["id"])))]
            return {
                "notifications": [notification.getData() for notification in notifications],
                "unchecked": len([notification for notification in notifications if not notification.checked])
            }
        
        except Notification.DoesNotExist:
            return {"message": "User not found"}
    

    @staticmethod
    def checkNotifications(request):
        
        try: 
            Notification.objects.filter(users = Citizen.objects.get(user_id = User.objects.get(id = TokenController.decodeToken(request.headers["Token"])["id"]))).update(checked = True)
            return {"message": "Notifications checked"}
        
        except Notification.DoesNotExist:
            return {"message": "You have no notification"}
        
        except Citizen.DoesNotExist:
            return {"message": "Citizen not found"}

        
