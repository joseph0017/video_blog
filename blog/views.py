from .models import Videos
from django.http import HttpResponseRedirect
from django.urls import reverse

from blog.models import Images
from blog.forms import DocumentForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.template import Context, RequestContext
from django.shortcuts import render_to_response

# Create your views here.


class Homepage(TemplateView):
    template_name = 'base.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'

class AboutPage(TemplateView):
    template_name = 'about.html'


class IndexPage(TemplateView):
    template_name = 'index.html'




def upload_video(request):
    if request.method == 'POST':
        title = request.POST['title']
        video = request.POST['video']

        content = Videos(title=title, video=video)
        content.save()
        return redirect('video')

    return render(request, 'upload.html')


def display(request):
    videos = Videos.objects.all()
    context = {
        'videos': videos,
    }

    return render(request, 'video-page.html', context)


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Images(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list.html'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    images = Images.objects.all()

    # Render list page with the documents and the form
    return render(request,
        'blog/list.html',
        {'images': images, 'form': form})

def index(request):
    return render(request,'blog/list.html')

