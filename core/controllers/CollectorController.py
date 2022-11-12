from rest_framework.decorators import api_view
from django.http import JsonResponse
from core.services import CollectorService, CitizenService
from core.decorators import checkAccessToken


class CollectorController:
    
    @api_view(["POST"])
    @staticmethod
    def signUp(request):
        return JsonResponse({"message" : CollectorService.signUp(request)})
    

    @api_view(["GET"])
    @staticmethod 
    def googleLoginGateway(request):
        return JsonResponse(CitizenService.googleLoginGateway(request))
    

    @api_view(["GET"])
    @staticmethod
    def googleLogin(request):
        return JsonResponse(CollectorService.googleLogin(request))


    @api_view(["GET"])
    @staticmethod 
    def facebookLoginGateway(request):
        return JsonResponse(CitizenService.facebookLoginGateway(request))
    
    @api_view(["GET"])
    @staticmethod
    def facebookLogin(request):
        return JsonResponse(CollectorService.facebookLogin(request))
    

    
