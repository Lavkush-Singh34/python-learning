# import random
# import time
# import turtle
#
# # ---------- SCREEN ----------
# screen = turtle.Screen()
# screen.setup(1.0, 1.0)
# screen.bgcolor("black")
# screen.title("2D Target Simulator")
# screen.tracer(0)
#
# # ---------- PLAYER ----------
# player = turtle.Turtle()
# player.shape("triangle")
# player.color("white")
# player.penup()
# player.setheading(90)
# player.goto(0, -300)
#
# # ---------- TARGET ----------
# target = turtle.Turtle()
# target.shape("circle")
# target.color("red")
# target.penup()
# target.goto(random.randint(-500, 500), 300)
#
# # ---------- BULLET ----------
# bullet = turtle.Turtle()
# bullet.shape("square")
# bullet.shapesize(0.5, 1)
# bullet.color("yellow")
# bullet.penup()
# bullet.hideturtle()
#
# bullet_active = False
# score = 0
#
# # ---------- SCORE ----------
# text = turtle.Turtle()
# text.hideturtle()
# text.color("white")
# text.penup()
# text.goto(-600, 350)
#
#
# def draw_score():
#     text.clear()
#     text.write(f"Score: {score}", font=("Arial", 20, "bold"))
#
#
# # ---------- MOVEMENT ----------
# def left():
#     x = player.xcor()
#     if x > -600:
#         player.setx(x - 30)
#
#
# def right():
#     x = player.xcor()
#     if x < 600:
#         player.setx(x + 30)
#
#
# # ---------- FIRE ----------
# def fire():
#     global bullet_active
#
#     if not bullet_active:
#         bullet_active = True
#         bullet.goto(player.xcor(), player.ycor() + 20)
#         bullet.showturtle()
#
#
# # ---------- CONTROLS ----------
# screen.listen()
# screen.onkeypress(left, "Left")
# screen.onkeypress(right, "Right")
# screen.onkeypress(fire, "space")
#
# draw_score()
#
# # ---------- GAME LOOP ----------
# while True:
#     # Move bullet
#     if bullet_active:
#         bullet.sety(bullet.ycor() + 25)
#
#         # Hit target
#         if bullet.distance(target) < 30:
#             score += 1
#             draw_score()
#
#             bullet.hideturtle()
#             bullet_active = False
#
#             target.goto(random.randint(-600, 600), random.randint(150, 350))
#
#         # Bullet leaves screen
#         elif bullet.ycor() > 400:
#             bullet.hideturtle()
#             bullet_active = False
#
#     # Move target
#     target.setx(target.xcor() + 4)
#
#     if target.xcor() > 600:
#         target.setx(-600)
#
#     screen.update()
#     time.sleep(0.02)


# import random
# import time
# import turtle
#
# # ---------- SCREEN ----------
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("2D Target Simulator")
# screen.tracer(0)
#
# root = screen.getcanvas().winfo_toplevel()
# root.attributes("-fullscreen", True)
#
# # Force Tkinter to calculate the actual screen size
# root.update_idletasks()
#
# W = screen.window_width()
# H = screen.window_height()
#
# print("Screen:", W, "x", H)
#
# # ---------- PLAYER ----------
# player = turtle.Turtle()
# player.shape("triangle")
# player.color("white")
# player.penup()
# player.setheading(90)
#
# player_y = -H / 2 + 100
# player.goto(0, player_y)
#
# # ---------- TARGET ----------
# target = turtle.Turtle()
# target.shape("circle")
# target.color("red")
# target.penup()
#
# target_x = random.randint(int(-W / 2 + 50), int(W / 2 - 50))
# target_y = H / 2 - 150
# target.goto(target_x, target_y)
#
# # ---------- BULLET ----------
# bullet = turtle.Turtle()
# bullet.shape("square")
# bullet.shapesize(0.5, 1)
# bullet.color("yellow")
# bullet.penup()
# bullet.hideturtle()
#
# bullet_active = False
# score = 0
#
# # ---------- SCORE ----------
# text = turtle.Turtle()
# text.hideturtle()
# text.color("white")
# text.penup()
#
# text.goto(-W / 2 + 20, H / 2 - 50)
#
#
# def draw_score():
#     text.clear()
#     text.write(f"Score: {score}", font=("Arial", 20, "bold"))
#
#
# # ---------- MOVEMENT ----------
# def left():
#     x = player.xcor()
#
#     if x > -W / 2 + 30:
#         player.setx(x - 30)
#
#
# def right():
#     x = player.xcor()
#
#     if x < W / 2 - 30:
#         player.setx(x + 30)
#
#
# # ---------- FIRE ----------
# def fire():
#     global bullet_active
#
#     if not bullet_active:
#         bullet_active = True
#
#         bullet.goto(player.xcor(), player.ycor() + 25)
#
#         bullet.showturtle()
#
#
# # ---------- CONTROLS ----------
# screen.listen()
#
# screen.onkeypress(left, "Left")
# screen.onkeypress(right, "Right")
# screen.onkeypress(fire, "space")
#
# draw_score()
#
# # ---------- GAME LOOP ----------
# while True:
#     # Move bullet
#     if bullet_active:
#         bullet.sety(bullet.ycor() + 30)
#
#         # Hit target
#         if bullet.distance(target) < 30:
#             score += 1
#             draw_score()
#
#             bullet.hideturtle()
#             bullet_active = False
#
#             target.goto(random.randint(int(-W / 2 + 50), int(W / 2 - 50)), H / 2 - 150)
#
#         # Bullet leaves screen
#         elif bullet.ycor() > H / 2:
#             bullet.hideturtle()
#             bullet_active = False
#
#     # Move target
#     target.setx(target.xcor() + 4)
#
#     if target.xcor() > W / 2:
#         target.setx(-W / 2)
#
#     screen.update()
#     time.sleep(0.02)


