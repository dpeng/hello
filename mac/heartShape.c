//gcc hello.c -lm -o hello.out

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <math.h>
#include <string.h>

// The first heart shape
// (x^2+y^2-1)^3 - x^2*y^3 = 0
// y ~ (-1.1 , 1.3 )
// x ~ (-1.2 , 1.2 )
int heartshape1(char* str)
{

    for( float y = 1.3 ; y >= -1.1 ; y -= 0.06 )
    {
        int i = 0;
        for( float x = -1.2 ; x <= 1.2 ; x += 0.025 )
            if( pow((x*x+y*y-1.0),3) - x*x*y*y*y <= 0.0 )  printf("%c", str[i++%strlen(str)]);
            else                                           printf(" ");
       printf("\n"); 
    }

    return 0;
}


// The second heart shape
// x^2 + (5.0*y/4.0-sqrt(|x|))^2 = 1
// y ~ (-1.1 , 1.3 )
// x ~ (-1.1 , 1.1 )
int heartshape2(char* str) 
{
    for( float y = 1.3 ; y >= -1.1 ; y -= 0.06 )
    {
        int i = 0;
        for( float x = -1.1 ; x <= 1.1 ; x += 0.025 )
            if( x*x + pow(5.0*y/4.0-sqrt(fabs(x)),2) - 1 <= 0.0 ) printf("%c", str[i++%strlen(str)]);
            else                                                  printf(" ");
        printf("\n");
    }
    return 0;
}

int main(void)
{
    char str1[28] = "Love you sweetheart!";
    heartshape1(&str1[0]);
    char str2[20] = "macbookpro!";
    heartshape2(&str2[0]);
    return 0;
}
