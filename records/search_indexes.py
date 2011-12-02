from datetime import datetime

from haystack import indexes

from records.models import Wish, Gift


class WishIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Wish

    def index_queryset(self):
        return self.get_model().objects.filter(created__lte=datetime.now())



class GiftIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Gift

    def index_queryset(self):
        return self.get_model().objects.filter(created__lte=datetime.now())
