#include "mex.h"
#include "matrix.h"
#include "string.h"

/*
Matlab��mex�����ӿڹ淶:
nlhs�����������Ŀ
plhs��ָ�����������ָ��
nrhs�����������Ŀ
����������ʱ������������plhs[0]��plhs[1]��ĵ�ַ����a��b���ﵽ�������ݵ�Ŀ
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
		mexPrintf("world hello��%d\n", i);
	}
	for(i = 0; i < 100; i++)
	{
		a[i] = sin(i);
	}
	plhs = a;
}