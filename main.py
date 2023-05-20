import pygame
pygame.init()

# --- DEFINIMOS LA LISTA ---
lista_imagenes = []
# --------------------------

# ----------- DEFINIR COLORES -----------
BLACK = (0, 0, 0)
BLUE = (52, 152, 219)
GAINSBORO = (220, 220, 220)
GREEN = (46, 204, 113)
LIGHTGRAY = (211, 211, 211)
RED = (231, 76, 60)
WHITE = (255, 255, 255)
#-----------------------------------------

# ------------- DEFINIR TEXTO -------------
FUENTE = pygame.font.SysFont('Calibri', 20)
NEGRILLA = pygame.font.SysFont('Calibri', 20, bold=True)
TEXTO = FUENTE.render('>>> Estado actual de la lista <<<', 1, BLACK)
TEXTO2 = FUENTE.render('Selecciona una imagen', 1, BLACK)
TEXTO3 = FUENTE.render('Opciones', 1, BLACK)
TITULO = NEGRILLA.render('SINGLE LINKED LIST', True, BLACK)
INFORMACION = NEGRILLA.render('Desarrollado por: Josue Franco Aguirre | SEM 3 - 2023 |', 1, BLACK)
#------------------------------------------

# ----------- MENÚ DE OPCIONES -----------
#                   X     Y   H    V
OPC1 = pygame.Rect(445, 270, 150, 40)
OPC2 = pygame.Rect(445, 315, 150, 40)
OPC3 = pygame.Rect(605, 270, 150, 40)
OPC4 = pygame.Rect(605, 315, 150, 40)
#-----------------------------------------

# --- COLORES INICIALES DE LOS CIRCULOS DE OPCIONES ---
circle1_color = BLACK  # Color inicial del círculo 1
circle2_color = BLACK  # Color inicial del círculo 2
circle3_color = BLACK  # Color inicial del círculo 3
# -----------------------------------------------------

# ----------- Cargar imagenes -----------
LOBO = pygame.image.load('lobo.png')
LOBO = pygame.transform.scale(LOBO, (100, 100))
TIBURON = pygame.image.load('tiburon.png')
TIBURON = pygame.transform.scale(TIBURON, (100, 100))
TIGRE = pygame.image.load('tigre.png')
TIGRE = pygame.transform.scale(TIGRE, (100, 100))
#-----------------------------------------

# --- Definir dimensiones de la pantalla ---
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PROYECTO")
#-----------------------------------------

# Iterar hasta que el usuario haga click sobre el boton cierre.
done = False
#-----------------------------------------

# --- SELECCIONAR IMAGEN ---
selected_image = None
# --------------------------

# Se usa para establecer cuan rapido se actualiza la pantalla
clock = pygame.time.Clock()
#-----------------------------------------

