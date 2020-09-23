i=1
while [ $i -le 15 ]
do 
	mkdir groot$i
	cd groot$i
	touch explanation.md
	cd ..
	((i++))
done 
