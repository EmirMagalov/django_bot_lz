from django.db import models

# Create your models here.

class Posts(models.Model):
    user_id=models.BigIntegerField(blank=True,null=True)
    message_id=models.BigIntegerField(blank=True,null=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'