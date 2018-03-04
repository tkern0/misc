class IntSet {
  private int[] data;
  private int currentSize;
  private int maxSize;

  public static void main() {

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
    for (int i=0; i<currentSize; i++) {
      if (data[i] != x) {
        // data.remove() doesn't work :(
        safeElements[safeElements.length] = data[i];
      }
    }
    data = safeElements;
  }

  public boolean hasElement(int x) {
    for (int i=0; i<currentSize; i++) {
      if (data[i] == x) return true;
    }
    return false;
  }
}
