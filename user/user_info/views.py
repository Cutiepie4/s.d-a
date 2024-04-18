from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import user_registration

def user_validation(uname, password):
    user_data = user_registration.objects.get(email=uname, password=password)
    if user_data:
        return 'Valid User'
    else:
        return 'Invalid User'

@csrf_exempt
def user_info(request):
    uname = request.POST.get("User Name")
    resp = {}
    if uname:
        respdata = user_data(uname)
        dict1 = {}
        if respdata:
            dict1['First Name'] = respdata.get('fname', '')
            dict1['Last Name'] = respdata.get('lname', '')
            dict1['Mobile Number'] = respdata.get('mobile', '')
            dict1['Email Id'] = respdata.get('email', '')
            dict1['Address'] = respdata.get('address', '')
            if dict1:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['data'] = dict1
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'User Not Found'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'All fields are mandatory'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched'
    return HttpResponse(json.dumps(resp), content_type='application/json')
