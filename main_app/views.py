from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Tool, Review
from django.shortcuts import redirect


class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Tools(TemplateView):
    template_name = "tools.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        name = self.request.GET.get("name")
        if name != None:
            context["tools"] = Tool.objects.filter(name__icontains=name)
        else:
            context["tools"] = Tool.objects.all().order_by('-price')
        return context

class ToolsAdd(CreateView):
    model = Tool
    fields = ['name', 'image', 'price', 'description']
    template_name = 'tools_add.html'
    def get_success_url(self):
        return reverse('tool_detail', kwargs={'pk': self.object.pk})

class ToolDetail(DetailView):
    model = Tool
    template_name = "tool_detail.html"

class ToolUpdate(UpdateView):
    model = Tool
    fields = ['name', 'image', 'price', 'description']
    template_name = 'tool_update.html'
    def get_success_url(self):
        return reverse('tool_detail', kwargs={'pk': self.object.pk})

class ToolDelete(DeleteView):
    model = Tool
    template_name = 'tool_delete.html'
    success_url = "/tools/"

class ReviewCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        body = request.POST.get("body")
        tool = Tool.objects.get(pk=pk)
        Review.objects.create(title=title, body=body, tool=tool)
        return redirect('artist_detail', pk=pk)