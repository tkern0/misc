class IntSet {
  private int[] data;
  private int currentSize;
  private int maxSize;

  public static void main(String[] args) {
    IntSet iSet1 = new IntSet();
    IntSet iSet2 = new IntSet();
    // Make two sets, one with 0->4, one with evens 0->8
    for (int i=0; i<5; i++) {
      iSet1.add(i);
      iSet2.add(i*2);
    }
    // Is 3 in set 1 (true)
    System.out.println(iSet1.hasElement(3));
    iSet1.remove(3);
    // Is 3 still in set 1 (false)
    System.out.println(iSet1.hasElement(3));
    // Find and print intersection of sets (0, 2, 4)
    IntSet iSet3 = iSet1.intersection(iSet2);
    for (int i=0; i<10; i++) {
      if (iSet3.hasElement(i)) {
        System.out.println(i + " yes");
      } else {
        System.out.println(i + " no");
      }
    }
  }

  public IntSet() {
    data = new int[100];
    maxSize = 100;
  }

  public int getSize() {return currentSize;}

  public void add(int x) {
    if (currentSize >= maxSize) {
      maxSize += 100;
      int[] tempData = new int[maxSize];
      for (int i=0; i<currentSize; i++) {
        tempData[i] = data[i];
      }
      data = tempData;
    }

    data[currentSize] = x;
    currentSize++;
  }

  public void remove(int x) {
    for (int i=0; i<currentSize; i++) {
      if (data[i] == x) {
        currentSize--;
        data[i] = data[currentSize];
      }
    }
  }

  public boolean hasElement(int x) {
    for (int i=0; i<currentSize; i++) {
      if (data[i] == x) return true;
    }
    return false;
  }

  public IntSet intersection(IntSet otherSet) {
    IntSet output = new IntSet();
    for (int i=0; i<currentSize; i++) {
      if (otherSet.hasElement(data[i])) {
        output.add(data[i]);
      }
    }
    return output;
  }

  public IntSet union(IntSet otherSet) {
    IntSet output = new IntSet();
    // do stuff
    return output;
  }
}
