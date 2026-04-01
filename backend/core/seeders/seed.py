from faker import Faker
from core.models import *

fake = Faker()

def seed_all():
    print("Seeding started...")

    tenant = Tenant.objects.create(
        name="Org",
        subscription_plan="Pro",
        status="active"
    )

    client = Client.objects.create(tenant=tenant, name="Client A")
    branch = Branch.objects.create(client=client, name="Branch A")
    site = Site.objects.create(branch=branch, name="Site A")

    user = User.objects.create(
        email=fake.email(),
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        client=client,
        branch=branch,
        site=site
    )

    course = Course.objects.create(
        title="AI Course",
        created_by=user
    )

    module = Module.objects.create(course=course, title="Intro Module")

    Enrollment.objects.create(user=user, course=course)
    ModuleProgress.objects.create(user=user, module=module)

    print("Seeding completed successfully!")