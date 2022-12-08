//Video Games
//Usman Ahmed and Kirk Martin
//This programs asks the user how many days they want to track their video game usage. It then calculates the average of the days and determines which day had the lowest amount of usage. 

import java.util.Scanner;

public class VideoGames 
{

    public static void main(String[] args) 
    {
    
        System.out.println("How many days do you want to track your video game usage?");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
    
        double[] hoursTracker = new double[n];
        double total = 0;
        double minValue = 24;
        int day = 0;

        for(int i=0; i<hoursTracker.length; i++)
        {
            System.out.print("Enter day No."+(i+1)+": ");
            hoursTracker[i] = scanner.nextDouble();
        }
        
        scanner.close();
        
        for(int i=0; i<hoursTracker.length; i++)
        {
            total = total + hoursTracker[i];
        }
        
        for(int i=0; i<hoursTracker.length; i++)
        {
            if (hoursTracker[i] < minValue)
            {
 
                minValue = hoursTracker[i];
                day = i+1;
            }

        }
        double average = total / hoursTracker.length;
        
        System.out.format("Your daily average is: %.3f", average);
        System.out.println();
        System.out.println("The day with the lowest amount of hours was on day " + day + " where you played a total of " + minValue + " hours.");
    }