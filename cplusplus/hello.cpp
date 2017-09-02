/*****************************************
*	gcc hello.cpp -lstdc++ -o hello.exe
******************************************/

#include <iostream>
using namespace std;


template <class T> void test_poly_template_case(T &t)
{
	t.print_local();
}

class A
{
public:
	void print_local(void) { cout<<"local area: A "<<endl; };
	A(){ };
	~A(){ };
};

class B:public A
{
public:
	virtual void print_local(void) { cout<<"local area: B "<<endl; };
	B(){ };
	~B(){ };
};

class C:public B
{
public:
	void print_local(void) { cout<<"local area: C "<<endl; };
	C(){ };
	~C(){ };
};

void test_poly_case(void)
{
	C objC;
	B objB;
	A objA;

	test_poly_template_case<C>(objC);

	test_poly_template_case<B>(objC);
	test_poly_template_case<B>(objB);

	test_poly_template_case<A>(objC);
	test_poly_template_case<A>(objB);
	test_poly_template_case<A>(objA);
}


int main(void)
{
     test_poly_case();
	 return 0;
}
