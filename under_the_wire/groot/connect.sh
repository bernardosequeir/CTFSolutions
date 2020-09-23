#!/bin/sh
sshpass -f ./groot$1/pass.txt ssh groot.underthewire.tech -p 22 -l groot$1 
