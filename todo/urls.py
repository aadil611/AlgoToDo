from rest_framework import routers

from .views import ToDoModelViewSet

router = routers.DefaultRouter()
router.register(r'todos', ToDoModelViewSet)


urlpatterns = router.urls