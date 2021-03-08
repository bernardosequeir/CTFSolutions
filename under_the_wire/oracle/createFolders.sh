i=1
while [ $i -le 15 ]
do 
	mkdir oracle$i
	cd oracle$i
	touch explanation.md
	cd ..
	((i++))
done 
