#!/bin/bash
pass="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"

for i in {1000..10000..1}
do
        echo "$pass $i" | nc localhost 30002 >> output &
done