# -------- Bucle Principal del Programa --------
while not done:
    # --- Bucle Principal de Eventos
    for event in pygame.event.get(): # El usuario realizo alguna accion
        if event.type == pygame.QUIT: # Si el usuario hizo click sobre salir
            done = True # Marcamos como hecho y salimos de este bucle
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            
            if OPCIMG1.collidepoint(pygame.mouse.get_pos()):
                print('Seleccionaste el lobo')
                selected_image = LOBO
                circle1_color = BLUE   # Cambia el color del círculo 1 al seleccionar el lobo
                circle2_color = BLACK  # Restablece el color del círculo 2
                circle3_color = BLACK  # Restablece el color del círculo 3
            if OPCIMG2.collidepoint(pygame.mouse.get_pos()):
                print('Seleccionaste el tiburon')
                selected_image = TIBURON
                circle1_color = BLACK  # Restablece el color del círculo 1
                circle2_color = BLUE   # Cambia el color del círculo 2 al seleccionar el tiburón
                circle3_color = BLACK  # Restablece el color del círculo 3
            if OPCIMG3.collidepoint(pygame.mouse.get_pos()):
                print('Seleccionaste el tigre')
                selected_image = TIGRE
                circle1_color = BLACK  # Restablece el color del círculo 1
                circle2_color = BLACK  # Restablece el color del círculo 2
                circle3_color = BLUE   # Cambia el color del círculo 3 al seleccionar el tigre
            
            if OPC1.collidepoint(pygame.mouse.get_pos()):
                print('Añadir al inicio')
                lista_imagenes.insert(0, selected_image)
            if OPC2.collidepoint(pygame.mouse.get_pos()):
                print('Añadir al final')
                lista_imagenes.append(selected_image)
            if OPC3.collidepoint(pygame.mouse.get_pos()):
                print('Eliminar al inicio')
                lista_imagenes.remove(selected_image)
            if OPC4.collidepoint(pygame.mouse.get_pos()):
                print('Eliminar al final')
                lista_imagenes.pop()

    screen.fill([255, 255, 255])

    #--------- Textos e Imagenes ---------
    screen.blit(TEXTO, (80, 10))
    screen.blit(INFORMACION, (170, 560))
    screen.blit(TEXTO2, (510, 45))
    screen.blit(TEXTO3, (560, 220))
    screen.blit(TITULO, (515, 10))
    screen.blit(LOBO, (430, 90))
    screen.blit(TIBURON, (555, 80))
    screen.blit(TIGRE, (680, 90))
    #---------------------------------------

    # -----------------------------------------------------------------
    #                                    X    Y    H    V    G  B
    pygame.draw.rect(screen, GAINSBORO, (10, 40, 400, 500),  0, 30)
    # -----------------------------------------------------------------

    # --------------------------- CIRCULOS ----------------------------
    OPCIMG1 = pygame.draw.circle(screen, BLACK, (480, 135), 60, 1)
    OPCIMG2 = pygame.draw.circle(screen, BLACK, (605, 135), 60, 1) 
    OPCIMG3 = pygame.draw.circle(screen, BLACK, (730, 135), 60, 1)
    # -----------------------------------------------------------------

    # ------------------ BOTONES COLORES ------------------
    if OPC1.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, GREEN, OPC1, 0, 8)
    else:
        pygame.draw.rect(screen, LIGHTGRAY, OPC1, 0, 8)
    
    if OPC2.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, GREEN, OPC2, 0, 8)
    else:
        pygame.draw.rect(screen, LIGHTGRAY, OPC2, 0, 8)
    
    if OPC3.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, RED, OPC3, 0, 8)
    else:
        pygame.draw.rect(screen, LIGHTGRAY, OPC3, 0, 8)

    if OPC4.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, RED, OPC4, 0, 8)
    else:
        pygame.draw.rect(screen, LIGHTGRAY, OPC4, 0, 8)
    #--------------------------------------------------------

    # ------------------------------------------ TEXTO DE LOS BOTONES -------------------------------------------
    texto1 = FUENTE.render('Añadir al inicio', True, BLACK)
    screen.blit(texto1, (OPC1.x +(OPC1.width-texto1.get_width())/2, OPC1.y+(OPC1.height-texto1.get_height())/2))
    texto2 = FUENTE.render('Añadir al final', True, BLACK)
    screen.blit(texto2, (OPC2.x +(OPC2.width-texto2.get_width())/2, OPC2.y+(OPC2.height-texto2.get_height())/2))
    texto1 = FUENTE.render('Eliminar al inicio', True, BLACK)
    screen.blit(texto1, (OPC3.x +(OPC1.width-texto1.get_width())/2, OPC3.y+(OPC1.height-texto1.get_height())/2))
    texto2 = FUENTE.render('Eliminar al final', True, BLACK)
    screen.blit(texto2, (OPC4.x +(OPC2.width-texto2.get_width())/2, OPC4.y+(OPC2.height-texto2.get_height())/2))
    # -----------------------------------------------------------------------------------------------------------

    # ------------------------------------------------ DIBUJAR CIRCULO ------------------------------------------------
    pygame.draw.circle(screen, circle1_color, (480, 135), 60, 1)  # Dibuja el círculo 1 con el color correspondiente
    pygame.draw.circle(screen, circle2_color, (605, 135), 60, 1)  # Dibuja el círculo 2 con el color correspondiente
    pygame.draw.circle(screen, circle3_color, (730, 135), 60, 1)  # Dibuja el círculo 3 con el color correspondiente
    # -----------------------------------------------------------------------------------------------------------------

    # ----- DIBUJA LAS IMÁGENES EN LA LISTA -----
    for i, imagen in enumerate(lista_imagenes): # iterar sobre la lista lista_imagenes y obtener tanto el índice como el valor de cada elemento de la lista
        screen.blit(imagen, (150, 50 + i * 110))
    # -------------------------------------------

    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    clock.tick(60)
