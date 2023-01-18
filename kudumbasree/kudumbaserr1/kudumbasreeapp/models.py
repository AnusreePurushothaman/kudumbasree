from django.db import models

class login(models.Model):
	Username=models.CharField(max_length=100,default='')
	Password=models.CharField(max_length=100,default='')
	type1=models.CharField(max_length=100,default='')

class member(models.Model):
	name=models.CharField(max_length=100,default='')
	phone=models.CharField(max_length=100,default='')
	email=models.CharField(max_length=100,default='')
	address=models.CharField(max_length=100,default='')
	remarks=models.CharField(max_length=100,default='')



class attendance_tb(models.Model):
	name=models.ForeignKey(member,on_delete=models.CASCADE,default='')
	current_time=models.CharField(max_length=100,default='')
	current_date=models.CharField(max_length=100,default='')


class loan(models.Model):
    loaner=models.CharField(max_length=50,default='')
    borrower=models.ForeignKey(member,on_delete=models.CASCADE,default='')
    amount=models.IntegerField()
    remarks=models.CharField(max_length=50,default='')
    applidate=models.CharField(max_length=100,default='')
    status=models.CharField(max_length=100,default='')
    balance=models.CharField(max_length=100,default='')

class loan_repayment(models.Model):
    loanid=models.ForeignKey(loan,on_delete=models.CASCADE,default='')
    amount_repay=models.IntegerField()
    date=models.CharField(max_length=100,default='')
