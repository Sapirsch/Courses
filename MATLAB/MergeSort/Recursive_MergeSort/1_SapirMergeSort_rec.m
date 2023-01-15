% This is my recursive version of the MergeSort function

function sorted_arr = SapirMergeSortRec(unsorted_arr)

    len = length(unsorted_arr);
    n = len;
    
    if len == 1
           
       return;
            
    else
        
        n = floor(n/2);
        arr1 = unsorted_arr(1:n);
        arr2 = unsorted_arr(n+1:end);
        
        disp(arr1)
        disp(arr2)
        
        sorted_arr1 = SapirMergeSortRec(arr1);
        sorted_arr2 = SapirMergeSortRec(arr2);
        
        sorted_arr = SapirMerge2(sorted_arr1, sorted_arr2);
    
    end
    
    end