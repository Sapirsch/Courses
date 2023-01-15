% This script measures the running time of Sapir_sort and the MATLAB sort function as a function of the number of elements in an array

n = [10.^0, 10.^1, 10.^2, 10.^3, 10.^4, 10.^5, 2.*10.^5, 3.*10.^5, 4.*10.^5, 5.*10.^5];

y1 = zeros(1,length(n));

for i=1:length(n)
    
    a = randperm(n(i));
    
    tic;
    Sapir_sort(a);
    time = toc;
    
   y1(i) = time;
    
end


y2 = zeros(1,length(n));

for k=1:length(n)
    
    b = randperm(n(k));
    
    tic;
    sort(b);
    time = toc;
    
   y2(k) = time;
    
end

x1 = n;
x2 = n;

plot(x1,y1,'-o','color','b','LineWidth',2)
hold on
plot(x2,y2,'-o','color','k','LineWidth',2)
title('Running time of various sorting algorithems as a function of array length')
xlabel('Array length')
ylabel('Time [seconds]')
legend('SapirSort', 'MatlabSort', 'SapirMergeSort')




