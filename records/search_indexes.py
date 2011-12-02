from haystack.indexes import CharField, SearchIndex
from haystack import site

from records.models import Wish, Gift


class WishIndex(SearchIndex):
    text = CharField(document=True, use_template=True)


class GiftIndex(SearchIndex):
    text = CharField(document=True, use_template=True)


site.register(Wish, WishIndex)
site.register(Gift, GiftIndex)
