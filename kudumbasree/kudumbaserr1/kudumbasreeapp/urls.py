from django.urls import path
from . import views
urlpatterns = [

    path('',views.function),
    path('function/',views.function),

    path('login_pg',views.login_pg),
    path('login_pg/',views.login_pg),
    path('addmem/',views.addmem),
    path('member_view/',views.member_view),
    path('removemember/',views.removemember),
    path('attendance/',views.attendance),
    path('loanapplication/',views.loanapplication),
    path('repayment/',views.repayment),
    path('Logout/',views.Logout),

################################################admin###############################

    path('adminaddmem/',views.adminaddmem),
    path('adminmember_view/',views.adminmember_view),
    path('adminattendance/',views.adminattendance),
    path('adminremovemember/',views.adminremovemember),

    path('adminattendanceview/',views.adminattendanceview),
    path('adminremoveatt/',views.adminremoveatt),
    path('adminloanapplication/',views.adminloanapplication),
    path('adminloanapprove/',views.adminloanapprove),
    path('adminloanview/',views.adminloanview),
    path('adminrepayment/',views.adminrepayment),
    path('adminrepaymentstatus/',views.adminrepaymentstatus),
    

    
##########################################################president###############################

    path('preaddmem/',views.preaddmem),
    path('premember_view/',views.premember_view),
    path('preattendanceview/',views.preattendanceview),
    path('preremoveatt/',views.preremoveatt),

    path('prerepaymentstatus/',views.prerepaymentstatus),
    path('preremovemember/',views.preremovemember),
    path('preloanview/',views.preloanview),
    path('preloanapprove/',views.preloanapprove),












]
