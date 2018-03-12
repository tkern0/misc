class List {
  private Item head;
  private int size;

  public static void main(String[] args) {
    List a = new List();
    for (int i=0; i<5; i++) {
      a.add((int)Math.pow(2, i) - 1);
    }
    a.printItems();
    System.out.println("Element 3 = " + a.getItem(3));
    System.out.println("Removing element 1:");
    a.remove(1);
    a.printItems();
    System.out.println("Removing last element:");
    a.remove();
    a.printItems();
    System.out.println("Add 7s:");
    for (int i=0; i<5; i++) {
      a.add(7);
    }
    a.printItems();
    System.out.println("Remove 7s:");
    a.removeValues(7);
    a.printItems();
  }

  public int getSize() {return size;}

  public void add(int x) {
    Item tmp = new Item();
    tmp.setValue(x);
    tmp.setNext(head);
    head = tmp;
    size++;
  }

  public void remove() {
    if (head.getNext() != null) {
      head = head.getNext();
      size--;
    }
  }

  public void remove(int index) {
    if (index >= size) {return;}
    if (index == 0) {
      remove();
      return;
    }
    Item tmp = head;
    int n = size - 1;
    while (tmp.getNext() != null) {
      n--;
      if (n == index) {
        tmp.setNext(tmp.getNext().getNext());
        size--;
        return;
      }
      tmp = tmp.getNext();
    }
  }

  public void removeValues(int value) {
    Item tmp = head;
    // TODO: make this also remove element 0
    while (tmp.getNext() != null) {
      if (tmp.getNext().getValue() == value) {
        tmp.setNext(tmp.getNext().getNext());
        size--;
      } else {
        tmp = tmp.getNext();
      }
    }
  }

  public int getItem(int index) {
    Item tmp = head;
    int n = size;
    while (tmp != null) {
      n--;
      if (n == index) {
        return tmp.getValue();
      }
      tmp = tmp.getNext();
    }
    // Don't like this at all but it'll break otherwise
    return 0;
  }

  public int[] getAllItems() {
    Item tmp = head;
    int n = size - 1;
    int[] output = new int[size];
    while (tmp != null) {
      output[n] = tmp.getValue();
      tmp = tmp.getNext();
      n--;
    }
    return output;
  }

  public void printItems() {
    int[] items = getAllItems();
    for (int i=0; i<items.length; i++) {
      System.out.println(i + ": " + items[i]);
    }
  }
}
