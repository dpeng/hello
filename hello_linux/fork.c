#include <stdio.h>

int main(void)
{
    pid_t pid = 0;
    pid = fork();
    if(pid < 0)
    {
        printf("error: fork failed!"); 
    }
    else if(pid == 0)
    {
        printf("I'm a child, My pid is: %d\n", getpid()); 
    }
    else
    {
        printf("I'm a parent, My pid is: %d\n", getpid()); 
    }

    return 0;    
}
