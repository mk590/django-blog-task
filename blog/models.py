from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=50)
    
    
class Tags(models.Model):
    category=models.CharField(max_length=100)

class Blog(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    content=models.CharField(max_length=1000)
    Tags=models.ManyToManyField(Tags)
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    Img= models.ImageField(null=True ,blank=True, upload_to="images/")
    
    class Meta:
        # orderning=['date_created']
        # take care of the spelling mistakes 
        ordering=['date_created']