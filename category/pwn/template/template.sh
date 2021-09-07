#!/bin/bash
function run()	{
	expect <<EOF
	eval spawn $1;
 	expect "input prompt here";
	send "$2\r"

	interact
EOF
# NOTE: you can use "expect -d" to debug if it does not work the first time around
}
declare -a exploit;

value=10

target="./a.out" #change this to the target
for((i=0; i != $value; i++))
do
	exploit+="A";
done
exploit+="input malicious code here"
#This is how the attack is lauunched
run $target $exploit
