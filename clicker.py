import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CASH = 0
PROFITS = 10
PROFITEVENT = pygame.USEREVENT + 1

BACKGROUND_COLOR = (0, 0, 0)
BUTTON_COLOR = (0, 255, 0)

FONT = pygame.font.SysFont('monospace', 15)

#Main Screen for drawing buttons
DRAW_SCREEN = pygame.Surface((WIDTH,HEIGHT))
DRAW_SCREEN.fill(BACKGROUND_COLOR)

#Buttons
GEN1 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 100, 200, 30), 1)
GEN2 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 135, 200, 30), 1)

#Button Text
GEN1_LABEL = FONT.render('100 for +10', 1, (255, 255, 0))
GEN2_LABEL = FONT.render('1000 for +100', 1, (255, 255, 0))

def make_it_rain():
	global CASH
	CASH += PROFITS

def handle_events():
	event_dict = {
		pygame.QUIT: exit,
		PROFITEVENT: make_it_rain,
	}
	for event in pygame.event.get():
		if event.type in event_dict:
			event_dict[event.type]()
	

def handle_mouse_clicks():
	global CASH, PROFITS
	if pygame.mouse.get_focused():
		left_button = pygame.mouse.get_pressed()
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if GEN1.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 100:
			CASH -= 100
			PROFITS += 10
		if GEN2.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 1000:
			CASH -= 1000
			PROFITS += 100

def update_text():
	WINDOW.blit(DRAW_SCREEN, (0, 0))
	CASHLabel = FONT.render('Total Cash: ${}'.format(CASH), 1, (255,255,0))
	WINDOW.blit(CASHLabel, (0, 0))
	WINDOW.blit(GEN1_LABEL, (10, 108))
	WINDOW.blit(GEN2_LABEL, (10, 143))
	pygame.display.flip()

def game_loop():
	while True:
		handle_events()
		handle_mouse_clicks()
		update_text()

def main():
	pygame.display.set_caption('Clicker')
	pygame.time.set_timer(PROFITEVENT, 1000)
	game_loop()
	
main()