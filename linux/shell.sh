#!/bin/bash
#****************************************************************
#								*
#version: draft							*
#author: dpeng							*	
#function: get ten input number and got the min/max/sum of it	*
#								*
#****************************************************************
declare -i max=0
declare -i min=0
declare -i sum=0
declare -i i=1
echo "#***********************************************************"
echo "#please input an number without space then press enter     *"
echo "#this shell script will calc the max min sum of what you   *"
echo "#have already entered                                      *" 
echo "#***********************************************************"
while ((i<=10));
do
   read x
   if ((i == 1))
     then
          max=$x;
	  min=$x;
   fi
   sum=`expr $sum + $x`
   if ((max<x))
     then
          max=$x
   fi
   if ((x<min))
     then
          min=$x
   fi   
    i=$(($i+1))
    echo current: x=$x i=$i max=$max min=$min sum=$sum
done
echo "result: sum=$sum max=$max min=$min"
