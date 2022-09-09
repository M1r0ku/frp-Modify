# frp-Modify

## Todo
- [x] 去除非 TLS 流量特征
- [x] 配置文件写入源码
- [x] 通过参数传入IP和端口
- [x] 传入参数加密，便于隐藏
- [x] 钉钉上线提醒

## 使用说明
- 在`cmd/frpc/sub/root.go#getFileContent()`函数中，按需修改 FRPC 配置和`key`（默认`testkey`）

```Go
func getFileContent(ip string, port string) {
	key := "testkey"
	ip = str2xor(ip, key)
	port = str2xor(port, key)

	var configContent string = `[common]
        server_addr = ` + ip + `
        server_port = ` + port + `
	tls_enable = true 
	[plugin_socks]
	type = tcp
	remote_port = 7788
	plugin = socks5
	#plugin_user = ""
	#plugin_passwd = ""
	`
	fileContent = configContent
}

```

- 确保安装 Go-1.16+ 和 GCC 环境，然后运行`package.sh`进行交叉编译

```bash
$ go env -w GOPROXY=https://goproxy.cn,direct  # 设置代理
$ ./package.sh

```

- FRPS正常运行，FRPC则需要传入异或后的字符串。可通过`xor.py`脚本进行异或，异或后的字符串存在特殊字符`\`，因此建议使用双引号包裹

```bash
$ ./frpc -t <IP> -p <端口>
$ ./frpc -t "E\AZZSAZTBEET" -p "CUCD"  # 192.168.111.1:7000

```

![](./frp-1.jpg)

## 钉钉提醒
- 需要在`client/control.go#HandleNewProxyResp()`函数中配置钉钉机器人`AccessToken`和`Secret`，然后在前面的配置部分添加相关`plugin_user`和`plugin_passwd`即可

```GO
func (ctl *Control) HandleNewProxyResp(inMsg *msg.NewProxyResp) {
    // ...

	if err != nil {
		xl.Warn("[%s] start error: %v", inMsg.ProxyName, err)
	} else {
		// 配置钉钉机器人
		dingAccessToken := ""
		dingSecret := ""
        
        // ...
	}

    // ...
}

```

![](./frp-2.jpg)

## 参考文章
- [FRP改造计划](https://uknowsec.cn/posts/notes/FRP%E6%94%B9%E9%80%A0%E8%AE%A1%E5%88%92.html)
- [https://github.com/wanghuiyt/ding](https://github.com/wanghuiyt/ding)