# import turtle
#
# screen = turtle.Screen()
# screen.bgcolor("black")
#
# root = screen.getcanvas().winfo_toplevel()
#
# # Get actual X11 display dimensions
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
#
# # Make the window exactly the display size
# root.geometry(f"{width}x{height}+0+0")
#
# # Fullscreen
# root.attributes("-fullscreen", True)
# root.update()

# Resize Turtle canvas
# canvas = screen.getcanvas()
# canvas.config(width=width, height=height)
#
# print("Display:", width, "x", height)
# print("Canvas:", canvas.winfo_width(), "x", canvas.winfo_height())
#
# t = turtle.Turtle()
# t.color("white")
# t.speed(0)
#
# # Draw a huge circle to test the available area
# t.circle(600)
#
# turtle.done()


# import math
# import random
# import turtle
# import tkinter as tk
#
# # =========================
# # FULLSCREEN TKINTER WINDOW
# # =========================
#
# root = tk.Tk()
# root.title("Turtle Shooting Game")
#
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
#
# root.geometry(f"{width}x{height}+0+0")
# root.attributes("-fullscreen", True)
#
# canvas = tk.Canvas(root, width=width, height=height, bg="black")
# canvas.pack(fill="both", expand=True)
#
# # =========================
# # TURTLE SCREEN
# # =========================
#
# screen = turtle.TurtleScreen(canvas)
# screen.bgcolor("black")
# screen.tracer(0)
#
# # =========================
# # PLAYER
# # =========================
#
# player = turtle.RawTurtle(screen)
# player.shape("triangle")
# player.color("cyan")
# player.penup()
# player.setheading(90)
# player.goto(0, -height // 2 + 80)
#
# # =========================
# # SCORE
# # =========================
#
# score = 0
#
# score_writer = turtle.RawTurtle(screen)
# score_writer.hideturtle()
# score_writer.color("white")
# score_writer.penup()
# score_writer.goto(-width // 2 + 30, height // 2 - 60)
#
#
# def show_score():
#     score_writer.clear()
#     score_writer.write(f"SCORE: {score}", font=("Arial", 24, "bold"))
#
#
# show_score()
#
# # =========================
# # BULLETS
# # =========================
#
# bullets = []
#
#
# def shoot():
#     bullet = turtle.RawTurtle(screen)
#     bullet.shape("square")
#     bullet.shapesize(stretch_wid=0.7, stretch_len=0.15)
#     bullet.color("yellow")
#     bullet.penup()
#
#     bullet.goto(player.xcor(), player.ycor() + 25)
#     bullets.append(bullet)
#
#
# # =========================
# # TARGETS
# # =========================
#
# targets = []
#
#
# def create_target():
#     target = turtle.RawTurtle(screen)
#
#     shapes = ["circle", "square", "triangle"]
#
#     target.shape(random.choice(shapes))
#     target.color(random.choice(["red", "orange", "magenta", "lime", "white"]))
#
#     target.penup()
#
#     x = random.randint(-width // 2 + 50, width // 2 - 50)
#
#     y = height // 2 + 50
#
#     target.goto(x, y)
#
#     targets.append(target)
#
#
# # =========================
# # PLAYER MOVEMENT
# # =========================
#
# player_speed = 35
#
#
# def move_left():
#     x = player.xcor() - player_speed
#
#     if x > -width // 2 + 40:
#         player.setx(x)
#
#
# def move_right():
#     x = player.xcor() + player_speed
#
#     if x < width // 2 - 40:
#         player.setx(x)
#
#
# # =========================
# # COLLISION
# # =========================
#
#
# def collision(a, b):
#     dx = a.xcor() - b.xcor()
#     dy = a.ycor() - b.ycor()
#
#     distance = math.sqrt(dx * dx + dy * dy)
#
#     return distance < 30
#
#
# # =========================
# # GAME OVER
# # =========================
#
# game_running = True
#
# game_over_writer = turtle.RawTurtle(screen)
# game_over_writer.hideturtle()
# game_over_writer.color("red")
#
#
# def game_over():
#     global game_running
#
#     game_running = False
#
#     game_over_writer.goto(0, 50)
#     game_over_writer.write("GAME OVER", align="center", font=("Arial", 50, "bold"))
#
#     game_over_writer.goto(0, -30)
#     game_over_writer.color("white")
#     game_over_writer.write(
#         f"Final Score: {score}", align="center", font=("Arial", 25, "normal")
#     )
#
#
# # =========================
# # GAME LOOP
# # =========================
#
# frame = 0
#
#
# def game_loop():
#     global frame, score
#
#     if not game_running:
#         return
#
#     frame += 1
#
#     # Create targets
#     if frame % 25 == 0:
#         create_target()
#
#     # Move bullets
#     for bullet in bullets[:]:
#         bullet.sety(bullet.ycor() + 45)
#
#         if bullet.ycor() > height // 2 + 50:
#             bullet.hideturtle()
#             bullets.remove(bullet)
#
#     # Move targets
#     target_speed = 5 + score * 0.05
#
#     for target in targets[:]:
#         target.sety(target.ycor() - target_speed)
#
#         # Target reached player
#         if target.ycor() < -height // 2 + 100:
#             game_over()
#             return
#
#         # Bullet collision
#         for bullet in bullets[:]:
#             if collision(bullet, target):
#                 bullet.hideturtle()
#                 target.hideturtle()
#
#                 if bullet in bullets:
#                     bullets.remove(bullet)
#
#                 if target in targets:
#                     targets.remove(target)
#
#                 score += 1
#                 show_score()
#
#                 break
#
#     screen.update()
#
#     root.after(16, game_loop)  # ~60 FPS
#
#
# # =========================
# # CONTROLS
# # =========================
#
# screen.listen()
#
# screen.onkeypress(move_left, "Left")
# screen.onkeypress(move_right, "Right")
#
# screen.onkeypress(move_left, "a")
# screen.onkeypress(move_right, "d")
#
# screen.onkeypress(shoot, "space")
#
#
# # ESC = exit fullscreen/game
# def quit_game():
#     root.destroy()
#
#
# root.bind("<Escape>", lambda event: quit_game())
#
# # =========================
# # START
# # =========================
#
# game_loop()
#
# root.mainloop()
#
#
#
# import tkinter as tk
# import turtle
# import random
# import math
# import time
#
# # ============================================================
# # WINDOW
# # ============================================================
#
# root = tk.Tk()
# root.title("Turtle Space Shooter")
#
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
#
# root.geometry(f"{width}x{height}+0+0")
# root.attributes("-fullscreen", True)
#
# canvas = tk.Canvas(root, width=width, height=height, bg="black", highlightthickness=0)
# canvas.pack(fill="both", expand=True)
#
# # ============================================================
# # TURTLE SCREEN
# # ============================================================
#
# screen = turtle.TurtleScreen(canvas)
# screen.bgcolor("black")
#
# # We manually control drawing.
# screen.tracer(0, 0)
#
# # ============================================================
# # GAME VARIABLES
# # ============================================================
#
# running = True
#
# score = 0
# frame = 0
#
# bullets = []
# targets = []
#
# # ============================================================
# # KEYBOARD STATE
# # ============================================================
#
# keys = {"left": False, "right": False, "shoot": False}
#
#
# def key_press(event):
#     key = event.keysym.lower()
#
#     if key in ("left", "a"):
#         keys["left"] = True
#
#     elif key in ("right", "d"):
#         keys["right"] = True
#
#     elif key == "space":
#         keys["shoot"] = True
#
#
# def key_release(event):
#     key = event.keysym.lower()
#
#     if key in ("left", "a"):
#         keys["left"] = False
#
#     elif key in ("right", "d"):
#         keys["right"] = False
#
#     elif key == "space":
#         keys["shoot"] = False
#
#
# canvas.bind("<KeyPress>", key_press)
# canvas.bind("<KeyRelease>", key_release)
#
# canvas.focus_set()
#
# # ============================================================
# # PLAYER
# # ============================================================
#
# player = turtle.RawTurtle(screen)
#
# player.shape("triangle")
# player.color("cyan")
#
# player.penup()
# player.setheading(90)
#
# player_x = 0
# player_y = -height / 2 + 100
#
# player.goto(player_x, player_y)
#
# # ============================================================
# # SCORE
# # ============================================================
#
# score_writer = turtle.RawTurtle(screen)
#
# score_writer.hideturtle()
# score_writer.penup()
# score_writer.color("white")
#
# score_writer.goto(-width / 2 + 30, height / 2 - 60)
#
#
# def update_score():
#
#     score_writer.clear()
#
#     score_writer.write(f"SCORE: {score}", font=("Arial", 24, "bold"))
#
#
# update_score()
#
# # ============================================================
# # GAME OVER TEXT
# # ============================================================
#
# game_over_writer = turtle.RawTurtle(screen)
#
# game_over_writer.hideturtle()
# game_over_writer.penup()
#
#
# def game_over():
#
#     global running
#
#     running = False
#
#     game_over_writer.color("red")
#
#     game_over_writer.goto(0, 60)
#
#     game_over_writer.write("GAME OVER", align="center", font=("Arial", 55, "bold"))
#
#     game_over_writer.color("white")
#
#     game_over_writer.goto(0, -20)
#
#     game_over_writer.write(
#         f"Score: {score}", align="center", font=("Arial", 28, "bold")
#     )
#
#     game_over_writer.goto(0, -70)
#
#     game_over_writer.write(
#         "Press R to restart    |    ESC to quit",
#         align="center",
#         font=("Arial", 18, "normal"),
#     )
#
#
# # ============================================================
# # BULLETS
# # ============================================================
#
#
# def shoot():
#
#     bullet = turtle.RawTurtle(screen)
#
#     bullet.shape("square")
#     bullet.shapesize(stretch_wid=0.8, stretch_len=0.15)
#
#     bullet.color("yellow")
#
#     bullet.penup()
#
#     bullet.goto(player.xcor(), player.ycor() + 25)
#
#     bullets.append(bullet)
#
#
# # ============================================================
# # TARGETS
# # ============================================================
#
#
# def create_target():
#
#     target = turtle.RawTurtle(screen)
#
#     target.shape(random.choice(["circle", "square", "triangle"]))
#
#     target.color(random.choice(["red", "orange", "magenta", "lime", "white"]))
#
#     target.penup()
#
#     x = random.randint(int(-width / 2 + 50), int(width / 2 - 50))
#
#     y = height / 2 + 50
#
#     target.goto(x, y)
#
#     targets.append(target)
#
#
# # ============================================================
# # COLLISION
# # ============================================================
#
#
# def collision(a, b):
#
#     dx = a.xcor() - b.xcor()
#     dy = a.ycor() - b.ycor()
#
#     return math.hypot(dx, dy) < 30
#
#
# # ============================================================
# # SHOOTING CONTROL
# # ============================================================
#
# shoot_timer = 0
#
# # milliseconds between shots
# SHOOT_DELAY = 90
#
#
# # ============================================================
# # TIME CONTROL
# # ============================================================
#
# last_time = time.perf_counter()
#
# # ============================================================
# # MAIN GAME LOOP
# # ============================================================
#
#
# def game_loop():
#
#     global frame
#     global score
#     global shoot_timer
#     global last_time
#
#     if not running:
#         return
#
#     # --------------------------------------------------------
#     # DELTA TIME
#     # --------------------------------------------------------
#
#     now = time.perf_counter()
#
#     dt = now - last_time
#     last_time = now
#
#     # Prevent huge jumps if Android pauses the window
#     dt = min(dt, 0.05)
#
#     frame += 1
#
#     # --------------------------------------------------------
#     # PLAYER MOVEMENT
#     # --------------------------------------------------------
#
#     PLAYER_SPEED = 750
#
#     if keys["left"]:
#         player.setx(player.xcor() - PLAYER_SPEED * dt)
#
#     if keys["right"]:
#         player.setx(player.xcor() + PLAYER_SPEED * dt)
#
#     # Keep player inside screen
#
#     left_limit = -width / 2 + 40
#     right_limit = width / 2 - 40
#
#     if player.xcor() < left_limit:
#         player.setx(left_limit)
#
#     if player.xcor() > right_limit:
#         player.setx(right_limit)
#
#     # --------------------------------------------------------
#     # SHOOTING
#     # --------------------------------------------------------
#
#     shoot_timer -= dt
#
#     if keys["shoot"] and shoot_timer <= 0:
#         shoot()
#
#         shoot_timer = SHOOT_DELAY / 1000
#
#     # --------------------------------------------------------
#     # CREATE ENEMIES
#     # --------------------------------------------------------
#
#     # Start slowly
#     spawn_interval = max(12, int(28 - score * 0.15))
#
#     if frame % spawn_interval == 0:
#         create_target()
#
#     # --------------------------------------------------------
#     # MOVE BULLETS
#     # --------------------------------------------------------
#
#     BULLET_SPEED = 1400
#
#     for bullet in bullets[:]:
#         bullet.sety(bullet.ycor() + BULLET_SPEED * dt)
#
#         if bullet.ycor() > height / 2 + 100:
#             bullet.hideturtle()
#
#             if bullet in bullets:
#                 bullets.remove(bullet)
#
#     # --------------------------------------------------------
#     # MOVE TARGETS
#     # --------------------------------------------------------
#
#     TARGET_SPEED = 300 + score * 3
#
#     for target in targets[:]:
#         target.sety(target.ycor() - TARGET_SPEED * dt)
#
#         # Enemy reached bottom
#
#         if target.ycor() < -height / 2 + 80:
#             target.hideturtle()
#
#             if target in targets:
#                 targets.remove(target)
#
#             game_over()
#
#             return
#
#         # ----------------------------------------------------
#         # BULLET COLLISION
#         # ----------------------------------------------------
#
#         for bullet in bullets[:]:
#             if collision(bullet, target):
#                 bullet.hideturtle()
#                 target.hideturtle()
#
#                 if bullet in bullets:
#                     bullets.remove(bullet)
#
#                 if target in targets:
#                     targets.remove(target)
#
#                 score += 1
#
#                 update_score()
#
#                 break
#
#     # --------------------------------------------------------
#     # DRAW
#     # --------------------------------------------------------
#
#     screen.update()
#
#     # --------------------------------------------------------
#     # NEXT FRAME
#     # --------------------------------------------------------
#
#     root.after(8, game_loop)
#
#
# # ============================================================
# # RESTART
# # ============================================================
#
#
# def restart(event=None):
#
#     global running
#     global score
#     global frame
#     global shoot_timer
#     global last_time
#
#     # Remove bullets
#
#     for bullet in bullets:
#         bullet.hideturtle()
#
#     bullets.clear()
#
#     # Remove enemies
#
#     for target in targets:
#         target.hideturtle()
#
#     targets.clear()
#
#     # Reset player
#
#     player.goto(0, -height / 2 + 100)
#
#     # Reset score
#
#     score = 0
#     frame = 0
#
#     shoot_timer = 0
#
#     score_writer.clear()
#
#     update_score()
#
#     game_over_writer.clear()
#
#     running = True
#
#     last_time = time.perf_counter()
#
#     game_loop()
#
#
# # ============================================================
# # ESCAPE
# # ============================================================
#
#
# def quit_game(event=None):
#
#     global running
#
#     running = False
#
#     root.destroy()
#
#
# # ============================================================
# # EXTRA KEYS
# # ============================================================
#
# canvas.bind("<KeyPress-r>", restart)
# canvas.bind("<KeyPress-R>", restart)
#
# canvas.bind("<Escape>", quit_game)
#
# # ============================================================
# # START
# # ============================================================
#
# canvas.focus_force()
#
# screen.update()
#
# game_loop()
#
# root.mainloop()
#
#
# import tkinter as tk
# import turtle
# import random
# import math
# import time
#
# # ============================================================
# # FULLSCREEN WINDOW
# # ============================================================
#
# root = tk.Tk()
# root.title("Turtle Shooter")
#
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
#
# root.geometry(f"{width}x{height}+0+0")
# root.attributes("-fullscreen", True)
#
# canvas = tk.Canvas(root, width=width, height=height, bg="black", highlightthickness=0)
#
# canvas.pack(fill="both", expand=True)
#
# # ============================================================
# # TURTLE
# # ============================================================
#
# screen = turtle.TurtleScreen(canvas)
# screen.bgcolor("black")
# screen.tracer(0, 0)
#
# # ============================================================
# # GAME STATE
# # ============================================================
#
# running = True
# score = 0
# frame = 0
#
# bullets = []
# targets = []
#
# keys = {"left": False, "right": False, "shoot": False}
#
# # ============================================================
# # KEYBOARD
# # ============================================================
#
#
# def key_down(event):
#
#     k = event.keysym.lower()
#
#     if k in ("left", "a"):
#         keys["left"] = True
#
#     elif k in ("right", "d"):
#         keys["right"] = True
#
#     elif k == "space":
#         # Immediately fire when Space is pressed
#         keys["shoot"] = True
#
#         if running:
#             fire()
#
#
# def key_up(event):
#
#     k = event.keysym.lower()
#
#     if k in ("left", "a"):
#         keys["left"] = False
#
#     elif k in ("right", "d"):
#         keys["right"] = False
#
#     elif k == "space":
#         keys["shoot"] = False
#
#
# # IMPORTANT:
# # bind_all catches keyboard input throughout the application.
#
# root.bind_all("<KeyPress>", key_down)
# root.bind_all("<KeyRelease>", key_up)
#
# # ============================================================
# # PLAYER
# # ============================================================
#
# player = turtle.RawTurtle(screen)
#
# player.shape("triangle")
# player.color("cyan")
#
# player.penup()
# player.setheading(90)
#
# player.goto(0, -height / 2 + 100)
#
# # ============================================================
# # SCORE
# # ============================================================
#
# score_writer = turtle.RawTurtle(screen)
#
# score_writer.hideturtle()
# score_writer.penup()
# score_writer.color("white")
#
# score_writer.goto(-width / 2 + 30, height / 2 - 60)
#
#
# def update_score():
#
#     score_writer.clear()
#
#     score_writer.write(f"SCORE: {score}", font=("Arial", 24, "bold"))
#
#
# update_score()
#
# # ============================================================
# # BULLETS
# # ============================================================
#
#
# def fire():
#
#     bullet = turtle.RawTurtle(screen)
#
#     bullet.shape("square")
#
#     bullet.shapesize(stretch_wid=0.8, stretch_len=0.18)
#
#     bullet.color("yellow")
#
#     bullet.penup()
#
#     bullet.goto(player.xcor(), player.ycor() + 25)
#
#     bullets.append(bullet)
#
#
# # ============================================================
# # ENEMIES
# # ============================================================
#
#
# def create_target():
#
#     target = turtle.RawTurtle(screen)
#
#     target.shape(random.choice(["circle", "square", "triangle"]))
#
#     target.color(random.choice(["red", "orange", "magenta", "lime", "white"]))
#
#     target.penup()
#
#     x = random.randint(int(-width / 2 + 50), int(width / 2 - 50))
#
#     target.goto(x, height / 2 + 50)
#
#     targets.append(target)
#
#
# # ============================================================
# # COLLISION
# # ============================================================
#
#
# def hit(a, b):
#
#     dx = a.xcor() - b.xcor()
#     dy = a.ycor() - b.ycor()
#
#     return math.hypot(dx, dy) < 30
#
#
# # ============================================================
# # GAME OVER
# # ============================================================
#
# game_over_text = turtle.RawTurtle(screen)
#
# game_over_text.hideturtle()
# game_over_text.penup()
#
#
# def game_over():
#
#     global running
#
#     running = False
#
#     game_over_text.color("red")
#
#     game_over_text.goto(0, 60)
#
#     game_over_text.write("GAME OVER", align="center", font=("Arial", 55, "bold"))
#
#     game_over_text.color("white")
#
#     game_over_text.goto(0, -10)
#
#     game_over_text.write(f"Score: {score}", align="center", font=("Arial", 28, "bold"))
#
#     game_over_text.goto(0, -60)
#
#     game_over_text.write(
#         "Press R to restart", align="center", font=("Arial", 20, "normal")
#     )
#
#
# # ============================================================
# # SHOOTING
# # ============================================================
#
# SHOT_INTERVAL = 0.10
# last_shot = 0
#
#
# # ============================================================
# # GAME LOOP
# # ============================================================
#
# last_time = time.perf_counter()
#
#
# def game_loop():
#
#     global frame
#     global score
#     global last_time
#     global last_shot
#
#     if not running:
#         return
#
#     now = time.perf_counter()
#
#     dt = now - last_time
#     last_time = now
#
#     # Protect against huge jumps
#     dt = min(dt, 0.05)
#
#     frame += 1
#
#     # ========================================================
#     # PLAYER
#     # ========================================================
#
#     PLAYER_SPEED = 850
#
#     if keys["left"]:
#         player.setx(player.xcor() - PLAYER_SPEED * dt)
#
#     if keys["right"]:
#         player.setx(player.xcor() + PLAYER_SPEED * dt)
#
#     # Screen boundaries
#
#     if player.xcor() < -width / 2 + 40:
#         player.setx(-width / 2 + 40)
#
#     if player.xcor() > width / 2 - 40:
#         player.setx(width / 2 - 40)
#
#     # ========================================================
#     # CONTINUOUS FIRE
#     # ========================================================
#
#     if keys["shoot"]:
#         if now - last_shot >= SHOT_INTERVAL:
#             fire()
#
#             last_shot = now
#
#     # ========================================================
#     # SPAWN ENEMIES
#     # ========================================================
#
#     spawn_rate = max(12, int(30 - score * 0.15))
#
#     if frame % spawn_rate == 0:
#         create_target()
#
#     # ========================================================
#     # BULLETS
#     # ========================================================
#
#     BULLET_SPEED = 1500
#
#     for bullet in bullets[:]:
#         bullet.sety(bullet.ycor() + BULLET_SPEED * dt)
#
#         if bullet.ycor() > height / 2 + 100:
#             bullet.hideturtle()
#
#             bullets.remove(bullet)
#
#     # ========================================================
#     # ENEMIES
#     # ========================================================
#
#     ENEMY_SPEED = 280 + score * 4
#
#     for target in targets[:]:
#         target.sety(target.ycor() - ENEMY_SPEED * dt)
#
#         # Enemy reached bottom
#
#         if target.ycor() < -height / 2 + 70:
#             target.hideturtle()
#
#             targets.remove(target)
#
#             game_over()
#
#             return
#
#         # ====================================================
#         # BULLET COLLISION
#         # ====================================================
#
#         for bullet in bullets[:]:
#             if hit(bullet, target):
#                 bullet.hideturtle()
#                 target.hideturtle()
#
#                 if bullet in bullets:
#                     bullets.remove(bullet)
#
#                 if target in targets:
#                     targets.remove(target)
#
#                 score += 1
#
#                 update_score()
#
#                 break
#
#     # ========================================================
#     # DRAW
#     # ========================================================
#
#     screen.update()
#
#     # 120 FPS target
#     root.after(8, game_loop)
#
#
# # ============================================================
# # RESTART
# # ============================================================
#
#
# def restart(event=None):
#
#     global running
#     global score
#     global frame
#     global last_shot
#     global last_time
#
#     for bullet in bullets:
#         bullet.hideturtle()
#
#     bullets.clear()
#
#     for target in targets:
#         target.hideturtle()
#
#     targets.clear()
#
#     player.goto(0, -height / 2 + 100)
#
#     score = 0
#     frame = 0
#     last_shot = 0
#
#     game_over_text.clear()
#
#     update_score()
#
#     running = True
#
#     last_time = time.perf_counter()
#
#     game_loop()
#
#
# root.bind_all("<KeyPress-r>", restart)
# root.bind_all("<KeyPress-R>", restart)
#
# # ============================================================
# # ESC
# # ============================================================
#
#
# def quit_game(event=None):
#
#     root.destroy()
#
#
# root.bind_all("<Escape>", quit_game)
#
# # ============================================================
# # START
# # ============================================================
#
# root.focus_force()
#
# screen.update()
#
# game_loop()
#
# root.mainloop()
#
#
import tkinter as tk
import turtle
import random
import math
import time

