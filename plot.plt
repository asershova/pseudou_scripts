set parametric
set urange [0:0.1]
set vrange [0:14]
set xlabel "GSM1464218"
set ylabel "GSM1464219"
set zlabel "log(starts)"
splot "GSM1464218_GSM1464219_evs.joined" using ($5/$6):($10/$11):(log($5)) with dots, "experiment.full" using ($5/$6):($10/$11):(log($5)),  u*8,u,v lc "blue", v/14,u,log(5) lc "blue" , 0.1,u,v lc "blue", u*8,u*8-0.3,v lc "green" , u*8,0.1,v lc "green"
