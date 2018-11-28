from django.contrib import admin
from tane.models import Student, Promotion, Project


class StudentAdmin(admin.ModelAdmin):
    pass


class PromotionAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Project, ProjectAdmin)
