from django.shortcuts import render
from kudumbasreeapp.models import *
from django.http import HttpResponseRedirect
import datetime
from django.views.decorators.cache import cache_control 

def function(request):
		return render(request,'index.html')



def login_pg(request):
	if request.method=='POST':
		Username=request.POST['Username']
		Password=request.POST['Password']
		a=login.objects.all().filter(Username=Username,Password=Password)
		if a:
			for x in a:
				request.session['loginid']=x.id
				a=x.type1
				print(a)
				if a=='admin':
					return render(request,'admin/adminhome.html')
				if a=='secretary':
					return render(request,'sechome.html')
				if a=='president':
					return render(request,'president/prehome.html')
		return render(request,'login.html')
	return render(request,'login.html')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def addmem(request):
	if request.method=='POST':
		name=request.POST['name']
		phone=request.POST['phone']
		email=request.POST['email']
		address=request.POST['address']
		remarks=request.POST['remarks']
		if member.objects.filter(name=name,phone=phone,email=email,address=address):
			return HttpResponseRedirect('/addmem/')

		else:
			a=member(name=name,phone=phone,email=email,address=address,remarks=remarks)
			a.save()
			return HttpResponseRedirect('/addmem/')

	return render(request,'addmember.html')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def member_view(request):
	a=member.objects.all()
	return render(request,'member_list.html',{'a':a})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def removemember(request):
	if request.method=='GET':
		idd=request.GET['id']
		member.objects.filter(id=idd).delete()
		return HttpResponseRedirect('/member_view/')
	return HttpResponseRedirect('/member_view/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def attendance(request):
	if request.method=='POST':
		name=request.POST['name']
		a=member.objects.get(id=name)
		x = datetime.datetime.now()
		cd=(x.strftime("%x"))
		ct=(x.strftime("%X"))
		print(cd)
		print(ct)
		if attendance_tb.objects.filter(name=a,current_date=cd):
				return HttpResponseRedirect('/attendance/')

		else:
			b=attendance_tb(name=a,current_time=ct,current_date=cd)
			b.save()
		return HttpResponseRedirect('/attendance/')
	a=member.objects.all()
	return render(request,'attentance.html',{'a':a})
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def loanapplication(request):
	if request.method=='POST':
		loaner=request.POST['loaner']
		borrower=request.POST['borrower']
		a=member.objects.get(id=borrower)
		amount=request.POST['amount']
		remarks=request.POST['remarks']
		x = datetime.datetime.now()
		cd=(x.strftime("%x"))
		if loan.objects.filter(loaner=loaner,borrower=a,amount=amount,remarks=remarks,status='pending',applidate=cd,balance=amount):
			return HttpResponseRedirect('/loanapplication/')
		else:
			a=loan(loaner=loaner,borrower=a,amount=amount,remarks=remarks,status='pending',applidate=cd,balance=amount)
			a.save()
	a=member.objects.all()
	return render(request,'add_loan.html',{'a':a})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def repayment(request):
	if request.method=='POST':
		amount=request.POST['amount']
		loanid=request.POST['id']
		a=loan.objects.get(id=loanid)

		x = datetime.datetime.now()
		cd=(x.strftime("%x"))
		b=loan_repayment(loanid=a,amount_repay=amount,date=cd)
		c=loan.objects.filter(id=loanid)
		for x in c:
			am=x.amount
			print(am)
			a=int(am)-int(amount)
			c=loan.objects.filter(id=loanid).update(balance=a)
			b.save()
	z=loan.objects.all().filter(status='approved')
	return render(request,'loanrepayment.html',{'a':z})

###########################################################################admin#############################################

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def adminaddmem(request):
	if request.method=='POST':
		name=request.POST['name']
		phone=request.POST['phone']
		email=request.POST['email']
		address=request.POST['address']
		remarks=request.POST['remarks']
		if member.objects.filter(name=name,phone=phone,email=email,address=address):
			return HttpResponseRedirect('/addmem/')

		else:
			a=member(name=name,phone=phone,email=email,address=address,remarks=remarks)
			a.save()
			return HttpResponseRedirect('/adminaddmem/')
	return render(request,'admin/adminaddmem.html')

def adminmember_view(request):
	a=member.objects.all()
	return render(request,'admin/adminmember_list.html',{'a':a})


@cache_control(no_cache=True, must_revalidate=True,no_store=True)


def adminattendance(request):
	if request.method=='POST':
		name=request.POST['name']
		a=member.objects.get(id=name)
		x = datetime.datetime.now()
		cd=(x.strftime("%x"))
		ct=(x.strftime("%X"))
		print(cd)
		print(ct)
		if attendance_tb.objects.filter(name=a,current_date=cd):
				return HttpResponseRedirect('/adminattendance/')

		else:
			b=attendance_tb(name=a,current_time=ct,current_date=cd)
			b.save()
		return HttpResponseRedirect('/adminattendance/')
	a=member.objects.all()
	return render(request,'admin/adminattentance.html',{'a':a})



def adminremovemember(request):
	if request.method=='GET':
		idd=request.GET['id']
		member.objects.filter(id=idd).delete()
		return HttpResponseRedirect('/adminmember_view/')
	return HttpResponseRedirect('/adminmember_view/')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def adminattendanceview(request):
	 a=attendance_tb.objects.all()
	 return render(request,'admin/adminattview.html',{'a':a})






@cache_control(no_cache=True, must_revalidate=True,no_store=True)


def adminloanapplication(request):
	if request.method=='POST':
		loaner=request.POST['loaner']
		borrower=request.POST['borrower']
		a=member.objects.get(id=borrower)
		amount=request.POST['amount']
		remarks=request.POST['remarks']
		x = datetime.datetime.now()
		cd=(x.strftime("%x"))
		if loan.objects.filter(loaner=loaner,borrower=a,amount=amount,remarks=remarks,status='pending',applidate=cd,balance=amount):
			return HttpResponseRedirect('/adminloanapplication/')
		else:
			a=loan(loaner=loaner,borrower=a,amount=amount,remarks=remarks,status='pending',applidate=cd,balance=amount)
			a.save()
	a=member.objects.all()
	return render(request,'admin/adminadd_loan.html',{'a':a})



def adminremoveatt(request):
	if request.method=='GET':
		idd=request.GET['id']
		attendance_tb.objects.filter(id=idd).delete()
		return HttpResponseRedirect('/adminattendanceview/')
	return HttpResponseRedirect('/adminattendanceview/')



def adminloanapprove(request):
	# if request.method=='GET':
	# 	idd=request.GET['id']
	# 	loan.objects.filter(id=idd).update(status='approved')
		return HttpResponseRedirect('/adminloanview/')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def adminloanview(request):		
	a=loan.objects.all().filter(status='pending')
	return render(request,'admin/adminapproveloan.html',{'a':a})




@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def adminrepayment(request):
	if request.method=='POST':
		amount=request.POST['amount']
		loanid=request.POST['id']
		a=loan.objects.get(id=loanid)

		x = datetime.datetime.now()
		cd=(x.strftime("%x"))
		b=loan_repayment(loanid=a,amount_repay=amount,date=cd)
		c=loan.objects.filter(id=loanid)
		for x in c:
			am=x.amount
			print(am)
			a=int(am)-int(amount)
			c=loan.objects.filter(id=loanid).update(balance=a)
			b.save()
	z=loan.objects.all().filter(status='approved')
	return render(request,'admin/adminloanrepayment.html',{'a':z})


def adminrepaymentstatus(request):
	a=loan.objects.all().filter(status='approved')
	return render(request,'admin/adminloantrack.html',{'a':a})


######################################################################President##########################################3
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def preaddmem(request):
	if request.method=='POST':
		name=request.POST['name']
		phone=request.POST['phone']
		email=request.POST['email']
		address=request.POST['address']
		remarks=request.POST['remarks']
		if member.objects.filter(name=name,phone=phone,email=email,address=address,remarks=remarks):
			return HttpResponseRedirect('/preaddmem/')

		else:
			a=member(name=name,phone=phone,email=email,address=address,remarks=remarks)
			a.save()
			return HttpResponseRedirect('/preaddmem/')

	return render(request,'president/preaddmember.html')


@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def premember_view(request):
	a=member.objects.all()
	return render(request,'president/premember_list.html',{'a':a})



def preremovemember(request):
	if request.method=='GET':
		idd=request.GET['id']
		member.objects.filter(id=idd).delete()
		return HttpResponseRedirect('/premember_view/')
	return HttpResponseRedirect('/premember_view/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def preattendanceview(request):
	 a=attendance_tb.objects.all()
	 return render(request,'president/preattview.html',{'a':a})



def preremoveatt(request):
	if request.method=='GET':
		idd=request.GET['id']
		attendance_tb.objects.filter(id=idd).delete()
		return HttpResponseRedirect('/preattendanceview/')
	return HttpResponseRedirect('/preattendanceview/')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def preloanview(request):		
	a=loan.objects.all().filter(status='pending')
	return render(request,'president/preapproveloan.html',{'a':a})



def preloanapprove(request):
	if request.method=='GET':
		idd=request.GET['id']
		loan.objects.filter(id=idd).update(status='approved')
		return HttpResponseRedirect('/preloanview/')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def prerepaymentstatus(request):
	a=loan.objects.all().filter(status='approved')
	return render(request,'president/preloantrack.html',{'a':a})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)

def prerepaymentstatus(request):
	a=loan.objects.all().filter(status='approved')
	return render(request,'president/preloantrack.html',{'a':a})


from django.contrib.auth import logout
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def Logout(request):

	try:
		 del  request.session['loginid']
	except KeyError:
		pass
	return HttpResponseRedirect('/function/')
	

