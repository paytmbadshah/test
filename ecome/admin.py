from django.contrib import admin

# Register your models here.
from ecome.models import website_settings, website_banner_image, website_menu, website_footer_settings, website_content_image

admin.site.register(website_settings)
admin.site.register(website_menu)
admin.site.register(website_banner_image)
admin.site.register(website_content_image)
admin.site.register(website_footer_settings)


