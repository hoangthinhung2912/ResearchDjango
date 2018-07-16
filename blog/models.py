from django.utils.encoding import smart_text
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save

def validate_author_email(value):
    if "@" in value:
        return value
    else:
        raise ValidationError("Not a valid value")

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('Publish', 'Publish'),
    ('private', 'Private')
)

class PostModel(models.Model):
    id              = models.BigAutoField(primary_key=True)
    active          = models.BooleanField(default=True)
    title           = models.CharField(max_length=240, verbose_name='Post title', unique=True, error_messages={"unique":"This title is not unique. Please try again"})
    slug            = models.SlugField(null=True, blank=True)
    content         = models.TextField(null=True, blank=True)
    publish         = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count      = models.IntegerField(default=0)
    publish_date    = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    author_email    = models.CharField(max_length=240, null=True, blank=True, validators=[validate_author_email])

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(PostModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return smart_text(self.title)
    def __str__(self):
        return smart_text(self.title)


def blog_post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    print("Before save")
    if not instance.slug and instance.title:
        instance.slug = slugify(instance.title)


pre_save.connect(blog_post_model_pre_save_receiver, sender=PostModel)


def blog_post_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    print("after save")
    print(created)
    if created:
        if not instance.slug and instance.title:
            instance.slug = slugify(instance.title)


post_save.connect(blog_post_model_post_save_receiver, sender=PostModel)

