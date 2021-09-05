#!/bin/bash
#change the above line to any shell you are using
declare -a exploit;

value=10

target="./a.out" #change this to the target(if its a server, you may need netcat[nc])
for((i=0; i != $value; i++))
do
	exploit+="A"; # you can choose any one that you want
done
#This is the attack
printf $exploit"stuff-here" | $target
