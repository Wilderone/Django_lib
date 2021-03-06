from django.contrib import admin
from p_library.models import Book, Author, Publishing
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author', 'description')
    exclude = ('copy_count',)


@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Publishing)
class PublishingAdmin(admin.ModelAdmin):
    pass
