package linkedlists;

public class DataClass
{
	private String name;
	private float value;

	public DataClass()
	{
		this("",0);
	}

	public DataClass(String name, float value)
	{
		this.name = name;
		this.value = value;
	}
	
	public void setName(String name)
	{
		this.name = name;
	}
	public void setValue(float value)
	{
		this.value = value;
	}
	public String getName()
	{
		return this.name;
	}
	public float getValue()
	{
		return this.value;
	}
}

