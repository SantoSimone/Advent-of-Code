#include <utils.h>
#include <set>
#include <vector>
#include <iostream>
#include <regex>
#include <string>

void d5p1(const std::vector<std::string> &lines)
{
    size_t nice_count = 0;
    std::set<char> vowels{'a', 'e', 'i', 'o', 'u'};

    for (const auto &line : lines)
    {
        size_t vowels_count = 0;
        bool twice = false;

        if (line.find("ab") != std::string::npos ||
            line.find("cd") != std::string::npos ||
            line.find("pq") != std::string::npos ||
            line.find("xy") != std::string::npos)
        {
            continue;
        }

        for (const auto &c : line)
        {
            if (vowels.find(c) != vowels.end())
            {
                vowels_count++;
            }

            if (!twice)
            {
                if (line.find(std::string() + c + c) != std::string::npos)
                {
                    twice = true;
                }
            }
        }

        if (vowels_count >= 3 && twice)
        {
            nice_count++;
        }
    }

    std::cout << "Nice string count is: " << nice_count << std::endl;
    return;
}

void d5p2(const std::vector<std::string> &lines)
{
    size_t nice_count = 0;

    for (const auto &line : lines)
    {
        bool twice = false;
        bool reg_true = false;

        for (size_t i = 0; i < line.size() - 2; i++)
        {
            if (twice && reg_true)
            {
                nice_count++;
                break;
            }
            std::string str{line[i]};
            str += line[i + 1];
            int count = 0;
            size_t pos = 0;

            if (!twice)
            {
                while ((pos = line.find(str, pos)) != std::string::npos)
                {
                    count++;
                    if (count == 2)
                    {
                        twice = true;
                        break;
                    }
                    pos += str.length();
                }
            }
            std::string r{line[i]};
            r += ".";
            r += line[i];
            std::regex reg(r);
            std::smatch match;

            if (std::regex_search(line.begin(), line.end(), match, reg))
            {
                reg_true = true;
            }
        }
    }

    std::cout << "Nice string count is: " << nice_count << std::endl;
    return;
}

int main()
{
    int day{5};
    const std::vector<std::string> lines{utils::getInputAsLines(day)};
    d5p1(lines);
    d5p2(lines);
}