## 1) scisnerof 70 points
   use python to reverse 4 byte at at a time in a file from reverse to get png image
 
 ##  2) Flag Collection
      we were given lot of image and thumbs.db file
      we have to extract thumbs,db using 7z x Thumbs.db -o out
      then we had to remove first 24 byte of all image using 
            for i in *; do dd if="$i" of="$i-" bs=1 skip=24 ;done
     
   
