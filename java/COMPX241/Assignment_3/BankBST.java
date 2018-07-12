/*
  Taran Kern
  <ID NUM>

  This class defines the BST we will use to store all the accounts
*/

public class BankBST {

  // The data class for the BST
  private class Account {
    private int key;
    private float balance;

    // Key won't change so the constructor is the only time to assign it
    public Account(int keyVal, float balanceVal) {
      key = keyVal;
      balance = balanceVal;
    }

    // Simple getter/setter methods
    public int getKey() {return key;}
    public float getBalance() {return balance;}
    // Sorry if this breaks somehow but the other name was super misleading
    public void updateBalance(float amount) {balance = balance + amount;}
  }

  private BankBST left;
  private BankBST right;
  private Account value;

  // Because not everything is done recursivly we do need some getter/setters
  public BankBST getLeft() {return left;}
  public BankBST getRight() {return right;}
  public Account getValue() {return value;}

  public void setLeft(BankBST x) {left = x;}
  public void setRight(BankBST x) {right = x;}
  public void setValue(Account x) {value = x;}

  /*
    Adds an account to the BST
    Returns the keys down the path it went to find a new spot
  */
  public String add(int key, float balance) {
    if (value == null) {
      value = new Account(key, balance);
    }
    String keyPath = Integer.toString(value.getKey()) + " ";
    if (key < value.getKey()) {
      if (left == null) {
        left = new BankBST();
      }
      keyPath += left.add(key, balance);
    } else if (key > value.getKey()) {
      if (right == null) {
        right = new BankBST();
      }
      keyPath += right.add(key, balance);
    }
    return keyPath;
  }
  // So you don't have to specify the amount just yet
  public String add(int key) {
    return add(key, 0);
  }

  /*
    Gets the balance of an account in the list from it's key
    Returns NaN if the key doesn't exist
  */
  public float get(int key) {
    if (value == null) {return Float.NaN;}
    if (value.getKey() == key) {return value.getBalance();}
    if (key < value.getKey()) {
      if (left != null) {
        return left.get(key);
      }
    } else if (key > value.getKey()) {
      if (right != null) {
        return right.get(key);
      }
    }
    return Float.NaN;
  }

  /*
    Returns true if the tree has a certain key
    There's no need to reimplent this if get() already gives us an accurate
     output, just have to convert it to a bool
  */
  public boolean hasKey(int key) {
    return !Float.isNaN(get(key));
  }

  /*
    Updates the balance of an account from it's key
    Returns a string of the keys down the path it went to find the relevant
     account, or an empty string if the account doesn't exist
  */
  public String update(int key, float amount) {
    if (value == null) {return "";}
    String keyPath = Integer.toString(value.getKey()) + " ";
    if (value.getKey() == key) {
      value.updateBalance(amount);
    }
    if (key < value.getKey()) {
      if (left == null) {return "";}
      keyPath += left.update(key, amount);
    } else if (key > value.getKey()) {
      if (right == null) {return "";}
      keyPath += right.update(key, amount);
    }
    return keyPath;
  }

  // Prints the key and balance of every account in the tree sorted by key
  public void traverse() {
    if (left != null) {
      left.traverse();
    }
    if (value != null) {
      System.out.println(String.format("%d: %.2f",
                         value.getKey(), value.getBalance()));
    }
    if (right != null) {
      right.traverse();
    }
  }

  /*
    Removes the account with the specified key from the tree
    Returns a string of the keys on the path to finding this key
    Runs recursivly at first to find the specified key, but then, if there are
     two subtrees it switches to using a while loop, as we need to stay a step
     behind the account we will move to the position of the one we removed
  */
  public String remove(int key) {
    if (value == null) {return " ";}
    String keyPath = Integer.toString(value.getKey()) + " ";
    /*
      If this segment comes last like in the other functions we'll end up
       comparing against the value we just removed
    */
    if (key < value.getKey()) {
      keyPath += left.remove(key);
    } else if (key > value.getKey()) {
      keyPath += right.remove(key);
    }
    if (key == value.getKey()) {
      BankBST tmp;
      int subTrees = 0;
      if (left != null) {subTrees++;}
      if (right != null) {subTrees++;}
      switch (subTrees) {
        case 0:
          value = null;
          // Just to be safe :)
          left = null;
          right = null;
          break;

        case 1:
          if (left == null) {
            tmp = right;
          } else {
            tmp = left;
          }
          value = tmp.getValue();
          left = tmp.getLeft();
          right = tmp.getRight();
          break;

        case 2:
          tmp = right;
          while (tmp.getLeft().getLeft() != null) {
            tmp = tmp.getLeft();
          }
          value = tmp.getLeft().getValue();
          tmp.setLeft(tmp.getLeft().getRight());
          break;
      }
    }
    return keyPath;
  }
}
