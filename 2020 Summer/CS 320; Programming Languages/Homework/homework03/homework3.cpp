/*
 Joseph Diaz
 CS 320
 Homework 3: Guitar Class
 */

#include <utility>
#include <stdio.h>
#include <cmath>
// Necessary import statements above. "utility" for the "pair" object, "stdio.h" to introduce 'printf', 'scanf', etc,
// into the global namespace, and "cmath" to introduce 'pow' and 'abs' into the standard namespace.

static const double initTune[] = {82.41, 110.0, 146.8, 196.0, 246.9, 329.6};
static const int fibres = sizeof(initTune)/sizeof(initTune[0]);
// The Guitar is meant to be a six-string, but these constant static variables allow for changes in string number
// but not during runtime.

class Guitar
{
    public:
    Guitar() {printf("\nYour Guitar is Born!\n"); init(21,initTune);}

    Guitar(const Guitar& warlock)
    {
        this->numberOfFrets = warlock.numberOfFrets;
        for(int i = 0; i < fibres; i++)
            this->tuning[i] = warlock.tuning[i];
    }

    ~Guitar() {printf("\nYour Guitar has been smashed on stage.\n");}
    // Above are the constructor, copy constructor, and destructor for the guitar class. The default constructor
    // calls a helper method called "init" to initialize the Guitar's private variables with their default values.

    bool setFretBoardLength(const unsigned char numFrets)
    {
        if(numFrets >= 1 && numFrets <= 24)
        {
            this->numberOfFrets = numFrets;
            return true;
        }
        else
            return false;
    }
    // The above method allows you to change the number of frets the guitar has; with a minimum of 1 and a maximum
    // of 24. Returns true if the change was made successfully, and false if the new fret number is invalid.

    double pitchAt(const unsigned char &stringNumber, const unsigned char &fret)
    {
        if(fret >= 1 && fret <= this->numberOfFrets && stringNumber >= 1 && stringNumber <= fibres)
            return this->tuning[(int)stringNumber - 1]*std::pow(2.0, (int)fret/12.0);
        else
            return 0.0;
    }
    // The above method allows you to check the pitch for a given string and fret combination. Returns a 
    // double with the pitch if the string and fret are valid, or 0.0 otherwise.

    std::pair<unsigned char, unsigned char> getStringAndFret(const double &timbre)
    {
        unsigned char string, fret = 1;
        while(fret <= this->numberOfFrets)
        {
            for(string = 1; string <=6; string++)
                if(std::abs(timbre - this->pitchAt(string, fret)) < 10)
                    return std::pair<unsigned char, unsigned char>(string, fret);
            fret++;
        }
        return std::pair<unsigned char, unsigned char>('\0','\0');
    }
    // The above method iterates through the string and frets of the guitar to determine if the given 
    // pitch is close enough as to be produceable by the guitar with the current tuning. "Close enough"
    // here is a difference of at most 10 Hz, this method calls pitchAt to find this difference. 
    // Returns the first string and fret combination that is close enough, and ('\0','\0') if no 
    // extent combination is found.

    void tuneString(unsigned char &string, const double &pitch)
    {
        if(string >= 1 && string <= fibres)
        {
            this->tuning[string-1] = pitch;
            printf("String %d has been tuned to %3.2f Hz.\n", string, pitch);
        }
        else
            printf("This is a %d string guitar, I can't tune the %d string.\n", fibres, string);
    }
    // The above method allows you to re-tune any of the strings of the guitar. Returns nothing, but 
    // displays to the terminal whether or not a string was successfully re-tuned.

    void init(const unsigned char fret, const double* tune)
    {
        this->numberOfFrets = fret;
        for(int i = 0; i < fibres; i++)
            this->tuning[i] = *(tune + i);
    }
    // The above method initialize the fields to their default values. This is used because arrays can
    // not be given as parameters to constructor initialization lists.

    private:
    unsigned char numberOfFrets;
    double tuning[fibres];
    // Above are the private members of Guitar: an unsigned char with the number of frets and an array 
    // of doubles containing the pitch of each string by array position.
};

// Main driver
int main()
{
    Guitar warlock = Guitar();
    // Here we create our Guitar. BC Rich Warlock is the only logical name to use.

    unsigned char select = '0', temp1, temp2;
    double dTemp;
    std::pair<unsigned char, unsigned char> result;
    // Above are the primitive variables (and pair) that we'll need for this driver. 

    while(select != 'q' && select != 'Q')
    {
        printf("\nMake a choice about your guitar:\n");
        printf("f: Set fretboard length.\np: Check pitch at string and fret.\n");
        printf("d: Determine closest fret and string by pitch.\nt: Tune string.\n");
        printf("q: Quit (your guitar will be smashed).\n\n");
        printf("Your choice: ");
        select = getchar();
        // The options relating to this guitar are given via a menu, and our selection is used in a switch
        // statement for branching.

        switch(select)
        {

            case 'f':
            case 'F':
                printf("Enter how many frets you want: ");
                scanf("%d", &temp1);
                
                if(warlock.setFretBoardLength(temp1))
                    printf("\nThe guitar now has %d frets (by magic)!\n", temp1);
                else
                    printf("\nThat number of frets is impossible (even by magic)!\n");

                break;
                // Case for changing number of frets.

            case 'p':
            case 'P':
                printf("Which string do you want? ");
                scanf("%d", &temp1);

                printf("Which fret? ");
                scanf("%d", &temp2);
                
                dTemp = warlock.pitchAt(temp1,temp2);
                if(dTemp > 0.0)
                    printf("The pitch for string %d and fret %d is %3.2f Hz.\n", temp1, temp2, dTemp);
                else
                {
                    printf("Either the string or the fret was invalid "); 
                    printf("(try an 8-string if you want more of both).\n");
                }

                break;
                // Case for checking pitch at a given string and fret.

            case 'd':
            case 'D':
                printf("\nEnter the pitch you had in mind: ");
                scanf("%lf", &dTemp);
                result = warlock.getStringAndFret(dTemp);

                if(result.first == 0)
                    printf("Can't quite get that pitch with the current tuning. Try another pitch.\n");
                else
                    printf("Best guess? String %d, Fret %d.\n", result.first, result.second);

                break;
                // Case for trying to find best approximation to given pitch.

            case 't':
            case 'T':
                printf("\nEnter the string you want to tune: ");
                scanf("%d", &temp1);

                printf("Enter the pitch you want to tune it to: ");
                scanf("%lf", &dTemp);

                warlock.tuneString(temp1, dTemp);

                break;
                // Case for re-tuning a given string.

            case 'q':
            case 'Q':
                printf("\nThanks for shredding!\n");

                break;
                // Case for quitting program.

            default:
                printf("That isn't a valid selection.\n");
                // Case for invalid input into switch statement.
        }

        while(getchar() != '\n');
        // This statement clears the buffer after getchar(), to avoid the '\n' ruining the next batch of inputs.

    }

    return 0;
    // End of program, end of main. Our Guitar object is stack-allocated, 
    // but it's destructor will be called nonetheless.
}
