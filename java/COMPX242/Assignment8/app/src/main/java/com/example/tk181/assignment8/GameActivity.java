package com.example.tk181.assignment8;

import android.content.Context;
import android.content.Intent;
import android.graphics.Canvas;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.CountDownTimer;
import android.support.constraint.ConstraintLayout;
import android.support.constraint.ConstraintSet;
import android.support.v4.view.GestureDetectorCompat;
import android.os.Bundle;
import android.util.DisplayMetrics;
import android.view.GestureDetector;
import android.view.MotionEvent;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.example.tk181.assignment8.physicsobject.Goal;
import com.example.tk181.assignment8.physicsobject.ObstacleBall;
import com.example.tk181.assignment8.physicsobject.PlayerBall;

import java.util.ArrayList;
import java.util.Random;

// The main activity for the actual game
public class GameActivity extends FullScreenActivity {
    private float GRAV_MULTIPLIER = 0.2f;
    private float FLING_MULTIPLIER = 0.0015f;
    private float OBSTACLE_CHANCE = 0.0025f;

    // Fling gesture listener
    GestureDetectorCompat gestureDetector;
    MyGestureListener gestureListener;
    private class MyGestureListener implements GestureDetector.OnGestureListener {
        @Override
        public boolean onDown(MotionEvent e) {return false;}
        @Override
        public void onShowPress(MotionEvent e) {}
        @Override
        public boolean onSingleTapUp(MotionEvent e) {return false;}
        @Override
        public boolean onScroll(MotionEvent e1, MotionEvent e2, float distanceX, float distanceY) {return false;}
        @Override
        public void onLongPress(MotionEvent e) {}
        @Override
        public boolean onFling(MotionEvent e1, MotionEvent e2, float velocityX, float velocityY) {
            /*
              'e1' contains the initial position, make sure this is on the player ball
              If the player ball radius gets too small it becomes extremely difficult to get a fling
               close enough, so we make sure withing 30 pixels is always fine
              This value may need to be adjusted for other pixel densities
            */
            if (pb.getDistanceTo(e1.getX(), e1.getY()) < Math.max(30, pb.getRadius())) {
                pb.fling(velocityX * FLING_MULTIPLIER, velocityY * FLING_MULTIPLIER);
            }
            return false;
        }
    }

    // The main view controlling the game
    private class GraphicsView extends View {
        Context ctx;
        Random rand;
        int w, h;
        int flingAreaMin;

        ArrayList<Goal> goals;
        ArrayList<ObstacleBall> obstacles;

        public GraphicsView(Context ctx) {
            super(ctx);
            this.ctx = ctx;

            // Get display width + height
            DisplayMetrics metrics = ctx.getResources().getDisplayMetrics();
            w = metrics.widthPixels;
            h = metrics.heightPixels;

            flingAreaMin = (int) (h * 0.66);

            // Setup our PhysicsObjects
            pb.setPos(w/2, h-200);
            pb.setScreenParams(w, h, flingAreaMin);

            goals = new ArrayList<>();
            goals.add(new Goal(w/2, 200));

            rand = new Random();
            obstacles = new ArrayList<>();
        }

        // Update the physics and redraw the whole game
        @Override
        protected void onDraw(Canvas canvas) {
            super.onDraw(canvas);

            // Draw a visual indication of where the ball is controlled by flings
            canvas.drawRect(0, flingAreaMin, w, h, CustomColours.PAINT_FLING_AREA);

            // The player ball gradually gets smaller the more points you get
            pb.setRadius(Math.max(20, 75 - (int)(score/50) * 5));
            pb.update();
            // We don't draw the player yet, as it'd be drawn under everything else

            /*
              Collision handling
              Goals are a bit weird with how we might add new ones in the middle of the loop
            */
            int goalSize = goals.size();
            for (int i= 0; i < goalSize; i++) {
                Goal g = goals.get(i);
                g.draw(canvas);
                if (pb.getDistanceTo(g) < (pb.getRadius() + g.getRadius())) {
                    if (g.isCollectable()) {
                        updateScore(5);
                        /*
                          The 'setCollectable' flag is used to make sure that the goal isn't
                           collected every frame
                        */
                        g.setCollectable(false);
                        /*
                          Changing the goal radius here does mean it's possible to go slowly enough
                           that upon collecting the goal the it shrinks and the player is no longer
                           touching it
                          This might seem undesirable but it plays much better than only having it
                           shrink when the player leaves it
                        */
                        g.setRadius(g.getRadius() - 10);
                    }
                // When the player ball is not touching the goal, but just was
                } else if (!g.isCollectable()) {
                    g.setCollectable(true);
                    if (g.getRadius() <= 35 && g.isNewGoalSpawnable()) {
                        /*
                          We add a new goal, but don't want to update it yet
                          If we did it would theoretically be possible for them to keep spawning
                           inside the player ball, giving unlimited points in a single frame, and
                           halting the app forever
                        */
                        goals.add(new Goal(rand.nextInt(w - 150) + 75,
                                           rand.nextInt(h - 150) + 75));
                        g.setNewGoalSpawned();
                    }
                    if (g.getRadius() <= 10) {
                        /*
                          If we remove a goal all the indexes shift down, so we have to check the
                           same one again, as it will be what used to be the next
                        */
                        goals.remove(i);
                        i--;
                        goalSize--;
                    }
                }
            }
            // Obstacle collision handling is simpler than goals
            for (int i = 0; i < obstacles.size(); i++) {
                ObstacleBall ob = obstacles.get(i);
                ob.update();
                ob.draw(canvas);
                // If the obstacle goes offscreen remove it
                if (ob.getY() > h + ob.getRadius()) {
                    obstacles.remove(i);
                    i--;
                // If the player touches an obstacle penalize them and then remove it
                } else if (pb.getDistanceTo(ob) < (pb.getRadius() + ob.getRadius())) {
                    // The bigger obstacles cost more points
                    updateScore(ob.isSmall() ? -1 : -5);
                    obstacles.remove(i);
                    i--;
                }
            }

            // Just on a random chance add new obstacles
            if (rand.nextFloat() < OBSTACLE_CHANCE) {
                obstacles.add(new ObstacleBall(w));
            }

            // Finally actually draw the player, ontop of everything else
            pb.draw(canvas);

            invalidate();
        }

