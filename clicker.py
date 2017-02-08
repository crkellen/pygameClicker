import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CASH = 0

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

#Profit Timers
GEN1_TIMER = 1000
GEN2_TIMER = 5100

#Generator Profits
GEN1_PROFIT = 10
GEN2_PROFIT = 100

#Generator Levels
GEN1_LEVEL = 1
GEN2_LEVEL = 0

#Generator Level Labels
GEN1_LEVEL_LABEL = 'Level: '
GEN2_LEVEL_LABEL = 'Level: '

#Events
GEN1_EVENT = pygame.USEREVENT + 1
GEN2_EVENT = pygame.USEREVENT + 2

def add_gen1_profit():
	global CASH
	CASH += GEN1_PROFIT
	
def add_gen2_profit():
	global CASH
	CASH += GEN2_PROFIT

def handle_events():
	event_dict = {
		pygame.QUIT: exit,
		GEN1_EVENT: add_gen1_profit,
		GEN2_EVENT: add_gen2_profit,
	}
	for event in pygame.event.get():
		if event.type in event_dict:
			event_dict[event.type]()

def handle_mouse_clicks():
	global CASH, PROFITS, GEN1_TIMER, GEN2_TIMER, GEN1_LEVEL, GEN2_LEVEL
	if pygame.mouse.get_focused():
		left_button = pygame.mouse.get_pressed()
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if GEN1.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 100 and GEN1_TIMER > 100:
			CASH -= 100
			GEN1_TIMER -= 100
			pygame.time.set_timer(GEN1_EVENT, GEN1_TIMER)
			GEN1_LEVEL += 1
		if GEN2.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 1000 and GEN2_TIMER > 100:
			CASH -= 1000
			GEN2_TIMER -= 100
			pygame.time.set_timer(GEN2_EVENT, GEN2_TIMER)
			GEN2_LEVEL += 1

def update_text():
	global CASH_LABEL, GEN1_LEVEL_LABEL, GEN2_LEVEL_LABEL
	WINDOW.blit(DRAW_SCREEN, (0, 0))
	WINDOW.blit(GEN1_LABEL, (10, 108))
	WINDOW.blit(GEN2_LABEL, (10, 143))
	CASH_LABEL = FONT.render('Total Cash: ${}'.format(CASH), 1, (255,255,0))
	WINDOW.blit(CASH_LABEL, (0, 0))
	GEN1_LEVEL_LABEL = FONT.render('Level: {}/{} --- $10/{} milliseconds'.format(GEN1_LEVEL, 10, GEN1_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN1_LEVEL_LABEL, (220, 108))
	GEN2_LEVEL_LABEL = FONT.render('Level: {}/{} --- $100/{} milliseconds'.format(GEN2_LEVEL, 50, GEN2_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN2_LEVEL_LABEL, (220, 143))
	pygame.display.flip()

def game_loop():
	while True:
		handle_events()
		handle_mouse_clicks()
		update_text()

def main():
	pygame.display.set_caption('Clicker')
	pygame.time.set_timer(GEN1_EVENT, GEN1_TIMER)
	game_loop()
	
main()