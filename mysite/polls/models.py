from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
	
    class Meta:
        permissions = (
            ("can_vote", "Whether a user can vote or not on polls."),
			("can_view", "Can the user view?")
        )
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
	
	# to string method
    def __str__(self):
        return self.question_text
	# Checks if the question was published recently
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
	
    def __str__(self):
	# to string method
        return self.choice_text