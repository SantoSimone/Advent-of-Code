#pragma once
#include <string>
#include <fstream>
#include <vector>
#include <sstream>

namespace utils
{
	std::string getInput(int day);
	std::vector<std::string> getInputAsLines(int day);
	std::vector<std::string> split(std::string input, std::string delim);
}
