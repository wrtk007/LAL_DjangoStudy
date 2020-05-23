from django.contrib import admin
from bookmark.models import Bookmark

# Register your models here.
@admin.register(Bookmark)

#동일한 함수 : admin.site.register(Bookmark, BookmarkAdmin)

class BookmarkAdmin(admin.ModelAdmin) :
    list_display = ('id', 'title', 'url')
