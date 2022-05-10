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

def adminlogin(request):
        t = loader.get_template('Administrator/adminlogin.html')
        return HttpResponse(t.render())
def adminlog(request):
        name = request.GET['username']
        password = request.GET['password']
        db = DBConnection()
        #qry = "select mkt_title from marketarea where mkt_id=5"
        #cnd=[]
        qry = "select * from empdetails where emp_email=%s and emp_password=%s"
        cnd = [name,password]
        #return HttpResponse(qry)
        login = db.gettable(qry, cnd)
        if(len(login)>0):

                for l in login:

                        usertype = l["user_type"]
                        request.session['emp_email'] = name
                                
                        if usertype == "admin":

                                return redirect('adminindex')
                        elif usertype == "emp":
                                #request.session['emp_email'] = name
                                return redirect('empindex')
                        else:
                                message = 'Incorrect Username & Password,Login Failed'
                                messages.success(request,message)
                                return render(request, 'Administrator/adminlogin.html', {})
                                
        else:

                message = 'Incorrect Username & Password,Login Failed'
                messages.success(request,message)
                return render(request, 'Administrator/adminlogin.html', {'message': message})
                 
def adminindex(request):
        t = get_template('Administrator/adminindex.html')
        html = t.render()
        return HttpResponse(html)

def empindex(request):
        t = get_template('Administrator/emp/empindex.html')
        html = t.render()
        return HttpResponse(html)
def empviewemploye(request): 
        qry = "select * from empdetails"
        db = DBConnection()
        emp = db.gettable(qry)
        return render(request, 'Administrator/emp/empviewemploye.html',{'emp_list': emp}) 
def empmonthlyads(request):
        t = get_template('Administrator/emp/empmonthlyads.html')
        html = t.render()
        return HttpResponse(html)
def empemployeeads(request):
        t = get_template('Administrator/emp/empemployeeads.html')
        html = t.render()
        return HttpResponse(html)
def empprogressads(request):
        t = get_template('Administrator/emp/empprogressads.html')
        html = t.render()
        return HttpResponse(html)


def changepwd(request):
        t = get_template('Administrator/changepwd.html')
        
        html = t.render()
        return HttpResponse(html)
def changepassword(request):
        email=request.session['emp_email'] 
        current = request.GET['pwd']
        new = request.GET['Npwd']        
        confirm = request.GET['Cpwd']
        if(new == confirm):
            message= 'successfully change password'
            db = DBConnection()
            qry = "select * from empdetails where emp_email=%s and emp_password=%s"
            cnd = [email,current]
            #return HttpResponse(qry)
            change = db.gettable(qry, cnd)
            #return HttpResponse(change)
            if(len(change)>0):
                qryupdate = "update  empdetails set emp_password=%s where emp_email=%s"
                update=(new,email)
                db.manipulate(qryupdate, update) 
                message='changepassword successfully' 
                return render(request, 'Administrator/changepwd.html', {'message': message})
        else:
            message = 'Mismaching Password,changepassword Failed'
            return render(request, 'Administrator/changepwd.html', {'message': message})


def changepwdemp(request):
        t = get_template('Administrator/emp/changepwd.html')
        
        html = t.render()
        return HttpResponse(html)
def changepasswordemp(request):
        email=request.session['emp_email'] 
        current = request.GET['pwd']
        new = request.GET['Npwd']        
        confirm = request.GET['Cpwd']
        if(new == confirm):
            message= 'successfully change password'
            db = DBConnection()
            qry = "select * from empdetails where emp_email=%s and emp_password=%s"
            cnd = [email,current]
            #return HttpResponse(qry)
            change = db.gettable(qry, cnd)
            #return HttpResponse(change)
            if(len(change)>0):
                qryupdate = "update  empdetails set emp_password=%s where emp_email=%s"
                update=(new,email)
                db.manipulate(qryupdate, update) 
                message='changepassword successfully' 
                return render(request, 'Administrator/emp/changepwd.html', {'message': message})
        else:
            message = 'Mismaching Password,changepassword Failed'
            return render(request, 'Administrator/emp/changepwd.html', {'message': message})

def addemployee(request):
        dictionary = {}
        return render(request, 'Administrator/employee/addemployee.html',dictionary)
