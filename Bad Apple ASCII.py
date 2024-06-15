import pygame
import sys
import cv2

pygame.init()
FPS = 30
clock = pygame.time.Clock()

# FONT
font_size = 12
font = pygame.font.SysFont('Courier', font_size) # For the same character size used are monospaced fonts
height_coef, width_coef = 6, 3 # ASCII character proportion
font_height = font.size("#")[1]


# VIDEO
video_path = "Bad Apple.mp4"
string = "#98&%?/*!+;><:'-,.' "
coef = 255 / (len(string) -1)
cap = cv2.VideoCapture(video_path)


# SCREEN
sc_width = font.size("#")[0] * int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) / width_coef
sc_height = font.size("#")[1] * int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) / height_coef
sc = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Bad Apple ASCII")


# AUDIO
pygame.mixer.init()
pygame.mixer.music.load("Bad Apple.mp3")
# input("Press to start")
pygame.mixer.music.play()
 

while True:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    sc.fill((0, 0, 0))

    # VIDEO
    ret, frame = cap.read()
    if ret == False:
        break

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = gray_image.shape
    # print(height, width)

    for y in range(0, height-1, height_coef):
        s = ""
        for x in range(0, width-1, width_coef):
            s += string[len(string) - int(gray_image[y, x] / coef) -1]
        if len(s) != 0:
            sc.blit(font.render(s, False, (255, 255, 255)), (0, font_size*(y/5)))

    pygame.display.update()

    # print(clock.get_fps())