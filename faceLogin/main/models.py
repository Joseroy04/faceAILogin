from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
# Create your models here.
class student1(models.Model):
    name = models.CharField(_("name "),blank=False,max_length=30,validators=[
            MinLengthValidator(3, 'the field must contain at least 3 characters')
            ])
    studentid = models.IntegerField(_("student id"),blank=False)
    email= models.EmailField(_("email address"), max_length=254,blank=False)
    password = models.CharField(_('password'),blank=False,max_length=15,validators=[
            MinLengthValidator(8, 'the field must contain at least 8 characters')
            ])
    images= models.ImageField(_("upload clear picture"), upload_to="images/studets", height_field=None, width_field=None, max_length=None)  
    class Meta:
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def __str__(self):
        return self.name


