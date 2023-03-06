from django.urls import path, include
# from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from .views import (
    UserRegistrationView, UserListView, LoginView, UserShiftViewSet, 
    UserShiftListView, UserShiftDetailListView, OrganizationViewSet, OrgListView)

router = DefaultRouter()
schema_view = get_swagger_view(title='My API')
urlpatterns = [
    path('createuser/', UserRegistrationView.as_view({'post': 'create'}), name='create-user'),
    path('create_shift/', UserShiftViewSet.as_view({'post': 'create'}), name='create-shift'),
    path('shifts/', UserShiftListView.as_view({'get': 'list'}), name='shift-list'),
    path('orgs/', OrgListView.as_view({'get': 'list'}), name='org-list'),
    path('listusers/', UserListView.as_view({'get': 'list'}), name='user-list'),
    path('create-org/', OrganizationViewSet.as_view({'post': 'create'}),name='create-org'),
    path('shifts/<uuid:user_id>/', UserShiftDetailListView.as_view({'get': 'list'}), name='shift-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('docs/', schema_view)
]
