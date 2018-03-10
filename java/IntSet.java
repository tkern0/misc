class IntSet {
  private int[] data;
  private int currentSize;
  private int maxSize;

  public static void main(String[] args) {
    IntSet iSet1 = new IntSet();
    IntSet iSet2 = new IntSet();
    for (int i=0; i<5; i++) {
      iSet1.add(i);
      iSet2.add(i*2);
    }
    System.out.println(iSet1.hasElement(3));
    iSet1.remove(3);
    System.out.println(iSet1.hasElement(3));
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
    int[] safeElements = new int[maxSize];
    int newSize = 0;
    for (int i=0; i<currentSize; i++) {
      if (data[i] != x) {
        // data.remove() doesn't work :(
        safeElements[newSize] = data[i];
        newSize++;
      }
    }
    data = safeElements;
    currentSize = newSize;
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
