from django.db import models
from django.contrib.auth import get_user_model
from posts.models import Posts

class Comments(models.Model):
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['id']
