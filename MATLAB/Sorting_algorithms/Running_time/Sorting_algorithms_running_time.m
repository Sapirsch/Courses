% This script compares the running time of both SapirSort and SapirMergeSort as a function of the number of elements in an array

n = [10.^0, 10.^1, 10.^2, 10.^3, 10.^4, 10.^5, 2.*10.^5, 3.*10.^5, 4.*10.^5, 5.*10.^5];

y_SapirSort = ones(1,length(n));

for i=1:length(n)
    
    a = randperm(n(i));
    
    tic;
    SapirSort(a);
    time = toc;
    
   y_SapirSort(i) = time;
    
end


y_SapirMergeSort = ones(1,length(n));

for j=1:length(n)
    
    a = randperm(n(j));
    
    tic;
    SapirSort(a);
    time = toc;
    
   y_SapirMergeSort(j) = time;
    
end


x = n;

plot(x,y_SapirSort,'-o','color','b','LineWidth',2)
hold on

plot(x,y_SapirMergeSort,'-o','color','r','LineWidth',2)

title('Running time of various sorting algorithems as a function of array length')
xlabel('Array length')
ylabel('Time [seconds]')
legend('SapirSort', 'SapirMergeSort')