        @Override
        public boolean onTouchEvent(MotionEvent event) {
            gestureDetector.onTouchEvent(event);
            invalidate();
            return true;
        }
    }

    // Accelerometer listener
    private SensorManager sManager;
    private Sensor accel;
    private AccelListener listener;
    private class AccelListener implements SensorEventListener {
        @Override
        public void onSensorChanged(SensorEvent e) {
            float x = e.values[0];
            float y = e.values[1];

            // Positive x is in opposite directions for accelerometer and canvas
            pb.gravity(-x * GRAV_MULTIPLIER, y * GRAV_MULTIPLIER);
        }

        public void onAccuracyChanged(Sensor s, int a) {}
    }

    ConstraintLayout layout;
    PlayerBall pb;
    TextView scoreTimerText;
    int score = 0;
    int timeLeft = 30;
    Intent gameOverIntent;
    Toast scoreToast;
    public static final String EXTRA_MESSAGE = "com.example.tk181.assignment8.SCORE";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        CustomColours.setupColours(getResources());
        pb = new PlayerBall();

        layout = new ConstraintLayout(this);

        scoreTimerText = new TextView(this);
        scoreTimerText.setTextColor(CustomColours.TEXT);
        scoreTimerText.setTextSize(24);
        scoreTimerText.setText("0\n30");
        layout.addView(scoreTimerText);

        GraphicsView gv = new GraphicsView(this);
        layout.addView(gv);

        // For some reason these don't have ids by default?
        scoreTimerText.setId(View.generateViewId());
        gv.setId(View.generateViewId());

        // There's a gap above the score text by default, this replicates it on the left
        ConstraintSet set = new ConstraintSet();
        set.clone(layout);
        set.connect(scoreTimerText.getId(), ConstraintSet.LEFT, ConstraintSet.PARENT_ID, ConstraintSet.LEFT, 20);
        set.applyTo(layout);

        setContentView(layout);

        // Setup our sensors
        gestureListener = new MyGestureListener();
        gestureDetector = new GestureDetectorCompat(this, gestureListener);

        sManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        accel = sManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        listener = new AccelListener();
        sManager.registerListener(listener, accel, SensorManager.SENSOR_DELAY_GAME);

        // Game timer
        gameOverIntent = new Intent(this, LeaderboardActivity.class);
        scoreToast = Toast.makeText(this, "Your score: 0", Toast.LENGTH_LONG);
        new CountDownTimer(60000, 1000) {
            // While running update our score/timer text
            public void onTick(long millisUntilFinished) {
                timeLeft = (int) millisUntilFinished / 1000;
                scoreTimerText.setText(String.format("%d\n%d", score, timeLeft));
            }

            // When finished send the score to the leaderboard activity, and display a toast
            public void onFinish() {
                scoreToast.setText(String.format("Your score: %d", score));
                scoreToast.show();

                gameOverIntent.putExtra(EXTRA_MESSAGE, score);
                startActivity(gameOverIntent);
            }
        }.start();

    }

    // Just a quick helper function
    public void updateScore(int amount) {
        score += amount;
        // I kind of want score to be able to overflow, though within 60s it will never really happen
        if (-10 <= score && score <= 0) {
            score = 0;
        }
        scoreTimerText.setText(String.format("%d\n%d", score, timeLeft));
    }

    @Override
    protected void onPause() {
        super.onPause();
        sManager.unregisterListener(listener, accel);
    }

    @Override
    protected void onResume() {
        super.onResume();
        sManager.registerListener(listener, accel, SensorManager.SENSOR_DELAY_GAME);
    }
}
