from django.db.models import Prefetch, F, Sum
from django.shortcuts import render

from clients.models import Client
from services.models import Subscription
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.serializers import SubjectSerializer


# Create your views here.

class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.all().select_related("plan", "service").prefetch_related(Prefetch('client', queryset= Client.objects
                                                                    .all()
                                                                    .select_related("user")
                                                                    .only("company_name", "user__email"))).\
        annotate(price=F("service__full_price") - F("service__full_price") * F("plan__discount_percent")/100.00)

    serializer_class = SubjectSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        response = super().list(request, *args, **kwargs)

        response_data = {"results": response.data}
        response_data["total_amount"] = queryset.aggregate(total=Sum("price"))["total"]
        response.data = response_data
        return response