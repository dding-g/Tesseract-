<?php
    //exec("env", $output, $return_var);
    exec("/home/pi/sp_pj/mpich3_install/bin/mpirun -np 4 -f /home/pi/myProject/machinefile /home/pi/myProject/parell_task.o > /dev/null &", $output, $return_var);
    print_r($output);