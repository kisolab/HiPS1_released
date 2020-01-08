set term x11
set datafile separator ","

set xtics nomirror
set ytics nomirror

set grid ytics

set xr[0:210]
set yr[0:4]

set xlabel 'Number of transition firings [M]'
set ylabel 'Memory usage [GBytes]'

  plot 'tcp6_single.csv' u 1:5 with line linewidth 5 title 'Proposed Algorithm 3'
replot 'tcp6_single.csv' u 1:4 with line linewidth 5 title 'Conventional Algorithm 1'

##set term postscript eps enhanced size 4.0,3.0 font "Courier,14"
set term postscript eps color enhanced "Helvetica" 21
set out "tcp6_single.eps"

replot

set output
set terminal x11
