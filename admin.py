from django.contrib import admin
from gameday.models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ('opponent', 'date', 'season', 'game_progress')
    fieldsets = [
        (None, {'fields': ['opponent', 'date', 'season', 'game_info', 'preview', 'preview_image', 'opponent_logo', 'videos', 'photos_fans', 'photos_action', 'live_chat', 'extras', 'game_progress']}),
        ('2-Minute Drill', {'fields': ['two_minute_drill_author', 'two_minute_drill_nu_rush_offense', 'two_minute_drill_nu_pass_offense', 'two_minute_drill_opp_rush_offense', 'two_minute_drill_opp_pass_offense', 'two_minute_drill_special_teams', 'two_minute_drill_intangibles', 'two_minute_drill_matchup', 'two_minute_drill_key_matchup', 'two_minute_drill_nu_wins_if', 'two_minute_drill_opp_wins_if', 'two_minute_drill_our_take', 'two_minute_drill_prediction']}),
    ]

admin.site.register(Game, GameAdmin)