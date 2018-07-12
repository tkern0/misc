/*
  Taran Kern
  <ID NUM>

  This class defines the linked list and all its functions
  I would have called this something like "IntLinkedList", but incase it
    matters I kept the same names as in the assignment outline
*/

class MyIntList {
  // Define a private class that we'll use for each item in our list
  private class Item {
    private int data;
    private Item next;

    // Just some simple getter/setter methods
    public int  getData() {return data;}
    public Item getNext() {return next;}
    public void setData(int  x) {data = x;}
    public void setNext(Item x) {next = x;}
  }

  private Item head;
  private int size;

  // Adds a new item to the list, replacing head
  public void add(int x) {
    Item tmp = new Item();
    tmp.setData(x);
    tmp.setNext(head);
    head = tmp;
    size++;
  }

  // Checks if an item is in the list
  public boolean hasItem(int x) {
    Item tmp = head;
    while (tmp != null) {
      if (tmp.getData() == x) {
        return true;
      }
    }
    return false;
  }

  /*
    Removes the latest element in the list
    Returns false if the list is empty
  */
  public boolean remove() {
    if (head == null) return false;
    head = head.getNext();
    size--;
    return true;
  }

  /*
    Removes the first item with value "x"
    Returns true if it was able to find such an item
    "remove" is not a good name for this at all, would rather use "removeValue"
    The while loop needs to check one value ahead of "tmp" because we'll need
      to change the "next" value of "tmp" when we remove something
  */
  public boolean remove(int x) {
    if (head.getData() == x) {
      head = head.getNext();
      size--;
      return true;
    }
    Item tmp = head;
    while (tmp.getNext() != null) {
      if (tmp.getNext().getData() == x) {
        tmp.setNext(tmp.getNext().getNext());
        size--;
        return true;
      }
      tmp = tmp.getNext();
    }
    return false;
  }

  /*
    Gets the length of the list, should really be called "getLength" or
      "getSize" but again incase it matters
  */
  public int length() {return size;}

  // The name here really says it all, checks if the list is empty
  public boolean isEmpty() {return size == 0;}

  /*
    Gets the first item in the list, the value of head, or -1 if the list is empty
    I would rather return "null" or "false", as you might actually want to store
      "-1", but those error for using the wrong type :(
  */
  public int getFirst() {return (size == 0) ? -1 : head.getData();}

  /*
    Prints all items in the list, indexed in reverse, so last added is 0
    Again I'd rather call this "printItems()"
    I do a bit of extra work in order to pad the indexes with spaces
    If it weren't O(n^2) I'd also pad the values
  */
  public void dump() {
    Item tmp = head;
    int n = 0;
    int maxSize = (size <= 1) ? 1 : (int)Math.log10(size - 1) + 1;
    System.out.println("List Contents:");
    while (tmp != null) {
      // We know indexes will never be negative
      int indexSize = (n == 0) ? 1 : (int)Math.log10(n) + 1;
      String padding = "";
      for (int i=0; i<(maxSize - indexSize); i++) {
        padding += " ";
      }
      System.out.println(padding + n + ": " + tmp.getData());
      tmp = tmp.getNext();
      n++;
    }
  }

  /*
    Inserts an item with value x immediately in front of (towards head) the
      first item of the list that is greater than or equal to x
    Like remove() we need tmp to stay a step behind the values we're comparing
    Man this name is misleading, I'd go with "sortedInsert" or "insertLessThan"
  */
  public void insert(int x) {
    Item newItem = new Item();
    newItem.setData(x);
    size++;
    if (head == null || head.getData() >= x) {
      newItem.setNext(head);
      head = newItem;
      return;
    }
    Item tmp = head;
    while (tmp.getNext() != null) {
      if (tmp.getNext().getData() >= x) {
        newItem.setNext(tmp.getNext());
        tmp.setNext(newItem);
        return;
      }
      tmp = tmp.getNext();
    }
    // When we get here tmp will be pointing at the last element
    tmp.setNext(newItem);
  }
}
