import tkinter
import pyautogui
import time
import keyboard
from tkinter import *
from tkinter.ttk import *
import random
import threading
t = tkinter.Tk()


def music():
   import winsound
   while gamerun == 1:
       winsound.Beep(100, 200)
       winsound.Beep(200, 200)
       winsound.Beep(300, 200)
       winsound.Beep(200, 400)
       winsound.Beep(200, 200)
       winsound.Beep(300, 200)
       winsound.Beep(100, 500)
       winsound.Beep(150, 200)
       winsound.Beep(200, 200)
       winsound.Beep(250, 200)
       winsound.Beep(300, 400)
       winsound.Beep(400, 200)
       if gamerun == 1:
           time.sleep(.5)
           winsound.Beep(100, 200)
           winsound.Beep(200, 200)
           winsound.Beep(300, 200)
           winsound.Beep(200, 400)
           winsound.Beep(200, 200)
           winsound.Beep(300, 200)
           winsound.Beep(100, 500)
           winsound.Beep(150, 200)
           winsound.Beep(200, 200)
           winsound.Beep(250, 200)
           winsound.Beep(300, 400)
           winsound.Beep(100, 200)
           time.sleep(.5)


t1 = threading.Thread(target=music, name='t1')
t1.start()


def stoppie2():
   global x
   global restartbut
   global EXIT
   global resume
   global Controls
   global ballrun
   ballrun = ballrun + 1
   if x % 2 == 0:
       restartbut = tkinter.Button(t, text="RESTART", bg='orange', command=restart, font=('Arial', 16), width=16)
       restartbut.place(x=width / 2 - 110, y=height / 2 - 120)
       EXIT = tkinter.Button(t, text="LEAVE", bg='red', command=leave, font=('Arial', 16), width=16)
       EXIT.place(x=width / 2 - 110, y=height / 2)
       resume = tkinter.Button(t, text="RESUME", bg='green', command=resume1, font=('Arial', 16), width=16)
       resume.place(x=width / 2 - 110, y=height / 2-240)
   else:
       restartbut.destroy()
       EXIT.destroy()
       resume.destroy()

   x = x + 1


def stoppie(event):
   global x
   global restartbut
   global EXIT
   global resume
   global Controls
   global ballrun
   ballrun = ballrun + 1
   if x % 2 == 0:
       restartbut = tkinter.Button(t, text="RESTART", bg='orange', command=restart, font=('Arial', 16), width=16)
       restartbut.place(x=width / 2 - 110, y=height / 2 - 120)
       EXIT = tkinter.Button(t, text="LEAVE", bg='red', command=leave, font=('Arial', 16), width=16)
       EXIT.place(x=width / 2 - 110, y=height / 2)
       resume = tkinter.Button(t, text="RESUME", bg='green', command=resume1, font=('Arial', 16), width=16)
       resume.place(x=width / 2 - 110, y=height / 2-240)

   else:
       restartbut.destroy()
       EXIT.destroy()
       resume.destroy()

   x = x + 1


def resume1():
   restartbut.destroy()
   EXIT.destroy()
   resume.destroy()


class app:
  def circle(self, r, x, y):
      return (x - r, y - r, x + r, y + r)


  def __init__(self, canvas, r, x, y, **kwargs):
      self.canvas = canvas
      self.r = r
      self.x = x
      self.y = y
      self.ball = canvas.create_oval(self.circle(r, x, y), **kwargs)


height = t.winfo_screenheight() - 90
height1 = t.winfo_screenheight()
width = t.winfo_screenwidth()
scoreleft = 0
scoreright = 0
redspeed = 10
momentud = random.randint(-5, 5)
ballrun = 0
gamerun = 1
print(width, height)
t.geometry(str(width) + "x" + str(height1))
t.resizable(True, False)
canvas = Canvas(t, width=width, height=height, bg='#1a1a1a')
ball1 = app(canvas, 40, 50, height/2, fill="blue")
ball2 = app(canvas, 40, (width - 40), (height/2), fill="red")
playball = app(canvas, 30, (width/2), (height/2), fill="green", outline='green')
canvas.place(x=-2, y=0)
scorel = tkinter.Button(t, bg='blue', text=scoreleft, font=('Arial', 16), width=4)
scorer = tkinter.Button(t, bg='red', text=scoreright, font=('Arial', 16), width=4)
scorer.place(x=(width/2) + 16, y=75)
scorel.place(x=(width/2) - 80, y=75)
slider = tkinter.Scale(t, from_=8, to=35, orient='horizontal', length=100, bg='green', label="speed")
slider.place(x=width/2, y=2)
slider2 = tkinter.Scale(t, from_=60, to=75, orient='horizontal', length=100, bg='green', label="hitbox")
slider2.place(x=width/2 -50 - 50, y=2)
diff = tkinter.Scale(t, from_=1, to=4, orient='horizontal', length=100, bg='orange', label="difficulty")
diff.place(x=width/2 - 50, y=height-80)
menu = tkinter.Button(t, text="=", width=4, bg="grey", command=stoppie2)
menu.place(x=width-100, y=20)
x = 0
o0 = random.randint(1, 2)
if o0 == 1:
  momentlr = slider.get()
