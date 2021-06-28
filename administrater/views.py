from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from administrater.models import Administrater
from ecome.models import website_settings, website_menu, website_banner_image, website_content_image, \
    website_footer_settings


def login(request):
    if 'username' in request.session:
        return redirect(home)
    else:
        if request.method =="POST":
            username = request.POST['username']
            password = request.POST['password']
            if Administrater.objects.filter(username=username,password=password).exists():
                request.session['username'] = username
                return redirect(home)
            else:
                messages.success(request,'Incorrect Details')
                return redirect(login)
        else:
            return  render(request, 'administrater/login.html')

def home(request):
    if 'username' in request.session:
        return render(request, 'administrater/home.html')
    else:
        return  redirect(login)


def add_website_name(request):
    if request.method == "POST":
        web_name = request.POST['web_name']
        if website_settings.objects.filter(web_name=web_name).exists():
            messages.success(request, 'This Name Is Already Exists !!')
            return redirect(add_website_name)
        else:
            data = website_settings(web_name = web_name)
            data.save()
            messages.success(request, 'Website Name Added Successfully')
            return  redirect(add_website_name)
    else:
        return render(request, 'administrater/add_website_name.html')



def add_website_menu(request):
    if request.method == "POST":
        menu_name= request.POST['menu_name']
        web_id = request.POST['website_id']
        web_name_get = website_settings.objects.get(id=web_id)
        if website_menu.objects.filter(web_name=web_name_get,menu_item = menu_name).exists():
            messages.success(request, 'This Menu Is Already Exists !!')
            return redirect(add_website_menu)
        else:
            data = website_menu(web_name=web_name_get,menu_item = menu_name)
            data.save()
            messages.success(request, 'Menu Added Successfully')
            return  redirect(add_website_menu)
    else:
        data = website_settings.objects.all()
        context = {
            'web_data':data,
        }
        return render(request, 'administrater/add_website_menu.html',{'data':context})


def add_website_banner(request):
    if request.method == "POST":
        web_id = request.POST['website_id']
        web_name_get = website_settings.objects.get(id=web_id)
        ban_image1 = request.FILES['image1']
        ban_image2 = request.FILES['image2']
        ban_image3 = request.FILES['image3']
        data = website_banner_image(ban_image1=ban_image1,ban_image2=ban_image2,ban_image3=ban_image3,web_name = web_name_get)
        data.save()
        messages.success(request, 'Menu Added Successfully')
        return  redirect(add_website_banner)
    else:
        data = website_settings.objects.all()
        context = {
            'web_data':data,
        }
        return render(request, 'administrater/add_website_banner.html',{'data':context})



def add_website_content(request):
    if request.method == "POST":
        web_id = request.POST['website_id']
        web_name_get = website_settings.objects.get(id=web_id)
        ban_image1 = request.FILES['image1']
        ban_image2 = request.FILES['image2']
        ban_image3 = request.FILES['image3']
        ban_image4 = request.FILES['image4']
        ban_image5 = request.FILES['image5']
        ban_image6 = request.FILES['image6']
        data = website_content_image(ban_image1=ban_image1,ban_image2=ban_image2,ban_image3=ban_image3,ban_image4=ban_image4,ban_image5=ban_image5,ban_image6=ban_image6,web_name = web_name_get)
        data.save()
        messages.success(request, 'Content Added Successfully')
        return  redirect(add_website_content)
    else:
        data = website_settings.objects.all()
        context = {
            'web_data':data,
        }
        return render(request, 'administrater/add_website_content.html',{'data':context})


def add_website_footer(request):
    if request.method == "POST":
        web_id = request.POST['website_id']
        web_name_get = website_settings.objects.get(id=web_id)
        contact_number = request.POST['contact_number']
        email_id = request.POST['email_id']
        address = request.POST['address']
        if website_footer_settings.objects.filter(web_name=web_name_get,contact_number=contact_number,email_id=email_id,address=address).exists():
            messages.success(request, 'Footer Already Exists !!')
            return redirect(add_website_footer)
        else:
            data = website_footer_settings(web_name=web_name_get,contact_number=contact_number,email_id=email_id,address=address)
            data.save()
            messages.success(request, 'Footer Added Successfully')
            return  redirect(add_website_footer)
    else:
        data = website_settings.objects.all()
        context = {
            'web_data':data,
        }
        return render(request, 'administrater/add_website_footer.html',{'data':context})

