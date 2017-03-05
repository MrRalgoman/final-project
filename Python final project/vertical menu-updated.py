# Play button
        GAME_DISP.fill(black)
        text("Pong", 100, white, DISP_W/2, 100)
        text("By Lucas and Shawn", 25, white, DISP_W/2, 175)
        button("Play", 40, black, (DISP_W/2)-100, (DISP_H/2)-40, 200, 50, "play")
        button("Quit", 40, black, (DISP_W/2)-100, (DISP_H/2)+60, 200, 50, "quit")
        button("High Scores", 40, black, (DISP_W/2)-150, (DISP_H/2)+160, 300, 50, "high scores" )
        pygame.display.update()
