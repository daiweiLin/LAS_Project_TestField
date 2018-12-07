
%Cam_2_3pm.time = Cam_2_3pm.time + Cam_1_2pm.time(end);
Cam_1_4pm = table([Cam_1_2pm.time; Cam_2_3pm.time + Cam_1_2pm.time(end); Cam_3_4pm.time + Cam_1_2pm.time(end) + Cam_2_3pm.time(end)], ...
    [Cam_1_2pm.occ; Cam_2_3pm.occ;Cam_3_4pm.occ],'VariableNames',{'time', 'occ'});


%%

i_span = [36000, 72000]
c_span = [86600, 189090]


figure
p1 = subplot(2,1,1);
plot(p1,IR_1_4pm.time(1:i_span(1)),IR_1_4pm.occ(1:i_span(1)));
title(p1,'IR Occupancy');
p2 = subplot(2,1,2);
plot(p2,Cam_1_4pm.time(1:c_span(1)),Cam_1_4pm.occ(1:c_span(1)));
title(p2,'CAM Occupancy');

figure
p1 = subplot(2,1,1);
plot(p1,IR_1_4pm.time(i_span(1)+1:i_span(2)),IR_1_4pm.occ(i_span(1)+1:i_span(2)));
title(p1,'IR Occupancy');
p2 = subplot(2,1,2);
plot(p2,Cam_1_4pm.time(c_span(1)+1:c_span(2)),Cam_1_4pm.occ(c_span(1)+1:c_span(2)));
title(p2,'CAM Occupancy');

figure
p1 = subplot(2,1,1);
plot(p1,IR_1_4pm.time(i_span(2)+1:end),IR_1_4pm.occ(i_span(2)+1:end));
title(p1,'IR Occupancy');
p2 = subplot(2,1,2);
plot(p2,Cam_1_4pm.time(c_span(2)+1:end),Cam_1_4pm.occ(c_span(2)+1:end));
title(p2,'CAM Occupancy');