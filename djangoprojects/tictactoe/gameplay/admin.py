from django.contrib import admin
from .models import Game, Move #import objects from models 

#admin class to view status of the game
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status',)
    
# Register the models so they can be modified from admin
admin.site.register(Move)