package homework01.Classes;

public class Student extends Person
{
	private int ID;

	public Student()
	{
		super();
		this.ID = 0;
	}
	public Student(String name, int age, int ID)
	{
		super(name, age);
		this.ID = ID;
	}
	public void setID(int ID)
	{
		this.ID = ID;
	}
	public int getID()
	{
		return this.ID;
	}
	public void printInfo(Student a)
	{
		System.out.printf(
		"ID: %-8d Name: %-16s Age: %-4d", a.getID(), a.getName(), a.getAge());
	}	
}
