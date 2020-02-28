if [ -n "$1" ];then
sshpass -f ./Bandit$(($1-1))-$1/pass.txt ssh bandit.labs.overthewire.org -p 2220 -l bandit$1 
else
  echo "Specify level please!"
fi  