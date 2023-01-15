% This script measure the running time of both of the SapirMergeSort function (bottom-up and recursive versions) as a function of the number of elements in an array

n = [10.^0, 10.^1, 10.^2, 10.^3, 10.^4, 10.^5, 2.*10.^5, 3.*10.^5, 4.*10.^5, 5.*10.^5];

y = ones(1,length(n));

for i=1:length(n)
    
    a = randperm(n(i));
    
    tic;
    SapirMergeSort(a);
    time = toc;
    
   y(i) = time;
    
end

x = n;

plot(x,y,'o-')