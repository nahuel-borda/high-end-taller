from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from devices.models import *
from devices.serializers import *

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

	@action(detail=False, methods=['GET'], name='Get Status Count')
	def status_count(self, request, *args, **kwargs):
		return Response(data=Service.status_count(), status=200)
	
	@action(detail=False, methods=['GET'], name='Get Status Count by Date')
	def status_count_by_date(self, request, *args, **kwargs):
		return Response(data=Service.status_count_by_date(), status=200)
	
	@action(detail=False, methods=['GET'], name='Get New Services Count by Date')
	def service_ingress_count_by_date(self, request, *args, **kwargs):
		return Response(data=Service.services_ingress_by_date(), status=200)
	
class OperatorViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Operator.objects.all()
	serializer_class = OperatorSerializer

	@action(detail=False, methods=['GET'], name='Get Operator by Workload')
	def operator_by_workload(self, request, *args, **kwargs):
		return Response(data=Operator.by_workload(), status=200)
	
class ProviderViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Provider.objects.all()
	serializer_class = ProviderSerializer

	@action(detail=False, methods=['GET'], name='Get Provider by Participation')
	def provider_by_participation(self, request, *args, **kwargs):
		return Response(data=Provider.by_participation(), status=200)

class DeviceViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Device.objects.all()
	serializer_class = DeviceSerializer

class ModelViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Model.objects.all()
	serializer_class = ModelSerializer

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer

class ClientViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Client.objects.all()
	serializer_class = ClientSerializer

class PartViewSet(viewsets.ReadOnlyModelViewSet):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = Part.objects.all()
	serializer_class = PartSerializer