from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from .resources import POST_TYPE


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        self.author_rating = 0
        for comm in Comment.objects.filter(user=self.user):
            self.author_rating += comm.comm_rating
        for post in Post.objects.filter(author=Author.objects.get(user=self.user)):
            self.author_rating += post.post_rating * 3
            for comm_to_post in Comment.objects.filter(post=post):
                self.author_rating += comm_to_post.comm_rating
        self.save()

    def __str__(self):
        return f'{self.user.username}'

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories')

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=2, choices=POST_TYPE)
    post_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    post_content = models.TextField()
    post_rating = models.IntegerField(default=0)

    category = models.ManyToManyField(Category, through="PostCategory")

    @property
    def rating(self):
        return self.post_rating

    @rating.setter
    def rating(self, value):
        if value >= 0 and isinstance(value, int):
            self.post_rating = value
        else:
            self.post_rating = 0
        self.save()

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return f'{self.post_content[0:124]}...'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title} | {self.category.category_name}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comm_content = models.TextField(max_length=1000)
    comm_created = models.DateTimeField(auto_now_add=True)
    comm_rating = models.IntegerField(default=0)

    @property
    def rating(self):
        return self.comm_rating

    @rating.setter
    def rating(self, value):
        if value >= 0 and isinstance(value, int):
            self.comm_rating = value
        else:
            self.comm_rating = 0
        self.save()

    def like(self):
        self.comm_rating += 1
        self.save()

    def dislike(self):
        self.comm_rating -= 1
        self.save()
