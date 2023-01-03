from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView, UserListView, LoginView


router = DefaultRouter()

router.register(r'createuser', UserRegistrationView)
router.register(r'listusers', UserListView)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
] + router.urls
# urlpatterns = [
#     path('createuser/', UserRegistrationView.as_view({'post': 'create'}), name='createuser')
# ] + router.urls

# urlpatterns = router.urls