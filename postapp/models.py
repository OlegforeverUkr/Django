from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Topic(models.Model):
    topic_name = models.CharField(max_length=64, unique=True)
    topic_description = models.CharField(max_length=255)
    users = models.ManyToManyField(UserModel, through='UserTopicRelation')



class Article(models.Model):
    title_article = models.CharField(max_length=255, default='Insert your text')
    text_article = models.TextField(default='Insert your text')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    topics = models.ManyToManyField(Topic)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(UserModel, related_name='liked_articles', blank=True)

    def __str__(self):
        return self.title_article



class Comment(models.Model):
    created_date_comment = models.DateTimeField(auto_now_add=True)
    text_comment = models.TextField()

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_comment = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.author_comment.username} on {self.article.title_article}"



class UserTopicRelation(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    notify = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.topic.title}"
