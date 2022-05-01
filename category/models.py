from django.db import models

# Create your models here.
# category model
class Category(models.Model):
    # objects = CommentManager()
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=("Parent Category"),
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created",)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

