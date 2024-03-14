from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.models import User
# for messages
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import *
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

import pdfplumber
import openai
import json
openai.api_key="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx"
# Create your views here.

def register_user(request):
    if  request.method=='GET':
        return render(request,'register.html')
    else:
        
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        em=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        print(uname)
        print(pass1)
        print(pass2)
        print(em)
        print(fname)
        print(lname)

        if pass1==pass2:
            try:
                user=User.objects.create_user(username=uname,password=pass1,email=em,first_name=fname,last_name=lname)
                user.save()
                u=authenticate(request,username=uname,password=pass1)
                login(request,u)
                messages.success(request,'registeration successfull')
                return redirect('home')
            except:
                messages.error(request,'username already taken !! try new one')
                return render(request,'register.html',{})
            
        else:
            messages.error(request,'passwords didnt matched')
            return render(request,'register.html',{})

def login_user(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        # to authenticate the user
        user=authenticate(request,username=username,password=password)
        # if the user is authenticated it wont refer none
        if user is not None:
            login(request,user)
            messages.success(request,'you have successfully logged in')
            return redirect('home')
        else:
            messages.error(request,'YOUR PASSWORD AND USERNAME DIDNT MATCHED   ENTER AGAIN')
            return render(request,'login.html',context={})
        

def logout_user(request):
    logout(request)
    # messages.warning(request,'you have logged out')
    return redirect('home')

@login_required(login_url='login')
def home(request):

    # if request.method=='POST':
    #     user=request.user
    #     report=request.FILES['report']
    #     report=Report(user=user,file=report)
    #     report.save()
    #     print(report.file.url)
    #     pdf_url="."+report.file.url
    #     pdf=pdfplumber.open(pdf_url)
    #     text=''
    #     for i in range(len(pdf.pages)):
    #         t=pdf.pages[i].extract_text()
    #         text=text+t
        
    #     prompt=f"""
    #     {text}
    #     extract only values and not units of hemoglobin ,rbc count,mcv,mch,bilirubin direct,bilirubin indirect
    #     bilirubin total,protien,urea,uric acid,pottasium,chloride,sodium ,calcium and doctor name. give me json format with all keys in lowercase. if not available return -1
    #         """
    #     output = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo", 
    #     messages=[{"role": "user", "content":prompt}]
    #     )
    #     data_dict=json.loads(output['choices'][0]['message']['content'])
    #     print(data_dict)
    #     pdf.close()
    #     report_detail=ReportDetail(
    #     user=user,
    #     report=report,
    #     hemoglobin=str(data_dict['hemoglobin']),
    #     rbc=str(data_dict['rbc count']),
    #     mch=str(data_dict['mch']),
    #     mcv=str(data_dict['mcv']),
    #     bilirubin_total=str(data_dict['bilirubin total']),
    #     bilirubin_direct=str(data_dict['bilirubin direct']),
    #     bilirubin_indirect=str(data_dict['bilirubin indirect']),
    #     protien=str(data_dict['protein']),
    #     urea=str(data_dict['urea']),
    #     uric_acid=str(data_dict['uric acid']),
    #     chloride=str(data_dict['chloride']),
    #     sodium=str(data_dict['sodium']),
    #     pottasium=str(data_dict['potassium'])
    #     )
    #     report_detail.save()
    #     return redirect('dashboard')
    return render(request,'index.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')


@csrf_exempt
def give_data(request):
    if request.method=='POST':
        uname=request.POST['username']
        print(uname.strip())
        user=User.objects.get(username=uname.strip())
        report_detail=json.dumps(list(ReportDetail.objects.filter(user=user).values()))
        print(report_detail)
        df=pd.read_json(report_detail)
        hemoglobin = list(map(str, list(df['hemoglobin'].values)))
        rbc = list(map(str, list(df['rbc'].values)))
        mch = list(map(str, list(df['mch'].values)))
        mcv = list(map(str, list(df['mcv'].values)))
        bilirubin_total = list(map(str, list(df['bilirubin_total'].values)))
        bilirubin_direct = list(map(str, list(df['bilirubin_direct'].values)))
        bilirubin_indirect = list(map(str, list(df['bilirubin_indirect'].values)))
        urea = list(map(str, list(df['urea'].values)))
        protien = list(map(str, list(df['protien'].values)))
        uric_acid = list(map(str, list(df['uric_acid'].values)))
        sodium = list(map(str, list(df['sodium'].values)))
        pottasium = list(map(str, list(df['pottasium'].values)))
        chloride = list(map(str, list(df['chloride'].values)))


        date_list=[]
        for data in Report.objects.filter(user=user):
            date_list.append(str(data.date))
        print(date_list)
        
        data= {
                'hemoglogin':hemoglobin,
                'rbc':rbc,
                'mch':mch,
                'mcv':mcv,
                'bilirubin_total':bilirubin_total,
                'bilirubin_direct':bilirubin_direct,
                'bilirubin_indirect':bilirubin_indirect,
                'urea':urea,
                'uric_acid':uric_acid,
                'protien':protien,
                'sodium':sodium,
                'pottasium':pottasium,
                'chloride':chloride,
                'labels':date_list
            }
        print(data)
        return JsonResponse(
           data
            )

@login_required(login_url='login')
def latest(request):
    user=request.user
    detail=ReportDetail.objects.latest(user=user)
    return render(request,'latest.html',{'detail':detail})

@login_required(login_url='login')
def reports(request):
    user=request.user
    reports=Report.objects.filter(user=user)
    return render(request,'report.html',{'reports':reports})

@login_required(login_url='login')
def upload(request):
    if request.method=='POST':
        user=request.user
        report=request.FILES['report']
        report=Report(user=user,file=report)
        report.save()
        print(report.file.url)
        pdf_url="."+report.file.url
        pdf=pdfplumber.open(pdf_url)
        text=''
        for i in range(len(pdf.pages)):
            t=pdf.pages[i].extract_text()
            text=text+t
        
        prompt=f"""
        {text}
        extract only values and not units of hemoglobin ,rbc count,mcv,mch,bilirubin direct,bilirubin indirect
        bilirubin total,protien,urea,uric acid,pottasium,chloride,sodium ,calcium and doctor name. give me json format with all keys in lowercase. if not available return -1
            """
        output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content":prompt}]
        )
        data_dict=json.loads(output['choices'][0]['message']['content'])
        print(data_dict)
        pdf.close()
        report_detail=ReportDetail(
        user=user,
        report=report,
        hemoglobin=str(data_dict['hemoglobin']),
        rbc=str(data_dict['rbc count']),
        mch=str(data_dict['mch']),
        mcv=str(data_dict['mcv']),
        bilirubin_total=str(data_dict['bilirubin total']),
        bilirubin_direct=str(data_dict['bilirubin direct']),
        bilirubin_indirect=str(data_dict['bilirubin indirect']),
        protien=str(data_dict['protein']),
        urea=str(data_dict['urea']),
        uric_acid=str(data_dict['uric acid']),
        chloride=str(data_dict['chloride']),
        sodium=str(data_dict['sodium']),
        pottasium=str(data_dict['potassium'])
        )
        report_detail.save()
        return redirect('dashboard')
    else:
        return render(request,'upload.html')

@login_required(login_url='login')
def singlereport(request,id):
    report=Report.objects.get(id=id)
    detail=ReportDetail.objects.get(report=report)
    if request.user==report.user:
        return render(request,'singlereport.html',{'details':detail})
    else:
        return redirect('home')