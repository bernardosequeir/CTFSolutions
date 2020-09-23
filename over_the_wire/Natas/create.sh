i=1
numberOfLevels=34
while [ $i -le $numberOfLevels ]
do 
	mkdir Natas$(($i-1))-$i
	cd Natas$(($i-1))-$i
	echo "```html```">explanation.md
  touch pass.txt
	cd ..
	((i++))
done 