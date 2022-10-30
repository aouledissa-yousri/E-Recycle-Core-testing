from rest_framework.decorators import api_view
from django.http import JsonResponse
from core.services import RecycleRequestService
from core.decorators import checkAccessToken

class RecycleRequestController: 
    

    @api_view(["POST"])
    @staticmethod
    @checkAccessToken
    def makeRecycleRequest(request):
        return JsonResponse(RecycleRequestService.makeRecycleRequest(request))
    

    @api_view(["DELETE"])
    @staticmethod
    @checkAccessToken
    def withdrawRecycleRequest(request):
        return JsonResponse(RecycleRequestService.withdrawRecycleRequest(request))
    

    @api_view(["GET"])
    @staticmethod
    @checkAccessToken
    def getRecycleRequests(request):
        return JsonResponse(RecycleRequestService.getRecycleRequests(request), safe = False)
    
    @api_view(["GET"])
    @staticmethod
    @checkAccessToken
    def getAllRecycleRequests(request):
        return JsonResponse(RecycleRequestService.getAllRecycleRequests(request))
    

    @api_view(["PATCH"])
    @staticmethod
    @checkAccessToken
    def validateRecycleRequest(request):
        return JsonResponse(RecycleRequestService.validateRecycleRequest(request))
    

    @api_view(["PATCH"])
    @staticmethod
    @checkAccessToken
    def completeRecycleRequest(request):
        return JsonResponse(RecycleRequestService.completeRecycleRequest(request))
    
