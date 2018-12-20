package com.example.tk181.a6project;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.util.DisplayMetrics;
import android.view.View;
import android.view.WindowManager;
import android.widget.RelativeLayout;

public class MainActivity extends AppCompatActivity {

    private class BallCanvasView extends View {
        private float SPEED = 2.25f;
        private float DAMPENING = 0.6f;
        private int RADIUS = 50;

        private int w, h;
        private float x, y;
        private float vx = 0;
        private float vy = 0;
        private float ax = 0;
        private float ay = 0;
        private Paint ball = new Paint();

        public BallCanvasView(Context c) {
            super(c);

            // Need to know these to prevent it going off screen
            DisplayMetrics metrics = c.getResources().getDisplayMetrics();
            w = metrics.widthPixels;
            h = metrics.heightPixels;

            // Center the ball by default
            x = w / 2;
            y = h / 2;

            ball.setColor(Color.RED);
        }

        @Override
        protected void onDraw(Canvas canvas) {
            super.onDraw(canvas);

            // Simulate both acceleration and velocity, makes for a smoother effect
            vx += ax;
            vy += ay;
            x += vx * SPEED;
            y += vy * SPEED;

            /*
              Make sure we're not going off screen
              By inverting velocity we can get a proper bounce off, but we need to add a bit of
               dampening otherwise it'll go on for too long
            */
            if (x - RADIUS < 0) {
                x = RADIUS;
                vx = -vx * DAMPENING;
            }
            if (x + RADIUS > w){
                x = w - RADIUS;
                vx = -vx * DAMPENING;
            }
            if (y - RADIUS < 0) {
                y = RADIUS;
                vy = -vy * DAMPENING;
            }
            if (y + RADIUS > h) {
                y = h - RADIUS;
                vy = -vy * DAMPENING;
            }

            canvas.drawCircle(x, y, RADIUS, ball);
            invalidate();
        }

        public void updateAccel(float x, float y) {
            ax = x;
            ay = y;
        }
    }

    private class AccelListener implements SensorEventListener {
        private BallCanvasView bcv;

        public AccelListener(BallCanvasView bcv) {
            super();
            this.bcv = bcv;
        }

        @Override
        public void onSensorChanged(SensorEvent e) {
            float x = e.values[0];
            float y = e.values[1];

            /*
              We only update the acceleration, not the actual x and y values, so that the ball's
               speed doesn't depend on the accelerometer's speed
              Positive x is in opposite directions for accelerometer and canvas
            */
            bcv.updateAccel(-x, y);
        }

        public void onAccuracyChanged(Sensor s, int a) {}
    }

    private SensorManager sManager;
    private Sensor accel;
    private AccelListener listener;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        RelativeLayout layout = new RelativeLayout(this);
        BallCanvasView bcv = new BallCanvasView(this);
        layout.addView(bcv);
        setContentView(layout);
        getWindow().setFlags(WindowManager.LayoutParams.FLAG_FULLSCREEN,
                             WindowManager.LayoutParams.FLAG_FULLSCREEN);

        sManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        accel = sManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        listener = new AccelListener(bcv);
        sManager.registerListener(listener, accel, SensorManager.SENSOR_DELAY_GAME);
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
