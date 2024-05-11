from django.contrib.auth.models import AbstractUser
from django.db import models
import sys
print(sys.path)

from .FacultyGPT.manager.chat_manager import ChatManager

class User(AbstractUser):
    
    pass
    
class Chat(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return f'{self.owner.username}: {self.message}'