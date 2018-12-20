package com.example.tk181.assignment8.physicsobject;

import android.graphics.Canvas;
import android.graphics.Paint;

/*
  Parent class for all objects used in the game
  Tracks and models position, velocity, acceleration
  Also tracks radius, which allows that to change mid-game
*/
public class PhysicsObject {
    protected float FRICTION = 0.95f;
    protected float x;
    protected float y;
    protected float vx;
    protected float vy;
    protected float ax;
    protected float ay;
    protected float r;
    protected Paint p = new Paint();

    // Lots of getters/setters
    public void setPos(float x, float y) {
        this.x = x;
        this.y = y;
    }
    public void setVel(float x, float y) {
        vx = x;
        vy = y;
    }
    public void setAccel(float x, float y) {
        ax = x;
        ay = y;
    }
    public void setRadius(float r) {
        this.r = r;
    }

    public float getX() {return x;}
    public float getY() {return y;}
    public float getVx() {return vx;}
    public float getVy() {return vy;}
    public float getAx() {return ax;}
    public float getAy() {return ay;}
    public float getRadius() {return r;}

    public void update() {
        vx += ax;
        vy += ay;
        x += vx;
        y += vy;
        // This part can be removed by setting friction to 1
        ax *= FRICTION;
        ay *= FRICTION;
        vx *= FRICTION;
        vy *= FRICTION;
    }

    public void draw(Canvas c) {
        c.drawCircle(x, y, r, p);
    }

    // Quick helper functions
    public double getDistanceTo(double x, double y) {
        return Math.sqrt((Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2)));
    }
    public double getDistanceTo(PhysicsObject po) {
        return getDistanceTo(po.getX(), po.getY());
    }
}
