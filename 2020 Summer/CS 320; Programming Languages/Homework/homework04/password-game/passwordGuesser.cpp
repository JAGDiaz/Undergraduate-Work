/*
 * Collaborators:
 * Joseph diaz 819-947-915
 * Kyle O'Dell 824-811-891
 */

#include <iostream>
#include <thread>
#include <list>
#include <string>
#include <chrono>
#include "passwordGenerator.cpp"


namespace mso
{
	class PasswordGuesser
	{
	private:
		std::string pword;
		mso::PasswordGenerator pGen;
		bool pwordFound;
		int num, seqWins = 0, ranWins = 0;
		
	public:
		PasswordGuesser(std::list<std::string> tokens, int numWords)
		{
			num = numWords;
			pGen = mso::PasswordGenerator(tokens);
			pGen.setIterationLength(numWords);
			pword = pGen.getRandomPassword(numWords);
			pwordFound = false;
			std::cout << "\nYour randomly generated password is: \"" << pword << "\".\n";
		}
		void randomGuesser()
		{
			std::string pass;
			bool randoWins = false;

			while(!pwordFound)
			{
				pass = pGen.getRandomPassword(num);
				
				if(pword.compare(pass) == 0)
				{
					pwordFound = true;
					randoWins = true;
				}
			}
			
			if(randoWins)
			{
				std::cout << "Rando wins! ";
                this->ranWins++;
			}
			else
			{
				std::cout << "Rando lost! ";
			}
		}
		void sequentialGuesser()
		{
			std::string pass;
			bool sequentoWins = false;

			while(!pwordFound)
			{
				pass = pGen.next();
				if(pword.compare(pass) == 0)
				{
					pwordFound = true;
					sequentoWins = true;
				}
			}
			
			if(sequentoWins)
			{
				std::cout << "Sequento wins! ";
                this->seqWins++;
			}
			else
			{
				std::cout << "Sequento lost! ";
			}
		}
        void officiator()
        {
            auto start = std::chrono::high_resolution_clock::now();
            while(!pwordFound)
            {
                auto elapsed = std::chrono::high_resolution_clock::now() - start;
                auto time = std::chrono::duration_cast<std::chrono::microseconds>(elapsed).count();
                if(time % 30000000 == 0)
                    std::cout << time/1000000 << " seconds have elapsed.\n";
            }
        }
		
		void startGuessing()
		{
			std::thread rando(&PasswordGuesser::randomGuesser, this);
			std::thread sequento(&PasswordGuesser::sequentialGuesser, this);
            std::thread offic(&PasswordGuesser::officiator, this);
            offic.join();
			rando.join();
			sequento.join();
		}
        
        int getRanWins()
        {
            return this->ranWins;
        }

        int getSeqWins()
        {
            return this->seqWins;
        }
	};
}
