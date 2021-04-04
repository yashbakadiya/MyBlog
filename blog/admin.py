from django.contrib import admin
from .models import Post

admin.site.register(Post)
fields = (...,'privacy',...)
radio_fields = {'privacy':admin.VERTICAL}