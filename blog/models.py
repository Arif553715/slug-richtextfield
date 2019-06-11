from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class BlogCategory(models.Model):
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=255, blank=False)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    description = RichTextField()
    post_date = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    objects = EntryQuerySet.as_manager()
    status = models.IntegerField(choices=STATUS, default=1)
    slug = models.SlugField(help_text="write your title use(hypen-), don't use space. Ex: Bangladesh-is-a")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ['-post_date']