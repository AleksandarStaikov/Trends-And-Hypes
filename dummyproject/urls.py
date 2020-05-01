from rest_framework.routers import DefaultRouter

from dummyproject.views import PersonViewSet

router = DefaultRouter()

router.register(r'api/person', PersonViewSet, basename='person')

urlpatterns = router.urls