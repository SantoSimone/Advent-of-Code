#include <utils.h>
#include <set>
#include <vector>
#include <iostream>
#include <regex>
#include <string>
#include <Eigen/Dense>
#include <Eigen/Core>

void d5p1(const std::vector<std::string> &lines)
{
    Eigen::MatrixXi lights(1000, 1000);
    lights.setConstant(0);

    for (const auto &line : lines)
    {
        std::regex reg("(\\bturn on\\b|\\bturn off\\b|\\btoggle\\b) (\\d+),(\\d+) through (\\d+),(\\d+)");
        std::smatch match;

        std::regex_search(line.begin(), line.end(), match, reg);
        auto start_x = std::stoi(match[2]);
        auto start_y = std::stoi(match[3]);
        auto end_x = std::stoi(match[4]);
        auto end_y = std::stoi(match[5]);

        if (match[1] == "toggle")
        {
            for (auto &v : lights.block(start_y, start_x, end_y - start_y + 1, end_x - start_x + 1).reshaped())
            {
                v = v == 0 ? 1 : 0;
            }
        }
        else
        {
            lights.block(start_y, start_x, end_y - start_y + 1, end_x - start_x + 1).setConstant(match[1] == "turn on" ? 1 : 0);
        }
    }

    std::cout << "Lights up count: " << lights.sum() << std::endl;
    return;
}

void d5p2(const std::vector<std::string> &lines)
{
    Eigen::MatrixXi lights(1000, 1000);
    lights.setConstant(0);
    for (const auto &line : lines)
    {
        std::regex reg("(\\bturn on\\b|\\bturn off\\b|\\btoggle\\b) (\\d+),(\\d+) through (\\d+),(\\d+)");
        std::smatch match;

        std::regex_search(line.begin(), line.end(), match, reg);
        auto start_x = std::stoi(match[2]);
        auto start_y = std::stoi(match[3]);
        auto end_x = std::stoi(match[4]);
        auto end_y = std::stoi(match[5]);

        auto height = end_y - start_y + 1;
        auto width = end_x - start_x + 1;
        Eigen::MatrixXi add(height, width);

        if (match[1] == "toggle")
        {
            add.setConstant(2);
            lights.block(start_y, start_x, height, width) += add;
        }
        else
        {
            add.setConstant(match[1] == "turn on" ? 1 : -1);
            lights.block(start_y, start_x, height, width) += add;
            lights.block(start_y, start_x, height, width) = lights.block(start_y, start_x, height, width).cwiseMax(0);
            // Slower but easier to understand:
            // lights = lights.cwiseMax(0);
        }
    }

    std::cout << "Lights up count: " << lights.sum() << std::endl;
    return;
}

int main()
{
    int day{6};
    const std::vector<std::string> lines{utils::getInputAsLines(day)};
    d5p1(lines);
    d5p2(lines);
}