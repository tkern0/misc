package com.example.tk181.a7project;

import android.Manifest;
import android.app.Activity;
import android.content.Context;
import android.content.pm.PackageManager;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Path;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.support.constraint.ConstraintLayout;
import android.support.constraint.ConstraintSet;
import android.util.DisplayMetrics;
import android.util.TypedValue;
import android.view.View;
import android.widget.TextView;

import java.util.ArrayList;

public class MainActivity extends Activity {

    private class MapCanvasView extends View {
        private int w;
        private int h;
        private ArrayList<Location> allLocations;
        private Path mapPath;
        private Paint line;
        private Path north;
        private Paint northLine;

        public MapCanvasView(Context c) {
            super(c);

            DisplayMetrics metrics = c.getResources().getDisplayMetrics();
            w = metrics.widthPixels;
            h = metrics.heightPixels;

            // Remove status and action bar from height
            int r = c.getResources().getIdentifier("status_bar_height", "dimen", "android");
            if (r > 0) {
                h -= c.getResources().getDimensionPixelSize(r);
            }
            TypedValue tv = new TypedValue();
            if (getTheme().resolveAttribute(android.R.attr.actionBarSize, tv, true))
            {
                h -= TypedValue.complexToDimensionPixelSize(tv.data,getResources().getDisplayMetrics());
            }

            mapPath = new Path();
            allLocations = new ArrayList<Location>();

            line = new Paint();
            line.setColor(0xff3399cc); // Light Blue
            line.setStyle(Paint.Style.STROKE);
            line.setStrokeJoin(Paint.Join.ROUND);
            line.setStrokeCap(Paint.Cap.ROUND);
            line.setStrokeWidth(10);

            // Setup the north indicator
            north = new Path();
            north.moveTo(50, 350);
            north.lineTo(150, 350);

            north.moveTo(100, 400);
            north.lineTo(100, 200);
            north.lineTo(70, 200);
            north.lineTo(100, 150);
            north.lineTo(130, 200);
            north.lineTo(100, 200);

            north.moveTo(80, 107.5f);
            north.lineTo(80, 50);
            north.lineTo(120, 100);
            north.lineTo(120, 42.5f);

            northLine = new Paint();
            northLine.setColor(0xff000000); // Black
            northLine.setStyle(Paint.Style.STROKE);
            northLine.setStrokeWidth(7.5f);
        }

        @Override
        protected void onDraw(Canvas canvas) {
            super.onDraw(canvas);

            // If we don't have a proper path yet just draw it in the center
            if (allLocations.size() < 2) {
                canvas.drawCircle(w/2, h/2, 5, line);
            } else {
                canvas.drawPath(mapPath, line);
            }
            canvas.drawPath(north, northLine);

            invalidate();
        }

        private double minLat;
        private double maxLat;
        private double minLon;
        private double maxLon;

