from django.db import models
from datetime import datetime
from django import forms
from django.contrib.auth.models import User


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    birthday = models.DateField(blank=True, null=True)
    avatar = models.ImageField(width_field=50, height_field=50, max_length=100)


class CompanyProfile(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User)
    name = models.CharField(max_length=10)
    cover = models.ImageField(width_field=50, height_field=50, max_length=100)


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    from_user = models.ForeignKey(User, related_name='from_user')
    to_user = models.ForeignKey(User, related_name='to_user')
    content = models.TextField()
    received = models.TextField()


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    description = models.TextField()
    seen = models.BooleanField()


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    text = models.TextField()
    date_added = models.DateTimeField(default=datetime.now())


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post)
    text = models.TextField()
    date_added = models.DateTimeField(default=datetime.now())
