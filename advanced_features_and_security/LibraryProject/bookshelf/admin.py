from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
from .models import Book




class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year') 
    search_fields = ('title', 'author')                    
    list_filter = ('publication_year',)                     
    ordering = ('-publication_year',)                       

admin.site.register(Book, BookAdmin)




# customizing admin to display new user details



class CustomUserAdmin(UserAdmin):

    model = CustomUser

    list_display = (
        'username',
        'email',
        'date_of_birth',
        'is_staff',
        'is_active',
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)

