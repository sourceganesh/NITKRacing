from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .models import *


def landing_page(request):
    return render(request, 'landing_page.html')
    
def index(request):
    banners_list = Banner.objects.filter(page_to_display=1)
    sponsors_list = Sponsor.objects.all()
    sig_head_list = Member.objects.filter(sig_head=True)
    document_list = Document.objects.filter(subsystem_filter=5)
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {'banners_list': banners_list,
               'sponsors_list': sponsors_list,
               'sig_head_list': sig_head_list,
               'image_gallery_full': image_gallery_full,
               'image_gallery_short': image_gallery_short,
               'document_list': document_list
               }
    return render(request, 'index_v1.html', context=context)


def about(request):
    sponsors_list = Sponsor.objects.all()
    banners_list = Banner.objects.filter(page_to_display=2)
    blog_list = Blog.objects.order_by('updated_on')[:3]
    sig_head_list = Member.objects.filter(sig_head=True)
    image_gallery_full = Image.objects.all()
    full_member_list = Member.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    document_list = Pitstop.objects.all()
    if(request.method=='POST'):
        subs = Subscribers(email=request.POST['mailid'])
        message ="Greetings from NITKRacing,\n enclosed below is a link to the latest editon of pitstop\n"
        message+=Pitstop.objects.all()[0].link
        message+="\nRegards NITKRacing"
        subs.save()
        send_mail('Thank you for subscribing!',
                      message,
                      settings.EMAIL_HOST_USER,
                      [subs.email],
                      fail_silently=False)
    context = {'banners_list': banners_list,
               'blog_list': blog_list,
               'sig_head_list': sig_head_list,
               'image_gallery_full': image_gallery_full,
               'image_gallery_short': image_gallery_short,
               'members_list': full_member_list,
               'sponsors_list': sponsors_list,
               'document_list': document_list
               }
    return render(request, 'about_v1.html', context=context)


def contact(request):
    sponsors_list = Sponsor.objects.all()
    banners_list = Banner.objects.filter(page_to_display=3)
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {'banners_list': banners_list,
               'image_gallery_full': image_gallery_full,
               'sponsors_list': sponsors_list,
               'image_gallery_short': image_gallery_short
               }
    if(request.method=='POST'):
        message ="Name :"+ request.POST['usr']+"\n"+ "Email :" + request.POST['mailid']
        message += "\n" + "website :" + request.POST['website']
        message += "\n" + "Content :\n" + request.POST['msg']

        send_mail('Website Contact Form',
                      message,
                      settings.EMAIL_HOST_USER,
                      ['addhyanmalhotra@gmail.com','captain.nitkracing@gmail.com'],
                      fail_silently=False)

    return render(request, 'contact_v1.html', context=context)


def team(request):
    sponsors_list = Sponsor.objects.all()
    full_member_list = Member.objects.all()
    banners_list = Banner.objects.filter(page_to_display=4)
    sig_head_list = Member.objects.filter(sig_head=True)
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    context = {
        'sig_head_list': sig_head_list,
        'banners_list': banners_list,
        'image_gallery_full': image_gallery_full,
        'image_gallery_short': image_gallery_short,
        'full_member_list': full_member_list,
        'sponsors_list': sponsors_list
    }
    return render(request, 'team_v1.html', context=context)


def aerodynamics(request):
    sponsors_list = Sponsor.objects.all()
    full_member_list = Member.objects.filter(sig=1)
    blog_list = Blog.objects.filter(blog_filter=1)
    banners_list = Banner.objects.filter(page_to_display=5)
    document_list = Document.objects.filter(subsystem_filter=1)
    context = {'full_member_list': full_member_list,
               'banners_list': banners_list,
               'blog_list': blog_list,
               'sponsors_list': sponsors_list,
               'document_list': document_list
               }
    return render(request, 'aerodynamics_v1.html', context=context)


def vehicledynamics(request):
    sponsors_list = Sponsor.objects.all()
    full_member_list = Member.objects.filter(sig=2)
    blog_list = Blog.objects.filter(blog_filter=2)
    banners_list = Banner.objects.filter(page_to_display=6)
    document_list = Document.objects.filter(subsystem_filter=2)
    context = {'full_member_list': full_member_list,
               'banners_list': banners_list,
               'sponsors_list': sponsors_list,
               'blog_list': blog_list,
               'document_list': document_list
               }
    return render(request, 'vehicledynamics_v1.html', context=context)


def powertrain(request):
    sponsors_list = Sponsor.objects.all()
    full_member_list = Member.objects.filter(sig=3)
    blog_list = Blog.objects.filter(blog_filter=3)
    banners_list = Banner.objects.filter(page_to_display=7)
    document_list = Document.objects.filter(subsystem_filter=3)
    context = {'full_member_list': full_member_list,
               'banners_list': banners_list,
               'sponsors_list': sponsors_list,
               'blog_list': blog_list,
               'document_list': document_list
               }
    return render(request, 'powertrain_v1.html', context=context)


def electronics(request):
    sponsors_list = Sponsor.objects.all()
    full_member_list = Member.objects.filter(sig=4)
    blog_list = Blog.objects.filter(blog_filter=4)
    banners_list = Banner.objects.filter(page_to_display=8)
    document_list = Document.objects.filter(subsystem_filter=4)
    context = {'full_member_list': full_member_list,
               'banners_list': banners_list,
               'blog_list': blog_list,
               'sponsors_list': sponsors_list,
               'document_list': document_list
               }
    return render(request, 'electronics_v1.html', context=context)


def marketing(request):
    sponsors_list = Sponsor.objects.all()
    full_member_list = Member.objects.filter(sig=5)
    blog_list = Blog.objects.filter(blog_filter=5)
    banners_list = Banner.objects.filter(page_to_display=9)
    context = {'full_member_list': full_member_list,
               'banners_list': banners_list,
               'blog_list': blog_list,
               'sponsors_list': sponsors_list
               }
    return render(request, 'marketing_v1.html', context=context)


def media(request):
    sponsors_list = Sponsor.objects.all()
    full_member_list = Member.objects.filter(sig=6)
    blog_list = Blog.objects.filter(blog_filter=6)
    banners_list = Banner.objects.filter(page_to_display=10)
    context = {'full_member_list': full_member_list,
               'banners_list': banners_list,
               'blog_list': blog_list,
               'sponsors_list': sponsors_list
               }
    return render(request, 'media_v1.html', context=context)


def gallery(request):
    sponsors_list = Sponsor.objects.all()
    image_gallery_full = Image.objects.all()
    image_gallery_short = Image.objects.filter(display_on_index=True)
    banners_list = Banner.objects.filter(page_to_display=11)
    context = {'image_gallery_short': image_gallery_short,
               'image_gallery_full': image_gallery_full,
               'banners_list': banners_list,
               'sponsors_list': sponsors_list,
               }
    return render(request, 'gallery_v1.html', context=context)
