from django.db import models

from django.contrib.auth.models import User

class Entry(models.Model):
	entry_title = models.CharField(max_length=50)
	entry_text = models.TextField()
	entry_date = models.DateTimeField(auto_now_add=True)
	entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "entries"

	def __str__(self):
		return f'{self.entry_title}'

class Comment(models.Model):
    entry = models.ForeignKey('entries.Entry', on_delete=models.CASCADE, related_name='comments')
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text