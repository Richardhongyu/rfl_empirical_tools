CONTAINER ID   IMAGE                            COMMAND                  CREATED        STATUS        PORTS                                                                                                                               NAMES
4a1cd57721f8   rros_dockerfile_test             "/bin/bash"              6 days ago     Up 6 days                                                                                                                                         rust-raspberrypi-OS
bff8ae380815   l543306408/bupt-rtos:v0.3        "/bin/bash"              9 days ago     Up 9 days                                                                                                                                         sty
d2f876f9a42c   rros_dockerfile_test:latest      "/bin/bash"              2 weeks ago    Up 2 weeks    0.0.0.0:8989->8080/tcp, :::8989->8080/tcp                                                                                           rros_jenkins
2c1b1d04cf79   5a534a6d8270                     "/bin/bash"              2 weeks ago    Up 9 days                                                                                                                                         test_rros
2956c958a175   rros_dockerfile_test:latest      "/bin/bash"              3 weeks ago    Up 3 weeks                                                                                                                                        djjnew
7a29d1bc6721   lava-test-1_master               "/root/entrypoint.sh…"   4 weeks ago    Up 4 weeks    3079/tcp, 5500/tcp, 5555-5556/tcp, 8000-8001/tcp, 0.0.0.0:9999->80/tcp                                                              lava-test-1_master_1
405b58cae38e   lava-test-1_lab-slave-1          "/root/entrypoint.sh…"   4 weeks ago    Up 4 weeks    0.0.0.0:80->80/tcp, :::80->80/tcp, 10.161.28.28:69->69/udp, 0.0.0.0:61950-62000->61950-62000/tcp, :::61950-62000->61950-62000/tcp   lava-test-1_lab-slave-1_1
43c7c7756ed8   rros_dockerfile_test             "/bin/bash"              6 weeks ago    Up 6 weeks                                                                                                                                        syx_dovetail_riscv_dev
aedc1e625f86   l543306408/bupt-rtos:civ4        "/bin/bash"              6 weeks ago    Up 6 weeks                                                                                                                                        rros_ci_7
e832eebee428   l543306408/bupt-rtos:v0.3        "/bin/bash"              2 months ago   Up 2 months                                                                                                                                       szt
4f4e183ec623   fedora                           "/bin/bash"              2 months ago   Up 2 months                                                                                                                                       lhy_image_builder_fedora_2
18c230581946   copr_backend-build               "/usr/bin/tini -- /r…"   2 months ago   Up 2 months                                                                                                                                       copr_backend-build_1
3d2fcb84fd81   copr_backend-action              "/usr/bin/tini -- /r…"   2 months ago   Up 2 months                                                                                                                                       copr_backend-action_1
ba194e2428b6   copr_backend_httpd               "container-entrypoin…"   2 months ago   Up 2 months   8080/tcp, 0.0.0.0:5002->5002/tcp, :::5002->5002/tcp, 8443/tcp                                                                       copr_backend_httpd_1
8c2887e35fe6   copr_frontend                    "/entrypoint"            2 months ago   Up 2 months   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp                                                                                           copr_frontend_1
207bdb7287d7   copr_resalloc                    "/usr/bin/resalloc-s…"   2 months ago   Up 2 months                                                                                                                                       copr_resalloc_1
3543b84a6c28   copr_backend-log                 "/usr/bin/tini -- /u…"   2 months ago   Up 2 months                                                                                                                                       copr_backend-log_1
563c1cdc8a67   copr_database                    "container-entrypoin…"   2 months ago   Up 2 months   0.0.0.0:5009->5432/tcp, :::5009->5432/tcp                                                                                           copr_database_1
b3ae640187cb   centos/redis-32-centos7          "container-entrypoin…"   2 months ago   Up 2 months   6379/tcp                                                                                                                            copr_redis_1
3ffe498dbaf7   copr_distgit-httpd               "/usr/bin/tini -- /u…"   2 months ago   Up 2 months   0.0.0.0:5001->5001/tcp, :::5001->5001/tcp                                                                                           copr_distgit-httpd_1
a2b0c8063c0f   copr_builder                     "/usr/sbin/sshd -D"      2 months ago   Up 2 months                                                                                                                                       copr_builder_1
ded3f0987738   copr_keygen-httpd                "/usr/bin/tini -- /u…"   2 months ago   Up 2 months                                                                                                                                       copr_keygen-httpd_1
36a87966262a   copr_keygen-signd                "/usr/bin/tini -- /s…"   2 months ago   Up 2 months                                                                                                                                       copr_keygen-signd_1
216cc3170bce   copr_distgit                     "/usr/bin/tini -- ba…"   2 months ago   Up 2 months                                                                                                                                       copr_distgit_1
104f78e6ce6e   fedora                           "/bin/bash"              2 months ago   Up 2 months                                                                                                                                       lhy_image_builder_fedora
70de9cdec0bc   centos                           "/bin/bash"              2 months ago   Up 2 months                                                                                                                                       lhy_image_builder
2a80a433f7fa   l543306408/bupt-rtos:syzkaller   "/bin/bash"              2 months ago   Up 2 months   0.0.0.0:5656->56741/tcp, :::5656->56741/tcp                                                                                         syzkaller-pri-1
a498cdf4dbda   ubuntu:20.04                     "/bin/bash"              2 months ago   Up 2 months                                                                                                                                       ci-test-pri
418dd5598456   ubuntu:20.04                     "/bin/bash"              2 months ago   Up 2 months                                                                                                                                       ci-test
5c6bd2a4534a   mysql:5.7                        "docker-entrypoint.s…"   2 months ago   Up 2 months   33060/tcp, 0.0.0.0:32778->3306/tcp, :::32778->3306/tcp                                                                              gitmaya_mysql_1
106ec91ba855   connectai/gitmaya                "/entrypoint.sh cele…"   2 months ago   Up 2 months                                                                                                                                       gitmaya_beat_1
9bc501789aa5   connectai/gitmaya                "/entrypoint.sh guni…"   2 months ago   Up 2 months   0.0.0.0:32777->8888/tcp, :::32777->8888/tcp                                                                                         gitmaya_gitmaya_1
774e11dfdee9   connectai/gitmaya                "/entrypoint.sh bash…"   2 months ago   Up 2 months   0.0.0.0:32779->5555/tcp, :::32779->5555/tcp                                                                                         gitmaya_flower_1
19fe62e6a6f4   connectai/gitmaya                "/entrypoint.sh cele…"   2 months ago   Up 2 months                                                                                                                                       gitmaya_worker_1
1c60a75ab613   connectai/gitmaya-proxy          "/app/docker-entrypo…"   2 months ago   Up 2 months   0.0.0.0:8000->80/tcp, :::8000->80/tcp, 0.0.0.0:8001->81/tcp, :::8001->81/tcp                                                        gitmaya_proxy_1
f29ade3a6ae3   redis:alpine                     "docker-entrypoint.s…"   2 months ago   Up 2 months   0.0.0.0:32776->6379/tcp, :::32776->6379/tcp                                                                                         gitmaya_redis_1
6a4de5340e89   5a534a6d8270                     "/bin/bash"              3 months ago   Up 3 months                                                                                                                                       syx_dev
8a83d9ad86e1   bf40b7bc7a11                     "/bin/bash"              3 months ago   Up 3 months                                                                                                                                       djjlang
a78cffcf5fac   mllm:latest                      "/sbin/entrypoint.sh"    4 months ago   Up 4 months   0.0.0.0:9822->22/tcp, :::9822->22/tcp                                                                                               mllm_yrj
0fa22cf89c8f   ubuntu:22.04                     "/bin/bash"              4 months ago   Up 4 months                                                                                                                                       sweet_sammet
cc72aa71e66f   l543306408/bupt-rtos:civ4        "/bin/bash"              4 months ago   Up 4 months                                                                                                                                       rros_ci_6
b901913c4cce   rros_dev                         "/bin/bash"              4 months ago   Up 4 weeks                                                                                                                                        hjt_dev
4b9efe247121   l543306408/bupt-rtos:civ3        "/bin/bash"              4 months ago   Up 4 months                                                                                                                                       rros_ci_5
59b677c66590   l543306408/bupt-rtos:civ2        "/bin/bash"              4 months ago   Up 4 months                                                                                                                                       rros_ci_2
c6b487f3e4fd   rros_dev:latest                  "/bin/bash"              4 months ago   Up 4 months                                                                                                                                       qqc
a89788d8963a   l543306408/bupt-rtos:v0.3        "bash"                   4 months ago   Up 4 months                                                                                                                                       qxk
0dc70f5276f6   l543306408/bupt-rtos:v0.3        "/bin/bash"              4 months ago   Up 4 months                                                                                                                                       wbc
a868ac9423df   l543306408/bupt-rtos:v0.3        "/bin/bash"              5 months ago   Up 2 months                                                                                                                                       yyx
dc23300904e5   l543306408/bupt-rtos:v0.3        "/bin/bash"              5 months ago   Up 3 weeks 

# 使用awk截取containerid 去掉第一行
docker ps | awk '{if(NR>1) print $1}'