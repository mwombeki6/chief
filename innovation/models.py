from django.db import models
from django.urls import reverse
from django.utils import timezone
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from cloudinary.models import CloudinaryField

from custom.models import User
from student.models import Student
from staff.models import Staff


class Category(MPTTModel):
    """
    Innovation Category table
    """
    
    CATEGORY_SELECT = (
        ("computer-engineering", "computer-engineering"),
        ("mining", "mining"),
        ("mechanical-engineering", "mechanical-engineering"),
        ("bioTechnology", "biotechnology"),
    )

    topic_name = models.CharField(max_length=250, choices=CATEGORY_SELECT)
    slug = AutoSlugField(populate_from = 'topic_name', unique=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    
    class MPTTMeta:
        order_insertion_by = ["topic_name"]
        
    def get_absolute_url(self):
        return reverse("innovation:category_list", args=[self.slug])
    
   
    def __str__(self):
        return self.topic_name

    class Meta:
        verbose_name_plural = _('categories')
        ordering = ['topic_name']

    
    
class Innovation(models.Model):
    """
    Innovation table
    """

    category = models.ForeignKey(Category, on_delete = models.RESTRICT)
    innovation_name = models.CharField(max_length=255, null=False )
    slug = AutoSlugField(populate_from = 'innovation_name', unique=True, primary_key=True)
    abstract = models.TextField()
    innovation_file = models.FileField(upload_to='innovation/files')
    uploaded_at = models.DateTimeField(default=timezone.now)
    uploaded_by = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
   
    
    class Meta:
        ordering = ("-uploaded_at",)
        verbose_name = _("Innovation")
        verbose_name_plural = _("Innovations")
     
   

    def get_absolute_url(self):
        return reverse("innovation:innovation_detail", args=[self.slug])

    def __str__(self):
        return self.innovation_name
    

    
class Media(models.Model):
    """
    Innovation Media table
    """    

    innovation = models.ForeignKey('Innovation', on_delete=models.CASCADE)
    images = CloudinaryField()
    alt_text = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField( default=timezone.now, editable=False)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Medias")
