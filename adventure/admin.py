from django.contrib import admin
<<<<<<< HEAD

from .models import Room, Player


=======
from .models import Room, Player
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'uuid')


admin.site.register(Room, RoomAdmin)
<<<<<<< HEAD
admin.site.register(Player, PlayerAdmin)
=======
admin.site.register(Player, PlayerAdmin)
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
