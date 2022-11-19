from rest_framework.decorators import api_view
from django.http import JsonResponse
from core.services import NotificationService
from UserManagement.decorators import checkAccessToken

class NotificationController: 

    @api_view(["POST"])
    @staticmethod
    @checkAccessToken
    def addMakeRecycleRequestNotification(request):
        return JsonResponse(NotificationService.addMakeRecycleRequestNotification(request))
    

    @api_view(["POST"])
    @staticmethod
    @checkAccessToken
    def addValidateRecycleRequestNotification(request):
        return JsonResponse(NotificationService.addValidateRecycleRequestNotification(request))
    

    @api_view(["POST"])
    @staticmethod
    @checkAccessToken
    def addCompleteRecycleRequestNotification(request):
        return JsonResponse(NotificationService.addCompleteRecycleRequestNotification(request))


    @api_view(["GET"])
    @staticmethod
    @checkAccessToken
    def getNotifications(request):
        return JsonResponse(NotificationService.getNotifications(request), safe= False)
    
    @api_view(["PATCH"])
    @staticmethod
    @checkAccessToken
    def checkNotifications(request):
        return JsonResponse(NotificationService.checkNotifications(request))
    
    