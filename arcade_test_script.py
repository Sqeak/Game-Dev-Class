import arcade
arcade.open_window(400, 200, "Arcade Test Script")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
arcade.draw_text("Welcome to Mr. Preston's Games Design class!",30, 100,arcade.color.BLACK, 14)
arcade.finish_render()
arcade.run()