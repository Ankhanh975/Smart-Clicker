import pygame
from _main2 import *

def CircleCollision(center, radius, pos):
	center = Vector2d.Vector(center)
	pos = Vector2d.Vector(pos)
	dis = (pos - center).getLength()
	if dis <= radius:
		return True
	else:
		return False

class RangeSlider:
	sliderVal1 = 7
	sliderVal2 = 11

	def __init__(self, pos=(50,50)):
		self.sliderBody = pygame.Rect(0+5, 2.5+5, 130+1, 5+1)
		self.sliderThumb1 = [(self.sliderVal1 / 20.0) * 130+5 , 0+10, 10]
		self.sliderThumb2 = [(self.sliderVal2 / 20.0) * 130+5 , 0+10, 10]
		self.sliderRange = pygame.Rect((self.sliderVal1 / 20.0) * 130 + 5+5, 3+5, ((self.sliderVal2 - self.sliderVal1) / 20.0) * 130+1, 4+1)

		self.thumbPressed1 = False
		self.thumbPressed2 = False

		self.surface = pygame.Surface((500, 500))
		self.pos = pos

	def update(self, events, screen):
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if CircleCollision((self.sliderThumb1[0], self.sliderThumb1[1]), self.sliderThumb1[2], self.mosuePos()):
					self.thumbPressed1 = True
				elif CircleCollision((self.sliderThumb2[0], self.sliderThumb2[1]), self.sliderThumb2[2], self.mosuePos()):
					self.thumbPressed2 = True
			elif event.type == pygame.MOUSEBUTTONUP:
				self.thumbPressed1 = False
				self.thumbPressed2 = False

		if self.thumbPressed1:
			if self.mosuePos()[0] - 5 < -5:
				self.sliderThumb1[0] = -5 +5
			elif self.mosuePos()[0] - 5 > 124:
				self.sliderThumb1[0] = 124+5
			else:
				self.sliderThumb1[0] = self.mosuePos()[0] - 5+5

			self.sliderRange.x = min(self.sliderThumb1[0], self.sliderThumb2[0]) + 5
			self.sliderRange.width = max(self.sliderThumb1[0], self.sliderThumb2[0]) - min(self.sliderThumb1[0], self.sliderThumb2[0])
			self.sliderVal1 = round(((self.sliderThumb1[0] + 2) / 130) * 20)

		elif self.thumbPressed2:
			if self.mosuePos()[0] - 5 < -5:
				self.sliderThumb2[0] = -5 +5
			elif self.mosuePos()[0] - 5 > 124:
				self.sliderThumb2[0] = 124+5
			else:
				self.sliderThumb2[0] = self.mosuePos()[0] - 5+5

			self.sliderRange.x = min(self.sliderThumb1[0], self.sliderThumb2[0]) + 5
			self.sliderRange.width = max(self.sliderThumb1[0], self.sliderThumb2[0]) - min(self.sliderThumb1[0], self.sliderThumb2[0])
			self.sliderVal1 = round(((self.sliderThumb2[0] + 2) / 130) * 20)

		self.draw(screen)

	def draw(self, screen):
		self.surface.fill((255,0,0))
		pygame.draw.rect(self.surface, (45, 47, 49), self.sliderBody)
		pygame.draw.rect(self.surface, (35, 168, 105), self.sliderRange)

		pygame.draw.circle(self.surface, (0, 0, 0), (self.sliderThumb1[0], self.sliderThumb1[1]), self.sliderThumb1[2])
		pygame.draw.circle(self.surface, (0, 0, 0), (self.sliderThumb2[0], self.sliderThumb2[1]), self.sliderThumb2[2])

		screen.blit(self.surface, self.pos)

	def mosuePos(self):
		pos = list(pygame.mouse.get_pos())
		pos[0] -= self.pos[0] 
		pos[1] -= self.pos[1] 
		return pos

if __name__== "__main__":
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((200,300), DOUBLEBUF)

	a = RangeSlider()
	
	while True:
		clock.tick(60)
		pygame.display.update()
		events = pygame.event.get()
		screen.fill((255,0,0))
		a.update(events, screen)

		for event in events:
			if event.type==pygame.QUIT:
				pygame.quit(); sys.exit()
