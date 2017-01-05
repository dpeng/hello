// hello.cpp : Defines the entry point for the console application.
//

#include "stdafx.h" 
#include<iostream>
#include<cmath>
//#include<Windows.h>
#include<afx.h>
char gKey[37] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-'};

void main()
{
	FILE *fp;
	char ch;
	int i,j,k,l,m;
	char *tempkey;
	tempkey = (char*)malloc(sizeof(char)*5);
	memset(tempkey, 0, sizeof(tempkey));
	if((fp=fopen("words.txt","a"))==NULL){
		printf("Cannot open file strike any key exit!");
		exit(1);
	}
	//only one character
	for(i = 0 ; i < sizeof(gKey)-1; i++){
		sprintf(tempkey++, "%c", gKey[i]);
		sprintf(tempkey, "\n");
		tempkey-=1;
		fwrite(tempkey,sizeof(char),sizeof(char)*2, fp);
	}
	//two characters
	for(i = 0 ; i < sizeof(gKey)-1; i++){
		for(j = 0; j < sizeof(gKey)-1; j++){
			sprintf(tempkey++, "%c", gKey[i]);
			sprintf(tempkey++, "%c", gKey[j]);
			sprintf(tempkey, "\n");
			tempkey-=2;
			fwrite(tempkey,sizeof(char),sizeof(char)*3, fp);
		}
	}
	//three caracters
	for(i = 0 ; i < sizeof(gKey)-1; i++){
		for(j = 0; j < sizeof(gKey); j++){
			for(k = 0; k < sizeof(gKey)-1; k++){
				sprintf(tempkey++, "%c", gKey[i]);
				sprintf(tempkey++, "%c", gKey[j]);
				sprintf(tempkey++, "%c", gKey[k]);
				sprintf(tempkey, "\n");
				tempkey-=3;
				fwrite(tempkey,sizeof(char),sizeof(char)*4, fp);
			}
		}
	}
	fclose(fp);
}

