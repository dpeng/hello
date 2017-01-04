#include <stdio.h>
unsigned int reverseBits(unsigned int value)
{
    unsigned int retValue = 0;
    unsigned int tmpValue = value;
    unsigned int length = 0;
    length = sizeof(unsigned int)<<3;
    for(unsigned int i = 0; i < length - 1; i++)
    {
        retValue |= (tmpValue & 0x1) << (length -i -1);
        tmpValue >>= 1;
    }
    return retValue;
}
int main(void)
{
    unsigned int input = 25;
    unsigned int output = 0;
    output = reverseBits(input);
    printf("before: %d\nafter : %ld\n", input, (long)output); 
    return 0;
}
