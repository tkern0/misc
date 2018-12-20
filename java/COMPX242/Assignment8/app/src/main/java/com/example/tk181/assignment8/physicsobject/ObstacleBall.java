package com.example.tk181.assignment8.physicsobject;

import com.example.tk181.assignment8.CustomColours;
import java.util.Random;

/*
  The green balls that remove points when you hit them
  There are two sizes, both handled by this as everything else is the same
*/
public class ObstacleBall extends PhysicsObject {
    private boolean small;
    public ObstacleBall(int w) {
        // We don't want them to stop until they're offscreen
        FRICTION = 1;
        p = CustomColours.PAINT_OBSTACLE;

        Random rand = new Random();
        small = rand.nextInt(3) != 0;
        if (small) {
            r = 25;
            vy = 5;
        } else {
            r = 50;
            vy = 1;
        }

        x = rand.nextInt((int)(w - 2 * r)) + r;
        // Start at -100 so that there's a small delay when you start the game before they appear
        y = -100;
    }

    public boolean isSmall() {return small;}
}
