from django.db import models
from django.contrib.auth import get_user_model
from categories.models import Categories



class Posts(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField( upload_to='images/', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, blank=True ,null=True , on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']