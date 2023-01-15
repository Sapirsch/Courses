% This function is used in the SapirMergeSort function, and returns an array of the indexes of each cycle of division by
%2 returns an odd number - therefore a breaking point

function inx_of_breaking_point = InxOfBreakingPoints(n)

    num = n;
    inx_of_breaking_point = [];
    
    for i=1:n/2
        
        if num < 2
           
            break
       
        elseif rem(num,2) == 1
            
            inx_of_breaking_point(end+1) = i;
            
        end
        
        num = floor(num/2);
        
    end
    
    end