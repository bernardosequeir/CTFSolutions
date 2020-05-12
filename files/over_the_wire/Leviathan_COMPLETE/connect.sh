if [ -n "$1" ];then
sshpass -f ./Leviathan$(($1-1))-$1/pass.txt ssh leviathan.labs.overthewire.org -p 2223 -l leviathan$1 
else
  echo "Specify level please!"
fi  