package com.example.tk181.assignment8;

import android.os.Bundle;
import android.view.View;
import android.support.v7.app.AppCompatActivity;

/*
  A parent activity for all others used in the app, that just tries to make sure it's always in
   fullscreen
  Even though it sets sticky immersive mode there are a number of things that can still break out of
   it if we only set it in onCreate()
   e.g. Bringing up the app list, swiping down the notification bar and quickly returning to the app
*/
public class FullScreenActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        fixFullscreen();
    }

    @Override
    protected void onPause() {
        super.onPause();
        fixFullscreen();
    }

    @Override
    protected void onResume() {
        super.onResume();
        fixFullscreen();
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        fixFullscreen();
    }

    private void fixFullscreen() {
        getWindow().getDecorView().setSystemUiVisibility(View.SYSTEM_UI_FLAG_FULLSCREEN
                | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION);
    }
}
