from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


# customized model manager
class TaggedItemManager(models.Manager):

    # created a method inside the new Model manager to get Tagged
    # items for a certain model
    def get_tags_for(self, object_type, object_id):
        return TaggedItem.objects \
            .select_related('tag') \
            .filter(
                content_type=ContentType.objects.get_for_model(object_type),
                object_id=object_id
            )


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # assigned customized model manager to objects attribute.
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
