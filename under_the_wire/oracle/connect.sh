#!/bin/sh
sshpass -f ./oracle$1/pass.txt ssh oracle.underthewire.tech -p 22 -l oracle$1 
