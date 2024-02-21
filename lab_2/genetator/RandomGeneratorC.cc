#define NUMBER_BITS 128

#include <iostream>
#include <cstdlib>
#include <ctime>

int main()
{
    srand(time(NULL));
    for (int i = 0; i < NUMBER_BITS; ++i) {
        std::cout << rand() % 2;
    }
    return 0;
}