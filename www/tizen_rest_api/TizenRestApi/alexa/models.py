from django.db import models

# Create your models here.

class Authentication(models.Model):
    email = models.EmailField(verbose_name='email')
    image = models.ImageField(upload_to="%Y/%m/%d",null = True)
    result = models.CharField(max_length=12,verbose_name='result',null = True)
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'tizen_mirror_auth'
        verbose_name = 'tizen_mirror_auth'
        verbose_name_plural = 'tizen_mirror_auth'
