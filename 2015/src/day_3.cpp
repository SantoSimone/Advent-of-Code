#include <utils.h>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

void insert(std::map<std::pair<int, int>, size_t> &houses, const int x, const int y)
{
    std::pair<int, int> pos = std::make_pair(x, y);
    if (houses.find(pos) != houses.end())
    {
        houses[pos]++;
    }
    else
    {
        houses[pos] = 0;
    }
}

void d3p1(const std::string &txt)
{
    std::map<std::pair<int, int>, size_t> houses;
    int x = 0;
    int y = 0;
    insert(houses, x, y);

    for (const auto &c : txt)
    {
        switch (c)
        {
        case '^':
            insert(houses, x, ++y);
            break;
        case 'v':
            insert(houses, x, --y);
            break;
        case '<':
            insert(houses, --x, y);
            break;
        case '>':
            insert(houses, ++x, y);
            break;
        default:
            break;
        }
    }

    std::cout << "Houses with at least one present: " << houses.size() << std::endl;
    return;
}

void d3p2(const std::string &txt)
{
    std::map<std::pair<int, int>, size_t> houses;
    int santa_x = 0;
    int santa_y = 0;
    int robo_x = 0;
    int robo_y = 0;
    insert(houses, 0, 0);
    bool robo = false;

    for (const auto &c : txt)
    {
        int &x = robo ? robo_x : santa_x;
        int &y = robo ? robo_y : santa_y;
        robo = !robo;
        switch (c)
        {
        case '^':
            insert(houses, x, ++y);
            break;
        case 'v':
            insert(houses, x, --y);
            break;
        case '<':
            insert(houses, --x, y);
            break;
        case '>':
            insert(houses, ++x, y);
            break;
        default:
            break;
        }
    }

    std::cout << "Houses with at least one present: " << houses.size() << std::endl;
    return;
}

int main()
{
    int day{3};
    const std::string txt{utils::getInput(day)};
    d3p1(txt);
    d3p2(txt);
}