from core.helpers import RequestHelper
from core.models import RecycleRequest, Citizen, Material, Collector
from UserManagement.Controllers import TokenController


class RecycleRequestService: 
    

    @staticmethod
    def makeRecycleRequest(request):
        recycleRequestData = RequestHelper.getRequestBody(request)

        try: 
            recycleRequest = RecycleRequest()
            recycleRequest.setData(recycleRequestData, request)
            recycleRequest.save()

            return {"message": "recycle request has been successfully submitted" }
        
        except Citizen.DoesNotExist:
            return {"message": "your account does not exist"}
        
        except Material.DoesNotExist:
            return {"message": "material doess not exist"}
        
        except KeyError:
            return {"message": "invalid parameters"}
    

    def withdrawRecycleRequest(request):

        recycleRequestData = RequestHelper.getRequestBody(request)

        try:
            recycleRequest = RecycleRequest.objects.get(id = recycleRequestData["id"])

            if recycleRequest.status == "pending":
                recycleRequest.delete()
                return {"message": "Recycle Request has been deleted successfully"}
            
            elif recycleRequest.status == "validated":
                return {"message": "Your recycle request has already been validated you cannot delete it"}
            
            else: 
                return {"message": "you cannot delete a request that already has been completed"}
        
        except RecycleRequest.DoesNotExist:
            return {"message": "Recycle Request not found"}
    
    
    def getRecycleRequests(request):
        try:
            recycleRequests = RecycleRequest.objects.filter(citizen_id = Citizen.objects.get(user_id = TokenController.decodeToken(request.headers["Token"])["id"]).id, status = "pending")
            recycleRequestsData = [recycleRequest.getData() for recycleRequest in recycleRequests]
            return recycleRequestsData
        
        except RecycleRequest.DoesNotExist:
            return {"message": "You didn't make any recycle requests"}
    

    def getAllRecycleRequests(request):
        try: 
            recycleRequests = RecycleRequest.objects.filter(status="pending")
            recycleRequestsData = [ recycleRequest.getData() for recycleRequest in recycleRequests]
            return recycleRequestsData
        
        except RecycleRequest.DoesNotExist:
            return {"message": "There are not recycle requests at the moment"}
    

    def getValidatedRecycleRequests(request):
        try:
            recycleRequests = RecycleRequest.objects.filter(collector_id = Citizen.objects.get(user_id = TokenController.decodeToken(request.headers["Token"])["id"]).id, status = "validated")
            recycleRequestsData = [recycleRequest.getData() for recycleRequest in recycleRequests]
            return recycleRequestsData
        
        except RecycleRequest.DoesNotExist:
            return {"message": "You didn't make any recycle requests"}
    

    def validateRecycleRequest(request):
        recycleRequestData = RequestHelper.getRequestBody(request)
        collectorId = TokenController.decodeToken(request.headers["Token"])["id"]

        try: 
            collectorId = Collector.objects.get(user_id = collectorId).id
            RecycleRequest.objects.filter(id = recycleRequestData["id"]).update(status = "validated", collector_id = collectorId)
            return {"message": "Request has been validated"}
        
        except RecycleRequest.DoesNotExist:
            return {"message": "Request does not exist"}
        
        except KeyError:
            return {"message": "invalid parameters"}
    

    def completeRecycleRequest(request):
        recycleRequestData = RequestHelper.getRequestBody(request)

        try: 
            RecycleRequest.objects.filter(id = recycleRequestData["id"]).update(status = "completed")
            return {"message": "Request has been completed"}
        
        except RecycleRequest.DoesNotExist:
            return {"message": "Request does not exist"}
        
        except KeyError:
            return {"message": "invalid parameters"}