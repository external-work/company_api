from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
def send_data(request, companyname):
	data = generate_data(companyname)
	# return JsonResponse({'data':data})
	data = "The company " + data + " contains these information."
	with open("logging.txt","a") as file:
		temp = "Sending data about " + data
		file.write(temp)
	return HttpResponse(data)

def generate_data(company):
	return company