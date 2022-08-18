#include <utils.h>
// #include "utils.h"
#include <map>
#include <iostream>

void d1p1(std::string txt)
{
	std::map<char, int> counts;
	for (const auto c : txt)
	{
		counts[c]++;
	}

	int floor{counts['('] - counts[')']};

	std::cout << "Final floor is: " << floor << "\n";
}

void d1p2(std::string txt)
{
	int floor{0};
	unsigned int i{0};
	for (; i < txt.size(); i++)
	{
		if (floor == -1)
		{
			break;
		}
		if (txt[i] == '(')
		{
			floor++;
		}
		if (txt[i] == ')')
		{
			floor--;
		}
	}

	std::cout << "Position of character that makes Santa enter the basement is: " << i << "\n";
}

int main()
{
	int day{1};
	std::string txt{utils::getInput(day)};
	d1p1(txt);
	d1p2(txt);
}