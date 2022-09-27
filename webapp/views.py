from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import DjangoModelPermissions, SAFE_METHODS, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from webapp.models import Quote
from webapp.serializer import QuoteSerializer, QuoteUpdateSerializer


# Create your views here.


class QuoteViewSet(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT']:
            return QuoteUpdateSerializer
        else:
            return QuoteSerializer

    def get_queryset(self):
        if not self.request.user.has_perms(['moderator']):
            quotes = Quote.objects.filter(status='moderated')
        else:
            quotes = Quote.objects.all()
        if self.kwargs.get('pk'):
            if self.request.user.has_perms(['moderator']):
                quotes = Quote.objects.filter(pk=self.kwargs.get('pk'))
            else:
                quotes = Quote.objects.filter(pk=self.kwargs.get('pk'), status='moderated')
        return quotes

    def update(self, request, *args, **kwargs):
        if not self.request.user.has_perms(['moderator']):
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not self.request.user.has_perms(['moderator']):
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)


class RaiseRate(View):
    def get(self, request, *args, pk, **kwargs):
        quote = get_object_or_404(Quote, pk=pk)
        quote.rating += 1
        quote.save()
        context = {
            'rating': quote.rating,
            'id': quote.pk
        }
        return JsonResponse(context)


class DecreaseRate(View):
    def get(self, request, *args, pk, **kwargs):
        quote = get_object_or_404(Quote, pk=pk)
        quote.rating -= 1
        quote.save()
        context = {
            'rating': quote.rating,
            'id': quote.pk
        }
        return JsonResponse(context)


class LogoutView(APIView):
    permission_classes = [DjangoModelPermissions]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({'status': 'ok'})
