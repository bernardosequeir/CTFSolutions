if [ -n "$1" ];then
sshpass -f ./Krypton$(($1-1))-$1/pass.txt ssh krypton.labs.overthewire.org -p 2222 -l krypton$1 
else
  echo "Specify level please!"
fi  