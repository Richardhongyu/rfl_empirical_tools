import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# 数据
data = [1053.79, 884.06, 2709.48, 3127.09, 525.97, 1345.76, 441.05, 517.28, 251.12, 502.99, 558.38, 976.89, 583.55, 1090.37, 2415.04, 1502.22, 803.55, 993.43, 1298.05, 562.72, 960.22, 802.32, 1540.24, 800.35, 669.49, 146.50, 117.99, 73.64, 377.22, 1059.85, 2247.91, 3687.76, 817.28, 346.86, 1436.70, 1092.67, 1664.42, 2582.41, 114.37, 1784.18, 667.75, 3912.41, 437.13, 1849.38, 568.95, 818.78, 1062.17, 4063.76, 1716.15, 3945.40, 197.05, 2512.56, 1290.58, 984.25, 1948.74, 680.21, 3491.08, 228.33, 513.54, 845.35, 1332.61, 210.07, 832.59, 5131.43, 423.91, 1264.73, 329.53]

data = [['netdev', 1053.7919827235319, 6853], ['linux-scsi', 884.0630982618328, 1142], ['linux-bluetooth', 2709.4831911690917, 243], ['linux-hams', 3127.0940361849453, 70], ['linux-wireless', 525.9697129384552, 1579], ['linux-serial', 1345.7630744001997, 151], ['linux-media', 441.0508035394327, 864], ['linux-hwmon', 517.2754796208675, 102], ['linux-gpio', 251.1164637980461, 125], ['linux-iio', 502.9948045931368, 152], ['platform-driver-x86', 558.3774631650996, 93], ['linux-acpi', 976.8936805608281, 193], ['linux-parisc', 583.5521653953566, 28], ['linux-wpan', 1090.3684123575088, 33], ['linux-fsdevel', 2415.0441244565927, 2686], ['linux-usb', 1502.2224015385339, 1117], ['linux-i2c', 803.5471693750253, 139], ['linux-rdma', 993.4344878126594, 629], ['linux-pm', 1298.0496531262272, 357], ['linux-crypto', 562.7227444196661, 243], ['dmaengine', 960.220433212494, 138], ['linux-input', 802.3172008648708, 236], ['linux-kernel', 1540.2414369354103, 1318], ['linux-pci', 800.3466469553692, 157], ['linux-omap', 669.4899420813352, 86], ['linux-arm-msm', 146.4970306178794, 169], ['linux-renesas-soc', 117.99012254117012, 14], ['linux-samsung-soc', 73.64041385912589, 2], ['linux-tegra', 377.2161448509996, 2], ['linux-leds', 1059.8522094974535, 36], ['keyrings', 2247.91265253693, 35], ['linux-block', 3687.764167866409, 479], ['bpf', 817.280029857503, 473], ['linux-mips', 346.8649643001902, 89], ['linux-spi', 1436.7028218598173, 131], ['linux-can', 1092.668074448755, 89], ['linux-security-module', 1664.4210192597288, 21], ['ceph-devel', 2582.4122077668003, 132], ['linux-clk', 114.37368606420176, 63], ['linux-cifs', 1784.1833306300252, 154], ['linux-cxl', 667.7477821234379, 7], ['cgroups', 3912.4145186743817, 119], ['linux-fbdev', 437.1266210112196, 132], ['linux-hyperv', 1849.3754801263265, 65], ['linux-edac', 568.9495768437522, 40], ['linux-efi', 818.7772925764192, 15], ['linux-mmc', 1062.1724968134824, 150], ['linux-ext4', 4063.764764186008, 246], ['linux-integrity', 1716.1489617298782, 70], ['linux-hardening', 3945.404137342717, 37], ['linux-fpga', 197.05404207103797, 4], ['linux-arch', 2512.5628140703516, 30], ['kvm', 1290.5806660539185, 271], ['linux-remoteproc', 984.2519685039371, 27], ['linux-xfs', 1948.740483173008, 204], ['linux-kbuild', 680.2060052473034, 14], ['linux-nfs', 3491.0842687779173, 687], ['linux-kselftest', 228.33294749293594, 72], ['linux-ide', 513.5370761826281, 43], ['linux-watchdog', 845.3493708185397, 35], ['linux-rtc', 1332.6085812978906, 76], ['devicetree', 210.07490256870898, 29], ['linux-pwm', 832.5932504440498, 15], ['rcu', 5131.427374594198, 98], ['linux-trace-devel', 423.908435777872, 3], ['linux-s390', 1264.731814114143, 383], ['sparclinux', 329.5268754515152, 26]]
sys_name = ['linux-block', 'linux-ext4', 'linux-clk']
data_dic = {}
for i in data:
    if i[0] in sys_name:
        data_dic[i[0]] = i[1]/100_0
print(data_dic)

# 将数据转换为NumPy数组并重塑为n*1的矩阵
X = np.array(data)[:,1].reshape(-1, 1)
print(X.shape)

# 应用K-means聚类
kmeans = KMeans(n_clusters=3)  # 假设我们分为3个聚类
kmeans.fit(X)

# 获取聚类中心和标签
centroids = kmeans.cluster_centers_
labels = kmeans.labels_

fig,axs=plt.subplots(1,1, figsize=(8, 1.5), dpi=100)

axs.spines['top'].set_visible(False)
axs.spines['right'].set_visible(False)
axs.spines['left'].set_visible(False)
axs.yaxis.set_ticks_position('left')
axs.set_xlim((0,6000/100_0))
axs.set_ylim((0,1))

# 绘制结果
colors = ["g", "r", "b"]
for i in range(len(X)):
    # print(data[i][1])
    # a = int(np.log([data[i][2]*100])[0])
    # print(a)
    # axs.scatter(int( data[i][1]),0.08, c= "b",s = data[i][2]/20)# markersize = 10 colors[labels[i]]
    axs.scatter(data[i][1]/100_0,0.15, c= colors[labels[i]],s = data[i][2]/20)# markersize = 10 colors[labels[i]]
print(labels)
print(len(labels))
axs.set_yticks([])
axs.set_xlabel('Bugs per KLoC Fixable by RFL', size=18)
# plt.scatter(centroids[:, 0], centroids[:, 0], marker = "x", s = 150, linewidths = 5, zorder = 10)
print(centroids[:, 0])
for k in data_dic.items():
    if k[0] == 'linux-block':
        axs.annotate(f'{k[0]}', xy=(k[1], 0.15), xytext=(k[1], 0.15 * 4),arrowprops=dict(arrowstyle="->",color='black'), fontsize=16, ha='right')
    elif k[0] == 'linux-ext4':
        axs.annotate(f'{k[0]}', xy=(k[1], 0.15), xytext=(k[1], 0.15 * 4),arrowprops=dict(arrowstyle="->",color='black'), fontsize=16, ha='left')
    else:
        axs.annotate(f'{k[0]}', xy=(k[1], 0.15), xytext=(k[1], 0.15 * 4),arrowprops=dict(arrowstyle="->",color='black'), fontsize=16, ha='center')

axs.tick_params(axis='x', labelsize=18)
plt.savefig("knn.pdf", bbox_inches='tight')