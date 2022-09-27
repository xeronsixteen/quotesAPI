from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from webapp.views import QuoteViewSet, LogoutView, RaiseRate, DecreaseRate

app_name = 'api_v1'

router = DefaultRouter()
router.register('quotes', QuoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rase/<int:pk>', RaiseRate.as_view(), name='raise_rate'),
    path('decrease/<int:pk>', DecreaseRate.as_view(), name='decrease_rate'),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='logout_view'),

]
