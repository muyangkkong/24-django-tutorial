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
        input_a = Decimal(serializer.validated_data["input_a"])
        input_b = Decimal(serializer.validated_data["input_b"])
        operator = serializer.validated_data["operator"]

        if operator == "+":
            result = input_a + input_b
        elif operator == "*":
            result = input_a * input_b
        elif operator == "-":
            result = input_a - input_b
        elif operator == "/":
            result = input_a / input_b if input_b != 0 else None  # 0으로 나눌 경우 None 반환
        else:
            result = None

        ## assignment1: 이곳에 과제를 작성해주세요
    
        ## end assignment1

        # serialization
        return Response(CalculatorResponseSerializer({"result": result}).data)
