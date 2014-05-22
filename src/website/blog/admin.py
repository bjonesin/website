from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
	#fields display on change list
	list_display =['title','description']
	#fields to filter the change list with
	list_filter = ['published','created']
	# fields to search in change list
	search_fields = ['title', 'description','content']
	# enanble the date drill down on change list
	date_hierarchy = 'created'
	# enable the save button on top on change form
	save_on_top = True
	#preopulate the slug from the title - big time saver
	prepopulated_fields = {"slug":("title",)}

admin.site.register(Post, PostAdmin)