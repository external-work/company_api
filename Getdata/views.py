from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
def send_data(request, companyname):
	data = generate_data(companyname)
	# return JsonResponse({'data':data})
	data = "The company " + data + " contains these information."
	print("Sent data about" + data)
	return HttpResponse(data)

def generate_data(company):
	return company