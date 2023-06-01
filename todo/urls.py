
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import routers
from django.urls import path
import json

from .views import ToDoModelViewSet

router = routers.DefaultRouter()
router.register(r'todos', ToDoModelViewSet)


# @api_view(["GET","POST"])
# def test(request):
#     print("Hello World")
#     print(request.data)
#     # data = json.loads(request.body)
#     # print(data)
#     return Response("ok")

urlpatterns = router.urls