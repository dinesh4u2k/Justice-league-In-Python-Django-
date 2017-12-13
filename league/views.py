from django.shortcuts import render
from django.views.generic import ListView
from .models import sp

# Create your views here.

# def index(request):
# 	return render(request,'league/home.html')

class HomeView(ListView):

	model = sp
	queryset = sp.objects.order_by('-date')[:9]
	template_name = 'home.html'

	def get_context_data(self, **kwargs):
		context = super(HomeView,self).get_context_data(**kwargs)
		return context
		