import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

BACKGROUND_IMAGE_PATH = "background.png"
CHARACTER_IMAGE_PATH = "character.png"
ENEMY_IMAGE_PATH = "enemy.png"

pygame.init()

# 창 크기 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("UG Spaceman dodging a falling planet")

# 이미지 로드
background_image = pygame.image.load("background.png")
character_image = pygame.image.load("character.png")
enemy_image = pygame.image.load("enemy.png")

# 시계 설정
clock = pygame.time.Clock()

# 폰트 설정
font = pygame.font.Font(None, 36)

# 게임 실행 여부
done = False

# 점수
score = 0

# 캐릭터 위치 초기화
character_x = SCREEN_WIDTH // 2
character_y = SCREEN_HEIGHT - character_image.get_height()

# 똥 위치 초기화
enemy_x = random.randint(0, SCREEN_WIDTH - enemy_image.get_width())
enemy_y = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and character_x > 0:
        character_x -= 5
    elif keys[pygame.K_RIGHT] and character_x < SCREEN_WIDTH - character_image.get_width():
        character_x += 5

    # 배경화면 그리기
    screen.blit(background_image, [0, 0])

    # 똥 위치 변경
    enemy_y += 10

    # 똥이 화면 밖으로 나가면 새로운 똥 생성
    if enemy_y > SCREEN_HEIGHT:
        enemy_x = random.randint(0, SCREEN_WIDTH - enemy_image.get_width())
        enemy_y = 0
        score += 1

    # 똥 그리기
    screen.blit(enemy_image, [enemy_x, enemy_y])

    # 캐릭터 그리기
    screen.blit(character_image, [character_x, character_y])

    # 충돌 검사
    if character_x + character_image.get_width() > enemy_x and \
       character_x < enemy_x + enemy_image.get_width() and \
       character_y + character_image.get_height() > enemy_y and \
       character_y < enemy_y + enemy_image.get_height():
        done = True

    # 점수 출력
    text = font.render("Score: "+str(score), True, BLACK)
    screen.blit(text, [10, 10])

    # 화면 업데이트
    pygame.display.flip()

    # 30프레임으로 설정
    clock.tick(30)

pygame.quit()
