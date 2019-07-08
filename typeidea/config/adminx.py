import xadmin

from .models import Link, SideBar

# Register your models here.


@xadmin.sites.register(Link)
class LinkAdmin(object):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')
    fields = ('title', 'href', 'status', 'weight')

    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()


@xadmin.sites.register(SideBar)
class SideBarAdmin(object):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    def save_models(self):
        self.new_obj.owner = self.request.user
        return super().save_models()
