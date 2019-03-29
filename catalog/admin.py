from django.contrib import admin
from .models import Genre, Book, Language, BookInstance, Author
# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)

# Inline editing of associated records
class BookInstancesInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# registering Book model with BookInstance inline display.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstancesInline]

# Inline view for Book Model to be displayed inline under Authors
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0

# registering Author model with Book inline display
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id', 'borrower')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )