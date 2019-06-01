from django.db import models

class Nameable(models.Model):
	name 		= models.CharField(max_length=15)

	class Meta:
		abstract = True

class Stockable(models.Model):
	ticker 		= models.ForeignKey('Stock', on_delete=models.CASCADE)

	class Meta:
		abstract = True


class Timestampable(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    @property
    def date(self):
    	return self.created_date.date()

    @property
    def day(self):
    	return self.created_date.strftime("%a")

    @property
    def month(self):
    	return self.created_date.strftime("%b")

    @property
    def calendar_week(self):
    	return self.created_date.isocalendar()[1]

    @property
    def month_week(self):
    	from math import ceil
    	first_day = self.created_date.replace(day=1)
    	dom = self.created_date.day
    	adjusted_dom = dom + first_day.weekday()
    	return int(ceil(adjusted_dom/7.0))

    class Meta:
        abstract = True
 