# ============================================================
# WINDOW
# ============================================================

root = tk.Tk()
root.title("Turtle Shooter")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.geometry(f"{width}x{height}+0+0")
root.attributes("-fullscreen", True)

canvas = tk.Canvas(root, width=width, height=height, bg="black", highlightthickness=0)

canvas.pack(fill="both", expand=True)

# ============================================================
# TURTLE
# ============================================================

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("black")
screen.tracer(0, 0)

# ============================================================
# GAME VARIABLES
# ============================================================

running = True

score = 0
frame = 0

bullets = []
targets = []

# ============================================================
# CONTROL STATE
# ============================================================

left_held = False
right_held = False

# IMPORTANT:
# This does NOT depend on Space remaining held.
firing = False

# ============================================================
# PLAYER
# ============================================================

player = turtle.RawTurtle(screen)

player.shape("triangle")
player.color("cyan")
player.penup()
player.setheading(90)

player.goto(0, -height / 2 + 100)

# ============================================================
# SCORE
# ============================================================

score_writer = turtle.RawTurtle(screen)

score_writer.hideturtle()
score_writer.penup()
score_writer.color("white")

score_writer.goto(-width / 2 + 30, height / 2 - 60)


def update_score():

    score_writer.clear()

    score_writer.write(f"SCORE: {score}", font=("Arial", 24, "bold"))


