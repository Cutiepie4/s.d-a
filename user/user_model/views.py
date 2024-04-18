from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

@csrf_exempt
def registration_req(request):
    resp = {}
    # uname = request.POST.get("User Name")
    resp['status'] = 'Success'
    resp['status_code'] = '200'
    resp['message'] = 'Welcome to Ecommerce website...'
    
    return HttpResponse(json.dumps(resp), content_type='application/json')
