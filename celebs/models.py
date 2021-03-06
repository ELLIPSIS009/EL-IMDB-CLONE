import re
from django.conf import settings
from django.db import models
from django.utils import timezone


class Duty(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Duties'

    def __str__(self):
        return self.name


class Celebrity(models.Model):
    date_added = models.DateTimeField('Added Date', auto_now_add=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100)
    nick_name = models.CharField(max_length=50, blank=True, null=True)

    birthdate = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=100, verbose_name='Birth place',
                        blank=True, null=True)
    duties = models.ManyToManyField(Duty, help_text="celebrity's duties in movies")
    bio = models.TextField(blank=True, null=True)

    source_content = models.URLField(blank=True, null=True, default='')
    source_image = models.CharField(max_length=250, blank=True, null=True)

    trailer = models.URLField(blank=True, null=True, default='', help_text='trailer url (for now, ONLY youtube videos)')

    class Meta:
        verbose_name_plural = 'Celebrities'
        ordering = ('last_name', 'first_name')

    def _get_movie(self, duty_name):
        if hasattr(self, '_prefetched_objects_cache') and 'movie_crews' in self._prefetched_objects_cache:
            return [c for c in self._prefetched_objects_cache['movie_crews'] if c.duty.name == duty_name]
        else:
            return self.movie_crews.filter(duty__name=duty_name)

    @property
    def as_director(self):
        return self._get_movie('Director')
    
    @property
    def as_writer(self):
        return self._get_movie('Writer')

    @property
    def as_cast(self):
        return self._get_movie('Cast')        

    @property
    def summary_long(self):
        sentences = re.split("[.!?]+", str(self.bio))
        sentences = '. '.join(sentences[0:2])
        return sentences

    @property
    def summary_short(self):
        sentences = re.split("[.!?]+", str(self.bio))
        return f'{sentences[0]}.'
        
    @property
    def youtube_video(self):
        """ gets youtube video specific code """
        if str(self.trailer).find('watch?v=') > -1:
            video_url = str(self.trailer).split('watch?v=')
            return video_url[1]
        return 'video does not exist'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        today = timezone.now()
        birthdate = self.birthdate
        return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    def __str__(self):
        return self.full_name
