from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import UserLogin, SubmitRequest, AssignWork

def index(request):
    return render(request, 'index.html')

def uslogin(request):
    return render(request, 'login.html')

def usregistration(request):
    return render(request, 'registration.html')

def usregister(request):
    if request.method == 'POST':
        try:
            r_name = request.POST['rName']
            r_email = request.POST['rEmail']
            r_password = request.POST['rPassword']
            UserLogin.objects.create(r_name=r_name, r_email=r_email, r_password=r_password)
            return redirect('login')
        except Exception as e:
            # Handle any specific exceptions here
            return render(request, 'registration.html', {'error_message': str(e)})
    return render(request, 'registration.html')

def urlogin(request):
    if request.method == 'POST':
        email = request.POST.get('rEmail')
        password = request.POST.get('rPassword')
        try:
            user = UserLogin.objects.get(r_email=email, r_password=password)
            request.session['user_id'] = user.id
            return render(request, 'userprofile.html')
        except UserLogin.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def usersubmitrequest(request):
    if request.method == 'POST':
        try:
            submit_request = SubmitRequest.objects.create(
                request_info=request.POST.get('requestinfo'),
                request_desc=request.POST.get('requestdesc'),
                requester_name=request.POST.get('requestername'),
                requester_add1=request.POST.get('requesteradd1'),
                requester_add2=request.POST.get('requesteradd2'),
                requester_city=request.POST.get('requestercity'),
                requester_state=request.POST.get('requesterstate'),
                requester_zip=request.POST.get('requesterzip'),
                requester_email=request.POST.get('requesteremail'),
                requester_mobile=request.POST.get('requestermobile'),
                request_date=request.POST.get('requestdate')
            )
            return redirect('submitrequestsuccess', request_id=submit_request.request_id)
        except Exception as e:
            return render(request, 'usersubmitrequest.html', {'error_message': str(e)})
    return render(request, 'usersubmitrequest.html')

def submit_request_success(request, request_id):
    submit_request = get_object_or_404(SubmitRequest, request_id=request_id)
    return render(request, 'submitrequestsuccess.html', {'submit_request': submit_request})

def servicestatus(request):
    if request.method == 'POST':
        request_id = request.POST.get('checkid')
        try:
            AssignWork.objects.get(request_id=request_id)
            message = f'The Work Order For ID : {request_id} Has Been Assigned'
        except AssignWork.DoesNotExist:
            message = 'Work Has Not Yet been Assigned'
        return render(request, 'servicestatus.html', {'message': message})
    return render(request, 'servicestatus.html')

def userprofile(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = UserLogin.objects.get(pk=user_id)
            user_email = user.r_email
            if request.method == 'POST':
                new_name = request.POST.get('rName')
                user.r_name = new_name
                user.save()
            user_name = user.r_name
            return render(request, 'userprofile.html', {'user_email': user_email, 'user_name': user_name})
        except UserLogin.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')

def userchangepassword(request):
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = UserLogin.objects.get(pk=user_id)
            user_email = user.r_email
            if request.method == 'POST':
                new_pass = request.POST.get('rPassword')
                user.r_password = new_pass
                user.save()
            return render(request, 'userchangepassword.html', {'user_email': user_email})
        except UserLogin.DoesNotExist:
            return redirect('login')
    return redirect('login')