def viewemployee(request): 
        qry = "select * from empdetails"
        db = DBConnection()
        emp = db.gettable(qry)
        return render(request, 'Administrator/employee/viewemployee.html',{'emp_list': emp})      
def monthlyads(request):
        t = get_template('Administrator/employee/monthlyads.html')
        html = t.render()
        return HttpResponse(html)
def employeeads(request):
        t = get_template('Administrator/employee/employeeads.html')
        html = t.render()
        return HttpResponse(html)
def progressads(request):
        t = get_template('Administrator/employee/progressads.html')
        html = t.render()
        return HttpResponse(html)
def managemarketing(request):
        qry = "select * from marketarea"
        db = DBConnection()
        data = db.gettable(qry)
        return render(request, 'Administrator/managemarketing/managemarketing.html',{'marketarea_list': data})        
def createteam(request):
        qryteam = "select * from marketarea"
        db = DBConnection()
        datateam = db.gettable(qryteam)
        qry1 = "select * from empdetails"
        empdata = db.gettable(qry1)
        qry2 = "select * from empdetails e join marketingteam mt on(e.emp_id=mt.emp_id) join marketarea ma on(ma.mkt_id=mt.mkt_id) "
        team_list = db.gettable(qry2)
        return render(request, 'Administrator/managemarketing/createteam.html',{'marketarea_list': datateam,'employee_list': empdata,'marketingteam_list':team_list})


def showads(request):
        db = DBConnection()
        qryteam = "select * from marketarea"
        datateam = db.gettable(qryteam)
        qryads = "select * from marketingteam"
        dataads = db.gettable(qryads)
        qry1 = "select * from empdetails"
        empdata = db.gettable(qry1)
        qrydate = "select * from advertisment"
        datadate = db.gettable(qrydate)
        qryad = "select * from marketingteam mt join advertisment a on(mt.code_no=a.code_no) join empdetails e on(e.emp_id=a.emp_id)join marketarea ma on(ma.mkt_id=mt.mkt_id)"
        ad_list = db.gettable(qryad)
        return render(request, 'Administrator/managemarketing/showads.html',{'code_list': dataads,'date_list':datadate,'employee_list': empdata,'marketarea_list': datateam,'ads_list':ad_list })

def searchads(request):
        db = DBConnection()
        date= request.GET["date"]
        qrydate= 'select * from marketingteam mt join advertisment a on(mt.code_no=a.code_no) join empdetails e on(e.emp_id=a.emp_id) join marketarea ma on(ma.mkt_id=mt.mkt_id) where a.ad_date=%s'

        val = [date]
        dataads = db.gettable(qrydate,val)
        #return HttpResponse(dataads)
        return render(request, 'Administrator/managemarketing/searchads.html',{'ads_list': dataads })

def admission(request):
        qryadm = "select * from admission"
        db = DBConnection()
        adm = db.gettable(qryadm)
        return render(request, 'Administrator/employee/admission.html',{'adm_list': adm})
def course(request):
        qrycur = "select * from course"
        db = DBConnection()
        cur = db.gettable(qrycur)
        return render(request, 'Administrator/employee/course.html',{'course_list': cur})
def telephonic(request):
        qrytele = "select * from telephonic_enq"
        db = DBConnection()
        tele = db.gettable(qrytele)
        return render(request, 'Administrator/employee/telephonic.html',{'tele_list': tele})

def saveemp(request):
        emp_name = request.POST['Name']
        emp_address = request.POST['Address']
        emp_gender = request.POST['Gender']
        emp_phone = request.POST['Phone']
        emp_joindate = request.POST['Joindate']
        emp_email = request.POST['Email'] 
        emp_password = request.POST['Password']
        utype='emp'
        db = DBConnection()
        qury2 = "insert into empdetails(emp_name,emp_address,emp_gender,emp_phone,emp_joindate,emp_email,emp_password,user_type)values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val2 = (emp_name,emp_address,emp_gender,emp_phone,emp_joindate,emp_email,emp_password,utype)
        db.manipulate(qury2,val2)
        t = get_template('Administrator/employee/addemployee.html')
        html = t.render() 
        message = 'Add employee successfully'
        return render(request,'Administrator/employee/addemployee.html',{'message': message} )
