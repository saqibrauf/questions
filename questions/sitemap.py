from django.contrib.sitemaps import Sitemap
from .models import Category, Question


class CategorySitemap(Sitemap):
    def items(self):
        return Category.objects.all()
    changefreq = "daily"
    priority = 0.5


class QuestionSitemap(Sitemap):
    def items(self):
        return Question.objects.all()
    changefreq = "daily"
    priority = 0.5