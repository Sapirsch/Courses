% I this folder we explored different versions of the sorting algorithms and compared their running time

% In these scripts we explored the MergeSort function by its two approchains: bottom-up and top-bottom (recursion).

% This specific script presents my version of bottom-up MergeSort  

function sorted_arr = SapirMergeSort(unsorted_arr)

    n=length(unsorted_arr);
    tmp_arr = unsorted_arr;
    
    % This vars are for the number of cycle to do
    inx_of_breaking_point = InxOfBreakingPoints(n);
    len_idx = length(inx_of_breaking_point);
    
    % Loop for increasing the width
    for i=0:floor(log2(n))+len_idx-1
       
        width = 2.^i;   
        step = width + i + 1;
        to = width.*(floor(n/width)-1) + 1;
        
        % Loop for traversing the temp array
        for j=1:step:to
            
            % Leaving the last stract untouched (when there is an odd
            % number of stracts)
            if j == (n - width + 1)
                
                break
            
            % Merging the unevened length last stracts (when we have an even number of stracts)    
            elseif j == width * (floor(n/width) - 1) + 1
                
                arr1 = tmp_arr(j:j+width-1);
                arr2 = tmp_arr(j+width:min(j+width*2-1, n));
                
                tmp_arr(j:min(j+width*2-1, n)) = SapirMerge2(arr1,arr2);
                
                break
                
            else
            
            arr1 = tmp_arr(j:j+width-1); 
            arr2 = tmp_arr(j+width:min(j+width*2-1, n));
    
            tmp_arr(j:min(j+width*2-1, n)) = SapirMerge2(arr1,arr2);  
            
            end
    
        end
    
    end
    
    sorted_arr = tmp_arr;
    
    end