def savearea(request):
        mkt_title = request.POST['Title']
        mkt_type = request.POST['Type']
        db = DBConnection()
        qury3 = "insert into marketarea(mkt_title,mkt_type)values(%s,%s)"
        val3 = (mkt_title,mkt_type)
        db.manipulate(qury3,val3)
        return redirect('managemarketing')  
def saveteam(request):
        emp_id = request.POST['Employee']
        mkt_id = request.POST['Area']
        code_no = request.POST['Code']
        db = DBConnection()
        sql = "select * from marketingteam where code_no = %s "
        val = [code_no]
        no = db.gettable(sql,val)
        #return HttpResponse(no)
        if(len(no)<=0):
            qury4 = "insert into marketingteam(emp_id,mkt_id,code_no)values(%s,%s,%s)"
            val4 = (emp_id,mkt_id,code_no)
            db.manipulate(qury4,val4)
        #return HttpResponse(code_no)
            return redirect('createteam')
        else:
            return redirect('createteam')
def savead(request):
        ad_date = +-request.POST['Date']
        code_no = request.POST['Code']
        ip_address = request.POST['IP']
        emp_id = request.POST['Employee']
        mkt_id = request.POST['Area']
        db = DBConnection()
        qury5 = "insert into advertisment(ad_date,emp_id,mkt_id,code_no,ip_address)values(%s,%s,%s,%s,%s)"
        val5 = (ad_date,emp_id,mkt_id,code_no,ip_address)
        db.manipulate(qury5,val5)
        return redirect('showads')

def monthlyadhit(request):
        month=request.GET['month']
        tuple=[]
        db = DBConnection()
        sql="select * from marketarea"
        marketArea = db.gettable(sql)
        #return HttpResponse(marketArea)
        for m in marketArea:
                diction={}
                diction['y']=gethit(month,m["mkt_id"])
                diction['label']=m['mkt_title']
				
                #return HttpResponse(m['mkt_title'].decode())
                tuple.append(diction);
        result=json.dumps(tuple)
        return HttpResponse(result)
def gethit(month,mktid):
        currentYear = "2021"
        startdate=""
        enddate=""
        if(month=="January"):
                startdate=currentYear+"-01-01"
                enddate=currentYear+"-01-31"
        elif(month=="February"):
                startdate=currentYear+"-02-01"
                enddate=currentYear+"-02-28"
        elif(month=="March"):
                startdate=currentYear+"-03-01"
                enddate=currentYear+"-03-31"
        elif(month=="April"):
                startdate=currentYear+"-04-01"
                enddate=currentYear+"-04-30"
        elif(month=="May"):
                startdate=currentYear+"-05-01"
                enddate=currentYear+"-05-31"
        elif(month=="June"):
                startdate=currentYear+"-06-01"
                enddate=currentYear+"-06-30"
        elif(month=="July"):
                startdate=currentYear+"-07-01"
                enddate=currentYear+"-07-31"
        elif(month=="August"):
                startdate=currentYear+"-08-01"
                enddate=currentYear+"-08-30"
        elif(month=="September"):
                startdate=currentYear+"-09-01"
                enddate=currentYear+"-09-31"
        elif(month=="October"):
                startdate=currentYear+"-10-01"
                enddate=currentYear+"-10-31"
        elif(month=="November"):
                startdate=currentYear+"-11-01"
                enddate=currentYear+"-11-30"
        elif(month=="December"):
                startdate=currentYear+"-12-01"
                enddate=currentYear+"-12-31"
        db = DBConnection()
        sql="select count(*) as counter from advertisment where ad_date between %s and %s and mkt_id=%s"
        condition=(startdate,enddate,mktid)  
        data = db.gettable(sql,condition)
        #return HttpResponse(data)
        v=data[0]['counter']
        return v

def monthlyreach(request):
        months=['January','February','March','April','May','June','July','August','September','October','November','December'];
         
        diction= {}
        tuple=[]
        index=0;
        for m in months:
                index=index+1
                diction={}
                diction['y']=getreach(m)
                diction['label']=m;
                tuple.append(diction);
        result=json.dumps(tuple)
        
         
        return HttpResponse(result)

      
