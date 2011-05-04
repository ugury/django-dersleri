from django.db import models
from markdown import markdown
import datetime


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def get_category_lessons(self):
        ls = Lesson.objects.filter(category=self)
        return ls


class Lesson(models.Model):
    IS_ACTIVE = (('0','Draft'),
                 ('1','Active'))
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    content = models.TextField()
    content_html = models.TextField(editable=False, blank=True, null=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    mod_date = models.DateTimeField(default=datetime.datetime.now)
    category = models.ForeignKey('Category')
    status = models.IntegerField(choices=IS_ACTIVE)

    def save(self):
        self.content_html = markdown(self.content,['codehilite'])
        super(Lesson,self).save()
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/lesson/%s/%s" % (self.pk,self.slug)
