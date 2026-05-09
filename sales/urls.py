from django.urls import path

from .views import HealthView, QuoteDetailView, QuoteListCreateView

urlpatterns = [
    path("health/", HealthView.as_view(), name="sales-health"),
    path("quotes/", QuoteListCreateView.as_view(), name="sales-quote-list-create"),
    path("quotes/<uuid:quote_id>/", QuoteDetailView.as_view(), name="sales-quote-detail"),
]