        public void addLocation(Location newLoc) {
            double lat = newLoc.getLatitude();
            double lon = newLoc.getLongitude();

            // Just to be sure nothing breaks
            if (allLocations.size() == 0) {
                minLat = lat;
                maxLat = lat;
                minLon = lon;
                maxLon = lon;
            }

            // We might need to rescale everything to keep it on screen
            boolean rescale = false;
            if (lat < minLat) {
                minLat = lat;
                rescale = true;
            } else if (lat > maxLat) {
                maxLat = lat;
                rescale = true;
            }
            if (lon < minLon) {
                minLon = lon;
                rescale = true;
            } else if (lon > maxLon) {
                maxLon = lon;
                rescale = true;
            }

            // We want to use the same scale for both axises
            double xScale = (w - 50) / (maxLon - minLon);
            double yScale = (h - 50) / (maxLat - minLat);
            double scale;
            // Because of that we need to find a correction to center the smaller one
            double xCorrection = 25;
            double yCorrection = 25;
            if (xScale < yScale) {
                scale = xScale;
                yCorrection += ((h - 50) - (scale * (maxLat - minLat))) / 2;
            } else {
                scale = yScale;
                xCorrection += ((w - 50) - (scale * (maxLon - minLon))) / 2;
            }

            // Go through everything and rescale it all
            if (rescale) {
                mapPath = new Path();
                boolean once = true;
                for (Location loc : allLocations) {
                    double cLat = loc.getLatitude();
                    double cLon = loc.getLongitude();
                    float x = (float) (scale * (cLon - minLon) + xCorrection);
                    // The y axis is in opposite directions
                    float y = (float) (h - (scale * (cLat - minLat) + yCorrection));
                    if (once) {
                        once = false;
                        mapPath.moveTo(x, y);
                    } else {
                        mapPath.lineTo(x, y);
                    }
                }
            }

            // Add the new location
            allLocations.add(newLoc);
            float x = (float) (scale * (lon - minLon) + xCorrection);
            float y = (float) (h - (scale * (lat - minLat) + yCorrection));

            if (allLocations.size() == 1) {
                mapPath.moveTo(x, y);
            } else {
                mapPath.lineTo(x, y);
            }
            mapPath.lineTo(x, y);
        }
    }

    private class CustomLocListener implements LocationListener {
        MapCanvasView map;
        TextView text;
        public CustomLocListener(MapCanvasView map, TextView text) {
            this.map = map;
            this.text = text;
        }

        @Override
        public void onLocationChanged(Location l) {
            map.addLocation(l);
            // Roughly meter precision, though gps is usually inaccurate that small
            text.setText(String.format("Latitude: %.5f, Longitude: %.5f", l.getLatitude(), l.getLongitude()));
        }

        @Override
        public void onStatusChanged(String provider, int status, Bundle extras) {}
        @Override
        public void onProviderEnabled(String provider) {}
        @Override
        public void onProviderDisabled(String provider) {}
    }

    private boolean isLocationOK;
    private LocationManager locMgr;
    private LocationListener listener;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        ConstraintLayout layout = new ConstraintLayout(this);
        MapCanvasView map = new MapCanvasView(this);
        // Defaults to top left like we want
        layout.addView(map);

        TextView text = new TextView(this);
        text.setText("Unknown location");
        layout.addView(text);

        // For some reason these don't have ids by default?
        text.setId(View.generateViewId());
        map.setId(View.generateViewId());
        // Align the text to the bottom left
        ConstraintSet set = new ConstraintSet();
        set.clone(layout);
        set.connect(text.getId(), ConstraintSet.BOTTOM, ConstraintSet.PARENT_ID, ConstraintSet.BOTTOM, 15);
        set.connect(text.getId(), ConstraintSet.LEFT, ConstraintSet.PARENT_ID, ConstraintSet.LEFT, 15);
        set.applyTo(layout);

        setContentView(layout);

        isLocationOK = false;
        if (checkSelfPermission(Manifest.permission.ACCESS_FINE_LOCATION)
                == PackageManager.PERMISSION_GRANTED) {
            isLocationOK = true;
        } else {
            requestPermissions(new String[] { Manifest.permission.ACCESS_FINE_LOCATION }, 0);
        }
        // We can create these without permission, just not use them
        locMgr = (LocationManager) getSystemService(Context.LOCATION_SERVICE);
        listener = new CustomLocListener(map, text);
    }

    private void registerListener() {
        if (isLocationOK) {
            try {
                locMgr.requestLocationUpdates(locMgr.GPS_PROVIDER, 2000, 5, listener);
            } catch (SecurityException e) {}
        }
    }

    private void unregisterListener() {
        locMgr.removeUpdates(listener);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
        if (grantResults[0] == PackageManager.PERMISSION_GRANTED) {
            isLocationOK = true;
            registerListener();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        unregisterListener();
    }

    @Override
    protected void onResume() {
        super.onResume();
        registerListener();
    }
}
