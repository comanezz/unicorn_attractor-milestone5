from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=150, default='', blank=False)
    description = models.TextField()
    slug = models.SlugField(max_length=150)
    created_date = models.DateTimeField(editable=False, default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User,
        related_name='author_feature',
        on_delete=models.CASCADE, null=True)
    upvotes = models.ManyToManyField(
        User,
        blank=True,
        related_name="feature_upvotes")
    contributions = models.IntegerField(default=0)

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In progress', 'In progress'),
        ('Done', 'Done'))
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='Pending')

    def __str__(self):
        return self.title

    # Ordered by the most recent modified date
    class Meta:
        ordering = ('-created_date',)

    def total_upvotes(self):
        """ Return total upvote """
        return self.upvotes.count()

    def get_absolute_url(self):
        """ Return a string with args. Id and slug """
        return reverse("feature_detail", args=[str(self.id), str(self.slug)])

    def save(self, *args, **kwargs):
        # This will automatically creates a slug when create or edit a feature
        # https://books.agiliq.com/projects/django-orm-cookbook/en/latest/slugfield.html
        self.slug = slugify(self.title)

        # On save, update timestamps.
        # Update the modified date when a post has been updated.
        self.modified_date = timezone.now()
        super(Feature, self).save(*args, **kwargs)


class Comment(models.Model):
    feature = models.ForeignKey(Feature, related_name="comments")
    author = models.ForeignKey(User, related_name='feature_comment_author')
    context = models.TextField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    reply = models.ForeignKey(
        'self',
        null=True,
        related_name="feature_replies",
        blank=True)

    def __str__(self):
        return '{}-{}'.format(
            str(self.feature.title),
            str(self.author.username))
