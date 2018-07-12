/*
  Taran Kern
  <ID NUM>

  The main program that actually simulates the queue
*/

import java.util.ArrayList;
import java.util.Random;

public class QSim {
  // The main method that actually runs the simulation
  public static void main(String[] args) {
    // A length is required so we return in the catch
    int MAX_DEPARTS;
    try {
      MAX_DEPARTS = Integer.parseInt(args[0]);
    } catch (ArrayIndexOutOfBoundsException|NumberFormatException e) {
      System.out.println("Format:\njava QSim <Amount of Departures> <Seed (Optional)>");
      return;
    }
    // A seed is optional so the catch just does nothing
    Random rand = new Random();
    try {
      rand.setSeed(Long.parseLong(args[1]));
    } catch (ArrayIndexOutOfBoundsException|NumberFormatException e) {}

    ClientQueue queue = new ClientQueue();
    // I got a bunch of "___ may not be initalized" errors so I just set them all
    int simTime = 0;
    int nextArrival = 0;
    int nextDepart = -1;
    int departAmount = 0;
    int totalWait = 0;
    int totalLength = 0;

    while (departAmount <= MAX_DEPARTS) {
      /*
        Process arrivals first to try make sure the queue empties less
        Shouldn't affect the simulation, just avoids a few code blocks that
          trigger on an empty queue so should speed the whole thing up
      */
      if (simTime == nextArrival) {
        int newUsage = rand.nextInt(3) + 1;
        if (queue.isEmpty()) {
          nextDepart = newUsage + simTime;
        }
        queue.add(simTime, newUsage);
        nextArrival = simTime + rand.nextInt(3) + 1;
      }

      if (simTime == nextDepart) {
        departAmount++;
        int[] data = queue.remove();

        int waitTime = simTime - data[0];
        int queueLength = queue.getLength();
        totalWait += waitTime;
        totalLength += queueLength;
        double avWait = (double)totalWait / (double)departAmount;
        double avQueue = (double)totalLength / (double)departAmount;
        /*
          The assignment specifed to only output waitTime and queueLength through
            System.out, in this format, but that seems like a terrible way to do it,
            and it doesn't show averages so there's my version too
        */
        System.out.println(String.format("%d %d", waitTime, queueLength));
        System.err.println(String.format("Client left, Waited: %d (%.2f), Queue Length: %d (%.2f)", waitTime, avWait, queueLength, avQueue));

        if (queue.isEmpty()) {
          nextDepart = -1;
        } else {
          nextDepart = queue.peek()[1] + simTime;
        }
      }

      // We don't need to simulate every value, we can jump straight to interesting ones
      if (nextDepart == -1 | nextArrival < nextDepart) {
        simTime = nextArrival;
      } else {
        simTime = nextDepart;
      }
    }
  }
}
