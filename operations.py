import pandas
from turtle import Turtle

DIR_REGIONS = "./ukraine_regions.csv"


class Operations(Turtle):

	def __init__(self):
		super().__init__()
		self.data = pandas.read_csv(DIR_REGIONS)
		self.list_name_regions = self.data.region.to_list()
		self.regions_len = len(self.data["region"])
		self.guessed_regions = []

	def add_label(self, guess):
		region_row = self.data[self.data["region"] == guess]
		self.guessed_regions.append(guess)
		self.hideturtle()
		self.penup()
		self.goto(int(region_row.x.iloc[0]), int(region_row.y.iloc[0]))
		self.write(f"{guess}", False, align="center", font=('Arial', 10, 'normal'))

	def exit_and_save(self):
		# missed_regions =[region for region in self.list_name_regions if region not in self.guessed_regions]
		# missed_regions = []
		# for region in self.list_name_regions:
		# 	if region not in self.guessed_regions:
		# 		missed_regions.append(region)
		dict_results = {
			"Your missed regions": [region for region in self.list_name_regions if region not in self.guessed_regions]
		}
		results_data = pandas.DataFrame(dict_results)
		results_data.to_csv("regions_to_learn.csv")
