from django.db import models

from paths import models as path_models


class Texture(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/textures/')
    path = models.ManyToManyField(path_models.Path, through='TexturePath', related_name="textures")

    class Meta:
        verbose_name_plural = "Textures"

    def __str__(self) -> str:
        return self.title


class TexturePath(models.Model):
    texture = models.ForeignKey(Texture, on_delete=models.CASCADE)
    path = models.ForeignKey(path_models.Path, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "TexturePaths"

    def __str__(self) -> str:
        return f" Path: {self.path.title} - texture: {self.texture.title}"
