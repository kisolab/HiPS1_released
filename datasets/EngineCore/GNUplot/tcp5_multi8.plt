set term x11
set datafile separator ","

set xtics nomirror
set ytics nomirror

set grid ytics

set xr[0:25]
set yr[0:2.25]

set xlabel 'Number of transition firings [M]'
set ylabel 'Memory usage [GBytes]'

  plot 'tcp5_multi8.csv' u 1:5 with line linewidth 5 title 'Proposed Algorithm 4'
replot 'tcp5_multi8.csv' u 1:4 with line linewidth 5 title 'Conventional Algorithm 2'

##set term postscript eps enhanced size 4.0,3.0 font "Courier,14"
set term postscript eps color enhanced "Helvetica" 21
set out "tcp5_multi8.eps"

replot

set output
set terminal x11
