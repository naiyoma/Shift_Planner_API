from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    UserRegistrationView, UserListView, LoginView, UserShiftViewSet, 
    UserShiftListView, UserShiftDetailListView)


router = DefaultRouter()

router.register(r'createuser', UserRegistrationView)
router.register(r'listusers', UserListView)
router.register(r'create_shift', UserShiftViewSet)
router.register(r'shifts', UserShiftListView)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('shifts/<uuid:user_id>/', UserShiftDetailListView.as_view({'get': 'list'}), name='shift-list')
] + router.urls
