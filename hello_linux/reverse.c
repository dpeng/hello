//$gcc hello.c -o hello -g
//$./hello
// -o: output
// -g: gdb debug

char g_inputStr[] = "I am from Hangzhou. aaa bbb ccc ddd";
char g_outputStr[256];

char* reverseWord(char* inputStr)
{
	char tmp[20];
	int inputStrLength;
	int wordLength;
	int i = 0;
	
	
	inputStrLength = strlen(inputStr) - 1;
	wordLength = 0;
	while(inputStrLength > 0)
	{
		if(inputStr[inputStrLength] != ' ')
		{
			tmp[wordLength++] = inputStr[inputStrLength--];
		}
		else
		{
			tmp[wordLength++] = inputStr[inputStrLength--];
			while(wordLength > 0)
			{
				g_outputStr[i++] = tmp[--wordLength];
			}	
		}
	}
	tmp[wordLength++] = inputStr[inputStrLength--];
	tmp[wordLength++] = ' ';
	while(wordLength > 0)
	{
		g_outputStr[i++] = tmp[--wordLength];
	}	
	return (char*)&g_outputStr;
}
int main()
{
	char* outputStr = reverseWord((char*)&g_inputStr);
	printf("%s ====> %s\n", g_inputStr, outputStr);
	return 0;    
}
