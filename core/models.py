from django.db import models



# Create your models here.
class user(models.Model):
    title = models.CharField(max_length=150)
    firstname = models.CharField(max_length=150)
    description = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    blog_image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    