// all can run parallel
// if ClickEvent or PressEvent when button down:
//	release button -> ClickEvent / PressEvent

Global:
	//Global.init_time  (=0)
	//Global.start_time
	//Global.run_time (s, count since Global.Start)
	//Global.init_run_time (s, count since Global.init)
	//Global.running object
	//Global.CreatedEvent (number of ClickEvent + PressEvent)
	Kill:
		KeyPress: Ctrl+Shift+Esc
		or run_time > 1000


O.Clicker:
	Name: Clicker1

	ClickEvent:
		Test.h:  // C:/src/Python/Smart Clicker/V2/Test.h
		// playback, error if data don't have D.Mouse object

		and Click: 
			Button: Middle
			Pos: 100, 100
			HoldTime: 0.1

	TPS : 5
	//ClickPerSec: 5
	//ClickDelay: 1/5

	Condition:
		O.Box:
			TopLeft:
				x: 100
				y: 100
			BottomRight:
				x: 200
				y: 200
			//Width: 100
			//Height: 100

		and ActiveWindow: 
			(716) YouTube - Brave

		and O.Switch:
			Name: Switch1
			SwitchSound: 10%
			SwitchEvent:
				//Click: Middle
				KeyPress: c
				//Condition:
				//	O.Box:
				//		TopLeft:
				//			x: 100
				//			y: 100
				//		BottomRight:
				//			x: 200
				//			y: 200
				//		//Width: 100
				//		//Height: 100
				//
				//or ActiveWindow: 
				//	(716) YouTube - Brave


	Kill:
		KeyPress: Ctrl+Shift+Esc
		or ClickCount > 1000


	TimePrecise: 2ms
	PosPrecise: 5 pixel //random around click pos
	//PosPrecise: 0.2 cm

	ClickSound: 10%

O.Typist:
	Name: Typist1
	PressEvent: 
		Press: a
	TPS : 5

O.Recorder:
	Name: Recorder1
	RecordEvent: 
			D.ActiveWindow

		and D.Mouse:
			n

	Output: Test.h //C:/src/Python/Smart Clicker/V2/self.Name.h
