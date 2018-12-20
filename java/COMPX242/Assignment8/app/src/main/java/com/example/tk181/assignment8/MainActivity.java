package com.example.tk181.assignment8;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import android.widget.EditText;

// The main menu activity, just handles the two buttons to send you to the others
public class MainActivity extends FullScreenActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);
    }

    public void startGame(View v) {
        Intent intent = new Intent(this, GameActivity.class);
        startActivity(intent);
    }

    public void startLeaderboard(View v) {
        // We don't need to send a score alongside this intent as it defaults to 0
        Intent intent = new Intent(this, LeaderboardActivity.class);
        startActivity(intent);
    }
}
