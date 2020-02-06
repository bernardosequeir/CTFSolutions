i=1
while [ $i -le 15 ]
do 
	mkdir cyborg$i
	cd cyborg$i
	touch explanation.md
	cd ..
	((i++))
done 
