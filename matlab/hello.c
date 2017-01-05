#include "mex.h"
#include "matrix.h"
#include "string.h"

/*
Matlab的mex函数接口规范:
nlhs：输出参数数目
plhs：指向输出参数的指针
nrhs：输入参数数目
当函数返回时，将会把你放在plhs[0]，plhs[1]里的地址赋给a和b，达到返回数据的目
*/

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{

	int i;
	int a[100];
	i=mxGetScalar(prhs[0]);

	if(i==1)
	{
		mexPrintf("hello,world! %d\n", i);
	}
	else
	{
		mexPrintf("world hello！%d\n", i);
	}
	for(i = 0; i < 100; i++)
	{
		a[i] = sin(i);
	}
	plhs = a;
}