def getreach(month):
        currentYear = "2021"
        startdate=""
        enddate=""
        if(month=="January"):
                startdate=currentYear+"-01-01"
                enddate=currentYear+"-01-31"

        elif(month=="February"):
                startdate=currentYear+"-02-01"
                enddate=currentYear+"-02-28"
        elif(month=="March"):
                startdate=currentYear+"-03-01"
                enddate=currentYear+"-03-31"
        elif(month=="April"):
                startdate=currentYear+"-04-01"
                enddate=currentYear+"-04-30"
        elif(month=="May"):
                startdate=currentYear+"-05-01"
                enddate=currentYear+"-05-31"
        elif(month=="June"):
                startdate=currentYear+"-06-01"
                enddate=currentYear+"-06-30"
        elif(month=="July"):
                startdate=currentYear+"-07-01"
                enddate=currentYear+"-07-31"
        elif(month=="August"):
                startdate=currentYear+"-08-01"
                enddate=currentYear+"-08-30"
        elif(month=="September"):
                startdate=currentYear+"-09-01"
                enddate=currentYear+"-09-31"
        elif(month=="October"):
                startdate=currentYear+"-10-01"
                enddate=currentYear+"-10-31"
        elif(month=="November"):
                startdate=currentYear+"-11-01"
                enddate=currentYear+"-11-30"
        elif(month=="December"):
                startdate=currentYear+"-12-01"
                enddate=currentYear+"-12-31"
        else:
             return HttpResponse(month)  
        db = DBConnection()
        sql="select count(*) as counter from advertisment where ad_date between %s and %s"
        condition=(startdate,enddate)  
        data = db.gettable(sql,condition)
        #return HttpResponse(data)
        v=data[0]['counter']
        return v
def employeereach(request):
        month=request.GET['month']
        qry = "select * from empdetails where user_type='emp'"
        #qry = "select * from empdetails"

        db = DBConnection()
        employess = db.gettable(qry) 
        diction= {}
        tuple=[]
        index=0;
        #return HttpResponse((employess))

        for m in employess:
                index=index+1
                diction={}
                hits =getemployemonthlyhit(month,m["emp_id"]);
                hit= hits[0];
                if hit > 0:

                        diction['y']=hit;
                        diction['indexLabel']=m["emp_name"]
                        tuple.append(diction);
        result=json.dumps(tuple)
          

         
        return HttpResponse(result)

def getemployemonthlyhit(month,emp_id):
        currentYear = "2021"
        startdate=""
        enddate=""
        if(month=="January"):
                startdate=currentYear+"-01-01"
                enddate=currentYear+"-01-31"
        elif(month=="February"):
                startdate=currentYear+"-02-01"
                enddate=currentYear+"-02-28"
        elif(month=="March"):
                startdate=currentYear+"-03-01"
                enddate=currentYear+"-03-31"
        elif(month=="April"):
                startdate=currentYear+"-04-01"
                enddate=currentYear+"-04-30"
        elif(month=="May"):
                startdate=currentYear+"-05-01"
                enddate=currentYear+"-05-31"
        elif(month=="June"):
                startdate=currentYear+"-06-01"
                enddate=currentYear+"-06-30"
        elif(month=="July"):
                startdate=currentYear+"-07-01"
                enddate=currentYear+"-07-31"
        elif(month=="August"):
                startdate=currentYear+"-08-01"
                enddate=currentYear+"-08-30"
        elif(month=="September"):
                startdate=currentYear+"-09-01"
                enddate=currentYear+"-09-31"
        elif(month=="October"):
                startdate=currentYear+"-10-01"
                enddate=currentYear+"-10-31"
        elif(month=="November"):
                startdate=currentYear+"-11-01"
                enddate=currentYear+"-11-30"
        elif(month=="December"):
                startdate=currentYear+"-12-01"
                enddate=currentYear+"-12-31"
        db = DBConnection()
        sql="select count(*) as counter from advertisment where ad_date between %s and %s and emp_id=%s"
        condition=(startdate,enddate,emp_id)  
        data = db.getsingle(sql,condition)
        
        
        #return HttpResponse(data)
        v=data
        return v

