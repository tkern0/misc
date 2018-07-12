/*
  Taran Kern
  <ID NUM>

  This class is the first test class for the "MyIntList" object
*/

class ListTestOne {
  /*
    To test it we're going to first add a bunch of values, all positive odd
      numbers less than 20
    After printing this list we remove all multiples of 3 and print it again
  */
  public static void main(String[] args) {
    MyIntList list = new MyIntList();
    for (int i=0; i<10; i++) {
      list.add((i*2)+1);
    }
    list.dump();
    for (int i=0; i<21; i+=3) {
      list.remove(i);
    }
    list.dump();
  }
}
