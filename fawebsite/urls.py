"""fawebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from fasite import views, solutions, roles
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path("robots.txt",TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain")), 
    path("sitemap.xml",TemplateView.as_view(
        template_name="sitemap.xml", content_type="text/plain")), 
       
   

    
    re_path(r'^page-login/$',views.page,name='page-login'),
    re_path(r'^privacy/$',views.privacy,name='privacy'),
    #re_path(r'^blog/$', views.blog, name='blog'),
    re_path(r'^blog/$', views.post_list,name='post_list'),
    re_path(r'^blog/(?P<id>[\w\-]+)/$',views.post_detail,name='post_detail'),
    re_path(r'^about/',views.about,name='about'),

    re_path(r'^platform/$',views.platform,name='platform'),
    re_path(r'^what-is-new/$', views.what_is_new, name='what is new'),
    re_path(r'^what-is-new/details/(?P<id>[\w\-]+)/$', views.what_is_new_detail, name='what is new'),
    re_path(r'^courses/$', views.course, name='course'),
    re_path(r'^contact-us/$', views.contact_us, name='contact_us'),
    re_path(r'^courses-details/$', views.cours, name='cours'),
    re_path(r'^educationblog/$', views.educationblog, name='educationblog'),
    re_path(r'^education/$', views.education, name='education'),
    re_path(r'^natural-language-processing/$', views.natural_language_processing, name='language_processing'),
    re_path(r'^ml-ops/$', views.ml_ops, name='ml_ops'),
    re_path(r'^explainable-ai/$', views.x_ai, name='x_ai'),
    re_path(r'^ai-marketplace/$', views.ai_marketplace, name='ai_apps'),
    re_path(r'^engage-with-experts/$', views.engage_with_experts, name='engage_with_experts'),
    re_path(r'^social-ai/$', views.social_ai, name='social_ai'),
    re_path(r'^predictive-ai/$', views.predictive_analytics, name='decision_ai'),
    re_path(r'^anomaly-detection/$', views.anomaly_detection, name='anomaly_detection'),
    re_path(r'^text-analytics/$', views.text_analytics, name='text_analytics'),
    re_path(r'^ai-forecast/$', views.forecast, name='forecast'),
    re_path(r'^contact-submit/$',views.save_contact,name='save_contact'),
    re_path(r'^comment-submit/$',views.save_comment,name='save_comment'),
    


    re_path(r'^ai-solutions/$', solutions.solutions, name='solutions'),
    re_path(r'^ai-solutions/retail/$', solutions.retail, name='retail'),
    re_path(r'^ai-solutions/banking/$', solutions.banking, name='banking'),
    re_path(r'^ai-solutions/financial-market/$', solutions.financial_market, name='banking'),
    re_path(r'^ai-solutions/manufacturing/$', solutions.manufacturing, name='banking'),
    re_path(r'^ai-solutions/healthcare/$', solutions.healthcare, name='healthcare'),
    re_path(r'^ai-solutions/roles/$', roles.solution_by_role, name='roles'),
     re_path(r'^ai-solutions/telecom/$', roles.solution_by_role, name='telecom'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
