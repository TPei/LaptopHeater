public class Main
{
	public static void main (String[] args)
	{
		int cpuCount = Runtime.getRuntime().availableProcessors();
		
		for(int i = 0; i < cpuCount; i++)
		{
			new HeatingThread().start();
		}
	}
}