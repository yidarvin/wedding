#!/bin/bash
for f in $HOME/origami/origami_src/*.jpg; do python jpg2svg.py --file $f --temp $HOME/origami/origami_tmp; done

for f in $HOME/origami/origami_tmp/*.png; do convert $f ${f/png/ppm}; potrace -s ${f/png/ppm} -o ${f/png/svg} -C $"#FFFFFF"; done

for f in $HOME/origami/origami_tmp/*.svg; do mv $f $HOME/origami/origami_dst/; done
