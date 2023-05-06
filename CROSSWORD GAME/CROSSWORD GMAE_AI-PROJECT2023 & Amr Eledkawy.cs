using System;
// AI_PROJECT
//AMR Eledkawy 
/* TEAM MEMBERS : 
 Ahmad AbulHameed Ahmad Hawwas|800159797
     Mariam sameh mohamed |803084650
       Anas samir Ahmad Yosief|800139140*/

class CrosswordGame
{
    static char[,] board = new char[4, 4];
    static bool[,] filled = new bool[4, 4];
    
    static void Main()
    {
        InitializeBoard();
        PrintBoard();
        
        while (!IsBoardFull())
        {
            Console.WriteLine("TEAM MEMBERS : \n Ahmad AbulHameed Ahmad Hawwas|800159797 \n Mariam sameh mohamed |803084650 \n Anas samir Ahmad Yosief|800139140\n\n*\t**\t*** ");

            Console.WriteLine("Enter row and column to fill (e.g., 1 2):");
            string[] input = Console.ReadLine().Split(' ');
            
            int row = int.Parse(input[0]);
            int col = int.Parse(input[1]);
            
            if (IsValidInput(row, col))
            {
                Console.WriteLine("Enter a letter:");
                char letter = char.Parse(Console.ReadLine().ToUpper());
                
                FillCell(row, col, letter);
                PrintBoard();
                
                if (IsBoardFull())
                {
                    Console.WriteLine("Congratulations! You completed the crossword.");
                    break;
                }
                
                Console.WriteLine("Do you need a hint? (Y/N)");
                string hintAnswer = Console.ReadLine().ToUpper();
                
                if (hintAnswer == "Y")
                {
                    string hint = GetHint(row, col);
                    Console.WriteLine("Hint: " + hint);
                }
            }
            else
            {
                Console.WriteLine("Invalid input. Please try again.");
            }
        }
    }
    
    static void InitializeBoard()
    {
        for (int row = 0; row < 4; row++)
        {
            for (int col = 0; col < 4; col++)
            {
                board[row, col] = '_';
                filled[row, col] = false;
            }
        }
    }
    
    static void PrintBoard()
    {
        Console.WriteLine("   1 2 3 4");
        
        for (int row = 0; row < 4; row++)
        {
            Console.Write(row + 1 + " ");
            
            for (int col = 0; col < 4; col++)
            {
                Console.Write(board[row, col] + " ");
            }
            
            Console.WriteLine();
        }
        
        Console.WriteLine();
    }
    
    static bool IsValidInput(int row, int col)
    {
        if (row >= 1 && row <= 4 && col >= 1 && col <= 4 && !filled[row - 1, col - 1])
        {
            return true;
        }
        
        return false;
    }
    
    static void FillCell(int row, int col, char letter)
    {
        board[row - 1, col - 1] = letter;
        filled[row - 1, col - 1] = true;
    }
    
    static bool IsBoardFull()
    {
        for (int row = 0; row < 4; row++)
        {
            for (int col = 0; col < 4; col++)
            {
                if (!filled[row, col])
                {
                    return false;
                }
            }
        }
        
        return true;
    }
    
    static string GetHint(int row, int col)
    {
        // Implement your AI hint generation logic here
        // You can use the current row and column as inputs to generate a hint
        
        // For demonstration purposes, a simple hint is returned
        return "The hint is: Animal with four legs";
    }
}
