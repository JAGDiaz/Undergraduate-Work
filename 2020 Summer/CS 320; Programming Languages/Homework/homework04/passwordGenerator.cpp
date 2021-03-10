#include <iostream>
#include <list>
#include <string>
#include <time.h>

class PasswordGenerator
{
    public:
    PasswordGenerator(std::list<std::string> uniques){this->tokens = uniques;}

    ~PasswordGenerator(){};
    
    std::string getRandomPassword(int numWords)
    {
        time_t now = time(NULL);
        std::srand(now);
        std::string pass = "";
        int temp;

        if(now % 2 == 0)
        {
            std::list<std::string> data, chance;

            for(int i = 0; i < numWords; i++)
                data.push_front("");

            combos(chance, data, this->tokens.size(), numWords, 0, 0);

            temp = std::rand() % chance.size();
            auto it = chance.begin();
            std::advance(it, temp);
            pass = *it;
            std::cout << "Super Luck activated.\n";
        }
        else
        {
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
                pass += *d + " ";
            }
        }
        return pass;
    }
    
    void setIterationLength(int numWords)
    {
        this->iterLength = numWords;
        this->setTrack();
    }
    

    std::string next()
    {
        std::string pass;
        if(this->hasNext())
        {
            std::list<std::string>::iterator d;
            for(auto it = this->track.begin(); it != this->track.end(); ++it)
            {
                d = this->tokens.begin();
                std::advance(d, *it);
                pass += *d + " ";
            }
            this->trackIterate();
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
            if(*it < this->tokens.size()-1)
                return true;
            it++;
        }
        return false;
    }

    private:
    std::list<std::string> tokens;
    unsigned int iterLength;
    std::list<int> track;


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

    void setTrack()
    {
        if(this->track.size() > 0)
            track.clear();

        for(int i = 0; i < this->iterLength; i++)
            track.push_front(0);
    }

    void trackIterate()
    {
        listRecur(this->track.begin());
    }
    void listRecur(std::list<int>::iterator it)
    {
        (*it)++;
        if(*it == this->tokens.size())
        {
            *it = 0;
            if(it != this->track.end())
                listRecur(std::next(it,1));

        }
    }
};

int main()
{
    std::srand(time(NULL));
    std::list<std::string> words;

    for(int j = 0; j < 10; j++)
        words.push_front(std::to_string(std::rand() % 117));

    for(auto it = words.begin(); it != words.end(); ++it)
        std::cout << *it + " ";
    std::cout << std::endl;
    PasswordGenerator suitcase = PasswordGenerator(words);
    std::cout << suitcase.getRandomPassword(5) << "\n";
    suitcase.setIterationLength(5);
    unsigned int q = 0;
    while(suitcase.hasNext())
    {
        std::cout << suitcase.next() << std::endl;
        q++;
    }
    std::cout << q << std::endl;
    for(auto it = words.begin(); it != words.end(); ++it)
        std::cout << *it + " ";
    std::cout << std::endl;

    //std::cout << "Next1:\n" + suitcase.next() << std::endl;
    //std::cout << "Next2:\n" + suitcase.next() << std::endl;

    return 0;
}

