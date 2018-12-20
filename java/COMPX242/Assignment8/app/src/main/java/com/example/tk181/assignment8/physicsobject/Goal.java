package com.example.tk181.assignment8.physicsobject;

import android.graphics.Canvas;
import com.example.tk181.assignment8.CustomColours;

// The targets that give you points when you hit them
public class Goal extends PhysicsObject{
    public Goal(int x, int y) {
        r = 75;
        this.x = x;
        this.y = y;
    }

    // Just some bools we want to track
    private boolean collectable = true;
    private boolean newGoalSpawnable = true;
    public void setCollectable(boolean collectable) {this.collectable = collectable;}
    public void setNewGoalSpawned() { newGoalSpawnable = false;}

    public boolean isCollectable() {return collectable;}
    public boolean isNewGoalSpawnable() {return newGoalSpawnable;}

    // Draws a target pattern
    @Override
    public void draw(Canvas c) {
        for (int i = 0; i < r/10; i++) {
            c.drawCircle(x, y, r - (10 * i),
                    i % 2 == 0 ? CustomColours.PAINT_GOAL_RED
                               : CustomColours.PAINT_GOAL_WHITE);
        }
    }
}
