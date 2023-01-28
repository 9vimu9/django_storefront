from django.contrib.contenttypes.models import ContentType
from django.db.models import Q, F, Count, Min, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.shortcuts import render
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem


def say_hello(request):
    # Task :
    # get tagged tags for a product.

    # Answer :
    # since Tag model is located in another application,
    # we have to use generic relationships to get data.
    #

    #  get content type id for a model
    content_type = ContentType.objects.get_for_model(Product)
    # SELECT `django_content_type`.`id`,
    # `django_content_type`.`app_label`,
    # `django_content_type`.`model`
    # FROM `django_content_type`
    # WHERE (`django_content_type`.`app_label` = 'store' AND `django_content_type`.`model` = 'product') LIMIT 21

    random_product_id = 1
    queryset = TaggedItem.objects. \
        select_related('tag') \
        .filter(
            content_type=content_type,  # set content type id
            object_id=random_product_id
        )
    # SELECT `tags_taggeditem`.`id`,
    # ...
    # FROM `tags_taggeditem`
    # INNER JOIN `tags_tag`
    # ON (`tags_taggeditem`.`tag_id` = `tags_tag`.`id`)
    # WHERE (`tags_taggeditem`.`content_type_id` = 12 AND `tags_taggeditem`.`object_id` = 1)

    return render(request, 'hello.html', {'name': 'Vim', 'products': list(queryset)})
