from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Puppy
from .serializers import PuppySerializer


class SinglePuppy(APIView):
    """
    Base class for GET, DELETE, UPDATE a single puppy
    """
    @staticmethod
    def get(request: Request, pk: int) -> Response:
        """
        Get details of a single puppy
        :param request: Http request
        :param pk: Puppy id
        :return: All puppy details
        """
        return Response({})

    @staticmethod
    def delete(request: Request, pk: int) -> Response:
        """
        Delete a single puppy
        :param request: Http request
        :param pk: Puppy id
        :return: Success message with status code
        """
        return Response({})

    @staticmethod
    def put(request: Request, pk: int) -> Response:
        """
        Update a single puppy
        :param request: Http request
        :param pk: Puppy id
        :return: Success message with status code
        """
        return Response({})


class Puppies(APIView):
    """
    Base class for GET and POST multiple puppies
    """
    @staticmethod
    def get(request: Request) -> Response:
        """
        Get all puppies
        :param request: Http request
        :return: List of puppies
        """
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request: Request) -> Response:
        """
        Add a puppy to the database
        :param request: Http request
        :return: Success message with status code
        """
        return Response({})

