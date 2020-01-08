set term x11
set datafile separator ","

set xtics nomirror
set ytics nomirror

set grid ytics

set xr[0:210]
set yr[0:15]

set xlabel 'Number of transition firings [M]'
set ylabel 'Memory usage [GBytes]'

  plot 'tcp6_multi8.csv' u 1:3 with line linewidth 5 title 'Proposed Algorithm 4'
replot 'tcp6_multi8.csv' u 1:2 with line linewidth 5 title 'Conventional Algorithm 2'

##set term postscript eps enhanced size 4.0,3.0 font "Courier,14"
set term postscript eps color enhanced "Helvetica" 21
set out "tcp6_multi8.eps"

replot

set output
set terminal x11
