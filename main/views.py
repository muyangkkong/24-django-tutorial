# Create your views here.
from decimal import Decimal

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from main.serializers import (
    CalculatorSerializer,
    CalculatorResponseSerializer,
)


class CalculatorAPIView(GenericAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = CalculatorSerializer

    def post(self, request):
        # de-serialization
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result: Decimal = None
        ## assignment1: 이곳에 과제를 작성해주세요
        switch(operator){
            case "+" :
             result =input_a+input_b
            case "*":
             result=input_a*input_b
            case "-" :
             result=input_a-input_b
            case "/" :
             result=input_a/input_b
               
            
        }
         
        ## end assignment1

        # serialization
        return Response(CalculatorResponseSerializer({"result": result}).data)