update_score()

# ============================================================
# FIRE
# ============================================================


def fire():

    bullet = turtle.RawTurtle(screen)

    bullet.shape("square")

    bullet.shapesize(stretch_wid=0.8, stretch_len=0.18)

    bullet.color("yellow")

    bullet.penup()

    bullet.goto(player.xcor(), player.ycor() + 25)

    bullets.append(bullet)


# ============================================================
# KEYBOARD
# ============================================================


def key_down(event):

    global left_held
    global right_held
    global firing

    key = event.keysym.lower()

    # LEFT
    if key == "left" or key == "a":
        left_held = True

    # RIGHT
    elif key == "right" or key == "d":
        right_held = True

    # SPACE
    elif key == "space":
        # Toggle firing.
        firing = not firing

        # Shoot IMMEDIATELY when turned on.
        if firing and running:
            fire()


def key_up(event):

    global left_held
    global right_held

    key = event.keysym.lower()

    if key == "left" or key == "a":
        left_held = False

    elif key == "right" or key == "d":
        right_held = False


root.bind_all("<KeyPress>", key_down)
root.bind_all("<KeyRelease>", key_up)

# ============================================================
# ENEMIES
# ============================================================


def create_target():

    target = turtle.RawTurtle(screen)

    target.shape(random.choice(["circle", "square", "triangle"]))

    target.color(random.choice(["red", "orange", "magenta", "lime", "white"]))

    target.penup()

    x = random.randint(int(-width / 2 + 50), int(width / 2 - 50))

    target.goto(x, height / 2 + 50)

    targets.append(target)


