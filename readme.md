# RFL-empirical-study AE

## Introduction

We present the data and the code of the RFL empirical study in each directory according to the RQ.
In each directory, you can follow the README.md to reproduce the results.
After collecting all the results, you can run the `.ipynb` file in that directory to generate the figures in `.pdf` format.

---- rq1
    |---- data
        rfl-path_generated_data
    |---- code
        plot.py
    |---- README.md
        bash.sh
        see images in imgs, corresponding to the figures/table/text.N in the paper
    |---- bash.sh
        cd /path/to/rfl-path/rq1
        do thing
        plot.py
    |---- imgs
        |---- *.pdf
-- rq2

## Environment setup

Considering the complexity of the environment setup, we provide a docker container, which can be reached by ssh, to run the code. 
Most of the RQs can be reproduced in the docker container. 
The docker container can be reached by the following command:

```bash
ssh -p tongchuan_port ae@panda_ip
# The password is `rfl_ae_docker`.

docker attach rfl_ae
```

However, some measurement experiments may not be able to run in the docker container because they need specific hardware, such as the `NVME` disk and `e1000` NIC.
We will provide a PC equipped with them.
The specific steps to reproduce the results will be provided in the README.md in the corresponding directory.


<!-- In these experiments, it may need to reboot the PC to change the kernel version for supporting the driver. You can send an issue to We will provide the detailed steps in the README.md in the corresponding directory. -->
