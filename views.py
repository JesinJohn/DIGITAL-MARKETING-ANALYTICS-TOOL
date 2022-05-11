from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import loader 
from django.template import Context
from administrator.models import DBConnection
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect 
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import json
from django.contrib import messages
from json import dumps
from django.http import JsonResponse
from django.views.decorators.cache import cache_control
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from OnlineAnalizer.settings import EMAIL_HOST_USER
def adminlogin(request):
        t = loader.get_template('Administrator/adminlogin.html')
        return HttpResponse(t.render())
def forget(request):
        template=loader.get_template('login/forget.html')
        return HttpResponse(template.render())
def otp(request):
        template=loader.get_template('login/otp.html')
        return HttpResponse(template.render())
def npass(request):
        template=loader.get_template('login/npass.html')
        return HttpResponse(template.render())

@csrf_exempt
def fpasswordemail(request):
        email_id=request.POST["email_id"]
        db = DBConnection()
        #qry = "select mkt_title from marketarea where mkt_id=5"
        #cnd=[]
        qry = "select * from empdetails where emp_email=%s"
        cnd = [email_id]
        #return HttpResponse(qry)
        login = db.gettable(qry, cnd)
        if(len(login)>0):
                subject = 'PASSWORD RESETING FOR CHARITY WORLD'
                message ="Your Password is : "+ login[0]["emp_password"]
                send_mail(subject,message, EMAIL_HOST_USER, [email_id], fail_silently=False)
                messages.success(request,'password sent to your email')
                 
                return render(request,'Administrator/adminlogin.html',{})
        else:

                messages.success(request,'email_id does not exists')
        return redirect("../forget/")




@csrf_exempt
def updatepassword(request):
        newpass=request.POST["newpassword"]
        conpass=request.POST["conpassword"]
        if newpass==conpass:
                password=models.login.objects.filter(user_name='a@gmail.com')
                password.update(password=newpass)
                messages.success(request,'password changed  successfully')
                return redirect("../login/")
                
        else:
                messages.success(request,'wrong password entered')
                
@csrf_exempt
def fpasswordotp(request):
        otp=request.POST["otp"]
        obj1=models.forgotpassword(random_number=otp)
        obj1.save()
        return redirect("../npass/")