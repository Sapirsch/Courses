% This script shows the recursive version for the find function

function inx = SapirFindRec(num, arr, start_ind)

    if start_ind == length(arr) 
        
        if arr(start_ind) == num
            inx = start_ind; 
        else
            inx = NaN;
        end
        
    elseif arr(start_ind) == num
        inx = start_ind;
    else
        inx = SapirFindRec(num, arr, start_ind+1);
    end
    
    end
end    