else:
  momentlr = slider.get() - slider.get() * 2
hits = 0
hitcounter = tkinter.Button(t, text=("hits=" + str(hits)), width=8, font=('Arial', 16), bg='purple')
hitcounter.place(x=width - 228, y=20)


def restart():
   global momentud
   global scoreleft
   global scoreright
   global ball1
   global ball2
   global playball
   global canvas
   global scorel
   global scorer
   global slider
   global diff
   global momentlr
   global x
   global redspeed
   global menu
   global hits
   global gamerun
   height = t.winfo_screenheight() - 90
   height1 = t.winfo_screenheight()
   width = t.winfo_screenwidth()
   scoreleft = 0
   gamerun = 1
   scoreright = 0
   redspeed = 10
   momentud = random.randint(-5, 5)
   print(width, height)
   t.geometry(str(width) + "x" + str(height1))
   t.resizable(True, False)
   canvas = Canvas(t, width=width, height=height, bg='#1a1a1a')
   ball1 = app(canvas, 40, 50, height / 2, fill="blue")
   ball2 = app(canvas, 40, (width - 40), (height / 2), fill="red")
   playball = app(canvas, 30, (width / 2), (height / 2), fill="green", outline='green')
   canvas.place(x=-2, y=0)
   scorel = tkinter.Button(t, bg='blue', text=scoreleft, font=('Arial', 16), width=4)
   scorer = tkinter.Button(t, bg='red', text=scoreright, font=('Arial', 16), width=4)
   scorer.place(x=(width / 2) + 16, y=75)
   scorel.place(x=(width / 2) - 80, y=75)
   slider = tkinter.Scale(t, from_=8, to=35, orient='horizontal', length=100, bg='green', label="speed")
   slider.place(x=width / 2 - 50, y=2)
   diff = tkinter.Scale(t, from_=1, to=4, orient='horizontal', length=100, bg='orange', label="difficulty")
   diff.place(x=width / 2 - 50, y=height - 80)
   menu = tkinter.Button(t, text="=", width=4, bg="grey", command=stoppie2)
   menu.place(x=width - 100, y=20)
   ballrun = 0
   x = 0
   o0 = random.randint(1, 2)
   if o0 == 1:
       momentlr = slider.get()
   else:
       momentlr = slider.get() - slider.get() * 2
   hits = 0
   hitcounter = tkinter.Button(t, text=("hits=" + str(hits)), width=8, font=('Arial', 16), bg='purple')
   hitcounter.place(x=width - 228, y=20)


def hitreset():
   global hits
   global hitcounter
   hits = 0
   hitcounter = tkinter.Button(t, text=("hits=" + str(hits)), width=8, font=('Arial', 16), bg='purple')
   hitcounter.place(x=width - 228, y=20)


def hitsup():
   global hits
   global hitcounter
   hits = hits + 1
   hitcounter = tkinter.Button(t, text=("hits=" + str(hits)), width=8, font=('Arial', 16), bg='purple')
   hitcounter.place(x=width - 228, y=20)



def diffin():
   global redspeed
   global playball
   if diff.get() == 1:
      if momentlr > 0:
          er = random.randint(-2, 12)
          if er > 8:
              rdown()
          elif er < 2:
              rup()
          else:
              if playball.y > ball2.y:
                  rdown()
              elif playball.y < ball2.y:
                  rup()
          redspeed = 10
   elif diff.get() == 2:
      er = random.randint(0, 10)
      if er > 8:
          rdown()
      elif er < 2:
          rup()
      else:
          if playball.y > ball2.y + momentud:
              rdown()
          elif playball.y < ball2.y + momentud:
              rup()
      redspeed = 15
   elif diff.get() == 3:
      if playball.y > ball2.y + momentud:
          rdown()
      elif playball.y < ball2.y + momentud:
          rup()
      redspeed = 20
   elif diff.get() == 4:
       qer = (width-100) - playball.x
       if momentlr > 0:
           turnsleft = qer / momentlr
       else:
           turnsleft = qer / (momentlr - momentlr*2)
       estiy = turnsleft * momentud
       goto = estiy + playball.y
       if ball2.y > goto + 25:
           rup()
       elif ball2.y < goto - 25:
           rdown()
       redspeed = 25
   elif diff.get() == 5:
       redspeed = 15



