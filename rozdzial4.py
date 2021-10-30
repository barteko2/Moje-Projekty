"""
WYŚWIETLENIE PRZEPUSTOWOŚCI
dd if=/dev/zero of=/dev/sdc count=10 bs=100M

!!!!!!!!!!!!!UŻYCIE IOSTAT
root@bartek-VirtualBox:~# iostat -d /dev/sda* 1 BĘDZIE GENEROWAĆ WYJŚCIE CO SEKUNDĘ
Linux 5.11.0-38-generic (bartek-VirtualBox)     29.10.2021      _x86_64_        (1 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd
sda               6,35       124,40       177,41         0,00    2057486    2934141          0
sda1              0,00         0,01         0,00         0,00        116          0          0
sda2              0,01         0,41         0,00         0,00       6812          1          0
sda3              6,28       123,83       177,41         0,00    2048057    2934140          0
root@bartek-VirtualBox:~# while true; do clear && iostat -d /dev/sda && sleep 1; done
Linux 5.11.0-38-generic (bartek-VirtualBox)     29.10.2021      _x86_64_        (1 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd
sda               6,26       122,22       173,74         0,00    2080990    2958093          0

!!!!!!!!!!!!!!!! WYKORZYSTANIE FIO DO GŁĘBSZEJ ANALIZY WYDAJNOŚCI
root@bartek-VirtualBox:~# fio --name=sda-performance --filename=/dev/sda --ioengine=libaio --iodepth=1 --rw=randrw --bs=32k --direct=0 --size=64m
sda-performance: (g=0): rw=randrw, bs=(R) 32.0KiB-32.0KiB, (W) 32.0KiB-32.0KiB, (T) 32.0KiB-32.0KiB, ioengine=libaio, iodepth=1
fio-3.25
Starting 1 process

sda-performance: (groupid=0, jobs=1): err= 0: pid=24868: Fri Oct 29 22:51:25 2021
  read: IOPS=4970, BW=155MiB/s (163MB/s)(31.1MiB/200msec)
    slat (usec): min=48, max=4161, avg=176.03, stdev=240.54
    clat (nsec): min=731, max=18120, avg=1471.02, stdev=1098.79
     lat (usec): min=49, max=4167, avg=178.11, stdev=241.27
    clat percentiles (nsec):
     |  1.00th=[  804],  5.00th=[ 1048], 10.00th=[ 1080], 20.00th=[ 1144],
     | 30.00th=[ 1176], 40.00th=[ 1208], 50.00th=[ 1240], 60.00th=[ 1272],
     | 70.00th=[ 1304], 80.00th=[ 1416], 90.00th=[ 1704], 95.00th=[ 2512],
     | 99.00th=[ 5920], 99.50th=[ 6752], 99.90th=[18048], 99.95th=[18048],
     | 99.99th=[18048]
  write: IOPS=5270, BW=165MiB/s (173MB/s)(32.9MiB/200msec); 0 zone resets
    slat (usec): min=6, max=4155, avg=18.21, stdev=128.91
    clat (nsec): min=233, max=173644, avg=584.56, stdev=5368.11
     lat (usec): min=7, max=4159, avg=18.90, stdev=129.19
    clat percentiles (nsec):
     |  1.00th=[   255],  5.00th=[   266], 10.00th=[   274], 20.00th=[   286],
     | 30.00th=[   294], 40.00th=[   314], 50.00th=[   330], 60.00th=[   342],
     | 70.00th=[   358], 80.00th=[   382], 90.00th=[   482], 95.00th=[   892],
     | 99.00th=[  1704], 99.50th=[  3664], 99.90th=[ 12096], 99.95th=[173056],
     | 99.99th=[173056]
  lat (nsec)   : 250=0.29%, 500=46.19%, 750=1.95%, 1000=2.93%
  lat (usec)   : 2=44.29%, 4=2.73%, 10=1.32%, 20=0.24%, 250=0.05%
  cpu          : usr=4.52%, sys=23.12%, ctx=1002, majf=0, minf=15
  IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
     submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
     issued rwts: total=994,1054,0,0 short=0,0,0,0 dropped=0,0,0,0
     latency   : target=0, window=0, percentile=100.00%, depth=1

Run status group 0 (all jobs):
   READ: bw=155MiB/s (163MB/s), 155MiB/s-155MiB/s (163MB/s-163MB/s), io=31.1MiB (32.6MB), run=200-200msec
  WRITE: bw=165MiB/s (173MB/s), 165MiB/s-165MiB/s (173MB/s-173MB/s), io=32.9MiB (34.5MB), run=200-200msec

Disk stats (read/write):
  sda: ios=566/3, merge=2/0, ticks=121/1, in_queue=122, util=76.85%

fdisk -l /dev/sda

!!!!!!!!!!!!wyświetla informacje na temat urządzenia
blkid /dev/sda


!!!POMIAR WYDAJNOŚCI ZA POMOCĄ APACHE BENCHMARK
bartek@bartek-VirtualBox:~/PycharmProjects/Moje-Projekty$ ab -c 100 -n 10000 http://www.inea.com.pl/


!!!NARZĘDZIA DO BADANIA CPU TOP I HTOP i inne

PS
ps -eo pcpu,pid,user,args|sort -r| head -10
%CPU     PID USER     COMMAND
 5.2    2778 bartek   /snap/pycharm-community/256/jbr/bin/java -classpath /snap/pycharm-community/256/lib/bootstrap.jar:/snap/pycharm-community/256/lib/util.jar:/snap/pycharm-community/256/lib/jna.jar -XX:ReservedCodeCacheSize=512m -Xms128m -Xmx750m -XX:+UseG1GC -XX:SoftRefLRUPolicyMSPerMB=50 -XX:CICompilerCount=2 -XX:+HeapDumpOnOutOfMemoryError -XX:-OmitStackTraceInFastThrow -ea -Dsun.io.useCanonCaches=false -Djdk.http.auth.tunneling.disabledSchemes="" -Djdk.attach.allowAttachSelf=true -Djdk.module.illegalAccess.silent=true -Dkotlinx.coroutines.debug=off -Dsun.tools.attach.tmp.only=true -XX:ErrorFile=/home/bartek/java_error_in_pycharm_%p.log -XX:HeapDumpPath=/home/bartek/java_error_in_pycharm_.hprof -Djb.vmOptionsFile=/home/bartek/.config/JetBrains/PyCharmCE2021.2/pycharm64.vmoptions -Djava.system.class.loader=com.intellij.util.lang.PathClassLoader -Didea.vendor.name=JetBrains -Didea.paths.selector=PyCharmCE2021.2 -Didea.platform.prefix=PyCharmCore -Dsplash=true com.intellij.idea.Main
 3.3    1075 bartek   /usr/bin/gnome-shell
 1.5   29095 bartek   /snap/pycharm-community/256/jbr/lib/jcef_helper --type=renderer --disable-in-process-stack-traces --no-sandbox --force-device-scale-factor=1.0 --log-file=/home/bartek/jcef_2778.log --field-trial-handle=5520432016304047528,3180874219848625964,131072 --enable-features=CastMediaRouteProvider --disable-features=SpareRendererForSitePerProcess --disable-gpu-compositing --lang=en-US --locales-dir-path=/snap/pycharm-community/256/jbr/lib/locales --log-file=/home/bartek/jcef_2778.log --log-severity=disable --resources-dir-path=/snap/pycharm-community/256/jbr/lib --num-raster-threads=1 --renderer-client-id=5 --no-v8-untrusted-code-mitigations --shared-files=v8_context_snapshot_data:100
 0.7    5287 bartek   /usr/lib/firefox/firefox -new-window
 0.4    1221 root     /usr/libexec/packagekitd
 0.3     890 bartek   /usr/bin/pulseaudio --daemonize=no --log-target=journal
 0.3    5467 bartek   /usr/lib/firefox/firefox -contentproc -childID 4 -isForBrowser -prefsLen 8311 -prefMapSize 242247 -jsInit 286204 -parentBuildID 20210927210923 -appdir /usr/lib/firefox/browser 5287 true tab
 0.3   29080 bartek   /snap/pycharm-community/256/jbr/lib/jcef_helper --type=gpu-process --field-trial-handle=5520432016304047528,3180874219848625964,131072 --enable-features=CastMediaRouteProvider --disable-features=SpareRendererForSitePerProcess --no-sandbox --locales-dir-path=/snap/pycharm-community/256/jbr/lib/locales --log-file=/home/bartek/jcef_2778.log --log-severity=disable --resources-dir-path=/snap/pycharm-community/256/jbr/lib --lang=en-US --gpu-preferences=UAAAAAAAAAAgACAQAAAAAAAAAAAAAAAAAABgAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAgAAAAAAAAACAAAAAAAAAA= --use-gl=swiftshader-webgl --disable-in-process-stack-traces --log-file=/home/bartek/jcef_2778.log --shared-files
 0.2    5493 bartek   /usr/lib/firefox/firefox -contentproc -childID 5 -isForBrowser -prefsLen 8429 -prefMapSize 242247 -jsInit 286204 -parentBuildID 20210927210923 -appdir /usr/lib/firefox/browser 5287 true tab

###########   HTOP   #############

########### REKURENCYJNY GLOBBING ###########
### REKURENCYJNIE WYSZUKUJEMY WSZYSTKIE PLIKI Z ROZSZERZENIEM PY
ls **/*.py

###WYŚWIETLA WSZYSTKIE PROCESY Z APACHE W NAZWIE, WYŚWIETLI TEŻ PROCES GREP
ps auxw | grep apache

NATOMIAST TERAZ NIE WYŚWIETLI:
ps auxw | grep apache | grep -v grep
alias pg='ps aux | grep -v grep | grep $1'
pg pycharm # wyświetli bez procesu związanego z grep



"""