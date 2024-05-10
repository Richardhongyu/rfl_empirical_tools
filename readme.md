# RFL-empirical-study AE

## Environment setup

Considering the complexity of the environment setup, we provide a docker container, which can be reached by ssh, to run the code.
This repo is already cloned in '/workspace/rfl_empirical_tools'.

```bash
ssh -p 9101 ae@149.129.120.139
# The password is `rfl_ae_docker`.

docker attach rfl_ae
```

## Introduction

We present the data and the code of the RFL empirical study in each directory according to the RQ.
<!-- After collecting all the results, you can run the `bash.sh` file in that directory to generate the figures in `.pdf` format. -->
Here is an example of the directory structure.

```bash
---- rqN_figure/tableM  
    |---- data  
        rfl_generated_data  
    |---- code  
        preprocess/calculate/plot scripts  
    |---- imgs/table  
        figureM.pdf/tableM_data  
    |---- README.md  
        give instuctions about how to run the code and indicate which figures/table/text this repo corresponds to  
    |---- bash.sh  
        the bash is organized as follows:  
        1) cd /path/to/rfl-path/rq1  
        2) call scripts  
        3) plot.py  
        4) cp data/imgs  
```

In each directory, you can follow the `README.md` to reproduce the results.
All the code we introduce in the paper is in the `code` directory.
To simplify the reproduction process, we provide a remote docker container.


<!-- ## special cases

Most of the RQs can be reproduced in the docker container. 
However, some measurement experiments may not be able to run in the docker container because they need specific hardware, such as the `NVME` disk and `e1000` NIC.
We will provide a PC equipped with them.
The specific steps to reproduce the results will be provided in the README.md in the corresponding directory. -->


<!-- In these experiments, it may need to reboot the PC to change the kernel version for supporting the driver. You can send an issue to We will provide the detailed steps in the README.md in the corresponding directory. -->
