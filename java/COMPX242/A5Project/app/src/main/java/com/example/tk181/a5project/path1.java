package com.example.tk181.a5project;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class path1 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_path1);
    }

    public void toFinal(View v) {
        startActivity(new Intent(this, finalScreen.class));
    }
}
