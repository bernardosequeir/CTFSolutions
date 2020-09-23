i=1
while [ $i -le 7 ]
do 
	mkdir Leviathan$(($i-1))-$i
	cd Leviathan$(($i-1))-$i
	touch explanation.md
  touch pass.txt
	cd ..
	((i++))
done 