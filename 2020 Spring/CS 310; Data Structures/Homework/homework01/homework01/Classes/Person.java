package homework01.Classes;

public class Person
{
	private String name;
	private int age;
	
	public Person()
	{
		this.name = "";
		this.age = 0;
	}
	public Person(String name, int age)
	{
		this.name = name;
		this.age = age;
	}
	public String getName()
	{
		return this.name;
	}
	public void setName(String name)
	{	
		this.name = name;
	}

	public int getAge()
	{
		return this.age;
	}
	public void setAge(int age)
	{	
		this.age = age;
	}
}
