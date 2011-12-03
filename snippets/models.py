import hashlib

from django.db import models
from django.core.cache import cache


class Snippet(models.Model):
    """ Represents a named snippet of text """

    key_format = 'snippet:{digest}'
    cache_timeout = 86400  # 24 hrs

    slug = models.SlugField(primary_key=True)
    text = models.TextField()

    def __unicode__(self):
        return self.slug

    @property
    def cache_key(self):
        return self.get_cache_key(self.slug)

    @classmethod
    def get_cache_key(cls, slug):
        digest = hashlib.md5(slug).hexdigest()
        return 

    @classmethod
    def get(cls, slug):
        """
        Retrieve snippet text by name. Try the cache first but default to
        a database lookup.
        """
        key = cls.get_cache_key(slug)
        cached_text = cache.get(key)
        if cached_text is not None:
            return cached_text
        text = cls.objects.get(slug=slug).text
        cache.set(key, text, cls.cache_timeout)
        return text
