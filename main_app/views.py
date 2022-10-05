from django.shortcuts import render, redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from .models import Tool, Review, Wishlist
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = "wishlist.html"
    
    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        context['wishlists'] = Wishlist.objects.filter(user = self.request.user)
        return context

class About(TemplateView):
    template_name = "about.html"

class Tools(TemplateView):
    template_name = "tools.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        name = self.request.GET.get("name")
        if name != None:
            context["tools"] = Tool.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["tools"] = Tool.objects.all().order_by('-price')
            context["header"] = "Popular Items"
        return context

@method_decorator(login_required, name='dispatch')
class ToolsAdd(CreateView):
    model = Tool
    fields = ['name', 'image', 'price', 'description']
    template_name = 'tools_add.html'
    def get_success_url(self):
        return reverse('tool_detail', kwargs={'pk': self.object.pk})

class ToolDetail(DetailView):
    model = Tool
    template_name = "tool_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wishlists'] = Wishlist.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class ToolUpdate(UpdateView):
    model = Tool
    fields = ['name', 'image', 'price', 'description']
    template_name = 'tool_update.html'
    def get_success_url(self):
        return reverse('tool_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class ToolDelete(DeleteView):
    model = Tool
    template_name = 'tool_delete.html'
    success_url = "/tools/"

@method_decorator(login_required, name='dispatch')
class ReviewCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        body = request.POST.get("body")
        tool = Tool.objects.get(pk=pk)
        Review.objects.create(title=title, body=body, tool=tool)
        return redirect('tool_detail', pk=pk)
    
        
@method_decorator(login_required, name='dispatch')
class WishlistToolAssoc(View):
    def get(self, request, pk, tool_pk):
        assoc = request.GET.get('assoc')
        if assoc == 'remove':
            Wishlist.objects.get(pk=pk).tools.remove(tool_pk)
        if assoc == 'add':
            Wishlist.objects.get(pk=pk).tools.add(tool_pk)
        return redirect('wishlists')
    
class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("tools")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
 