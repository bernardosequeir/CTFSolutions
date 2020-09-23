i=1
while [ $i -le 7 ]
do 
	mkdir Krypton$(($i-1))-$i
	cd Krypton$(($i-1))-$i
	touch explanation.md
	cd ..
	((i++))
done 
