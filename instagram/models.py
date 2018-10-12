from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):    
    bio = models.CharField(max_length = 100)
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, default=1)
    

    def save_profile(self):
        self.save()

    @classmethod
    def display_profile(cls):
        profiles=cls.objects.get(pk=1)
        return profiles

    def delete_profile(self):
        return self.delete()

    @classmethod
    def find_username(cls, search_term):
        profiles=cls.objects.filter(user__username__icontains=search_term)
        return profiles 

    def __str__(self):
        return self.user.username


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_caption = HTMLField()
    profile = models.ForeignKey(Profile, related_name="user_profile")
    posted = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.image_caption

    def save_photo(self):
        self.save()

    def delete_photot(self):
        self.delete()

    @classmethod
    def display_images(cls):
        images=cls.objects.all()
        return images
    
    @classmethod
    def filter_imagebyprofile(cls):
        cls.objects.all().filter() 