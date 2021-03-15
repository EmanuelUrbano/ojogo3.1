import pygame
import sys
import keyword

import pygame.mixer

from PySimpleGUI import PySimpleGUI as sg

pygame.init()

altura = 600
largura = 1230
mainClock = pygame.time.Clock()
screen = pygame.display.set_mode((largura, altura), 0, 32)

font = pygame.font.SysFont(None, 20)
font2 = pygame.font.SysFont(None, 70)
font3 = pygame.font.Font("Gameplay.ttf", 150)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

valoresRangeEpyCCH = {
    'game': {

        'cch': [
            {'orange': range(30, 310), 'py': 330},
            {'orange': range(200, 250), 'py': 360},
            {'orange': range(250, 310), 'py': 190},
            {'orange': range(380, 450), 'py': 190},
            {'orange': range(30, 80), 'py': 190},
            {'orange': range(30, 90), 'py': 160},
            {'orange': range(180, 250), 'py': 190},
            {'orange': range(180, 250), 'py': 160},
            {'orange': range(500, 650), 'py': 90},
            {'orange': range(530, 610), 'py': 130},
            {'orange': range(470, 540), 'py': 320},
            {'orange': range(600, 650), 'py': 350},
            {'orange': range(460, 650), 'py': 300},
            {'orange': range(30, 90), 'py': 380},
            {'orange': range(80, 130), 'py': 350},
            {'orange': range(160, 200), 'py': 380},
            {'orange': range(-20, 640), 'py': 80},

        ],
        'cev': [
            {'orange': range(340, 380), 'px': 210},
            {'orange': range(240, 330), 'px': 310},
            {'orange': range(340, 360), 'px': 250},
            {'orange': range(80, 190), 'px': 310},
            {'orange': range(80, 195), 'px': 440},
            {'orange': range(80, 160), 'px': 90},
            {'orange': range(160, 200), 'px': 80},
            {'orange': range(80, 140), 'px': 590},
            {'orange': range(240, 440), 'px': 440},
            {'orange': range(300, 330), 'px': 540},
            {'orange': range(340, 390), 'px': 80},
            {'orange': range(340, 360), 'px': 130},
            {'orange': range(-20, 460), 'px': 30},
        ],
        'cdv': [
            {'orange': range(340, 390), 'px': 150},
            {'orange': range(80, 170), 'px': 170},
            {'orange': range(170, 200), 'px': 170},
            {'orange': range(80, 100), 'px': 480},
            {'orange': range(100, 140), 'px': 520},
            {'orange': range(80, 200), 'px': 360},
            {'orange': range(190, 330), 'px': 460},
            {'orange': range(310, 360), 'px': 580},
            {'orange': range(230, 440), 'px': 360},
            {'orange': range(70, 450), 'px': 640},

        ],
        'cbh': [
            {'orange': range(310, 40), 'py': 240},
            {'orange': range(-20, 310), 'py': 230},
            {'orange': range(365, 450), 'py': 230},
            {'orange': range(450, 650), 'py': 200},
            {'orange': range(-20, 670), 'py': 420},
        ],
    }
}

def collisaEsquerdaParedeVertical(vel, bd, pos_x, pos_y):
    for a in range(len(valoresRangeEpyCCH[bd]['cev'])):
        for i in valoresRangeEpyCCH[bd]['cev'][a]['orange']:
            if pos_x == valoresRangeEpyCCH[bd]['cev'][a]['px'] and pos_y == i:
                pos_x += vel
    return pos_x

def collisaDireitaVertical(vel, bd, pos_x, pos_y):
    for a in range(len(valoresRangeEpyCCH[bd]['cdv'])):
        for i in valoresRangeEpyCCH[bd]['cdv'][a]['orange']:
            if pos_x == valoresRangeEpyCCH[bd]['cdv'][a]['px'] and pos_y == i:
                pos_x -= vel
    return pos_x

def collisaCimaHorizontal(vel, bd, pos_x, pos_y):
    for a in range(len(valoresRangeEpyCCH[bd]['cch'])):
        for i in valoresRangeEpyCCH[bd]['cch'][a]['orange']:
            if pos_x == i and pos_y == valoresRangeEpyCCH[bd]['cch'][a]['py']:
                pos_y += vel
    return pos_y

def collisaBaixoHorizontal(vel, bd, pos_x, pos_y):
    for a in range(len(valoresRangeEpyCCH[bd]['cbh'])):
        for i in valoresRangeEpyCCH[bd]['cbh'][a]['orange']:
            if pos_x == i and pos_y == valoresRangeEpyCCH[bd]['cbh'][a]['py']:
                pos_y -= vel
    return pos_y

spritesCenario = {
    'home': pygame.image.load("images\home.png")

}

