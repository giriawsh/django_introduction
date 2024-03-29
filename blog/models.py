from django.db import models


# Create your models here.

class Article(models.Model):
    # 文章的唯一ID
    article_id = models.AutoField(primary_key=True)  # 自动增加
    # 文章的标题-文本类型
    title = models.TextField()
    # 文章的摘要
    brief_content = models.TextField()
    # 文章的主要内容
    content = models.TextField()
    # 文章的日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title