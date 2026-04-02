# 1 April 2026 - Role and Permission tables currently skipped though models exist
# If you run seed_all() twice, you will have duplicate data. If you want a fresh start, run User.objects.all().delete() in the shell first


from faker import Faker
import random
from core.models import *

fake = Faker()

def seed_all():
    print("🚀 Bulk seeding started...")

    # ----------------------------
    # TENANT STRUCTURE
    # ----------------------------
    tenant = Tenant.objects.create(
        name="Org",
        subscription_plan="Pro",
        status="active"
    )

    clients = [Client.objects.create(tenant=tenant, name=fake.company()) for _ in range(3)]
    branches = [Branch.objects.create(client=random.choice(clients), name=fake.city()) for _ in range(5)]
    sites = [Site.objects.create(branch=random.choice(branches), name=fake.street_name()) for _ in range(8)]

    # ----------------------------
    # USERS
    # ----------------------------
    users = []
    for _ in range(50):
        user = User.objects.create(
            email=fake.unique.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            client=random.choice(clients),
            branch=random.choice(branches),
            site=random.choice(sites)
        )
        users.append(user)

    # ----------------------------
    # COURSES & MODULES
    # ----------------------------
    courses = []
    for _ in range(20):
        course = Course.objects.create(
            title=fake.sentence(),
            created_by=random.choice(users)
        )
        courses.append(course)

        for i in range(3):
            Module.objects.create(
                course=course,
                title=f"Module {i+1}"
            )

    modules = list(Module.objects.all())

    # ----------------------------
    # ENROLLMENTS & PROGRESS
    # ----------------------------
    for user in users:
        enrolled_courses = random.sample(courses, k=random.randint(1, 5))
        for course in enrolled_courses:
            Enrollment.objects.create(user=user, course=course)

            for module in modules:
                if module.course == course:
                    ModuleProgress.objects.create(
                        user=user,
                        module=module
                    )

    # ----------------------------
    # CONTENT
    # ----------------------------
    files = [File.objects.create(file_name=fake.file_name(), uploaded_by=random.choice(users)) for _ in range(20)]
    contents = [Content.objects.create(file=f, title=fake.sentence()) for f in files]

    tags = [Tag.objects.create(name=fake.word()) for _ in range(10)]

    for content in contents:
        for _ in range(2):
            ContentTag.objects.create(
                content=content,
                tag=random.choice(tags)
            )

    # ----------------------------
    # ASSESSMENTS
    # ----------------------------
    for course in courses:
        assessment = Assessment.objects.create(course=course)

        for _ in range(5):
            q = Question.objects.create(assessment=assessment)

            for i in range(4):
                Option.objects.create(
                    question=q,
                    is_correct=(i == 0)
                )

    # ----------------------------
    # TRAINING
    # ----------------------------
    sessions = []
    for _ in range(10):
        session = TrainingSession.objects.create(
            course=random.choice(courses),
            trainer=random.choice(users),
            training_date=fake.date(),
            start_time=fake.time(),
            duration_minutes=random.randint(30, 120),
            status="completed"
        )
        sessions.append(session)

        for user in random.sample(users, 10):
            TrainingAttendance.objects.create(
                session=session,
                user=user,
                attendance_status=random.choice(["present", "absent"])
            )

            TrainingResult.objects.create(
                session=session,
                user=user,
                score=random.uniform(40, 100),
                total_marks=100,
                percentage=random.uniform(40, 100),
                submitted_at=fake.date_time()
            )

    # ----------------------------
    # COMMUNICATION
    # ----------------------------
    groups = [Group.objects.create(name=fake.word(), created_by=random.choice(users)) for _ in range(5)]

    for group in groups:
        members = random.sample(users, 10)

        for user in members:
            GroupMember.objects.create(group=group, user=user)

        for _ in range(20):
            Message.objects.create(
                group=group,
                sender=random.choice(members),
                message_text=fake.sentence()
            )

    for user in users:
        Notification.objects.create(
            user=user,
            title="Notification",
            message=fake.sentence(),
            type="system"
        )

    # ----------------------------
    # ANALYTICS
    # ----------------------------
    for _ in range(10):
        Report.objects.create(
            report_type="performance",
            generated_by=random.choice(users),
            date_from=fake.date(),
            date_to=fake.date(),
            export_format="pdf",
            status="completed"
        )

    for _ in range(5):
        ScheduledReport.objects.create(
            report_type="weekly",
            frequency="weekly",
            recipient_emails=fake.email(),
            created_by=random.choice(users),
            next_run=fake.date_time()
        )

    for user in users:
        ActivityLog.objects.create(
            user=user,
            activity_type="login",
            description="User logged in"
        )

    print("✅ Bulk seeding completed!")