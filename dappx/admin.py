# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from dappx.models import UserProfileInfo, User,Comment
admin.site.register(UserProfileInfo)
import os
import uuid
import zipfile
import dprojx.settings
from datetime import datetime
from zipfile import ZipFile
from django.contrib import admin
from django.core.files.base import ContentFile
from PIL import Image
from dappx.models import Album, AlbumImage,Comment
from dappx.forms import AlbumForm

admin.site.register(Album)
# In case image should be removed from album.
admin.site.register(AlbumImage)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body',  'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
