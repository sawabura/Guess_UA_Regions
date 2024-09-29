import turtle

DIR_IMG = "./blank_ukraine.gif"


# screen setup

screen = turtle.Screen()
screen.setup(width=1000, height=710)
# screen.setup(width=725, height=491)
screen.title("CHECKING THE COORDINATES")
screen.addshape(DIR_IMG)
turtle.shape(DIR_IMG)


def print_click_coor(x, y):
	print(f"{x},{y}")

screen.onscreenclick(print_click_coor)


screen.mainloop()
