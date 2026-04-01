from django.contrib import admin
from core.models import *

# Register all models
admin.site.register(Tenant)
admin.site.register(Client)
admin.site.register(Branch)
admin.site.register(Site)

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(UserRole)
admin.site.register(RolePermission)

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Enrollment)
admin.site.register(ModuleProgress)

admin.site.register(File)
admin.site.register(Content)
admin.site.register(Tag)
admin.site.register(ContentTag)

admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Submission)

admin.site.register(TrainingSession)
admin.site.register(TrainingAttendance)
admin.site.register(TrainingResult)

admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(Message)
admin.site.register(Notification)

admin.site.register(Report)
admin.site.register(ScheduledReport)
admin.site.register(ActivityLog)