from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TimeStampMixin(models.Model):
    """Реализация атрибутов времени создания и обновления записи"""

    created_at = models.DateTimeField("Время создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления записи", auto_now=True)

    class Meta:
        abstract = True


class Author(TimeStampMixin):
    """Автор книги"""

    lastname = models.CharField("Фамилия", max_length=50, null=False)
    firstname = models.CharField("Имя", max_length=50, null=False)
    patronymic = models.CharField(
        "Отчество", max_length=50, null=True, default=None, blank=True
    )
    birth_date = models.DateField("Дата рождения", null=True, default=None, blank=True)
    email = models.CharField(
        "Email", max_length=50, null=True, default=None, blank=True
    )
    phone = models.CharField(
        "Телефон", max_length=30, null=True, default=None, blank=True
    )

    def __str__(self):
        return f"{self.lastname} {self.firstname} {self.patronymic if self.patronymic else ''}".strip()

    class Meta:
        app_label = "booklist"
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class PublishingHouse(TimeStampMixin):
    """Издательство книги"""

    title = models.CharField("Наименование", max_length=50, null=False)
    address = models.CharField("Адрес", max_length=50, null=False)
    email = models.CharField(
        "Email", max_length=50, null=True, default=None, blank=True
    )
    phone = models.CharField(
        "Телефон", max_length=30, null=True, default=None, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        app_label = "booklist"
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"


class Book(TimeStampMixin):
    """Книга"""

    authors = models.ManyToManyField(
        "Author", verbose_name="Авторы", related_name="author_books",
    )
    publishing_house = models.ForeignKey(
        "PublishingHouse",
        on_delete=models.PROTECT,
        verbose_name="Издательство",
        null=False,
        blank=False,
        related_name="publishing_house_book",
    )
    title = models.CharField(
        "Название", max_length=255, null=False, blank=False, db_index=True
    )
    publishing_year = models.SmallIntegerField(
        "Год издания",
        null=False,
        blank=False,
        validators=[MaxValueValidator(3000), MinValueValidator(1)],
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        null=False,
        blank=False,
        unique=True,
        help_text='<a href="https://www.isbn-international.org/content/what-isbn" target="_blank">ISBN номер</a>',
    )

    def __str__(self):
        return f"{self.title}, {self.publishing_year} г."

    class Meta:
        app_label = "booklist"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
