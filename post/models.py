from django.db import models

from users.models import User


class Post(models.Model):
    """Модель поста"""

    title = models.CharField(max_length=150, verbose_name="заголовок")
    text = models.TextField(verbose_name="текст", blank=True, null=True)
    image = models.ImageField(
        upload_to="post/images", blank=True, null=True, verbose_name="изображение"
    )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="автор"
    )
    creation_date = models.DateField(
        verbose_name="дата создания", blank=True, null=True
    )
    modif_date = models.DateField(
        verbose_name="дата редактирования", blank=True, null=True
    )

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель комментария"""

    text = models.TextField(verbose_name="текст")
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="автор"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="пост")
    creation_date = models.DateField(
        verbose_name="дата создания", blank=True, null=True
    )
    modif_date = models.DateField(
        verbose_name="дата редактирования", blank=True, null=True
    )

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
