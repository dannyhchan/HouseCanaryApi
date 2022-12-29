from django.shortcuts import render
from rest_framework import viewsets

# import local data
from .serializers import AnswerSerializer
from .models import AnswerModel
from .services import PropertyDataApiService
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated

# create a viewset
class AnswersViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey]
    
    # define queryset
    queryset = AnswerModel.objects.all()
     
    # specify serializer to be used
    serializer_class = AnswerSerializer

@api_view(['GET'])
@permission_classes([HasAPIKey])
def property_detail(request):
  # Retrieve property data via HousingCanaryApiService
  if request.method == 'GET':
    try:
      # TODO: Should add validation for these required params. Throw custom validation back to the response if these does not exists in the query params
      address = request.GET.get('address')
      zip_code = request.GET.get('zipcode')

      # In the future, if we decide to switch 3rd party service, we can create a different service for that return the relavant data.
      # The API method here should never be touched, business logic should be handled within the services.py (or any service layer)
      property_data = PropertyDataApiService().get_property_data(address, zip_code)
      return Response(property_data)
    except Exception as e:
      return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

