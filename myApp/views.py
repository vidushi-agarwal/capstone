from django.shortcuts import render,redirect
from . custom_form import RegisterDp
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponse

from . import predict
from . import api
import glob

def result(request):
    return render(request,"myApp/result.html",{})

def process(request):
    if(request.method=="POST"):
        pr_form= RegisterDp(request.POST,request.FILES)
        if  pr_form.is_valid():
            x = Profile()
            x.Image = request.FILES['Image']
            if x.Image==None:
                x.Image=x.Image.default;
            x.save()
            print(x.Image)
            static_path = "C:/Users/VIDUSHI/Desktop/python_frameworks/django assign/capstone/myApp/static/myApp/images/"
            #################
            image_paths = glob.glob("C:/Users/VIDUSHI/Desktop/python_frameworks/django assign/capstone/media/"+str(x.Image))
            results = []
            for image_path in image_paths:
                impred=api.func(image_path)
                # impred = predict.predict(image_path)
                # print(impred.get("len"))
            ###############
            from PIL import Image
            import requests
            im = Image.open("C:/Users/VIDUSHI/Desktop/python_frameworks/django assign/capstone/media/"+str(x.Image))
            im.save(static_path +"b.png")
            messages.success(request, f' Woah, Photo is successfully processed' )
            return render(request,"myApp/new_result.html",{"Image":x.Image,"result":impred.get("result"),"ans":impred.get("latex1")})
            # return render(request,"myApp/result.html",{"Image":x.Image,"image_name":impred.get("image_name"),"len":impred.get("len"),"eqn":impred.get("eqn"),"result":impred.get("result"),"ans":impred.get("ans")})

    else:
         pr_form= RegisterDp()
    return render(request,"myApp/main_page.html",{"Image":pr_form})
