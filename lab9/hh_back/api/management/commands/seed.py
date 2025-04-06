import random
from django.core.management.base import BaseCommand
from api.models import Company, Vacancy

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Company.objects.all().delete()
        Vacancy.objects.all().delete()

        for i in range(5):
            company = Company.objects.create(
                name=f"Company {i}",
                description="Test company",
                city="City",
                address="Address"
            )
            for j in range(4):
                Vacancy.objects.create(
                    name=f"Vacancy {j} at {company.name}",
                    description="Some job description",
                    salary=random.uniform(1000, 5000),
                    company=company
                )
        self.stdout.write(self.style.SUCCESS("Test data created!"))
