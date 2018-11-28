from django.contrib import admin
from tane.models import Student, Promotion


class StudentAdmin(admin.ModelAdmin):
    pass

class PromotionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)
admin.site.register(Promotion, PromotionAdmin)
