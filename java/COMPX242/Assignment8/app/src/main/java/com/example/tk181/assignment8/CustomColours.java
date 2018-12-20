package com.example.tk181.assignment8;

import android.content.res.Resources;
import android.graphics.Paint;

/*
  Just a helper class importing the colours from 'main/res/values/colors.xml'
  Not everything is used, but for consistency it all exists
*/
public class CustomColours {
    public static int BACKGROUND;
    public static int BUTTON;
    public static int TEXT;
    public static int GOAL_RED;
    public static int GOAL_WHITE;
    public static int OBSTACLE;
    public static int PLAYER;
    public static int FLING_AREA;
    public static int TABLE_ROW_SEPARATOR;
    public static int TEXT_DIALOG;

    public static Paint PAINT_BACKGROUND = new Paint();
    public static Paint PAINT_BUTTON = new Paint();
    public static Paint PAINT_TEXT = new Paint();
    public static Paint PAINT_GOAL_RED = new Paint();
    public static Paint PAINT_GOAL_WHITE = new Paint();
    public static Paint PAINT_OBSTACLE = new Paint();
    public static Paint PAINT_PLAYER = new Paint();
    public static Paint PAINT_FLING_AREA = new Paint();
    public static Paint PAINT_TABLE_ROW_SEPARATOR = new Paint();
    public static Paint PAINT_TEXT_DIALOG = new Paint();

    public static void setupColours(Resources res) {
        BACKGROUND = res.getColor(R.color.background);
        BUTTON = res.getColor(R.color.button);
        TEXT = res.getColor(R.color.text);
        GOAL_RED = res.getColor(R.color.goalRed);
        GOAL_WHITE = res.getColor(R.color.goalWhite);
        OBSTACLE = res.getColor(R.color.obstacle);
        PLAYER = res.getColor(R.color.player);
        FLING_AREA = res.getColor(R.color.flingArea);
        TABLE_ROW_SEPARATOR = res.getColor(R.color.tableRowSeparator);
        TEXT_DIALOG = res.getColor(R.color.textDialog);

        PAINT_BACKGROUND.setColor(BACKGROUND);
        PAINT_BUTTON.setColor(BUTTON);
        PAINT_TEXT.setColor(TEXT);
        PAINT_GOAL_RED.setColor(GOAL_RED);
        PAINT_GOAL_WHITE.setColor(GOAL_WHITE);
        PAINT_OBSTACLE.setColor(OBSTACLE);
        PAINT_PLAYER.setColor(PLAYER);
        PAINT_FLING_AREA.setColor(FLING_AREA);
        PAINT_TABLE_ROW_SEPARATOR.setColor(TABLE_ROW_SEPARATOR);
        PAINT_TEXT_DIALOG.setColor(TEXT_DIALOG);
    }
}
