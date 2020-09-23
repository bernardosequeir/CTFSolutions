i=1
while [ $i -le 34 ]
do 
	mkdir Bandit$(($i-1))-$i
	cd Bandit$(($i-1))-$i
	touch explanation.md
	cd ..
	((i++))
done 
