/*
 * Joseph Diaz
 * CS 320
 * Homework 2
 * Exercises 1 & 4
 */

#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

int howManyCaps(char* word);
bool differByBit(char a, char b);
// Imports and function declarations.

int main()
{
    char s = '0', a, b, *temp;
    // s is used to control program flow, along with all the other variables we'll need.

    do
    {
        printf("Enter which exercise you want to examine (1, 4, or q to quit): ");
        s = getchar();
        while(getchar() != '\n');
        // The user is prompted for input, choices are given, and getchar() is used to capture input.
        // The next line of code essentially clears the buffer, so that the left over '\n' isn't used
        // the next time we ask for input.

        if(s == '1')
        {
            printf("\nExercise 1:\n");
            printf("Enter a string and I'll tell you how many capital letters it has: ");

            temp = (char*) malloc(100*sizeof(char));
            scanf("%[^\n]%*c", temp);

            printf("\"%s\" has %d capital letter(s).\n\n",temp,howManyCaps(temp));
            free(temp);
        }
        // This code block serves as "Exercise 1". We prompt the user for a string, and store the input
        // in an allocated space in memory with the pointer to char called temp. We then call howManyCaps()
        // in the printf function to display input string and also tell the user how many capital letter the
        // string had. Having served it's purpose, we free the memory associated with temp.

        if(s == '4')
        {
            printf("\nExercise 4:\n");
            printf("Enter 2 characters, and I'll tell you if they differ by a single bit.\n");

            printf("Please enter the first character: ");
            a = getchar();
            while(getchar() != '\n');

            printf("Please enter the second character: ");
            b = getchar();
            while(getchar() != '\n');

            if(differByBit(a,b))
                printf("\'%c\' and \'%c\' differ by one bit.\n\n", a, b);
            else
                printf("\'%c\' and \'%c\' DO NOT differ by one bit.\n\n", a, b);
        }
        // The code block serves as "Exercise 4". We prompt the user for 2 characters, store the input,
        // and call differByBit() in the if-statement. Based on what the function returns, we let the 
        // user know if the 2 characters only differ by a single bit.

        if(s != '1' && s != '4' && s != 'q')
            printf("\'%c\' is not a valid input.\n\n",s);
        // This lets the user know if what they entered is not a valid input for the selection.

    }while(s!='q'); 
    // The user only escapes this do-while loop if the user enters a lowercase q (or, due to the weirdness 
    // of getchar(), a string that begins with 'q').

    printf("Cool, peace!\n");
    return 0;
    // Thanks for playing!
}

int howManyCaps(char* word)
{
    int count = 0;
    char ch = '0';

    while(ch != '\0')
    {
        ch = *(word++);
        if(ch >= 'A' && ch <= 'Z')
            count++;
    }
    return count;
}
// This function accepts a pointer to a char as an argument, and iterates through the string
// like an array. Each character is compared with 'A' and 'Z' to determine if the character is
// in the range of capital letters; if so, count is incremented. The while loop will terminate 
// when the null terminator in word is reached. Finally, count is returned.

bool differByBit(char a, char b)
{
    if(a == b)
        return false;
    int n = a ^ b;
    while(n > 1)
    {
        if(n%2 != 0)
            return false;
        n /= 2;
    }
    return true;
}
// This function accepts 2 chars as arguments and determines if their binary representations differ
// by a single bit. First, the chars are compared to each other and if equal the function returns
// false, as this means they're the same character. Next the result of the bitwise XOR of a and b 
// is stored in n. Then, the while loop is used to determine if n is a power of 2. For a and b to
// differ by a single bit, the result of their bitwise XOR must be a bit string that contains a
// single 1 with the remaining bits being 0s; which means if that bit string represents an integer
// then that integer is a power of 2. So while n is greater than 1, the loop checks if n is odd and
// then halves it until the loop terminates (meaning n was a power of 2). Alternatively, if n is 
// ever odd, the function returns false. 
