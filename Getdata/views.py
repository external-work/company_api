from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
# Create your views here.
def send_data(request, companyname):
	main_data = json.loads(request.body)
	custom_data = main_data['parameters']['Company']
	data = generate_data(companyname)
	# return JsonResponse({'data':data})
	data = "The company " + custom_data + " contains these information."
	return HttpResponse(data)

def generate_data(company):
	return company