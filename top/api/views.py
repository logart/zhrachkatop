import random

from drf_yasg.utils import swagger_auto_schema
from receipt.models import Printer, CheckType
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema

from .serializers import PrinterSerializer


class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        return 0


class OrderViewSet(viewsets.ViewSet):
    """
    Api for creating orders
    """
    schema = CustomAutoSchema()

    def list(self, request):
        rnd = random.randint(0, 22)
        Printer(rnd, 'name', 'key', CheckType.KITCHEN.name, 1).save()
        printers = Printer.objects.all()
        serializer = PrinterSerializer(printers, many=True)
        return Response(serializer.data)

    def retrieve(self, request):
        rnd = random.randint(0, 22)
        Printer(rnd, 'name', 'key', CheckType.KITCHEN.name, 1).save()
        printers = Printer.objects.all()
        serializer = PrinterSerializer(printers, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PrinterSerializer, responses={200: PrinterSerializer(many=True)})
    def create(self, request):
        print(request.data)
        return Response(request.data)
