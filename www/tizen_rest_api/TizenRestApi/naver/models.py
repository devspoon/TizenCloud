from django.db import models

# Create your models here.

class AIAnalysis(models.Model):
    email = models.EmailField(verbose_name='email')
    image = models.ImageField(upload_to="%Y/%m/%d",null = True)
    age = models.CharField(max_length=6,verbose_name='age',null = True)
    resultage = models.CharField(max_length=6,verbose_name='resultage',null = True)
    compareyesterday = models.CharField(max_length=6,verbose_name='compareyesterday',null = True)
    skincolor = models.CharField(max_length=12,verbose_name='skincolor',null = True)
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'tizen_mirror_aianalysis'
        verbose_name = 'tizen_mirror_aianalysis'
        verbose_name_plural = 'tizen_mirror_aianalysis'
