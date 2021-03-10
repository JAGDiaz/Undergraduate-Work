/*
 * Joseph Diaz
 * Homework 1
 * CS310
 *
 * This program uses an internal array to hold 'Student' objects
 * and, through a text menu, allows the user to add, remove, 
 * search for, and display info for Students who have their own
 * IDs, Names, and Ages associated with each object.
 */
package homework01.MainClasses;
import homework01.Classes.Student;
import homework01.Interfaces.Studentmethods;
import java.util.Scanner;
import java.lang.Exception;
/* 
  Above are the package declaration and imports for the class.
  The Student Class and Studentmethods interface are user defined
  and used in the execution of the main method in MainClass.
  The Scanner is used to accept input, and Exception is used for 
  validation.
 */

public class MainClass implements Studentmethods
{
	
	public MainClass(){}
	/*
	  The methods that we implement from Studentmethods are non-static,
	  so we must make an instance of the MainClass. To do so we need
	  the above constructor for the class
	 */

	public static Student[] studentArray = new Student[10];
	public static int currIndex = 0;
	public static boolean foundFlag = false;
	/*
	  The above static variables are used throughout the class. So in order
	  to avoid passing them as arguments all the time, we leave them visible 
	  to all methods within MainClass. studentArray is the more important of
	  the 3, as it holds our Student objects. 
	 */

	public static void main(String[] args)
	{
		MainClass caller = new MainClass();
		Scanner input = new Scanner(System.in);	
		int idTemp, ageTemp;
		String sTemp = "";	
		// The Scanner and MainClass instances are needed for interactivty.
		// The temp variables are needed for input.

		do
		{
			// This do-while will only exit if a specific value is input,
			// and it represents the main looping structure of the program.	

			generateMenu();
			// The above method prints the menu of options to the console.
			// More on that later.

			idTemp = validateInteger("selection", input);		
			// Here we accept input for the variable that our branching 
			// switch statement will use, instead of calling input.nextInt()
			// we instead call validateInteger(), more on that later.

			switch(idTemp)
			{
				// This switch statement handles the branching that is required for
				// this program, the previously called validateInteger() ensures 
				// that whatever gets put into idTemp is an integer.

				case 1:
						if(currIndex == studentArray.length)
						{
							System.out.println("\nThe Student Roll is full.\n" 
											 + "Remove a student before adding more.\n");
						}
						else
						{
							System.out.print("\nInsert Student ID: ");
							idTemp = validateInteger("ID", input);
							if(currIndex > 0)
							{
								caller.searchStudent(Integer.toString(idTemp));
								if(foundFlag == true)
								{
									System.out.println("That ID is already in use.");
									break;
								}
							}
							System.out.print("\nInsert Student Name: ");
							sTemp = input.nextLine();
							System.out.print("\nInsert Student Age: ");
							ageTemp = validateInteger("age", input);
							addStudent(new Student(sTemp, ageTemp, idTemp));
							System.out.printf("\n%s has been added to the Roll.\n",
								 			  studentArray[currIndex - 1].getName());
							if(currIndex == studentArray.length)
								System.out.println("\nThe Student Rolls are now full.\n");
						}
						break;
						/*
						  The above case is where we attempt to add new Students to the 
						  'Roll'. If the index we intend to insert at equals the length
						  of the list, then our list is full and inform the user of that.
						  If not, prompt the user for information regarding the new student
                          and collect the input with validateInteger(). The addStudent()
						  method is called with a new Student object to add that student
						  to our list, and the user is notified. There is also a check for
						  the insertion index's value, so that the user can be notified 
						  that it is now full.
						 */						

				case 2:
						if(currIndex > 0)
						{
							System.out.print("\nInsert Student ID: ");
							idTemp = validateInteger("ID", input);
							caller.removeStudent(Integer.toString(idTemp));
						}
						else
							System.out.println("\nThe Roll is empty.\n"
											 + "There are no Students to remove.");
						break;
						/*
						  The above case is for attempting to remove students from the list.
						  First, the insertion index is checked to make sure that there are
						  students in the list at all. If there are, we prompt the user for
						  the ID of the student they wish to remove and use validateInteger 
						  for input. We call removeStudent() using our instance of the 
						  MainClass object, caller. If the list is empty, we inform then 
						  that there are no students to look for.
						 */

				case 3:
						if(currIndex > 0)
						{
							System.out.print("\nInsert Student ID: ");
							idTemp = validateInteger("ID", input);
							caller.searchStudent(Integer.toString(idTemp));
						}
						else
							System.out.println("\nThe Roll is empty.\n"
											 + "There are no Students to search for.");
						break;
						/*
						  The above case is nearly identical to the previous, except that
						  we are calling searchStudent() instead of removeStudent(). The
						  message in case of an empty list is slightly different as well.
						*/

				case 4:
						if(currIndex > 0)
							caller.displayAll();
						else
							System.out.println("\nThe Roll is empty.\n"
											 + "There are no Students to display.");
						break;
						/*
						  The above case is for displaying the contents of the list using
						  caller to call displayAll(). Like the previous, we check for an 
						  empty list beforehand; and let the user know if the list has 
						  nothing in it. 
						*/

				case 5:
						System.out.println("\nThanks!\nExiting...");
						break;
						/*
						  The above case is for thanking the user before exiting the program.
						 */
				
				default:
						System.out.printf("\"%d\" is not a valid selection.\n\n",
										  idTemp);
						// The default case catches all invalid inputs by the user.
			}
		}while(idTemp != 5);
		// End of do-while above, end of main below.	
	}	
	
