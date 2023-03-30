from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    class Meta:
        ordering = ('-published',)

    class PostManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default='published')

    objects = models.Manager()
    postobjects = PostManager()

    def __str__(self):
        return self.title