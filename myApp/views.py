from django.shortcuts import render,redirect
from . custom_form import RegisterDp
from django.contrib import messages
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponse

from . import predict
import glob

def process(request):
    if(request.method=="POST"):
        pr_form= RegisterDp(request.POST,request.FILES)
        if  pr_form.is_valid():
            x = Profile()
            x.dp = request.FILES['dp']
            if x.dp==None:
                x.dp=x.dp.default;
            x.save()

            #################''
            image_folder_path = "./data" ############
            image_paths = glob.glob("C:/Users/VIDUSHI/Desktop/python_frameworks/django assign/capstone/myApp/data/Untitled.png")
            print(image_paths) ###########

            results = []

            for image_path in image_paths:
                print(image_path)
                impred = predict.predict(image_path)
                print(impred)
                results.append(impred)

            with open('predictions.txt', 'w') as fout:
                for res in results:
                    fout.write(str(res))

################
            messages.success(request, f' Hi, Photo is successfully uploaded' )
            return redirect("process")
    else:
         pr_form= RegisterDp()
    return render(request,"myApp/main_page.html",{"dp":pr_form})
