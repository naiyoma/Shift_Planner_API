from django.urls import path
# from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from .views import (
    UserRegistrationView, UserListView, LoginView, UserShiftViewSet, 
    UserShiftListView, UserShiftDetailListView)

router = DefaultRouter()

router.register(r'createuser', UserRegistrationView)
router.register(r'listusers', UserListView)
router.register(r'create_shift', UserShiftViewSet)
router.register(r'shifts', UserShiftListView)

schema_view = get_swagger_view(title='My API')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('shifts/<uuid:user_id>/', UserShiftDetailListView.as_view({'get': 'list'}), name='shift-list'),
    path('docs/', schema_view)
] + router.urls
