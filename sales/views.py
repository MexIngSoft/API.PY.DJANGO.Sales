from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Quote
from .serializers import QuoteSerializer


class HealthView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response({"status": "ok", "service": "sales-api"})


class QuoteListCreateView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        serializer = QuoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quote = serializer.save()
        return Response(QuoteSerializer(quote).data, status=201)


class QuoteDetailView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, quote_id):
        quote = Quote.objects.prefetch_related("Items").filter(Id=quote_id).first()
        if quote is None:
            return Response({"error": {"code": "QUOTE_NOT_FOUND", "id": str(quote_id)}}, status=404)
        return Response(QuoteSerializer(quote).data)
