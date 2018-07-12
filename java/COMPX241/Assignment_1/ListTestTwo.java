/*
  Taran Kern
  <ID NUM>

  This class is the second test class for the "MyIntList" object
*/

import java.util.Random;

class ListTestTwo {
  /*
    This time to test the list we create two lists with 50 random values from
      0-99 (inclusive) each
    We then find the interscetion of these lists in a third
    Note that this intersection takes into account duplicates - if both lists
      have two copies of a number then the intersection will also have two
    This process does end up destroying the lists, implementing it as part of
      "MyIntList" would be better
    As we print all three lists I definitly recommend piping this into less
  */
  public static void main(String[] args) {
    MyIntList list1 = new MyIntList();
    MyIntList list2 = new MyIntList();
    Random rand = new Random();

    for (int i=0; i<50; i++) {
      // nextInt(x) returns numbers from 0 to x-1
      list1.insert(rand.nextInt(100));
      list2.insert(rand.nextInt(100));
    }

    System.out.println("Inital lists:\n");
    list1.dump();
    list2.dump();

    MyIntList intersection = new MyIntList();
    int n = list1.getFirst();
    while (n != -1) {
      if (list2.remove(n)) {
        intersection.insert(n);
      }
      list1.remove();
      n = list1.getFirst();
    }

    System.out.println("\nIntersection:\n");
    intersection.dump();
  }
}
