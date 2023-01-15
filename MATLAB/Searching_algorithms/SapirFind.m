% This script shows my version of the find function

function inx = SapirFind(num, arr)

    len = length(arr);
    
    for inx=1:len
    
        if arr(inx) == num
            break
        end
    
    end
    
    if arr(inx) ~= num
        inx = NaN;
    end
    
    end