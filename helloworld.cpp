#include <iostream>
#include <vector>
#include <string>

int main()
{
    std::vector<std::string> const msg{"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!"};

    for (std::string const &word : msg)
    {
        std::cout << word << " ";
    }
    std::cout << std::endl;
}