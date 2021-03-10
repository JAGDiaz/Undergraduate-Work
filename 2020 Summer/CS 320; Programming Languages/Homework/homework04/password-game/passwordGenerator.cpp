/*
 * Collaborators:
 * Joseph diaz 819-947-915
 * Kyle O'Dell 824-811-891
 */

#include <iostream>
#include <list>
#include <string>
#include <time.h>

namespace mso
{
	class PasswordGenerator
	{
		public:
		PasswordGenerator(){}
		PasswordGenerator(std::list<std::string> uniques)
        {
            this->tokens = uniques;
            this->setSeed();
        }

		~PasswordGenerator(){};
		
		std::string getRandomPassword(int numWords)
		{
			std::string pass = "";
			int temp, j = 1;

            std::list<int> chosen;

            while (chosen.size() < numWords)
            {
                temp = std::rand() % this->tokens.size();
                chosen.push_front(temp);
            }
            std::list<std::string>::iterator d;

            for (auto it = chosen.begin(); it != chosen.end(); ++it)
            {
                temp = *it;
                d = this->tokens.begin();
                std::advance(d, temp);

                if(j++ == numWords)
                    pass += *d;
                else
                    pass += *d + " ";
            }
			return pass;
		}
		
		void setIterationLength(int numWords)
		{
			this->setTrack(numWords);
		}
		

		std::string next()
		{
			std::string pass;
            int j = 1;
			if(this->hasNext())
			{
				std::list<std::string>::iterator d;
				for(auto it = this->track.begin(); it != this->track.end(); ++it)
				{
					d = this->tokens.begin();
					std::advance(d, *it);
                    if(j++ == this->track.size())
                        pass += *d;
                    else
					    pass += *d + " ";
				}
				this->trackIterate(this->track.begin());
			}
			else
				pass = "None";

			return pass;
		}

		bool hasNext()
		{
			std::list<int>::iterator it = this->track.begin();
			while(it != this->track.end())
			{
				if(*it != this->tokens.size()-1)
					return true;
				it++;
			}
			return false;
		}

		private:
		std::list<std::string> tokens;
		unsigned int iterLength;
		std::list<int> track;

        void setSeed()
        {
            std::srand(time(NULL));
        }

		void combos(std::list<std::string> &out, std::list<std::string>data, int n, int r, int index, int i)
		{
			std::list<std::string>::iterator d, t;

			if(index == r)
			{
				std::string give = "";
				for(int j = 0; j < r; j++)
				{
					d = data.begin();
					std::advance(d, j);
					give += *d + " ";
				}
				out.push_back(give);
				return;
			}


			if(i < n)
			{
				d = data.begin();
				t = this->tokens.begin();
				std::advance(d, index);
				std::advance(t, i);
				*d = *t;

				combos(out, data, n, r, index + 1, i + 1);
				combos(out, data, n, r, index, i + 1);
			}

		}

		void setTrack(int iterLength)
		{
			if(this->track.size() > 0)
				track.clear();

			for(int i = 0; i < iterLength; i++)
				track.push_front(0);

		}

		void trackIterate(std::list<int>::iterator it)
		{
			(*it)++;
			if(*it == this->tokens.size())
			{
				*it = 0;
				if(it != this->track.end())
					trackIterate(std::next(it,1));

			}
		}
	};
}


/*int main()
{
    std::srand(time(NULL));
    std::list<std::string> words;

    for(int j = 0; j < 12; j++)
        words.push_front(std::to_string(std::rand() % 117));

    for(auto it = words.begin(); it != words.end(); ++it)
        std::cout << *it + " ";
    std::cout << std::endl;
    mso::PasswordGenerator suitcase = mso::PasswordGenerator(words);
    std::cout << suitcase.getRandomPassword(5) << "\n";
    suitcase.setIterationLength(5);
    unsigned int q = 0;
    while(q < 100)
    {
        std::cout << suitcase.getRandomPassword(6) << std::endl;
        q++;
    }
    std::cout << q << std::endl;


    return 0;
}*/
