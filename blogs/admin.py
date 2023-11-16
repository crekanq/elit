from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import Biography, Employees, Photo, Blog


class BiographyAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Biography
        fields = '__all__'


class BiographyAdmin(admin.ModelAdmin):
    form = BiographyAdminForm


class BlogAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


admin.site.register(Employees)
admin.site.register(Photo)
admin.site.register(Biography, BiographyAdmin)
admin.site.register(Blog, BlogAdmin)