	public static void generateMenu()
	{
		
		System.out.println("\nUser Menu:\n");
			
		System.out.print("1. Insert Student\n" +
						 "2. Delete Student by ID\n" +
						 "3. Search Student by ID\n" +
						 "4. Display All Students\n" +
						 "5. Exit\n\n" + 
						 "Please make your selection: ");
	}
	// The above method prints the menu options to the console. Using the method
	// helps to modularise the code.

	public static int validateInteger(String data, Scanner input)
	{
		int out = 0;
		String temp = "";
		do
		{
			try
			{
				temp = input.nextLine().trim();
				out = Integer.parseInt(temp);
			}
			catch(Exception e)
			{
				
				System.out.printf("\"%s\" is not a valid %s.\n\n", 
								  temp, data);
				if("selection".equals(data))
				{
					generateMenu();
				}
				else
				{
					System.out.printf("Valid %ss are positive integers", data);
					System.out.print(" with no spaces.\n"
									+ "Please re-enter: ");
					out = 0;
				}
				continue;
			}
			finally
			{
				
			}
			if(out < 1)
			{
				if("selection".equals(data))
				{
					generateMenu();
				}
				else
				{
					System.out.printf("Valid %ss are positive integers", data);
					System.out.print(" with no spaces.\n"
									+ "Please re-enter: ");
				}
			}
		}while(out < 1);
		return out;
	}
	/*
	  The above method validates input to ensure that the methods expecting integers
	  will get them. It's used for all cases where integers are necessary and uses
	  exception handling along Integer.parseInt() to accept String input and determine
	  whether the string can be parsed to int. It does so, if possible, but as the 
	  program isn't interested in non-positive integers, we remain in the do-while to
	  re-prompt for valid input if negative integers are given. The necessary print 
	  outs to the user are dictated by the String parameter given when validateInteger()
	  is called. If the String fails to parse to int, an exception is thrown and caught,
	  and relevant usage information is printed. The local variables out and temp facilitate
	  the function of the method and out's value is returned at the end of the method.
	 */

	@Override
	public void searchStudent(String id)
	{
		int identity = Integer.parseInt(id);
		foundFlag = false;
		for(int i = 0; i < currIndex; i++)
		{
			if(studentArray[i] != null)
			{
				if(identity == studentArray[i].getID())
				{
					System.out.println("\nStudent found:");
					studentArray[i].printInfo(studentArray[i]);
					System.out.println();
					foundFlag = true;
					break;
				}
			}
		}
		if(foundFlag == false)
			System.out.printf("Student with ID %d not found.\nThat ID is available.\n", identity);
	}
	/*
	  The above method is implemented from Studentmethods, and searches the list of 
	  students for a student with the matching ID. The argument for the method is 
	  of type String, so it is parsed to int after being passed in. A local boolean
	  variable is used to print a message if the ID in question is never found. A 
	  for-loop is used to iterate through the list and check each element of the list
	  to determine if an object's reference is stored there. If so, that object's ID
	  member (retrieved by calling a getter) is compared with the local variable. If 
	  a match is found, the user is notified, the found flag is set to true, and the
	  loop is broken out of. If not, the loop continues, until we reach the insertion
	  index. If nothing was found, the user is notified. 
	 */

	public void removeStudent(String id)
	{
		int identity = Integer.parseInt(id);
		foundFlag = false;
		for(int i = 0; i < currIndex; i++)
		{
			if(studentArray[i] != null)
			{
				if(identity == studentArray[i].getID())
				{
					System.out.println("\nStudent removed:");
					studentArray[i].printInfo(studentArray[i]);
					System.out.println();
					foundFlag = true;
					studentArray[i] = studentArray[--currIndex];
					studentArray[currIndex] = null;
					if(currIndex == 0)
						System.out.println("The Roll is now empty.");
					break;
				}
			}
		}
		if(foundFlag == false)
		{
			System.out.printf("Student with ID %d not found.\n", identity);
			System.out.print("That ID is available.\n");
		}
	}
	/*
	  The above method is identical to the searchStudent method, except that when
	  there is a match between the local variable and a student object's ID that
	  object's reference is removed from trhe array, and the object reference 
	  whose index in the list is highest is moved up to fill the 'gap' in the 
	  array. currIndex is likewise updated to reflect this.
	 */

	public static void addStudent(Student stud)
	{
		studentArray[currIndex++] = stud;
	}
	/*
	  The above method adds the student reference passed in to the list of students
	  and uses the post-increment to increase the current insertion index, currIndex.
	 */

	@Override
	public void displayAll()
	{
		System.out.println("\nAll students:");
		for(Student stud : studentArray)
		{
			if(stud != null)
			{
				stud.printInfo(stud);
				System.out.println();
			}	
		}
	}
	/*
	  The above method is implemented from Studentmethods, and is called with 
	  an instance of MainClass to call each reference's printInfo sequentially.
	  As the index of each reference is irrelevant (unlike the search and remove
	  methods) an enhanced of for-each loop is used. The possibility of null 
	  reference's methods being called is accounted for by checking ahead of 
	  time.
	 */
}
