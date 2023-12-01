/*****************************************
*	gcc hello.cpp -lstdc++ -o hello.exe -f sanitize=address
******************************************/

#include <iostream>


int main(void)
{
	int *p = nullptr;
	std::cout << "p = " << *p << '\n';
}
