import pyglet
from pyglet import gl, graphics, event, text
from pyglet.window import key
import itertools as it
import time
from collections import deque

window = pyglet.window.Window(width=450, height=450)


class ArrowSprite(object):

    def __init__(self, x=0, y=0, rot=0., color=(255, 255, 255, 255)):
        self.x = x
        self.y = y
        self.rot = rot
        self.rot_velocity = 150.0

        self.verts = [(-10, 0), (10, 0), (0, 150)]
        self.vertex_list = graphics.vertex_list(
                                len(self.verts),
                                ('v2f', list(it.chain(*self.verts))),
                                ('c4B', color * 3)
                                )

    def draw(self):
        gl.glPushMatrix()
        gl.glTranslatef(self.x, self.y, 0)
        gl.glRotatef(self.rot, 0, 0, 1)
        self.vertex_list.draw(gl.GL_TRIANGLES)
        gl.glPopMatrix()

    def update(self, dt):
        self.rot += self.rot_velocity * dt * 360.


arrow = ArrowSprite(x=window.width / 2., y=window.height / 2.)
ref_arrow = ArrowSprite(x=window.width / 2., y=window.height / 2., color=(255, 0, 0, 255))

fmt_str = 'Revs/Sec: {}'
speed_label = text.Label(text=fmt_str.format(arrow.rot_velocity), x=window.width / 2., y=window.height - 30, align='center',
                         font_size=14, anchor_x='center', anchor_y='baseline')

instruction_label = text.Label(text='Press Space on each robot rotation to update rotation speed estimate.',
                               font_size=8.5, x=10, y=10)

@window.event
def on_draw():
    window.clear()
    ref_arrow.draw()
    arrow.draw()
    speed_label.draw()
    instruction_label.draw()

speed_histories = deque(maxlen=5)

def update(dt):
    arrow.update(dt)
    print(speed_histories)
pyglet.clock.schedule(update)


prev_time = time.time()

@window.event
def on_key_press(mod, sym):
    global prev_time
    if key.SPACE == mod:
        curr_time = time.time()
        new_rot_vel_estimate = 1. / (curr_time - prev_time)
        speed_histories.append(new_rot_vel_estimate)
        arrow.rot_velocity = sum(speed_histories) / float(len(speed_histories))
        arrow.rot = 0.
        prev_time = curr_time
        speed_label.text = fmt_str.format(arrow.rot_velocity)

pyglet.app.run()

