class IntSet {
  private int[] data;
  private int currentSize;
  private int maxSize;

  public static void main(String[] args) {
    IntSet iSet = new IntSet();
    for (int i=0; i<5; i++) {
      iSet.add(i);
    }
    System.out.println(iSet.hasElement(3));
    iSet.remove(3);
    System.out.println(iSet.hasElement(3));
  }

  public IntSet() {
    data = new int[100];
    maxSize = 100;
  }

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
}
