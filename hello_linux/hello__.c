//$gcc hello.c -o hello
//$./hello

const int speed[7] = {10, 30, 54, 85, 117, 168, 218};

#define GET_SPEED_INDEX(a) ((a) < 8)
#define GET_SPEED_STEP() if(GET_SPEED_INDEX((getSpeedIndex(speedIndex)))) {speed = getSpeed(speedIndex);}
int getSpeedIndex(int a)
{
	int b = a + 1;
	
	printf("2 a:%d b: %d\n", a, b);
	return b;
}
int getSpeed(int a)
{
	int tmp = speed[a] + 1;
	printf("3 a:%d speed: %d tmp: %d\n", a, speed[a], tmp);
	return tmp;
}
int main()
{
	int speedIndex = 3;
	int speed = 0;
	printf("1 index:%d speed: %d\n", speedIndex, speed);
	GET_SPEED_STEP();
	printf("4 index:%d speed: %d\n", speedIndex, speed);	
	
	printf("======================\n");
	if(GET_SPEED_INDEX((getSpeedIndex(speedIndex)))) {speed = getSpeed(speedIndex);}
	printf("5 index:%d speed: %d\n", speedIndex, speed);
	
	
	printf("======================\n");
	if((getSpeedIndex(speedIndex) < 8))
	{
		speed = getSpeed(speedIndex);
	}
	printf("6 index:%d speed: %d\n", speedIndex, speed);
	
	speed = 0xffffffff;
	return 0;    
}
