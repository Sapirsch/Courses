% This is my version of the sort function

function sorted_array = SapirSort(unsorted_array)

    n = length(unsorted_array);
    sorted_array = zeros(1,n);
    
    for i=1:n
        
        min_num = min(unsorted_array);
        sorted_array(i) = min_num;
        
        min_idx = find(unsorted_array == min_num);
        unsorted_array(min_idx) = NaN;   
        
    end
    
    end