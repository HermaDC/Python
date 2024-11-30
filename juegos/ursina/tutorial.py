from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

# Inicializar la aplicación
app = Ursina()

# Configuración inicial
window.title = 'Juego de Plataformas - Mejorado'
window.borderless = False
window.fullscreen = False
window.fps_counter.enabled = True

# Fondo del juego
background = Entity(model='quad', scale=(20, 10), texture='sky_default', z=10)

# Jugador con control de plataforma
player = PlatformerController2d(scale=(0.5, 0.5), color=color.orange, jump_height=2)

# Suelo
ground = Entity(model='quad', color=color.green, scale=(20, 1), position=(0, -2), collider='box')

# Plataformas
platforms = [
    Entity(model='quad', color=color.gray, scale=(3, 0.5), position=(-3, 0), collider='box'),
    Entity(model='quad', color=color.gray, scale=(3, 0.5), position=(3, 1), collider='box'),
    Entity(model='quad', color=color.gray, scale=(2, 0.5), position=(7, 2), collider='box'),
]

# Monedas
coins = [
    Entity(model='circle', color=color.yellow, scale=0.5, position=(-3, 1), collider='box'),
    Entity(model='circle', color=color.yellow, scale=0.5, position=(3, 2), collider='box'),
    Entity(model='circle', color=color.yellow, scale=0.5, position=(7, 3), collider='box'),
]

# Espadas
armas = [
    Entity(model='quad', color=color.white, texture='sword', scale=(0.3, 0.3), position=(-5, 1), collider='box')
]

# Variables globales
score = 120
has_sword = False
camera_zoomed_out = False
game_paused = False  # Flag para pausar el juego
score_text = Text(f"Puntos: {score}", position=(-0.25, 0.45), scale=2, origin=(0, 0))

# Sonidos
coin_sound = Audio('coin.wav', autoplay=False)
jump_sound = Audio('jump.wav', autoplay=False)
enemy_hit_sound = Audio('hit.wav', autoplay=False)

# Crear enemigos con velocidad personalizada
def create_enemy(position, speed=1):
    """Crea un enemigo con posición y velocidad personalizada."""
    enemy = Entity(model='quad', color=color.red, scale=(0.5, 0.5), position=position, collider='box')
    enemy.speed = speed
    return enemy

# Agregar enemigos con velocidades independientes
enemies = [
    create_enemy(position=(-5, -1), speed=1),
    create_enemy(position=(2, -1), speed=1.5),
]

def update():
    global score, has_sword, camera_zoomed_out, game_paused

    # Si el puntaje es mayor que 120, pausamos el juego
    if score > 120 and not game_paused:
        game_paused = True  # Pausar el juego
        camera.position = Vec3(0, 0, -20)  # Aleja la cámara para ver más
        camera.look_at(Vec3(0, 0, 0))      # Enfoca el origen
        camera.fov = 80                    # Ajusta el campo de visión (zoom)
        score_text.text += " - ¡Juego pausado!"  # Mensaje en pantalla
        x = player.x
        y = player.y
        player.position = Vec3(x, y, 0) 
        player.disable()
        # Detener sonidos si quieres
        coin_sound.stop()
        jump_sound.stop()
        enemy_hit_sound.stop()

    # Si el juego está pausado, no se realiza ninguna acción de actualización
    if game_paused:
        return  # Esta línea se mantiene para "pausar" el juego pero sin afectar el ciclo principal

    # Movimiento de enemigos
    for enemy in enemies:
        enemy.x += time.dt * enemy.speed
        if enemy.x > 6 or enemy.x < -4:  # Cambia dirección en los límites
            enemy.speed *= -1

    # Detectar colisiones con monedas
    for coin in coins[:]:
        if player.intersects(coin).hit:
            coin_sound.play()
            coins.remove(coin)
            destroy(coin, delay=0.1)
            score += 10
            score_text.text = f"Puntos: {score}"

    # Detectar colisiones con la espada
    for a in armas:
        if player.intersects(a).hit:
            has_sword = True
            armas.remove(a)
            destroy(a)
            score_text.text = f"Puntos: {score} - ¡Tienes la espada!"

    # Detectar colisiones con enemigos
    for enemy in enemies[:]:
        if player.intersects(enemy).hit:
            if has_sword:
                enemy_hit_sound.play()
                enemies.remove(enemy)
                destroy(enemy)
                score += 50
                score_text.text = f"Puntos: {score}"
            else:
                player.position = Vec3(0, 0, 0)  # Reinicia la posición del jugador

    # Salto del jugador
    if held_keys['space'] and player.grounded:
        jump_sound.play()

# Cámara dinámica
camera.add_script(SmoothFollow(target=player, offset=[0, 1, -20], speed=4))

# Ejecutar el juego
app.run()
