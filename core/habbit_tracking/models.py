from operator import mod
from django.db import models
from datetime import datetime    

# Create your models here.
class pushup_logs(models.Model):
    exercize_date = models.DateField(default=datetime.now)
    pushup_count = models.IntegerField()

    def __str__(self):  
        return str(self.exercize_date) + ' (Count: ' + str(self.pushup_count) + ')'
    
    class Meta:
        verbose_name_plural = "Pushup Logs"
        verbose_name = "Pushup Log"