from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그명")

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "fastcampus_tag"
        verbose_name = "패스트캠퍼스 태그"
        verbose_name_plural = "패스트캠퍼스 태그"
