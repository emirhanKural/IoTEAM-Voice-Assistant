import pyglet

animation = pyglet.image.load_animation('ezgif.com-gif-maker (3).gif')
animSprite = pyglet.sprite.Sprite(animation, x=130, y=38)

w = animSprite.width
h = animSprite.height

window = pyglet.window.Window(fullscreen=True)

r,g,b,alpha = 0,0,0,0

pyglet.gl.glClearColor(r,g,b,alpha)

@window.event
def on_draw():
    window.clear()
    animSprite.draw()

pyglet.app.run()
