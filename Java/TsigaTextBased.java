import java.util.Scanner;
import java.util.Random;

class TsigaTextBased {
  public static void main(String[] args) {
    
    //
    Scanner in = new Scanner(System.in);
    Random rand = new Random();

  //enemy variables
  String[] enemies = {"skeleton", "zombie", "slime", "wolf"};
  int maxEnemyHealth = 70;
  int enemyAttackDamage = 10;

  //player variables
  int health = 100;
  int attackDamage = 25;
  int numHealthPotions = 5;
  int healthPotionHealAmount = 30;
  int healthPotionDropChance = 50;

  boolean running = true;
  
  System.out.println("Welcome to a mini DND solo session!");

  GAME:
  while (running){
    System.out.println("----------------------------------------");

    //enemy encounter
    int enemyHealth = rand.nextInt(maxEnemyHealth);
    String enemy = enemies[rand.nextInt(enemies.length)];
    System.out.println("You have encountered "+ "\t#"+ enemy+"! #\n");

    //status and options
    while(enemyHealth>0){
      System.out.println("\tYour HP: "+ health);
      System.out.println("\t"+ enemy + "'s HP: "+ enemyHealth);
      System.out.println("\n\tWhat would you like to do?");
      System.out.println("\t1. Attack");
      System.out.println("\t2. Drink health potion");
      System.out.println("\t3. Run");

      //attack and damage
      String input = in.nextLine();
      if (input.equals("1")){
        int damageDealt = rand.nextInt(attackDamage);
        int damageTaken = rand.nextInt(enemyAttackDamage);

        enemyHealth -= damageDealt;
        health -= damageTaken;

        System.out.println("\t> You strike the "+ enemy +" for "+ damageDealt+ " damage.");
        System.out.println("\t> You recieve "+ damageTaken +" in retaliation!");

        if (health < 1){
          System.out.println("\t> You have taken too much damage, you are too weak to continue!");
          break;
        }

      }
      //drinking potions
      else if(input.equals("2")){
        if (numHealthPotions>0){
          health += healthPotionHealAmount;
          numHealthPotions--;
          System.out.println("\t> You drink a health potion, gaining "+ healthPotionHealAmount +"\n\t> You now have "+ health +"HP."
          +"\n\t> You have "+ numHealthPotions +" health potions left.\n");
        }
        else{
          System.out.println("\t> You have no health potions left! Try to gain more by defeating enemies");
        }
      }
      //running away
      else if(input.equals("3")){
        System.out.println("\tYou run away from the "+enemy);
        continue;
      }
      else{
        System.out.println("\tInvalid command");
      }
    }

    if (health < 1){
      System.out.println("You fainted");
      break;
    }
    //victory
    System.out.println("----------------------------------------");
    System.out.println(" # "+enemy+" was defeated! #");
    System.out.println(" # You have "+ health+" HP left. # ");
    if(rand.nextInt(100)>healthPotionDropChance){
      numHealthPotions++;
      System.out.println(" # The "+enemy+" dropped a health potion! # ");
      System.out.println(" # You now have "+numHealthPotions+" health potions! # ");
    }
    //options
    System.out.println("----------------------------------------");
    System.out.println("What would you like to do now?");
    System.out.println("1. Continue fighting");
    System.out.println("2. Exit dungeon");

    String input = in.nextLine();

    //invalid commands
    while(!input.equals("1") && !input.equals("2")){
      System.out.println("Invalid command!");
      input = in.nextLine();
    }
    //continuing
    if(input.equals("1")){
      System.out.println("You continue on your adventure!");
    }
    //leaving
    else if(input.equals("2")){
      System.out.println("You exit the dungeon.");    
      System.out.println("######################################");
      System.out.println("Thanks for playing! See you next time!");
      System.out.println("######################################");
      break;
    }

    }
  }
}