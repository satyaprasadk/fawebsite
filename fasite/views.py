from django.shortcuts import render  
from django.http import HttpResponseRedirect , HttpResponse
from fasite.models import Post, Comment, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import  render, get_object_or_404
from taggit.models import Tag
from django.http import  JsonResponse
from django.template.context_processors import csrf

# Create your views here.


def privacy(request):
    values={}
    return render(request,'site/privacy.html',values)

##------ Homepage
def homepage(request):
    values={}
    
    return render(request,'site/index-classic.html', values)

def kk(request):
    return render(request,'site/sitemap.xml')  

def book_demo(request):
    values = {}
    return render(request,'site/book-demo.html',values)    

def about(request):
    values = {}
    return render(request,'site/about.html',values)

def blog(request):
    values = {}
    return render(request,'blog.html',values)


def page(request):
    values = {}
    return render(request, 'site/page-login.html', values)    

def collaboration_data_scientist(request):
    values = {}
    return render(request, 'site/collb-data-science.html', values)

def collaboration_it_dev(request):
    values = {}
    return render(request, 'site/collb-data-science.html', values)

def collaboration_executive(request):
    values = {}
    return render(request, 'site/collb-data-science.html', values)

def platform(request):
    values = {}
    return render(request, 'site/platform.html', values)

def what_is_new(request):
    values={}
    return render(request,'site/what_is_new.html',values)

def what_is_new_detail(request,id):
    values={}
    return render(request,'site/what_new_detail.html',values)

def course(request):
    values = {}
    return render(request, 'site/courses.html', values)


def contact_us(request):
    values = {}
    return render(request, 'site/contact-us.html', values)

def cours(request):
    values = {}
    return render(request, 'site/courses-details.html', values)

def educationblog(request):
    values = {}
    return render(request, 'site/education-blog-post.html', values)

def education(request):
    values = {}
    return render(request, 'site/education-blog.html', values)

def natural_language_processing(request):
    values = {}
    return render(request, 'site/natural_language_processing.html', values)

def ml_ops(request):
    values = {}
    return render(request, 'site/ml_ops.html', values)

def x_ai(request):
    values = {}
    return render(request, 'site/x_ai.html', values)

def ai_marketplace(request):
    values = {}
    return render(request, 'site/ai-apps.html', values)

def engage_with_experts(request):
    values = {}
    return render(request, 'site/engage_with_experts.html', values)

def social_ai(request):
    values = {}
    return render(request, 'site/social-ai.html', values)

def predictive_analytics(request):
    values = {}
    return render(request, 'site/predictive_analytics.html', values)

def anomaly_detection(request):
    values = {}
    return render(request, 'site/anomaly_detection.html', values)

def text_analytics(request):
    values = {}
    return render(request, 'site/text_analytics.html', values)

def forecast(request):
    values = {}
    return render(request, 'site/forecast.html', values)


#def post_list(request):
    values = {}
    
    object_list = Post.objects.filter(status='published').order_by("-publish")  # it shoudl be filtered by posts that are published.
    if request.GET.get('tag_slug', None):
        tag = get_object_or_404(Tag, slug=request.GET.get('tag_slug'))
        object_list = object_list.filter(tags__in=[tag])
        values['tag'] = tag
    elif request.GET.get('title', None):
        title = request.GET.get('title', None)
        object_list = object_list.filter(title__icontains=title)
        values['search_title'] = title
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    recent_post = Post.objects.filter(status='published').order_by("-updated")[:4]

    values['posts'] = posts
    tag_count={}
    for post in posts:
        for tag in post.tags.all():
            if tag.name in tag_count:
                pass
            else:
                tag_count[tag.name.lower()] = tag
    values["tag_count"] = tag_count
    values['all_posts'] = Post.objects.filter(status='published')
    values['page'] = page

    values['recent_post'] = recent_post
    return render(request, 'site/blog.html', values)


def post_list(request):
    values = {}
    object_list = Post.objects.filter(status='published').order_by("-publish")  # it shoudl be filtered by posts that are published.
    if request.GET.get('tag_slug', None):
        tag = get_object_or_404(Tag, slug=request.GET.get('tag_slug'))
        object_list = object_list.filter(tags__in=[tag])
        values['tag'] = tag
    elif request.GET.get('title', None):
        title = request.GET.get('title', None)
        object_list = object_list.filter(title__icontains=title)
        values['search_title'] = title
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    recent_post = Post.objects.filter(status='published').order_by("-updated")[:4]

    values['posts'] = posts
    tag_count={}
    for post in posts:
        for tag in post.tags.all():
            if tag.name in tag_count:
                pass
            else:
                tag_count[tag.name.lower()] = tag
    values["tag_count"] = tag_count
    values['all_posts'] = Post.objects.filter(status='published')
    values['page'] = page

    values['recent_post'] = recent_post
    return render(request, 'site/blog.html', values)



def post_detail(request, id=""):
    values = {}
    post_id = id
    if 1==1: # TODO try catch blog
        post = Post.objects.get(slug=post_id)
        recent_post = Post.objects.order_by("-updated")[:4]
        values["paragraphs"] = [x for x in post.body.split("\n")]
        values["paragraphs2"] = [x for x in post.body2.split("\n")]
        values['post'] = post
        #summ_words = summarize(post.body, word_count=50)
        #values["summary"] = summ_words
        values['recent_post'] = recent_post
        values['all_posts'] = posts = Post.objects.filter(status='published')
        values["posts"] = Post.objects.filter(status='published').order_by("-publish")[:3]
        values["comments"] = Comment.objects.filter(post = post)
        tag_count = {}
        for post in posts:
            for tag in post.tags.all():
                if tag.name in tag_count:
                    pass
                else:
                    tag_count[tag.name.lower()] = tag
        values["tag_count"] = tag_count
        return render(request, 'site/blog-details.html', values)
    else:
        return render(request, '404.html')


def save_comment(request):
    values = {}
    if request.method == "POST":
        c = {}
        c.update(csrf(request))
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        website = request.POST.get('website', None)
        message = request.POST.get('message', None)
        if name and email and website and message:
            instance = Comment(name=name, email=email, website=website, message=message)
            instance.save()
            values["message"] = "Thank you for posting, your message is posted."
            return JsonResponse(values)
    else:
        pass
    
def save_contact(request):
    values={}
    if request.method == "POST":
        c = {}
        c.update(csrf(request))
        name = request.POST.get('name',None)
        email = request.POST.get('email', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)
        if name and email and subject and message:
            instance = Contact(name=name,email=email,subject=subject,message=message)
            instance.save()
            values["message"] = "Thank you for contacting us, we will soon reach out to you."
            return JsonResponse(values)
    else:
        pass


