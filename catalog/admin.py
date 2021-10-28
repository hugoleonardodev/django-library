from django.contrib import admin

# Custom Admin Site

from django.contrib.admin import AdminSite

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance


class MyAdminSite(AdminSite):
    site_header = 'My Site Administration'
    default_site = 'catalog.admin.MyAdminSite'
    
    
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

admin_site = MyAdminSite(name='myadmin')

admin_site.register(Book)
admin_site.register(Author)
admin_site.register(Genre)
admin_site.register(BookInstance)

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
