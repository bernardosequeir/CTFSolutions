#!/bin/bash
pass="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
echo "$pass 0000" 
for t in {0..9}
do 
  for h in {0..9}
  do 
    for d in {0..9}
    do 
      for u in {0..9}
      do 
        echo "$pass $t$h$d$u"
      done
    done
  done
done