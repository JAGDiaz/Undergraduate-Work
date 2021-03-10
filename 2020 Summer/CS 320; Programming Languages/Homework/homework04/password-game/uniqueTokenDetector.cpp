/*
 * Collaborators:
 * Joseph diaz 819-947-915
 * Kyle O'Dell 824-811-891
 */

#include <iostream>
#include <list>
#include <string>
#include <fstream>

namespace mso
{
	class UniqueTokenDetector
	{
	private:
		std::list<std::string> tokens;
		
	public:
		UniqueTokenDetector()
		{
			
		}
		
		bool listBuilder(std::string word)
		{
			tokens.push_back(word);
			return true;
		}
		
		void viewTokens()
		{
			for(std::string token : tokens)
			{
				std::cout << token << " ";
			}
			std::cout << std::endl;
		}
		
		std::list<std::string> getTokens()
		{
			return tokens;
		}
		
		bool tokenParser()
		{
			std::list<std::string> copyOfTokens;
			if(!tokens.empty())
			{
				
				for(std::string token : tokens)
				{
					for(int i = 0; i < token.size(); i++)
					{
						if(token[i] > 64 && token[i] < 91)
						{
							//std::cout << token[i] << " ";
							token[i] += 32;
							//std::cout << token[i] << " ";
						}
						else if(((token[i] > 90 && token[i] < 97) || (token[i] > 122 && token[i] < 127) || (token[i] > 31 && token[i] < 65)) && i + 1 == token.size())
						{
							token.erase(token.begin() + i);
						}
					}
					copyOfTokens.push_back(token);
					//std::cout << std::endl << token << " ";
				}
				
				copyOfTokens.sort();
				copyOfTokens.unique();
				tokens = copyOfTokens;
			}
			
			return true;
		}
	};
}
