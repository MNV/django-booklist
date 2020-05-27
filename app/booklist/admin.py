from django.contrib import admin
from django.utils.safestring import mark_safe

from booklist.filters import PublishingHouseFilter
from booklist.models import Author, PublishingHouse, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        "lastname",
        "firstname",
        "patronymic",
        "birth_date",
        "email",
        "phone",
    )

    search_fields = (
        "lastname",
        "firstname",
        "patronymic",
        "email",
        "phone",
    )

    ordering = ("lastname", "firstname", "patronymic")


@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "address",
        "email",
        "phone",
    )

    search_fields = (
        "title",
        "email",
        "address",
        "phone",
    )

    ordering = ("title",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = (
        "title",
        "isbn",
    )

    list_display = (
        "title",
        "isbn",
        "publishing_year",
        "publishing_house",
        "authors_list",
    )

    list_select_related = ("publishing_house",)

    list_filter = (PublishingHouseFilter,)

    autocomplete_fields = ("publishing_house",)

    ordering = ("title",)

    def authors_list(self, obj):
        if not obj.authors:
            return "-"

        return mark_safe("<br/>".join(str(author) for author in obj.authors.all()))

    authors_list.short_description = "Авторы"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related("authors")

    class Media:
        pass
