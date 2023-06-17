from django.db import models
from django.urls import reverse
from django.utils import timezone
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _
from datetime import datetime

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField
from cloudinary.models import CloudinaryField

from custom.models import User
from student.models import Student
from staff.models import Staff


class Category(MPTTModel):
    """
    Publication Category table
    """
    
    CATEGORY_SELECT = (
        ("computer-engineering", "computer-engineering"),
        ("mining", "mining"),
        ("mechanical-engineering", "mechanical-engineering"),
        ("bioTechnology", "biotechnology"),
    )

    topic_name = models.CharField(max_length=250, choices=CATEGORY_SELECT)
    slug = AutoSlugField(populate_from = 'topic_name', unique=True, primary_key=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    
    class MPTTMeta:
        order_insertion_by = ["topic_name"]
        
    def get_absolute_url(self):
        return reverse("publication:category_list", args=[self.slug])
    
   
    def __str__(self):
        return self.topic_name

    class Meta:
        verbose_name_plural = _('categories')
        ordering = ['topic_name']

    
    
class Publication(models.Model):
    """
    Publication table
    """

    STATUS_CHOICES = (
        ('in_progress', 'In Progress'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )


    category = models.ForeignKey(Category, on_delete = models.RESTRICT)
    publication_name = models.CharField(max_length=255, null=False )
    slug = AutoSlugField(populate_from = 'publication_name', unique=True, primary_key=True)
    abstract = models.TextField()
    published_file = models.FileField(upload_to='publication/files')
    pages = models.IntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=255, null=False)
    published_at = models.DateField(auto_now = True)
    uploaded_by = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #research_duration = models.CharField(max_length=100)
    authors = models.CharField(max_length=255 , null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    
    class Meta:
        ordering = ("-published_at",)
        verbose_name = _("Publication")
        verbose_name_plural = _("Publications")
     
   

    def get_absolute_url(self):
        return reverse("publication:publication_detail", args=[self.slug])

    def __str__(self):
        return self.publication_name
    
