from rest_framework.decorators import api_view
from django.http import JsonResponse
from core.services import CollectorService
from core.decorators import checkAccessToken


class CollectorController:
    
    @api_view(["POST"])
    @staticmethod
    def signUp(request):
        return JsonResponse({"message" : CollectorService.signUp(request)})
