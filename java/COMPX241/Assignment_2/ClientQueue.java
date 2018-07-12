/*
  Taran Kern
  <ID NUM>

  This class implements a Queue (through a linked list) for usage with the QSim program
*/

public class ClientQueue {

  /*
    Private class for the nodes in our list
    Because it's private I didn't bother with getter/setters
  */
  private class Client {
    public Client next;
    public int arrivalTime;
    public int usageTime;
  }

  private Client head;
  private Client tail;
  private int length;

  // Simple getter methods
  public int getLength() {return length;}
  public boolean isEmpty() {return length == 0;}

  // Adds a client to the list
  public void add(int arrivalTime, int usageTime) {
    Client newClient = new Client();
    newClient.arrivalTime = arrivalTime;
    newClient.usageTime = usageTime;

    if (length == 0) {
      head = newClient;
    } else {
      tail.next = newClient;
    }

    /*
      If the list was empty this sets tail to the last (and only) element in the list
      If the list has items newClient and tail.next are pointers to the same thing, so
        rather than checking if I can do tail.next I can just set it to newClient and
        get the same result
    */
    tail = newClient;
    length++;
  }

  // If I'm returning data through arrays might as well let you add using them too
  public void add(int[] data) {
    add(data[0], data[1]);
  }

  // Returns the data from the front client in the list
  public int[] peek() {
    int[] data = new int[2];
    if (length > 0) {
      data[0] = head.arrivalTime;
      data[1] = head.usageTime;
    }
    return data;
  }

  // Removes the front client in the list, and returns its data
  public int[] remove() {
    int[] data = new int[2];
    if (length > 0) {
      data[0] = head.arrivalTime;
      data[1] = head.usageTime;
      length--;
      head = head.next;
    }

    if (length == 0) {
      tail = null;
    }

    return data;
  }
}
