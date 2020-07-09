from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Project(models.Model):
    p_id = models.AutoField(primary_key=True)
    title = models.TextField(null=True, default="")
    github_url = models.URLField(null=True, blank=True, default="")
    desc = models.TextField(null=True, default="")
    language = models.CharField(null=True, max_length=150, default="")
    framework = models.CharField(max_length=250, default="")
    client = models.CharField(max_length=250, default="")
    date = models.CharField(max_length=100, default="")
    keyword = models.CharField(null=True, max_length=350, default="")
    subtitle = models.CharField(max_length=300, default="")
    web_url = models.URLField(null=True, blank=True, default="")
    image_url = models.ImageField(null=True, blank=True, default="")

    def __str__(self):
        return self.title


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=150, default="")
    message = models.TextField(default="")

    def __str__(self):
        return self.name


class Register(models.Model):
    msg_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=70, default="")

    def __int__(self):
        return self.msg_id


class Blogs(models.Model):
    p_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=True, default="")
    subtitle = models.TextField(null=True, blank=True, default="")
    specialmsg = models.TextField(null=True, blank=True, default="")
    referral_url = models.URLField(null=True, blank=True, default="")
    desc = models.TextField(null=True, default="")
    category = models.CharField(null=True, max_length=150, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True)
    keyword = models.CharField(null=True, max_length=350, default="")

    # image1 = models.ImageField(upload_to='media/',null=True, blank=True, default="")

    def __str__(self):
        return self.title + "by " + self.user.username


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:5] + "..." + "by " + self.user.username
