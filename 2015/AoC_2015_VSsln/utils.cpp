#include <string>
#include <fstream>
#include <vector>
#include <sstream>

#include "utils.h"

namespace utils {
	std::string getInput(int day) {
		std::string input_file{ "../input_files/input" + std::to_string(day) + ".txt" };
		std::ifstream is(input_file);
		std::string content((std::istreambuf_iterator<char>(is)),
			(std::istreambuf_iterator<char>()));
		return content;
	}

	std::vector<std::string> getInputAsLines(int day) {
		std::string input_file{ "../input_files/input" + std::to_string(day) + ".txt" };
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
}