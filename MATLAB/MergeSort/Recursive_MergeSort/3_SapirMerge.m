% This function is used in the the SapirMergeSort function

function sorted_arr_combined = SapirMerge2(sorted_arr1,sorted_arr2)

    arr1_ind = 1;
    arr2_ind = 1;
    
    arr3_len = length(sorted_arr1) + length(sorted_arr2);
    
    for i=1:arr3_len
        
        % check if both arrays are not completed
        if (arr1_ind<=length(sorted_arr1) && arr2_ind<=length(sorted_arr2))
        
            if (sorted_arr1(arr1_ind) <= sorted_arr2(arr2_ind))
                sorted_arr_combined(i) = sorted_arr1(arr1_ind);
                arr1_ind = arr1_ind +1;
            else
                sorted_arr_combined(i) = sorted_arr2(arr2_ind);
                arr2_ind = arr2_ind +1;
            end
    
        elseif (arr1_ind>length(sorted_arr1))
            sorted_arr_combined = [sorted_arr_combined sorted_arr2(arr2_ind:end)];
            break;
        else (arr2_ind>length(sorted_arr2))
            sorted_arr_combined = [sorted_arr_combined sorted_arr1(arr1_ind:end)];
            break;
        end
        
    end
    
    
    