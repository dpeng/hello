//$gcc hello.c -o hello -g
//$./hello
// -o: output
// -g: gdb debug
#include <stdio.h>
#include <string.h>
char g_inputStr[] = "We apologize for the network outage that may have impacted you yesterday. This is to inform you that the network and connectivity maintenance work has been successfully completed in Hangzhou China ";
char g_outputStr[] = " ";


int main()
{
    int wordLength = 0x0;
    int inputStrLength = 0x0;
    int i = 0x0;

    inputStrLength = strlen(g_inputStr) - 1;
    while(inputStrLength > 0)
    {
        if(g_inputStr[inputStrLength] == ' ')
        {
            int tempLength = inputStrLength + wordLength;
            while(wordLength > 0)
            {
                g_outputStr[i++] = g_inputStr[tempLength - wordLength-- + 1];
            }
        }
        wordLength++;
        inputStrLength--;
    }
    /*reverse the first word*/
    int tempLength = inputStrLength + wordLength;
    while(wordLength > 0)
    {
        g_outputStr[i++] = g_inputStr[tempLength - wordLength--];
    }
    printf("%s\n===============================>\n%s\n", g_inputStr, g_outputStr);
    return 0;    
}
