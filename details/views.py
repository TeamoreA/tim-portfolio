from django.shortcuts import render
from django.views import generic
from .models import Project


def index(request):
    """
    view for the index page
    """
    project_list = Project.objects.order_by('-start_date')
    context = {'project_list': project_list}
    images = []
    for project in project_list:
        # get the right image path
        img_path = "/"+'/'.join(project.image.name.split('/')[1:])
        images.append(img_path)
    project_list = zip(project_list, images)
    context = {'project_list': project_list}
    return render(request, 'details/index.html', context)
    