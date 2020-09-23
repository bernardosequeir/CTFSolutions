#!/bin/sh
sshpass -f ./cyborg$1/pass.txt ssh cyborg.underthewire.tech -p 22 -l cyborg$1 
