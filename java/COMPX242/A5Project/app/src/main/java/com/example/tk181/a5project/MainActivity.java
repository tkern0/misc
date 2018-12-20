package com.example.tk181.a5project;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;

public class MainActivity extends AppCompatActivity {
    public static final String EXTRA_MESSAGE = "com.example.tk181.a5project.MESSAGE";
    private EditText editTextMessage;
    private EditText[] editTextsToSort;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        editTextMessage = findViewById(R.id.editTextMessage);
        editTextsToSort = new EditText[3];
        editTextsToSort[0] = findViewById(R.id.editTextSort1);
        editTextsToSort[1] = findViewById(R.id.editTextSort2);
        editTextsToSort[2] = findViewById(R.id.editTextSort3);
        buttonMoving = findViewById(R.id.buttonMoving);
    }

    /** Called when the user taps the Send button */
    public void sendMessage(View view) {
        Intent intent = new Intent(this, DisplayMessageActivity.class);
        String message = editTextMessage.getText().toString();
        intent.putExtra(EXTRA_MESSAGE, message);
        startActivity(intent);
    }

    public void clearMessage(View v) {
        editTextMessage.setText("");
    }

    public void sortInputs(View v) {
        ArrayList<String> inputs = new ArrayList<String>();
        for (EditText et : editTextsToSort) {
            inputs.add(et.getText().toString());
        }
        Collections.sort(inputs);
        Iterator<String> it = inputs.iterator();
        for (EditText et : editTextsToSort) {
            et.setText(it.next());
        }
    }

    public void path1(View v) {
        startActivity(new Intent(this, path1.class));
    }
    public void path2(View v) {
        startActivity(new Intent(this, path2.class));
    }
    public void path3(View v) {
        startActivity(new Intent(this, path3.class));
    }

    private Button buttonMoving;
    private int bw;
    private int bh;
    private float minX;
    private float maxX;
    private float minY;
    private float maxY;

    // Let's use some nice prime numbers :)
    private float velX = 37;
    private float velY = -23;

    public void moveButton(View v) {
        // These are still set to 0 during onCreate, so as a quick hack I can set them here
        if (bw == 0) {
            bw = buttonMoving.getWidth();
            bh = buttonMoving.getHeight();
            minX = buttonMoving.getX();
            maxX = buttonMoving.getX() + (bw * 2.5f);
            minY = buttonMoving.getY() - (bh * 5);
            maxY = buttonMoving.getY() + bh;
        }

        float x = buttonMoving.getX();
        float y = buttonMoving.getY();

        // Simple logic to try keep it on screen
        if ((x + velX) < minX || (x + velX + bw) > maxX) {
            velX = -velX;
        }
        if ((y + velY) < minY || (y + velY + bh) > maxY) {
            velY = -velY;
        }

        buttonMoving.setX(x + velX);
        buttonMoving.setY(y + velY);
    }
}
