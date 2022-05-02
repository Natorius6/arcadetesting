"""
Platformer Game

python -m arcade.examples.platform_tutorial.11_animate_character
"""
import os
from re import S
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
TILE_SCALING = 2
SPRITE_PIXEL_SIZE = 16
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):
        """
        Initializer for the game
        """

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the path to start with this program
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)


        # Our TileMap Object
        self.tile_map = None

        # Our Scene Object
        self.scene = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # A Camera that can be used to draw GUI elements
        self.gui_camera = None

        self.end_of_map = 0

        self.arcade_machine = 0
        
        self.arcade_machines_x = []
        self.arcade_machines_y = []

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Map name
        map_name = "arcade_machine_testing.tmx"

        # Load in TileMap
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING)

        # Initiate New Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # Calculate the right edge of the my_map in pixels
        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        self.arcade_machine = 0

        self.arcade_machines_x = [0, 600]
        self.arcade_machines_y = [0, 0]

        # --- Other stuff
        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)


    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""
        if key == arcade.key.LEFT or key == arcade.key.A:
            if self.arcade_machine > 0:
                self.arcade_machine -= 1
            print(self.arcade_machine)
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.arcade_machine += 1
            print(self.arcade_machine)


    def center_camera_to_arcade_machine(self):
        screen_center_x = self.arcade_machines_x[self.arcade_machine]
        screen_center_y = self.arcade_machines_y[self.arcade_machine]
        centered = screen_center_x, screen_center_y

        self.camera.move_to(centered, 0.2)

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Position the camera
        self.center_camera_to_arcade_machine()


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()