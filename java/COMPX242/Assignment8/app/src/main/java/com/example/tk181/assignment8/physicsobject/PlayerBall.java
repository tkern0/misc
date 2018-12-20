package com.example.tk181.assignment8.physicsobject;

import com.example.tk181.assignment8.CustomColours;

// The ball the player controls
public class PlayerBall extends PhysicsObject {
    public PlayerBall() {
        r = 75;
        p = CustomColours.PAINT_PLAYER;
    }

    /*
      The ball needs to be accessed by every private class in GameActivity, so we have to define it
       in the main onCreate() method, meaning we don't have access to width/height yet
      When we do actually have access we can set the values through here
    */
    private int w, h;
    private int flingAreaMin;
    public void setScreenParams(int w, int h, int flingAreaMin){
        this.w = w;
        this.h = h;
        this.flingAreaMin = flingAreaMin;

        x = w/2;
        y = h - 200;
    }

    /*
      Wrapper functions to make sure flings and gravity only have effects on certain parts of the
       screen
    */
    public void fling(float x, float y) {
        if (this.y >= flingAreaMin) {
            super.setAccel(x, y);
        }
    }

    public void gravity(float x, float y) {
        if (this.y < flingAreaMin) {
            super.setAccel(x, y);
        }
    }

    // We want the ball to bounce of the edge of the screen so we have to overwrite this
    private float DAMPENING = 0.8f;
    @Override
    public void update() {
        super.update();

        if (x < r) {
            x = r;
            vx = -vx * DAMPENING;
            ax = 0;
        }
        if (x > w - r) {
            x = w - r;
            vx = -vx * DAMPENING;
            ax = 0;
        }
        if (y < r) {
            y = r;
            vy = -vy * DAMPENING;
            ay = 0;
        }
        if (y > h - r) {
            y = h - r;
            vy = -vy * DAMPENING;
            ay = 0;
        }
    }
}
