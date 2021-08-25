WindowManager:
	FirstWindow:
	SecondWindow:

<FirstWindow>:
	name:"first"

	Boxlayout:
		orientation:"vertical"
		size:root.width , root.height

		Label:
			text:"First Screen"
			font_size::32

		Button:
			text:"Next Screen"
			font_size:32
			on_release:


<SecondWindow>:
	name:"second"	

	Boxlayout:
		orientation:"vertical"
		size:root.width , root.height

		Label:
			text:"Second Screen"
			font_size::32

		Button:
			text:"Go back Screen"
			font_size:32
			on_release:
			

