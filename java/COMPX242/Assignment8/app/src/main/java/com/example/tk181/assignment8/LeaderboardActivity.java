package com.example.tk181.assignment8;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Bundle;
import android.text.InputType;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

// The leaderboard activity to display the best few scores
public class LeaderboardActivity extends FullScreenActivity {

    private TextView[] nameTexts;
    private TextView[] scoreTexts;
    private String[] names;
    private int[] scores;
    private String newName;
    private int newScore;
    private int overwriteIndex = -1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_leaderboard);

        // Don't think there's a better way to setup these arrays unfortunately
        nameTexts = new TextView[] {
            findViewById(R.id.name0),
            findViewById(R.id.name1),
            findViewById(R.id.name2),
            findViewById(R.id.name3),
            findViewById(R.id.name4)
        };

        scoreTexts = new TextView[] {
            findViewById(R.id.score0),
            findViewById(R.id.score1),
            findViewById(R.id.score2),
            findViewById(R.id.score3),
            findViewById(R.id.score4)
        };

        // Read the scores from disk
        names = new String[5];
        scores = new int[5];
        readData();

        /*
          If we came from the game activity, read the player's score
          If we came from the main menu this defaults to 0, which will not overwrite anything
        */
        Intent intent = getIntent();
        newScore = intent.getIntExtra(GameActivity.EXTRA_MESSAGE, 0);

        // Find which index to overwrite
        for (int i = 0; i < scores.length; i++) {
            if (scores[i] < newScore) {
                overwriteIndex = i;
                break;
            }
        }

        if (overwriteIndex >= 0) {
            // Get the player's name
            AlertDialog.Builder builder = new AlertDialog.Builder(this, R.style.AlertDialogCustom);
            builder.setTitle(String.format("New Highscore: %d\n Please enter your name:", newScore));

            final EditText input = new EditText(this);
            input.setInputType(InputType.TYPE_CLASS_TEXT);
            builder.setView(input);

            // If the player cancels we won't save their score
            builder.setPositiveButton("OK", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    newName = input.getText().toString();
                    // Copy all scores down one spot to make room for the new one
                    for (int j = scores.length - 2; j >= overwriteIndex; j--) {
                        scores[j + 1] = scores[j];
                        names[j + 1] = names[j];
                    }
                    // Add the new score
                    scores[overwriteIndex] = newScore;
                    names[overwriteIndex] = newName;
                    displayAndSaveScores();
                }
            });
            builder.setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    dialog.cancel();
                }
            });
            builder.show();

        }

        // Regardless of if we have the new score yet, display all existing ones
        displayAndSaveScores();
    }

    // A simple helper function to update the displayed scores and save them to disk
    private void displayAndSaveScores() {
        for (int i = 0; i < scores.length; i++) {
            if (names[i] != null) {
                scoreTexts[i].setText(Integer.toString(scores[i]));
                nameTexts[i].setText(names[i]);
            } else {
                scoreTexts[i].setText("-");
                nameTexts[i].setText("-");
            }
        }
        writeData();
    }

    /*
      Read existing scores from disk
      We save scores in a JSON file, if it doesn't exist or isn't formatted properly we can assume
       there are no scores
      If the file has less than 5 entries we can assume the remaining scores don't exist, the
       display function can handle that perfectly fine
    */
    private void readData() {
        try {
            File file = new File(getFilesDir(), "scores.json");
            FileInputStream fis = new FileInputStream(file);
            byte[] data = new byte[(int) file.length()];
            fis.read(data);
            fis.close();

            JSONObject json = new JSONObject(new String(data, "UTF-8"));
            JSONArray array = json.getJSONArray("entries");
            for(int i = 0 ; i < array.length() ; i++){
                names[i] = array.getJSONObject(i).getString("name");
                scores[i] = array.getJSONObject(i).getInt("score");
            }

        } catch (IOException e) {
            Log.d("BallGame", "File reading error:\n" + e.toString());
        } catch (JSONException e) {
            Log.d("BallGame", "JSON error:\n" + e.toString());
        }
    }

    // Write all existing scores to disk
    private void writeData() {
        try {
            JSONArray array = new JSONArray();
            for (int i = 0; i < names.length; i++) {
                /*
                  Ignore scores that haven't been filled in yet
                  If one name in the middle somehow gets set to null this will also remove it for
                   next time the activity starts
                */
                if (names[i] == null) {
                    continue;
                }
                JSONObject entry = new JSONObject();
                entry.put("name", names[i]);
                entry.put("score", scores[i]);
                array.put(entry);
            }

            JSONObject json = new JSONObject();
            json.put("entries", array);

            FileOutputStream fos = openFileOutput("scores.json", Context.MODE_PRIVATE);
            fos.write(json.toString().getBytes());
            fos.close();
        } catch (IOException e) {
            Log.d("BallGame", "File reading error:\n" + e.toString());
        } catch (JSONException e) {
            Log.d("BallGame", "JSON error:\n" + e.toString());
        }
    }

    /*
      We don't want the back key to send you back into the game as that's actually still running,
       and won't call onCreate() again
      Instead we make sure you always get sent to the main menu
    */
    @Override
    public void onBackPressed() {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }

    // Used for debugging
    public void clearScores(View v) {
        names = new String[5];
        scores = new int[5];
        displayAndSaveScores();
    }
}
