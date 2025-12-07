from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Topic, Entry

def index(request):
    return render(request, "learning_logs/index.html")

class TopicList(ListView):
    model = Topic
    template_name = "learning_logs/topics.html"
    context_object_name = "topics"

class TopicDetail(DetailView):
    model = Topic
    template_name = "learning_logs/topic.html"
    context_object_name = "topic"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["entries"] = Entry.objects.filter(topic=self.object).order_by("-date_added")
        return context
