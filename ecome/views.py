from django.shortcuts import render

# Create your views here.
from ecome.models import website_settings, website_menu, website_banner_image, website_content_image, \
    website_footer_settings


def index(request):
    web_data = website_settings.objects.all()
    web_nam = web_data[0].web_name
    menu = website_menu.objects.filter(web_name=web_data[0].id)
    banner = website_banner_image.objects.filter(web_name=web_data[0].id)
    body_content = website_content_image.objects.filter(web_name=web_data[0].id)
    footer = website_footer_settings.objects.filter(web_name=web_data[0].id)

    context = {
        'web_name':web_nam,
        'menu':menu,
        'banner':banner,
        'body_content':body_content,
        'footer':footer,
    }
    return render(request,'index.html',{'data':context})

