<?php
    $name       = $_FILES['file_upload']['name'];  
    $temp_name  = $_FILES['file_upload']['tmp_name'];  
    if(isset($name)){
        if(!empty($name)){      
            $location = '/home/pi/myProject/img_path/'; 
            if(move_uploaded_file($temp_name, $location.$name)){
                echo 'File uploaded successfully ';
                //exec("./shell_script_practice.sh", $output, $return_var);
                exec("/home/pi/sp_pj/mpich3_install/bin/mpirun -np 4 -f /home/pi/myProject/machinefile /home/pi/myProject/parell_task.o", $output, $return_var);
                print_r($output);
            }
        }
    } else {
        echo 'You should select a file to upload !!';
    }
