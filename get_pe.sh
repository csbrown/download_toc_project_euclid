HEADER=$(sed "s/^/--header='/g" header | sed "s/$/'/g")
eval wget $HEADER $1 -O $2
