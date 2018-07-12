/*
  Taran Kern
  <ID NUM>

  This class reads an input file and runs various BST functions based on it
*/

import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;

public class XProcess {
  public static void main (String[] args) {
    // We need to have a file otherwise we can't do anything
    if (args.length != 1) {
      System.err.println("Format: java XProcess <File Path>");
      return;
    }

    /*
      I've only triggered this on files that don't exist, but it might also
       happen if you don't have read permission
    */
    BufferedReader reader;
    try {
      reader = new BufferedReader(new FileReader(args[0]));
    } catch (IOException e) {
      System.err.println("Could not access file \"" + args[0] + "\"");
      return;
    }

    BankBST tree = new BankBST();
    // No idea what would trigger this block but it won't compile without it
    try {
      String line = reader.readLine();

      while (line != null) {
        /*
          Lucikly the lines are always the same length, even though there's no
           use for it close commands still get a float value
          Otherwise I'd just use the following regex:
            ([0-9]+) ?([dwc]) ?([0-9]*\.?[0-9]*)
        */
        String[] words = line.split(" ");

        int key;
        float amount;
        // If there's an error parsing ignore the whole transaction
        try {
          key = Integer.parseInt(words[0]);
          amount = Float.parseFloat(words[2]);
        } catch (NumberFormatException e) {
          continue;
        }

        String path = "";
        switch (words[1].toLowerCase()) {
          case "d":
            /*
              The assignment wanted me to add and update seperatly, I would be
               fine doing them both at once however
            */
            if (!tree.hasKey(key)) {
              tree.add(key);
            }
            path = tree.update(key, amount);
            System.out.println(path + "DEPOSIT");
            break;

          case "w":
            if (!tree.hasKey(key)) {
              tree.add(key);
            }
            path = tree.update(key, -amount);
            System.out.println(path + "WITHDRAW");
            break;

          case "c":
            path = tree.remove(key);
            System.out.println(path + "CLOSE");
            break;
        }

        line = reader.readLine();
      }

      System.out.println("RESULT");
      tree.traverse();

    } catch (IOException e) {
      System.err.println("\nSomething went wrong while reading the file");
      return;
    }
  }
}
