from django.shortcuts import render
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'details/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return ["Hello world","what now"]