def saveadmission(request):
        adm_course_no = request.POST['Couno']
        adm_name = request.POST['Name']
        adm_address = request.POST['Address']
        adm_phone = request.POST['Phone']
        adm_email = request.POST['Email']
        adm_gender = request.POST['Gender']
        adm_date = request.POST['Date']
        db = DBConnection()
        qury6 = "insert into admission( adm_course_no,adm_name,adm_address,adm_phone,adm_email,adm_gender,adm_date)values(%s,%s,%s,%s,%s,%s,%s)"
        val6 = (adm_course_no,adm_name,adm_address,adm_phone,adm_email,adm_gender,adm_date)
        db.manipulate(qury6,val6)
        return redirect('admission')
def savecourse(request):
        course_name = request.POST['Curname']
        course_duration = request.POST['Duration']
        course_type = request.POST['Type']
        db = DBConnection()
        qury7 = "insert into course(course_name,course_duration,course_type)values(%s,%s,%s)"
        val7 = (course_name,course_duration,course_type)
        db.manipulate(qury7,val7)
        return redirect('course')
def teleenq(request):
        tel_name = request.POST['Name']
        tel_phone = request.POST['Phone']
        tel_date = request.POST['Date']
        tel_purpose = request.POST['Purpose']
        tel_attended = request.POST['Cname']
        db = DBConnection()
        qury6 = "insert into telephonic_enq(tel_name,tel_phone,tel_date,tel_purpose,tel_attended)values(%s,%s,%s,%s,%s)"
        val6 = (tel_name,tel_phone,tel_date,tel_purpose,tel_attended)
        db.manipulate(qury6,val6)
        return redirect('telephonic')
def deleteemp(request,empid):
        db = DBConnection()
        qrydelete = " delete from  empdetails where emp_id=%s "
        delet=[empid]
        del_list = db.manipulate(qrydelete, delet)
        return redirect('viewemployee')
def deletemarketing(request,mktid):
        db = DBConnection()
        qrydelete = " delete from  marketarea where mkt_id=%s "
        delet=[mktid]
        del_list = db.manipulate(qrydelete, delet)
        return redirect('managemarketing')
def deleteteam(request,teamid):
        db = DBConnection()
        qrydelete = " delete from  marketingteam where team_id=%s "
        delet=[teamid]
        del_list = db.manipulate(qrydelete, delet)
        return redirect('createteam')
def deletead(request,adid):
        db = DBConnection()
        qrydelete = " delete from  advertisment where ad_id=%s "
        delet=[adid]
        del_list = db.manipulate(qrydelete, delet)
        return redirect('showads')
def deleteadm(request,admid):
        db = DBConnection()
        qrydelete = " delete from  admission where adm_id=%s "
        delet=[admid]
        del_list = db.manipulate(qrydelete, delet)
        return redirect('admission')
def deletecourse(request,courseid):
        db = DBConnection()
        qrydelete = " delete from  course where course_id=%s "
        delet=[courseid]
        del_list = db.manipulate(qrydelete, delet)
        return redirect('course')
def deleteteleenq(request,telid):
        db = DBConnection()
        qrydelete = " delete from  telephonic_enq where tel_id=%s "
        delet=[telid]
        del_list = db.manipulate(qrydelete, delet)
        return redirect('telephonic')

def empshowteam(request):
        db = DBConnection()
        qry2 = "select * from empdetails e join marketingteam mt on(e.emp_id=mt.emp_id) join marketarea ma on(ma.mkt_id=mt.mkt_id) "
        team_list = db.gettable(qry2)
        return render(request, 'Administrator/emp/empshowteam.html',{'marketingteam_list':team_list})

def editemp(request,empid):
        db = DBConnection()
        qryedit = "select * from empdetails where emp_id=%s"
        edit=[empid]
        edit_list = db.gettable(qryedit, edit)
        return render(request,'Administrator/employee/editemp.html',{'emp_list':edit_list})