def rscored():
   global scoreright
   global momentud
   global momentlr
   global scorer
   scoreright = scoreright + 1
   scorer = tkinter.Button(t, bg='red', text=scoreright, font=('Arial', 16), width=4)
   scorer.place(x=(width / 2) + 16, y=75)
   playball.x = width / 2
   playball.y = height / 2
   momentud = random.randint(-5, 5)
   ball1.y = height / 2
   canvas.delete(ball1.ball)
   ball1.ball = canvas.create_oval(ball1.circle(ball1.r, ball1.x, ball1.y), fill='blue', outline='pink')
   o0 = random.randint(1, 2)
   if o0 == 1:
       momentlr = slider.get() - slider.get() * 2
   else:
       momentlr = slider.get()
   hitreset()
   time.sleep(.5)



def lscored():
   global scoreleft
   global momentud
   global momentlr
   global scorel
   scoreleft = scoreleft + 1
   scorel = tkinter.Button(t, bg='blue', text=scoreleft, font=('Arial', 16), width=4)
   scorel.place(x=(width / 2) - 80, y=75)
   playball.x = width / 2
   playball.y = height / 2
   momentud = random.randint(-5, 5)
   ball2.y = height / 2
   canvas.delete(ball2.ball)
   ball2.ball = canvas.create_oval(ball1.circle(ball2.r, ball2.x, ball2.y), fill='red', outline='green')
   o0 = random.randint(1, 2)
   if o0 == 1:
       momentlr = slider.get() - slider.get() * 2
   else:
       momentlr = slider.get()
   hitreset()
   time.sleep(.5)


def up(event):
   canvas.delete(ball1.ball)
   ball1.y -= 10
   if ball1.y < 25:
       ball1.y = 0
   ball1.ball = canvas.create_oval(ball1.circle(ball1.r, ball1.x, ball1.y), fill='blue', outline='pink')


def down(event):
  canvas.delete(ball1.ball)
  ball1.y += 10
  if ball1.y > height:
      ball1.y = height
  ball1.ball = canvas.create_oval(ball1.circle(ball1.r, ball1.x, ball1.y), fill='blue', outline='pink')


def rdown():
   global redspeed
   if momentlr > -50:
      canvas.delete(ball2.ball)
      ball2.y += redspeed
      if ball2.y > height:
          ball2.y = height
      ball2.ball = canvas.create_oval(ball2.circle(ball2.r, ball2.x, ball2.y), fill='red', outline='green')


def rup():
   global redspeed
   if momentlr > -50:
      canvas.delete(ball2.ball)
      ball2.y -= redspeed
      if ball2.y < 25:
          ball2.y = 0
      ball2.ball = canvas.create_oval(ball2.circle(ball2.r, ball2.x, ball2.y), fill='red', outline='green')


def ballmove():
  global momentud
  global momentlr
  global scoreright
  global scoreleft
  global ballrun
  while ballrun % 2 != 0 and gamerun == 1:
      time.sleep(0.07)
      fishy = slider2.get()
      if scoreright == scoreleft:
          outie = "green"
      elif scoreright > scoreleft:
          outie = "red"
      else:
          outie = "blue"
      canvas.delete(playball.ball)
      playball.y = playball.y + momentud
      playball.x = playball.x + momentlr
      if playball.y > height or playball.y < 0:
          playball.y = playball.y - momentud
          momentud = momentud - momentud*2
      playball.ball = canvas.create_oval(playball.circle(playball.r, playball.x, playball.y), fill='green', outline=outie)
      if playball.x < 120 and playball.y in range((int(ball1.y) - fishy), int(ball1.y) + fishy):
          q = ball1.y - playball.y
          momentud = momentud - momentud*2 - q/2
          momentlr = slider.get()
          hitsup()
      elif playball.x < 25:
          rscored()
      if int(playball.x) > int(width) - 100 and int(playball.y) in range((int(ball2.y) - fishy), int(ball2.y) + fishy):
          q = ball2.y - playball.y
          momentud = momentud - momentud * 2 - q / 2
          momentlr = slider.get() - slider.get() * 2
          hitsup()
      elif playball.x > (width - 25):
          lscored()
      diffin()


def leave():
    global gamerun
    gamerun = 0
    t.destroy()


def r74(event):
    global ballrun
    ballrun = ballrun + 1
    t3 = threading.Thread(target=ballmove, name='t3')
    t3.start()


def binding():
    t.bind('<a>', r74)
    t.bind('<A>', r74)



t.bind('<w>', up)
t.bind('<W>', up)
t.bind('<S>', down)
t.bind('<s>', down)
t.bind('<q>', stoppie)
t.bind('<Q>', stoppie)

t2 = threading.Thread(target=binding, name='t2')
t2.start()


mainloop()







