from rest_framework.views import APIView
from rest_framework.response import Response
from mainapp import serializers


class HelloAPIView(APIView):
    """Test view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request):

        test_message = [
            'This is my test program',
        ]

        return Response({'Greeting': 'Hello!', 'message': test_message})