sprites = {
    'boy': {
        'IdleDonw': pygame.image.load("images\spritesTestes\imagem_1.png"),
        'IdleLeft': pygame.image.load("images\spritesTestes\imagem_4.png"),
        'IdleUp': pygame.image.load("images\spritesTestes\imagem_7.png"),
        'IdleRigth': pygame.image.load("images\spritesTestes\imagem_10.png"),
        'animImgDonw': ["images\spritesTestes\imagem_1.png", "images\spritesTestes\imagem_2.png",
                        "images\spritesTestes\imagem_1.png", "images\spritesTestes\imagem_3.png"],
        'animImgLeft': ["images\spritesTestes\imagem_4.png", "images\spritesTestes\imagem_5.png",
                        "images\spritesTestes\imagem_4.png", "images\spritesTestes\imagem_6.png"],
        'animImgUP': ["images\spritesTestes\imagem_7.png", "images\spritesTestes\imagem_8.png",
                      "images\spritesTestes\imagem_7.png", "images\spritesTestes\imagem_9.png"],
        'animImgRight': ["images\spritesTestes\imagem_10.png", "images\spritesTestes\imagem_11.png",
                         "images\spritesTestes\imagem_10.png", "images\spritesTestes\imagem_12.png"],
    },
    'girl': {
        'IdleDonw': pygame.image.load("images\sprites\imagem_1.png"),
        'IdleLeft': pygame.image.load("images\sprites\imagem_4.png"),
        'IdleUp': pygame.image.load("images\sprites\imagem_7.png"),
        'IdleRigth': pygame.image.load("images\sprites\imagem_10.png"),
        'animImgDonw': ["images\sprites\imagem_1.png", "images\sprites\imagem_2.png",
                        "images\sprites\imagem_3.png", "images\sprites\imagem_4.png"],
        'animImgLeft': ["images\sprites\imagem_5.png", "images\sprites\imagem_6.png",
                        "images\sprites\imagem_7.png", "images\sprites\imagem_8.png"],
        'animImgUP': ["images\sprites\imagem_13.png", "images\sprites\imagem_14.png",
                      "images\sprites\imagem_15.png", "images\sprites\imagem_16.png"],
        'animImgRight': ["images\sprites\imagem_9.png", "images\sprites\imagem_10.png",
                         "images\sprites\imagem_11.png", "images\sprites\imagem_12.png"],
    }

}
def main_menu():
    seta_px = 190
    seta_py = 300

    while True:

        screen.fill((5, 0, 205))

        clique = pygame.mixer.Sound("clique_2.wav")
        seta = pygame.image.load("seta-removebg-preview.png")
        escreverLista(265, 300,'mainMenu')
        draw_text("O Jogo", font3, (225, 225, 225), screen, 70, 50)

        for event in pygame.event.get():
            fechartela(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == pygame.K_e:
                    if seta_px == 190 and seta_py == 420:
                        options()
                ativarFuncao(event, seta_px, seta_py, pygame.K_e, 190, 300)
                seta_py = moverSeta(event, seta_py, 300, 420, 120)

        escreverLista(265, 300,'mainMenu')
        screen.blit(seta, (seta_px, seta_py))
        pygame.display.update()
        mainClock.tick(60)

def moverX(keys, pos_x, vel):
    if keys[pygame.K_LEFT]:
        pos_x -= vel

    if keys[pygame.K_RIGHT]:
        pos_x += vel

    return pos_x

def moverY(keys, pos_y, vel):

    if keys[pygame.K_UP]:
        pos_y -= vel

    if keys[pygame.K_DOWN]:
        pos_y += vel

    return pos_y

def voltar(keys, çao):
    if keys[pygame.K_LEFT]:

        çao = 1

    if keys[pygame.K_RIGHT]:

        çao = 2

    if keys[pygame.K_UP]:

        çao = 3

    if keys[pygame.K_DOWN]:

        çao = 0
    return çao

def animacao(keys, anim, character, bd):

    if keys[pygame.K_LEFT]:
        anim += 1
        if anim == len(sprites[bd]['animImgLeft']):
            anim = 0
        character = pygame.image.load(sprites[bd]['animImgLeft'][anim])

    if keys[pygame.K_RIGHT]:
        anim += 1
        if anim == len(sprites[bd]['animImgRight']):
            anim = 0
        character = pygame.image.load(sprites[bd]['animImgRight'][anim])

    if keys[pygame.K_UP]:
        anim += 1
        if anim == len(sprites[bd]['animImgUP']):
            anim = 0

        character = pygame.image.load(sprites[bd]['animImgUP'][anim])

    if keys[pygame.K_DOWN]:
        anim += 1
        if anim == len(sprites[bd]['animImgDonw']):
            anim = 0
        character = pygame.image.load(sprites[bd]['animImgDonw'][anim])

    return character

def retornarAnim(anim, keys):
    if keys[pygame.K_LEFT]:
        anim += 1
        if anim == 4:
            anim = 0
    if keys[pygame.K_RIGHT]:
        anim += 1
        if anim == 4:
            anim = 0

    if keys[pygame.K_UP]:
        anim += 1
        if anim == 4:
            anim = 0

    if keys[pygame.K_DOWN]:
        anim += 1
        if anim == 4:
            anim = 0
    return anim

def moverSeta(event, seta_py, posLimitCima, posLimitbaixo, intervalo):
    if seta_py < posLimitCima+120:
        seta_py = seta_py + intervalo

    if event.key == pygame.K_DOWN:
        seta_py = seta_py + intervalo

    if seta_py > posLimitbaixo:
        seta_py = seta_py - intervalo

    if event.key == pygame.K_UP:
        seta_py = seta_py - intervalo

    return seta_py

def ativarFuncao(event, seta_px, seta_py, chaveEnter, posx ,posy):
    if event.key == chaveEnter:
        if seta_px == posx and seta_py == posy:
            game()

def fechartela(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
def carto():
    terrp = pygame.image.load("quart-fer.png")
    terrp = pygame.transform.scale(terrp, (900, 720))
    vel = 10
    anim = 0
    pos_x = 450 + 20
    pos_y = 500 - 50

    dire = [sprites['boy']['animImgDonw'], sprites['boy']['animImgLeft'],
            sprites['boy']['animImgRight'], sprites['boy']['animImgUP']]
    çao = 0

    voltar = range(410, 470)
    cara = pygame.image.load("cara_1.png")
    cara = pygame.transform.scale(cara, (60, 70))
    character = pygame.image.load("images\spritesTestes\imagem_4.png")
    screen.blit(terrp, (0, 0))
    screen.blit(character, (pos_x, pos_y))

    running = True
    while running:
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        character = pygame.image.load(dire[çao][0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pos_x = moverX(keys, pos_x, vel)
        pos_y = moverY(keys, pos_y, vel)

        character = animacao(keys, anim, character)

        çao = voltar(keys, çao)

        anim = retornarAnim(character, anim, keys)

        for tel in voltar:
            if pos_y == tel and pos_x == 510:
                running = False
                game()

        if pos_x >= 520:
            pos_x -= 10
        if pos_y <= 120:
            pos_y += 10
        if pos_x <= 180:
            pos_x += 10
        if pos_y >= 520:
            pos_y -= 10

        screen.blit(terrp, (0, 0))
        screen.blit(cara, (290, 230))
        screen.blit(character, (pos_x, pos_y))
        pygame.display.update()
        mainClock.tick(10)
        print(pos_y, pos_x)
        pygame.display.update()

def options():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text("options", font, (255, 255, 255), screen, 40, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

def battle():
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(10)

def game():
    vel = 10
    anim = 0
    pos_x = 340
    pos_y = 130
    spritePer = 'girl'
    dire = [sprites[spritePer]['animImgDonw'], sprites[spritePer]['animImgLeft'],
            sprites[spritePer]['animImgRight'], sprites[spritePer]['animImgUP']]
    çao = 0
    character = sprites[spritePer]['IdleDonw']
    screen.blit(spritesCenario['home'], (0, 0))
    screen.blit(character, (pos_x, pos_y))
    running = True
    while running:
        
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        character = pygame.image.load(dire[çao][0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_m:
                    GUI()
        pos_x = moverX(keys, pos_x, vel)
        pos_y = moverY(keys, pos_y, vel)
        character = animacao(keys, anim, character,spritePer)
        çao = voltar(keys, çao)
        anim = retornarAnim(anim, keys)
        character = pygame.transform.scale(character,(55, 75))
        pos_y = collisaBaixoHorizontal(vel, 'game', pos_x, pos_y)
        pos_y = collisaCimaHorizontal(vel, 'game', pos_x, pos_y)
        pos_x = collisaEsquerdaParedeVertical(vel, 'game', pos_x, pos_y)
        pos_x = collisaDireitaVertical(vel, 'game', pos_x, pos_y)
        screen.blit(spritesCenario['home'], (0, 0))
        screen.blit(character, (pos_x, pos_y))
        mainClock.tick(10)
        print(pos_y, pos_x)
        pygame.display.flip()

funcoesEnomesDeSelecao = {
    'mainMenu':[
        {'nome': 'start' },
        {'nome': 'options' },
    ]
}


def escreverLista(posx, posyInicial, bd):
    for i in range(len(funcoesEnomesDeSelecao[bd])):
        draw_text(funcoesEnomesDeSelecao[bd][i]['nome'], font2, (225,225,225),screen, posx,posyInicial)
        posyInicial = posyInicial+ 120

def GUI():
    o = True
    while o:

        screen.fill((5, 0, 205))
        draw_text("VIDA: ", font2, (225, 225, 225), screen, 44, 56)

        draw_text("Personagens ", font2, (225,225,225), screen, 644, 56)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    o = False

        pygame.display.flip()
        mainClock.tick(60)





main_menu()
