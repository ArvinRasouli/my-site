from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
#admin : username = arvin , pass = arvin27021379

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField() 

    def full_name (self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()



class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name="comments")