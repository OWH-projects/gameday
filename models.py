from django.db import models
from django.template.defaultfilters import slugify
from django.db.models import *

ACTIVE = (
    ("preview", "Preview"),
    ("two-minute-drill", "Two-minute drill"),
    ("live-stats", "Live updates"),
    ("articles", "Articles"),
    ("videos", "Videos"),
    ("photos", "Photos"),
    ("extras", "Extras"),
)

class Game(models.Model):
    season = models.CharField(max_length=4, help_text="2013, 2014, etc.")
    date = models.DateField(blank=True, null=True)
    opponent = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, blank=True, help_text="Lowercase. No spaces.", editable=False)
    game_info = models.TextField(blank=True, help_text="Date, time, location, TV info, etc.")
    preview = models.TextField(blank=True, help_text='HTML allowed. H3 tag for headline. Use p.summary for intro text.')
    preview_image = models.ImageField(upload_to='gameday/images/', max_length=100, null=True, blank=True)
    opponent_logo = models.ImageField(upload_to='gameday/images/', max_length=100, null=True, blank=True)
    videos = models.TextField(blank=True)
    photos_fans = models.CharField(max_length=200, blank=True, help_text='Enter full gallery URL, e.g. http://odc.omaha.com/index.php?u_page=5002&p=4715')
    photos_action = models.CharField(max_length=200, blank=True, help_text='Enter full gallery URL, e.g. http://odc.omaha.com/index.php?u_page=5002&p=4715')
    live_chat = models.TextField(blank=True, help_text="Remember to adjust the width and height, as necessary.")
#    twitter_widget = models.TextField(blank=True)
    live_stats = models.TextField(blank=True, editable=False, help_text="Use the Stats Inc javascript code.")
    extras = models.TextField(blank=True, help_text="Additional game day content. HTML accepted.")
    two_minute_drill_author = models.CharField('Author', max_length=100, blank=True)
    two_minute_drill_nu_rush_offense = models.TextField('NU rush offense vs. opponent rush defense', blank=True)
    two_minute_drill_nu_pass_offense = models.TextField('NU pass offense vs. opponent pass defense', blank=True)
    two_minute_drill_opp_rush_offense = models.TextField('Opponent rush offense vs. NU rush defense', blank=True)
    two_minute_drill_opp_pass_offense = models.TextField('Opponent pass offense vs. NU pass defense', blank=True)
    two_minute_drill_special_teams = models.TextField('Special Teams', blank=True)
    two_minute_drill_intangibles = models.TextField('Intangibles', blank=True)
    two_minute_drill_matchup = models.CharField('Key matchup header', max_length=200, blank=True, help_text="Example: Big guys vs. little guys")
    two_minute_drill_key_matchup = models.TextField('Key matchup text', blank=True)
    two_minute_drill_nu_wins_if = models.TextField('NU wins if ...', blank=True)
    two_minute_drill_opp_wins_if = models.TextField('Opponent wins if ...', blank=True)
    two_minute_drill_our_take = models.TextField('Our take', blank=True)
    two_minute_drill_prediction = models.TextField('Prediction', blank=True)
    game_progress = models.CharField('Active tab', max_length=100, blank=True, choices=ACTIVE)

	
    def save(self):
        self.slug = slugify(self.opponent)
        super(Game, self).save()

    def __unicode__(self):
        return self.opponent

		
class Featured(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    priority = models.IntegerField(blank=True)
    #image = models.ImageField(ImageField(upload_to='gameday/featured/', max_length=100, null=True, blank=True)

    def __unicode__(self):
	    return self.name