from django.shortcuts import render
from django.http import HttpResponse ,  Http404
import requests
import json
from .country import Country
import pycountry
import os
#89f3c3da224041ce8e20fb9df9087e4d

p = os.getcwd()
print(p)

def home(request):
	c = requests.get("http://ipinfo.io/json")
	country = pycountry.countries.get(alpha_2=c.json()['country'])
	contn= country.name
	cata = 'business'
	url = ('http://newsapi.org/v2/top-headlines?'
       'country='+c.json()['country'].lower()+'&'
       'apiKey=89f3c3da224041ce8e20fb9df9087e4d')
	try:
		response = requests.get(url)
		news = response.json()
	except:
		raise Http404("Poll does not exist")
	return render(request , "html/index.html" ,{
					 'news':news['articles'],
					 'country_name':Country.country_name.keys() , 
					 'catagory':Country.catagory,	
					 'cont_name':contn,
					 'cata' : cata
					 })
def next(request):
	if request.method == 'GET':
		cont = request.GET['cont']
		cata = request.GET['cata']
	contn = Country.country_name[cont]
	url = ('http://newsapi.org/v2/top-headlines?'+
			'country='+contn+'&'
			'category='+cata+'&'
			'apiKey=89f3c3da224041ce8e20fb9df9087e4d')
	try:
		response = requests.get(url)
		news = response.json()
	except:
		raise Http404("Poll does not exist")
	return render(request , "html/index.html" ,{
					 'news':news['articles'],
					 'country_name':Country.country_name.keys() , 
					 'catagory':Country.catagory,
					 'cont_name':cont,
					 'cata' : cata
					 })