from __future__ import unicode_literals

from django.contrib import admin

from oembed.models import ProviderRule, StoredOEmbed

admin.site.register(ProviderRule)
admin.site.register(StoredOEmbed)
