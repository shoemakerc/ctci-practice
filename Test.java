import java.io.*;
class Test
{
	public static void concat1(String s1)
	{
		s1 = s1 + "forgeeks";
		System.out.println("String s1 in concat1: " + s1);
	}
	public static void concat2(StringBuffer s2)
	{
		s2.append("forgeeks");
		System.out.println("String s2 in concat2: " + s2);
	}
	public static void main(String[] args)
	{
		StringBuffer s = new StringBuffer("Christopher");
		System.out.println("Length of string is: " + s.length());
		System.out.println("Capacity of StringBuffer is: " + s.capacity());
		s.delete(0, 3);
		System.out.println(s);
		s.deleteCharAt(7);
		System.out.println(s);
		String s1 = "Geeks";
		concat1(s1);
		System.out.println("String s1: " + s1);
		StringBuffer s2 = new StringBuffer("Geeks");	
		concat2(s2);
		System.out.println("String s2: " + s2);
		String s3 = "-123";
		int in3 = parseInt(s3);
		System.out.println(in3);
	}
}
