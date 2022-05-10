from django.urls import path
from . import views 
from django.conf.urls.static import static


urlpatterns = [
  path(r'^adminlogin', views.adminlogin, name='adminlogin'),
  path(r'^adminlog', views.adminlog, name="adminlog"),
  path(r'^changepwdemp', views.changepwdemp, name="changepwdemp"),
  path(r'^changepasswordemp', views.changepasswordemp, name="changepasswordemp"),
   path(r'^changepwd', views.changepwd, name="changepwd"),
  path(r'^changepassword', views.changepassword, name="changepassword"),
   path("logout", views.logout, name="logout"),
  
  
  path('empindex', views.empindex, name='empindex'),
  path('empviewemploye', views.empviewemploye, name='empviewemploye'),
  path('empmonthlyads', views.empmonthlyads, name='empmonthlyads'),
  path('empemployeeads', views.empemployeeads, name='empemployeeads'),
  path('empprogressads', views.empprogressads, name='empprogressads'),
 
  path('empshowteam', views.empshowteam, name='empshowteam'),
  

  path('adminindex', views.adminindex, name='adminindex'),
  path('addemployee', views.addemployee, name='addemployee'),
  path('viewemployee', views.viewemployee, name='viewemployee'),
  path('monthlyads', views.monthlyads, name='monthlyads'),
  path('employeeads', views.employeeads, name='employeeads'),
  path('progressads', views.progressads, name='progressads'),
  path('managemarketing', views.managemarketing, name='managemarketing'),
  
   path('monthlyadhit', views.monthlyadhit, name='monthlyadhit'),
   path('gethit', views.gethit, name='gethit'),
  
   path('monthlyreach', views.monthlyreach, name='monthlyreach'),
   path('getreach', views.getreach, name='getreach'),
   
 path('employeereach', views.employeereach, name='employeereach'),
 path('getemployemonthlyhit', views.getemployemonthlyhit, name='getemployemonthlyhit'),
 
  path('createteam', views.createteam, name='createteam'),
  path('showads', views.showads, name='showads'),
  path('admission/', views.admission, name='admission'),
  path('course/', views.course, name='course'),
  path('telephonic', views.telephonic, name='telephonic'),

  path('saveemp', views.saveemp, name='saveemp'),
  path('savearea', views.savearea, name='savearea'),
  path('saveteam', views.saveteam, name='saveteam'),
  path('savead', views.savead, name='savead'), 
   path('searchads', views.searchads, name='searchads'), 
 
  path('saveadmission', views.saveadmission, name='saveadmission'),
  path('savecourse', views.savecourse, name='savecourse'),
  path('teleenq', views.teleenq, name='teleenq'),
  
  path(r'^deleteemp/(?P<empid>\d+)/', views.deleteemp, name="deleteemp"),
  path(r'^deletemarketing/(?P<mktid>\d+)/', views.deletemarketing, name="deletemarketing"),
  path(r'^deleteteam/(?P<teamid>\d+)/', views.deleteteam, name="deleteteam"),
  path(r'^deletead/(?P<adid>\d+)/', views.deletead, name="deletead"),
  path(r'^deleteadm/(?P<admid>\d+)/', views.deleteadm, name="deleteadm"),
  path(r'^deletecourse/(?P<courseid>\d+)/', views.deletecourse, name="deletecourse"),
  path(r'^deleteteleenq/(?P<telid>\d+)/', views.deleteteleenq, name="deleteteleenq"),
  
  path(r'^editemp/(?P<empid>\d+)/', views.editemp, name="editemp"),
  path(r'^updateemp', views.updateemp, name="updateemp"),
  path(r'^editmarketing/(?P<mktid>\d+)/', views.editmarketing, name="editmarketing"),
  path(r'^updatemarketing', views.updatemarketing, name="updatemarketing"),
  path(r'^editteam/(?P<teamid>\d+)/', views.editteam, name="editteam"),
  path(r'^updateteam', views.updateteam, name="updateteam"),
  path(r'^editad/(?P<adid>\d+)/', views.editad, name="editad"),
  path(r'^updatead', views.updatead, name="updatead"),

  path('csrf_failure', views.csrf_failure, name='csrf_failure'),

]
