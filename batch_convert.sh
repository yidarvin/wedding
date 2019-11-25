#!/bin/bash
for f in $HOME/Documents/origami/origami_src/*.jpg
do
  python jpg2svg.py --file $f --temp $HOME/Documents/origami/origami_tmp
done

for f in $HOME/Documents/origami/origami_tmp/*.png
do
  echo $f
  echo ${f/png/ppm}
  convert $f $HOME/Documents/origami/origami_tmp/asdf.ppm #${f/png/ppm}
done
