from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from pyhalo import PyHalo

def index(request):
	return HttpResponse("<h1> This is the retrieve image app homepage")

class TestView(TemplateView):
	template_name = 'test.html'

	def get_context_data(self, **kwargs):
		context = super(TestView, self).get_context_data(**kwargs)
		ocp_apim_subscription_key = "7480bf871b6f4b758c3975ae3b7de8af"
		h = PyHalo(ocp_apim_subscription_key)
		emblem_image_url = h.get_emblem_image("ummmYAAaaa")
		stats = h.get_arena_service_records("yams101390")
		context['kills'] = stats['Results'][0]['Result']['ArenaStats']['TotalKills']
		context['headshot'] = stats['Results'][0]['Result']['ArenaStats']['TotalHeadshots']


		return context
