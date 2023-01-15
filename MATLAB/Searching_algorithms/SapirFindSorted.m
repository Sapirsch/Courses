% This function returns the first index correspoding to the input argument in a sorted array

function inx = SapirFindSorted(num, sorted_arr)

    len = length(sorted_arr);
    n = len;
    temp_arr = sorted_arr;
    inx = 0;
    
    for i=1:log2(len)
    
        if temp_arr(floor(n/2)) == num
    
            inx = inx + floor(n/2);
    
            break
    
        elseif sorted_arr(floor(n/2)) > num
            
            temp_arr = temp_arr(1:floor(n/2));
            n = floor(n/2);
    
        else 
            
           temp_arr = temp_arr(floor(n/2)+1:n); 
           
           inx = inx + floor(n/2); 
           n = floor(n/2);
           
        end
        
    end
    
    if sorted_arr(inx) ~= num
    
        inx = NaN;
        
    end
    
    end