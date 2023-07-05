"""
Title: Rotate and Bullets
Name: Jonah Honsberger
Date: 12/08/2022 [MM-DD-YYYY]
"""

"""
CONTROLS

Arrow Keys - Rotate Ship
Space - Shoot Bullets
"""

import math
import arcade

BULLET_SPEED = 5
MAX_BULLETS = 10
MAX_BULLET_FRAMES = 5


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.angle_speed = 0
        self.player_sprite = arcade.Sprite("character.png", 0.1)
        self.player_sprite.center_x = 800 / 2
        self.player_sprite.center_y = 600 / 2
        self.player_sprite.angle = 0
        self.bullet_list = arcade.SpriteList()
        self.fire_button = False
        self.frame_count = 0

    def on_draw(self):
        arcade.start_render()
        self.player_sprite.draw()
        if len(self.bullet_list) != 0:
            self.bullet_list.draw()

    def on_update(self, delta_time):
        self.player_sprite.angle += self.angle_speed
        self.frame_count += 1
        if self.frame_count == MAX_BULLET_FRAMES:
            self.frame_count = 0
            if self.fire_button and len(self.bullet_list) < MAX_BULLETS:
                self.spawn_bullet()

        for b in self.bullet_list:
            b.update()
            if b.center_x > 800 or b.center_y > 600 or b.center_x < 0 or b.center_y < 0:
                self.bullet_list.remove(b)

    def spawn_bullet(self):
        b = arcade.Sprite("bullet.png", 0.3)
        b.center_x = self.player_sprite.center_x + 70 * math.cos(math.radians(self.player_sprite.angle + 90))
        b.center_y = self.player_sprite.center_y + 70 * math.sin(math.radians(self.player_sprite.angle + 90))
        b.change_x = BULLET_SPEED * math.cos(math.radians(self.player_sprite.angle + 90))
        b.change_y = BULLET_SPEED * math.sin(math.radians(self.player_sprite.angle + 90))
        b.angle = self.player_sprite.angle + 155
        self.bullet_list.append(b)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.angle_speed = 1
        elif key == arcade.key.RIGHT:
            self.angle_speed = -1
        elif key == arcade.key.SPACE:
            self.fire_button = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.angle_speed = 0
        elif key == arcade.key.SPACE:
            self.fire_button = False


MyGame(800, 600, "rotate")
arcade.run()