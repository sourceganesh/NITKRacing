from django.db import models


# Create your models here.
class Banner(models.Model):
    CHOICES = [(1, 'Home'), (2, 'About'), (3, 'Team'), (4, 'Contact'), (5, 'Aero'),
               (6, 'VD'), (7, 'PWR'), (8, 'ELEC'), (11, 'Gallery'), (10, 'Media'), (9, 'Marketing')]
    page_to_display = models.IntegerField(default=1, choices=CHOICES)
    bg_img = models.ImageField(upload_to='images/')
    small_text = models.CharField(max_length=50, blank=True)
    large_text = models.CharField(max_length=150)

    def __str__(self):
        return self.large_text


class Sponsor(models.Model):
    sponsor_name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    img = models.ImageField(upload_to='images/sponsors')
    sponsor_link = models.URLField(default=" ")

    def __str__(self):
        return self.sponsor_name


# 12345678
class Member(models.Model):
    CHOICES = [(1, 'AERO'), (2, 'VD'), (3, 'PWR'), (4, 'ELEC'), (6, 'MEDIA'), (5, 'MARKETING')]
    roll_number = models.CharField(max_length=8, primary_key=True)
    priority = models.IntegerField(default=5,unique=False,choices=[(0,'cap'),(1,'op'),(2,'tech head'),(3,'subsytem head'),(4,'media/marketing'),(5,'other')])
    sig = models.IntegerField(default=0, choices=CHOICES)
    writeup = models.CharField(max_length=144, blank=True)
    member_name = models.CharField(max_length=50)
    post = models.CharField(max_length=300)
    insta = models.URLField(default="")
    linkdin = models.URLField(default="")
    email = models.EmailField(blank=True)
    member_img = models.ImageField(upload_to='images/members')
    sig_head = models.BooleanField(default=False)
    class Meta:
        ordering = ['priority']
    def __str__(self):
        return self.member_name


class Image(models.Model):
    img = models.ImageField(upload_to='images/')
    alt_text = models.CharField(max_length=50, blank=True)
    display_on_index = models.BooleanField()

    def __str__(self):
        return self.alt_text


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    blog_filter = models.IntegerField(default=0, choices=[(1, 'AERO'), (2, 'VD'), (3, 'PWR'), (4, 'ELEC'), (6, 'MEDIA'),
                                                          (5, 'MARKETING')]
                                      )
    author = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Document(models.Model):
    CHOICES = [(5,'INDEX'),(1, 'AERO'), (2, 'VD'), (3, 'PWR'), (4, 'ELEC')]
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='3dModels/')
    subsystem_filter = models.IntegerField(default=0, choices=CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Pitstop(models.Model):
    link = models.URLField(default="#")
    # Google_id = models.CharField(max_length=100,default=" ",blank=True,help_text="ignore maadi!!! <br> leave blank")
    edition = models.CharField(max_length=100, default=" ")
    created_on = models.DateTimeField()
    cover = models.ImageField(upload_to='pits', blank=True)

    class Meta:
        ordering = ['-created_on']


class Subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class about_us_content(models.Model):
    youtube_link= models.URLField()
    text_next_to_video=models.TextField()
