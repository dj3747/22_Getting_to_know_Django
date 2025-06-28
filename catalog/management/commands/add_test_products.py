from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавляет тестовые продукты"

    def handle(self, *args, **kwargs):
        # Удаляем существующие данные
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Получение или создание категорий
        category1, create = Category.objects.get_or_create(
            name="Учебная литература", description="Образовательные пособия"
        )

        category2, create = Category.objects.get_or_create(
            name="Книги для детей", description="Литература для маленьких"
        )

        # Создание тестовых продуктов
        Product.objects.create(
            name="Физика",
            description="Учебник по физике",
            category=category1,
            price="100.00",
        )

        Product.objects.create(
            name="Химия",
            descriptuon="Учебник по химии",
            category=category1,
            price="150.00",
        )

        Product.objects.create(
            name="Басни",
            description="Истории со смыслом",
            category=category2,
            price="250.00"
        )

        self.stdout.write(self.style.SUCCESS("Тестовые продукты добавлены!"))
