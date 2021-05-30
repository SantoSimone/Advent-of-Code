#include <string>
#include <fstream>
#include <vector>
#include <sstream>

#include "utils.h"

namespace utils
{
	std::string getInput(int day)
	{
		std::string input_file{"../../input_files/input" + std::to_string(day) + ".txt"};
		std::ifstream is(input_file);
		std::string content((std::istreambuf_iterator<char>(is)),
							(std::istreambuf_iterator<char>()));
		return content;
	}

	std::vector<std::string> getInputAsLines(int day)
	{
		std::string input_file{"../../input_files/input" + std::to_string(day) + ".txt"};
		std::ifstream is(input_file);
		std::vector<std::string> lines;
		std::string line;
		while (std::getline(is, line))
		{
			std::istringstream iss(line);
			lines.push_back(line);
		}

		return lines;
	}

	std::vector<std::string> split(std::string input, std::string delim)
	{
		size_t pos = 0;
		std::string token;
		std::vector<std::string> ret_vec;
		while ((pos = input.find(delim)) != std::string::npos)
		{
			token = input.substr(0, pos);
			ret_vec.push_back(token);
			input.erase(0, pos + delim.length());
		}
		ret_vec.push_back(input);
		return ret_vec;
	}
}