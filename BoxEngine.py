import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
width = 640
height = 480

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Коробка из точек")

# Цвета
BLACK = (0, 0, 0)

# Параметры коробки
box_start_width = 100
box_start_height = 100
box_center_x = width // 2
box_center_y = height // 2
box_color = (255, 255, 255)
box_line_width = 6
box_points = []

def create_points():
    points = []
    half_width = box_width // 2
    half_height = box_height // 2
    for x in range(box_center_x - half_width, box_center_x + half_width + 1):
        points.append((x, box_center_y - half_height))
        points.append((x, box_center_y + half_height))
    for y in range(box_center_y - half_height, box_center_y + half_height + 1):
        points.append((box_center_x - half_width, y))
        points.append((box_center_x + half_width, y))
    return points

# Зажатые клавиши
keys_pressed = set()

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка нажатий и отпускания клавиш
        if event.type == pygame.KEYDOWN:
            keys_pressed.add(event.key)
        elif event.type == pygame.KEYUP:
            keys_pressed.discard(event.key)

    screen.fill(BLACK)

    # Изменение размера коробки при зажатии клавиш
    if pygame.K_w in keys_pressed and box_start_height > 10:
        box_start_height -= 5
    elif pygame.K_s in keys_pressed:
        box_start_height += 5
    if pygame.K_a in keys_pressed and box_start_width > 10:
        box_start_width -= 5
    elif pygame.K_d in keys_pressed:
        box_start_width += 5

    box_width = box_start_width + 2 * box_line_width
    box_height = box_start_height + 2 * box_line_width

    box_points = create_points()

    pygame.draw.rect(screen, box_color, pygame.Rect(box_center_x - box_width // 2, box_center_y - box_height // 2,
                                                    box_width, box_height), box_line_width)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
