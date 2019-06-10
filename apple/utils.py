
import datetime

class CurrentDateTime():
	def __init__(self):
		self.current_date = datetime.datetime.today()

	@property
	def today(self):
		return self.current_date
	
	@property
	def date(self):
		return self.current_date.date()

	@property
	def day(self):
		return self.current_date.strftime("%a")

	@property
	def month(self):
		return self.current_date.strftime("%b")

	@property
	def calendar_week(self):
		return self.current_date.isocalendar()[1]

	@property
	def month_week(self):
		from math import ceil
		first_day = self.current_date.replace(day=1)
		dom = self.current_date.day
		adjusted_dom = dom + first_day.weekday()
		return int(ceil(adjusted_dom/7.0))

	@property
	def week_ago_datetime(self):
		return self.current_date - datetime.timedelta(days=7)
	