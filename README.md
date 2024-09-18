# blueteam_darkweb_leak_monitor
监控企业数据是否出现在暗网搜索引擎的结果中，一旦发现就会告警出来。

目前覆盖的暗网搜索引擎有3个,这些在国内不需要通过挂代理就可以访问。
```
http://onionland.io/
https://ahmia.fi/
https://torsearch.com/
```

纯python 3.11编程环境，每10秒发出一次请求，不建议访问速度过快，不建议一次性使用过多关键词进行请求。

python darkweb_leak_monitor.py

想要监控的关键词可以在darkweb_leak_monitor.py修改，query_params = []，加进去就行，一天监测一次并发出结果就可以了。

结果示例：
```
Querying with: baidu

http://onionland.io/search/ 可能存在信息泄露。

https://ahmia.fi/search/ 可能存在信息泄露。

https://torsearch.com/search/ 可能存在信息泄露。


Querying with: baidukeji

http://onionland.io/search/ 没有信息泄露。

https://ahmia.fi/search/ 没有信息泄露。

https://torsearch.com/search/ 没有信息泄露。
```


