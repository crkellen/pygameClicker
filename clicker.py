import pygame

class Button:
	def __init__(self, x=0, y=0, w=1, h=1, c=0):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.cost = c
		self.level = 0
	
	def click(self):
		if cash >= self.cost:
			self.level += 1

pygame.init()
cash = 0
profits = 10
width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Clicker')
background_color = (0,0,0)
button_color = (0,255,0)

font = pygame.font.SysFont("monospace", 15)

draw_screen = pygame.Surface((width,height))
draw_screen.fill(background_color)

brush_color = (0,150,160)
brush_size = 5
brush_thickness = 0 #filling of circle
brush_screen = pygame.Surface((2*brush_size+1, 2*brush_size+1))
offset = brush_size+1
transparent_color = (255 - brush_color[0], 255 - brush_color[1], 255 - brush_color[2], brush_thickness)
#this creates a valid color which is not the brush_color
brush_screen.set_colorkey(transparent_color) #set this color as transparent
brush_screen.fill(transparent_color)
pygame.draw.circle(brush_screen, brush_color, (offset, offset), brush_size, brush_thickness)

gen1 = pygame.draw.rect(draw_screen, button_color, pygame.Rect(0, 100, 200, 30), 1)
gen2 = pygame.draw.rect(draw_screen, button_color, pygame.Rect(0, 135, 200, 30), 1)

gen1Label = font.render("100 for +10", 1, (255,255,0))
gen2Label = font.render("1000 for +100", 1, (255,255,0))

done = False
clock = pygame.time.Clock()
PROFITEVENT = pygame.USEREVENT+1
pygame.time.set_timer(PROFITEVENT, 1000)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == PROFITEVENT:
			cash += profits
	(left_button) = pygame.mouse.get_pressed()
	window.blit(draw_screen, (0,0))
	if pygame.mouse.get_focused():
		(mouse_x, mouse_y) = pygame.mouse.get_pos()
		if( gen1.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and cash >= 100 ):
			cash -= 100
			profits += 10
		if( gen2.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and cash >= 1000 ):
			cash -= 1000
			profits += 100
	cashLabel = font.render("Total Cash: " + str(cash), 1, (255,255,0))
	window.blit(cashLabel, (0,0))
	window.blit(gen1Label, (10, 108))
	window.blit(gen2Label, (10, 143))
	pygame.display.flip()
	clock.tick(60)
pygame.quit()