
/*********************************************************************************************************************
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
*********************************************************************************************************************/

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <math.h>
#include <string.h>



void reverseString(char* s, int sSize){
    if( s == NULL || sSize < 1)
        return;
    char tmp = ' ';
    for(int i = 0; i < sSize/2; i++){
        tmp = s[i];
        s[i] = s[sSize - i - 2];
        s[sSize - i - 2] = tmp;
    }

}

int main(int argc, char const *argv[])
{
	char inputStr[] = {"hello world~"};
	printf("From: %s\n", inputStr);
	reverseString(&inputStr[0], sizeof(inputStr)/sizeof(char));
	printf("To: %s\n", inputStr);
	return 0;
}
