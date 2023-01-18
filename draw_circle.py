import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)

    def on_draw(self):
        """
        C'est la méthode que Arcade invoque à chaque "frame" pour afficher les éléments
        de votre jeu à l'écran.
        """

        arcade.set_background_color(arcade.color.BABY_BLUE)
        arcade.start_render()

        arcade.draw_circle_filled(300, 300, 50, arcade.color.CASTLETON_GREEN)

        arcade.finish_render()


def main():
    window = MyGame(680, 420, "Drawing Example")
    window.run()


main()
