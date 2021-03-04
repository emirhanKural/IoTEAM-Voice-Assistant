import pyglet
"""from __future__ import print_function
from PIL import Image

im = Image.open('eys.gif')
im.show()"""

animation = pyglet.image.load_animation('eys.gif')
animSprite = pyglet.sprite.Sprite(animation)

w = animSprite.width
h = animSprite.height

window = pyglet.window.Window(fullscreen=True)

r,g,b,alpha = 0.5,0.5,0.8,0.5

pyglet.gl.glClearColor(r,g,b,alpha)

@window.event
def on_draw():
    window.clear()
    animSprite.draw()

pyglet.app.run()
