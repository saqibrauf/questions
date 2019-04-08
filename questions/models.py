
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from datetime import datetime


class Category(MPTTModel):
	name = models.CharField(max_length=70, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

	class MPTTMeta:
		order_insertion_by = ['name']

	class Meta:
		verbose_name_plural = 'Categories'
		ordering = ['name']

	def __str__(self):
		return self.name.title()

class Question(models.Model):
	category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'questions')
	question = models.TextField()
	slug = models.SlugField(max_length = 250, blank=True)
	date = models.DateTimeField(auto_now_add = True)
	source = models.CharField(max_length = 100, blank = True, default = '')
	source_id = models.CharField(max_length = 250, blank = True, default = '')

	class Meta:
		verbose_name_plural = 'Questions'
		ordering = ['-date']

	def __str__(self):
		return self.question.title()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.question[:150])
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('question', args=[str(self.id), str(self.slug)])

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name = 'answers')
	answer = models.TextField(blank = True, default = 'Not Answered Yet')
	date = models.DateTimeField(auto_now_add = True)

	class Meta:
		verbose_name_plural = 'Answers'
		ordering = ['-date']

	def __str__(self):
		return self.answer
