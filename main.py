from flet import *

def main(page:Page):
	page.window_width = 300
	page.window_height = 500

	def runscroll(e:OnScrollEvent):
		# AND YOU CAN SET EFFECT IN THIS 
		# IF YOU SCROLL DOWN SCROLLBAR
		print(e)
		# I WILL SET BGCOLOR TO RED IF YOU SCROLL DOWN
		animatedbar.bgcolor = "red" if e.pixels > 140  else "blue"
		# AND CHANGE HEIGHT TO SMALL SIZE DENSE
		animatedbar.height = 50  if e.pixels > 140  else 80

		# AND I HIDE SEARCH ICON IF YOU SCROLL DOWN 
		animatedbar.content.controls[0].content.controls[0].visible = False if e.pixels > 140  else True

		# AND SHOW FAVORITE ICON IF YOU SCROLL DOWN
		animatedbar.content.controls[1].content.visible = True if e.pixels > 140  else False

		page.update()


	mylist = Column(scroll="always",
		# AND I DETECT IF SCROLL DOWN
		on_scroll=runscroll
		)

	# NOW I CREATE FAKE DATA FOR YOU CAN SCROLLING
	for x in range(1,40):
		mylist.controls.append(
			Text(f"sample - {x}")
			)
	listnav =Row([
		Container(
			content=Row([
				# THIS I WILL CREATE ICON AND TEXT APPBAR
				Icon(name="search",
					color="white",size=25,
					visible=True
					),
				Text("this APPbar",
					color="white",weight="bold",
					size=25
					)

				])
			),
		# AND I CREATE ICON FAVORITE 
		# THIS WILL SHOW IF YOU SCROLL BAR DOWN 
		Container(
			Icon(name="favorite",
				size=25,color="white",
				# AND I SET VISIBLE TO FALSE
				# THIS WILL SHOW IF YOU SCROLL DOWN
				visible=False
				)

			)

		],alignment="spaceBetween")




	# AND NOW I CREATE APPBAR ANIMATED HERE
	animatedbar = Container(
		height=80,
		bgcolor="blue",
		padding=10,
		animate=animation.Animation(400,"easeIn"),
		content=listnav
		)
	# AND NOW I WILL SET animatedbar to FIXED SCROLL
	# like css like name is fixed

	page.overlay.append(animatedbar)

	page.add(
		Container(
			margin=margin.only(top=80),
			height=page.window_height,
			width=page.window_width,
			content=mylist
			)
		)

flet.app(target=main)
