import pygame, sys
pygame.init()

class _Slider():
	def __init__(self, name, val, maxi, mini, pos):
		self.val = val  # start value
		self.maxi = maxi  # maximum at slider position right
		self.mini = mini  # minimum at slider position left
		self.xpos = pos[0]  # x-location on screen
		self.ypos = pos[1]  # y-location on
		self.surf = pygame.surface.Surface((100, 50))
		self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

		self.surf.fill((100, 100, 100))
		pygame.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)


		# dynamic graphics - button surface #
		self.button_surf = pygame.surface.Surface((20, 20))
		self.button_surf.fill(TRANS)
		self.button_surf.set_colorkey(TRANS)
		pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
		pygame.draw.circle(self.button_surf, ORANGE, (10, 10), 4, 0)

	def draw(self):
		surf = self.surf.copy()
		# dynamic
		pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
		self.button_rect = self.button_surf.get_rect(center=pos)
		surf.blit(self.button_surf, self.button_rect)
		self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position

		screen.blit(surf, (self.xpos, self.ypos))

	def move(self):
		self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
		if self.val < self.mini:
			self.val = self.mini
		if self.val > self.maxi:
			self.val = self.maxi

class RangeSlider: #? Why don't work
	def __init__(self, val, maxi, mini, pos):
		self.button = _Slider("Java", val, maxi, mini, pos)

	def update(self, events):
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if self.button.button_rect.collidepoint(pos):
					self.button.hit = True
			elif event.type == pygame.MOUSEBUTTONUP:
				self.button.hit = False


		if self.button.hit:
			self.button.move()
		self.button.draw()

		print(self.button.val, self.button.hit, self.button.maxi, self.button.mini, self.button.xpos, self.button.ypos, self.button.surf)


if __name__ == "__main__":
	screen = pygame.display.set_mode((900, 600))
	clock = pygame.time.Clock()

	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	RED = (255, 50, 50)
	YELLOW = (255, 255, 0)
	GREEN = (0, 255, 50)
	BLUE = (50, 50, 255)
	GREY = (200, 200, 200)
	ORANGE = (200, 100, 50)
	CYAN = (0, 255, 255)
	MAGENTA = (255, 0, 255)
	TRANS = (1, 1, 1)
	COLORS = [MAGENTA, RED, YELLOW, GREEN, CYAN, BLUE]


	pen = _Slider("Pen", 10, 30, 1, (100,100))
	a = RangeSlider(10, 30, 1, (200,200))

	num = 0

	while True:
		events =  pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if pen.button_rect.collidepoint(pos):
					pen.hit = True
			elif event.type == pygame.MOUSEBUTTONUP:
					pen.hit = False

		a.update(events)
		if pen.hit:
			pen.move()

		screen.fill((0,0,0))

		pen.draw()
		print(pen.val, pen.hit, pen.maxi, pen.mini, pen.xpos, pen.ypos, pen.surf)


		#print(pen.val)
		pygame.display.flip()
		clock.tick(60)