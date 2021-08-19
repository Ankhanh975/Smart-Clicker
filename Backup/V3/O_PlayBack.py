from O_Global import Base	
class O_PlayBack(Base):
	def __init__(self):
		super().__init__()
		self.Cursor = 0
		self.type = "Mouse" 
		#self.type = "Keyboard"
	def Update(self):
		super().Update()
			


class O_MousePlayBack(Base)
	def __init__(self):
		s