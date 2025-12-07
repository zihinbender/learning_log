from django.urls import path

from .views import index, TopicList, TopicDetail

urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicList.as_view(), name="topics"),
    path("topics/<int:pk>/", TopicDetail.as_view(), name="topic"),
]