def updateemp(request):
        emp_name = request.POST['Name']
        emp_address = request.POST['Address']
        emp_gender = request.POST['Gender']
        emp_phone = request.POST['Phone']
        emp_joindate = request.POST['Joindate']
        emp_email = request.POST['Email'] 
        emp_password = request.POST['Password']  
        empid = request.POST['empid']
        db = DBConnection()
        qryupdate = "update  empdetails set emp_name=%s,emp_address=%s,emp_gender=%s,emp_phone=%s,emp_joindate=%s,emp_email=%s,emp_password=%s where emp_id=%s"
        update=(emp_name,emp_address,emp_gender,emp_phone,emp_joindate,emp_email,emp_password,empid)
        update_list = db.manipulate(qryupdate, update)
        return redirect('viewemployee')

def editmarketing(request,mktid):
        db = DBConnection()
        Type_list=['Online','Email','Shared']
        qryedit = "select * from marketarea where mkt_id=%s"
        edit=[mktid]
        edit_list = db.gettable(qryedit, edit)
        return render(request,'Administrator/managemarketing/editmarketing.html',{'marketarea_list':edit_list,'type_list':Type_list})
def updatemarketing(request):
        mktid = request.POST['mktid']
        mkt_title = request.POST['Title']
        mkt_type = request.POST['Type']
        db = DBConnection()
        qryupdate = "update  marketarea set mkt_title=%s,mkt_type=%s where mkt_id=%s"
        update=(mkt_title,mkt_type,mktid)
        update_list = db.manipulate(qryupdate, update)
        return redirect('managemarketing')

def editteam(request,teamid):
        db = DBConnection()
        qryteam = "select * from marketarea"
        datateam = db.gettable(qryteam)
        qry1 = "select * from empdetails where user_type='emp'"
        empdata = db.gettable(qry1)
        qryedit = "select * from empdetails e join marketingteam mt on(e.emp_id=mt.emp_id) join marketarea ma on(ma.mkt_id=mt.mkt_id) where team_id=%s"
        cond=[teamid]
        edit_list = db.gettable(qryedit,cond)
        #return HttpResponse(cond)
        return render(request,'Administrator/managemarketing/editteam.html',{'marketarea_list': datateam,'employee_list': empdata,'marketteam_list':edit_list})
def updateteam(request):
        emp_id = request.POST['Employee']
        mkt_id = request.POST['Area']
        code_no = request.POST['Code']
        teamid = request.POST['teamid']
        db = DBConnection()
        qryupdate = "update  marketingteam set emp_id=%s,mkt_id=%s,code_no=%s where team_id=%s"
        update=[emp_id,mkt_id,code_no,teamid]
        update_list = db.manipulate(qryupdate, update) 
        return redirect('createteam')
def editad(request,adid):
        db = DBConnection()
        qryarea = "select * from marketarea"
        dataarea = db.gettable(qryarea)
        qry1 = "select * from empdetails"
        empdata = db.gettable(qry1)
        qryteam = "select * from marketingteam"
        datateam = db.gettable(qryteam)
        qryedit = "select * from marketingteam mt join advertisment a on(mt.code_no=a.code_no) join marketarea ma on(ma.mkt_id=a.mkt_id)join empdetails e on(e.emp_id=a.emp_id)where ad_id=%s"
        ad = [adid]
        edit_list = db.gettable(qryedit,ad)
        #return HttpResponse(cond)
        return render(request,'Administrator/managemarketing/editad.html',{'code_list':datateam,'marketarea_list': dataarea,'employee_list': empdata,'ad_list':edit_list})
def updatead(request):
        ad_date = request.POST['Date']
        emp_id = request.POST['Employee']
        mkt_id = request.POST['Area']
        code_no = request.POST['Code']
        ip_address = request.POST['IP']
        adid = request.POST['adid']
        db = DBConnection()
        qryupdate = "update  advertisment set ad_date=%s,emp_id=%s,mkt_id=%s,code_no=%s,ip_address=%s where ad_id=%s"
        update=[ad_date,emp_id,mkt_id,code_no,ip_address,adid]
        update_list = db.manipulate(qryupdate, update)
        return redirect('showads')
@cache_control(no_cache=True, must_revalidate=True)
def logout(request):
    cache.clear()
    return redirect("../administrator/adminlogin")
def csrf_failure(request, reason=""):
        ctx = {'reason':reason}
        return render_to_response("Administrator/employee/.html", ctx)