# ============================================================
# COLLISION
# ============================================================


def hit(a, b):

    dx = a.xcor() - b.xcor()
    dy = a.ycor() - b.ycor()

    return math.hypot(dx, dy) < 30


# ============================================================
# GAME OVER
# ============================================================

game_over_text = turtle.RawTurtle(screen)

game_over_text.hideturtle()
game_over_text.penup()


def game_over():

    global running
    global firing

    running = False
    firing = False

    game_over_text.color("red")

    game_over_text.goto(0, 60)

    game_over_text.write("GAME OVER", align="center", font=("Arial", 55, "bold"))

    game_over_text.color("white")

    game_over_text.goto(0, -10)

    game_over_text.write(f"Score: {score}", align="center", font=("Arial", 28, "bold"))

    game_over_text.goto(0, -60)

    game_over_text.write(
        "Press R to restart", align="center", font=("Arial", 20, "normal")
    )


# ============================================================
# TIMING
# ============================================================

SHOT_INTERVAL = 0.09

last_shot = 0
last_time = time.perf_counter()


# ============================================================
# GAME LOOP
# ============================================================


def game_loop():

    global frame
    global score
    global last_time
    global last_shot

    if not running:
        return

    now = time.perf_counter()

    dt = now - last_time
    last_time = now

    # Prevent massive jumps after Android pauses the app.
    dt = min(dt, 0.05)

    frame += 1

    # ========================================================
    # PLAYER MOVEMENT
    # ========================================================

    PLAYER_SPEED = 900

    if left_held:
        player.setx(player.xcor() - PLAYER_SPEED * dt)

    if right_held:
        player.setx(player.xcor() + PLAYER_SPEED * dt)

    # Boundaries

    if player.xcor() < -width / 2 + 40:
        player.setx(-width / 2 + 40)

    if player.xcor() > width / 2 - 40:
        player.setx(width / 2 - 40)

    # ========================================================
    # AUTO FIRE
    # ========================================================

    if firing:
        if now - last_shot >= SHOT_INTERVAL:
            fire()

            last_shot = now

    # ========================================================
    # SPAWN ENEMIES
    # ========================================================

    spawn_rate = max(10, int(28 - score * 0.12))

    if frame % spawn_rate == 0:
        create_target()

    # ========================================================
    # BULLETS
    # ========================================================

    BULLET_SPEED = 1500

    for bullet in bullets[:]:
        bullet.sety(bullet.ycor() + BULLET_SPEED * dt)

        if bullet.ycor() > height / 2 + 100:
            bullet.hideturtle()
            bullets.remove(bullet)

    # ========================================================
    # ENEMIES
    # ========================================================

    ENEMY_SPEED = 280 + score * 4

    for target in targets[:]:
        target.sety(target.ycor() - ENEMY_SPEED * dt)

        if target.ycor() < -height / 2 + 70:
            target.hideturtle()
            targets.remove(target)

            game_over()

            return

        # ====================================================
        # COLLISION
        # ====================================================

        for bullet in bullets[:]:
            if hit(bullet, target):
                bullet.hideturtle()
                target.hideturtle()

                if bullet in bullets:
                    bullets.remove(bullet)

                if target in targets:
                    targets.remove(target)

                score += 1

                update_score()

                break

    # ========================================================
    # DRAW
    # ========================================================

    screen.update()

    # ~120 FPS
    root.after(8, game_loop)


# ============================================================
# RESTART
# ============================================================


def restart(event=None):

    global running
    global score
    global frame
    global firing
    global last_shot
    global last_time

    for bullet in bullets:
        bullet.hideturtle()

    bullets.clear()

    for target in targets:
        target.hideturtle()

    targets.clear()

    player.goto(0, -height / 2 + 100)

    score = 0
    frame = 0

    firing = False

    last_shot = 0

    game_over_text.clear()

    update_score()

    running = True

    last_time = time.perf_counter()

    game_loop()


root.bind_all("<KeyPress-r>", restart)
root.bind_all("<KeyPress-R>", restart)

# ============================================================
# ESCAPE
# ============================================================


def quit_game(event=None):

    root.destroy()


root.bind_all("<Escape>", quit_game)

# ============================================================
# START
# ============================================================

canvas.focus_force()

screen.update()

game_loop()

root.mainloop()
