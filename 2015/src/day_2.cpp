#include <utils.h>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>

struct Box
{
    Box() = default;

    Box(int l, int w, int h)
        : m_l(l), m_w(w), m_h(h) {}

    int m_w;
    int m_h;
    int m_l;

    int area() const
    {
        std::vector<int> vals = sides();
        int min_side = *std::min_element(vals.begin(), vals.end());
        return 2 * vals[0] + 2 * vals[1] + 2 * vals[2] + min_side;
    }

    int ribbon_area() const
    {
        std::vector<int> vals{m_w, m_h, m_l};
        std::sort(vals.begin(), vals.end());
        return 2 * vals[0] + 2 * vals[1] + std::accumulate(vals.begin(), vals.end(), 1, std::multiplies<int>());
    }

    std::vector<int> sides() const
    {
        return std::vector<int>{m_l * m_w, m_w * m_h, m_h * m_l};
    }
};

std::vector<Box> parse_input(const std::vector<std::string> &lines)
{
    std::vector<Box> boxes;
    for (const auto &line : lines)
    {
        std::vector<std::string> box_info = utils::split(line, "x");
        boxes.emplace_back(
            Box(
                std::stoi(box_info[0]),
                std::stoi(box_info[1]),
                std::stoi(box_info[2])));
    }
    return boxes;
}

void d2p1(const std::vector<Box> &boxes)
{
    size_t wrapping_paper{0};

    for (const auto &box : boxes)
    {
        wrapping_paper += box.area();
    }

    std::cout << "Total wrapping paper: " << wrapping_paper << "\n";
}

void d2p2(const std::vector<Box> &boxes)
{
    size_t wrapping_paper{0};

    for (const auto &box : boxes)
    {
        wrapping_paper += box.ribbon_area();
    }

    std::cout << "Total wrapping paper: " << wrapping_paper << "\n";
}

int main()
{
    int day{2};
    const std::vector<std::string> lines{utils::getInputAsLines(day)};
    const std::vector<Box> boxes = parse_input(lines);
    d2p1(boxes);
    d2p2(boxes);
}