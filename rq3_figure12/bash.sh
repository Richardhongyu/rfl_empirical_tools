cp code/block.py /workspace/linux-doc-coverage
cp code/plot.py /workspace/linux-doc-coverage
pushd /workspace/linux-doc-coverage
# this script needs huge time to run lines and bugs analyze, you can uncomment this in a night:)
# data.txt is the rename of MAINTAINERS file, just delete the begin lines and leave the maintainer blocks
# python3 block.py
# consider the blocks that have the same mail list as one community
# The log is as follows:
    # 290 L:      linux-media@vger.kernel.org
    # 209 L:      netdev@vger.kernel.org
    #  88 L:      linux-kernel@vger.kernel.org
    #  82 L:      linux-iio@vger.kernel.org
    #  74 L:      platform-driver-x86@vger.kernel.org
    #  66 L:      linux-hwmon@vger.kernel.org
    #  59 L:      linux-scsi@vger.kernel.org
    #  57 L:      linux-usb@vger.kernel.org
    #  53 L:      linux-pm@vger.kernel.org
    #  53 L:      linux-pci@vger.kernel.org
    #  47 L:      linux-i2c@vger.kernel.org
    #  46 L:      linux-wireless@vger.kernel.org
    #  45 L:      linux-input@vger.kernel.org
    #  34 L:      linux-gpio@vger.kernel.org
    #  31 L:      linux-edac@vger.kernel.org
    #  30 L:      linux-crypto@vger.kernel.org
    #  29 L:      bpf@vger.kernel.org
    #  28 L:      linux-renesas-soc@vger.kernel.org
    #  27 L:      linux-rdma@vger.kernel.org
    #  27 L:      linux-mips@vger.kernel.org
    #  26 L:      linux-omap@vger.kernel.org
    #  26 L:      linux-arm-msm@vger.kernel.org
    #  25 L:      linux-fbdev@vger.kernel.org
    #  23 L:      linux-fsdevel@vger.kernel.org
    #  22 L:      kvm@vger.kernel.org
    #  18 L:      linux-mmc@vger.kernel.org
    #  17 L:      linux-samsung-soc@vger.kernel.org
    #  16 L:      linux-s390@vger.kernel.org
    #  14 L:      linux-spi@vger.kernel.org
    #  13 L:      linux-can@vger.kernel.org
    #  13 L:      dmaengine@vger.kernel.org
    #  12 L:      linux-acpi@vger.kernel.org
    #  10 L:      linux-tegra@vger.kernel.org
    #   9 L:      linux-serial@vger.kernel.org
    #   9 L:      linux-hams@vger.kernel.org
    #   8 L:      linux-wpan@vger.kernel.org
    #   8 L:      linux-integrity@vger.kernel.org
    #   8 L:      linux-ide@vger.kernel.org
    #   8 L:      linux-block@vger.kernel.org
    #   8 L:      keyrings@vger.kernel.org
    #   7 L:      target-devel@vger.kernel.org
    #   6 L:      linux-watchdog@vger.kernel.org
    #   6 L:      linux-rtc@vger.kernel.org
    #   5 L:      linux-remoteproc@vger.kernel.org
    #   5 L:      linux-hardening@vger.kernel.org
    #   5 L:      linux-fpga@vger.kernel.org
    #   5 L:      linux-doc@vger.kernel.org
    #   5 L:      linux-clk@vger.kernel.org
    #   4 L:      linux-trace-kernel@vger.kernel.org
    #   4 L:      linux-security-module@vger.kernel.org
    #   4 L:      linux-parisc@vger.kernel.org
    #   4 L:      linux-kselftest@vger.kernel.org
    #   4 L:      linux-efi@vger.kernel.org
    #   4 L:      linux-bluetooth@vger.kernel.org
    #   4 L:      cgroups@vger.kernel.org
    #   3 L:      rcu@vger.kernel.org
    #   3 L:      linux-leds@vger.kernel.org
    #   3 L:      linux-ext4@vger.kernel.org
    #   3 L:      linux-arch@vger.kernel.org
    #   3 L:      devicetree@vger.kernel.org
    #   3 L:      ceph-devel@vger.kernel.org
    #   2 L:      sparclinux@vger.kernel.org
    #   2 L:      linux-xfs@vger.kernel.org
    #   2 L:      linux-trace-devel@vger.kernel.org
    #   2 L:      linux-pwm@vger.kernel.org
    #   2 L:      linux-nfs@vger.kernel.org
    #   2 L:      linux-kbuild@vger.kernel.org
    #   2 L:      linux-hyperv@vger.kernel.org
    #   2 L:      linux-cxl@vger.kernel.org
    #   2 L:      linux-cifs@vger.kernel.org
    #   1 L:      util-linux@vger.kernel.org
    #   1 L:      stable@vger.kernel.org
    #   1 L:      selinux@vger.kernel.org
    #   1 L:      rust-for-linux@vger.kernel.org
    #   1 L:      reiserfs-devel@vger.kernel.org
    #   1 L:      netfilter-devel@vger.kernel.org
    #   1 L:      netdev@vger.kernel.org (core kernel code)
    #   1 L:      lvs-devel@vger.kernel.org
    #   1 L:      live-patching@vger.kernel.org
    #   1 L:      linux-x25@vger.kernel.org
    #   1 L:      linux-unionfs@vger.kernel.org
    #   1 L:      linux-spdx@vger.kernel.org
    #   1 L:      linux-sparse@vger.kernel.org
    #   1 L:      linux-sh@vger.kernel.org
    #   1 L:      linux-sgx@vger.kernel.org
    #   1 L:      linux-security-module@vger.kernel.org (suggested Cc:)
    #   1 L:      linux-sctp@vger.kernel.org
    #   1 L:      linux-raid@vger.kernel.org
    #   1 L:      linux-ppp@vger.kernel.org
    #   1 L:      linux-perf-users@vger.kernel.org
    #   1 L:      linux-openrisc@vger.kernel.org
    #   1 L:      linux-nilfs@vger.kernel.org
    #   1 L:      linux-modules@vger.kernel.org
    #   1 L:      linux-man@vger.kernel.org
    #   1 L:      linux-ia64@vger.kernel.org
    #   1 L:      linux-hexagon@vger.kernel.org
    #   1 L:      linux-gpio@vger.kernel.org (pinctrl driver)
    #   1 L:      linux-fscrypt@vger.kernel.org
    #   1 L:      linux-csky@vger.kernel.org
    #   1 L:      linux-btrfs@vger.kernel.org
    #   1 L:      linux-bcache@vger.kernel.org
    #   1 L:      linux-api@vger.kernel.org
    #   1 L:      linux-alpha@vger.kernel.org
    #   1 L:      kernel-janitors@vger.kernel.org
    #   1 L:      io-uring@vger.kernel.org
    #   1 L:      ecryptfs@vger.kernel.org
    #   1 L:      dccp@vger.kernel.org
    #   1 L:      autofs@vger.kernel.org
    #   1 L:      audit@vger.kernel.org
# run the plot.py to use knn classify the communities and plot the figure
python3 plot.py
cp knn.pdf /workspace/rfl_empirical_tools/rq3_figure12/imgs
popd