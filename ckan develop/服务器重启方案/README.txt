
=========================
服务器重启方案 By Sion.Qi
=========================

1、上传文件 restart/ 到 /home/opendata/目录下

   cd ../restart/bin/

   chmod +x restart-ckan.sh ->设置脚本为可执行脚本

2、创建定时任务

   crontab ../restart/bin/rootcron -> 启动定时任务

   定时任务会在设置的时间执行任务，并将执行任务的结果打印到日志文件 -> ../restart/log/restart.log


关于crontab命令的使用详情请参考 -> Crontab.txt

注意事项：用户都可设置定时任务，要注意在添加任务时的用户角色，建议使用root或具有root权限的用户来设置。因为要确保脚本中的命令可正确执行。
