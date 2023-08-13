**项目名称**
> VeryMocker

**项目简介**

> 该项目是一个基于 FastAPI 构建的mock工具，旨在帮助开发人员在进行 UI 测试时进行 API 的模拟。它允许您在开发尚未完成的 API 或进行极端情况测试时，模拟 API 的行为。通过修改 hosts 文件或自建 DNS，您可以将要测试的域名指向该工具，从而达到无缝模拟 API 的效果。如果您的测试涉及 HTTPS，客户端则需要安装信任证书以确保安全连接。


**功能特性**
* 快速模拟：基于 FastAPI 构建，具有出色的性能、启动速度和响应速度
* 自定义模拟：在 endpoints 目录下定义API路径和相应的数据，精准实现要模拟的API及其行为
* 自动回退：如果在 endpoints 目录下未找到匹配路径，工具将自动返回后端内容，确保测试过程的无缝体验
* HTTPS 支持：支持模拟 HTTPS API，需要客户端安装信任证书，以确保安全连接
* 客户端无感知：UI 测试过程中，客户端无需修改代码，即可使用模拟的 API

**项目结构**
```
├─app
│  ├─endpoints   #mock路径及数据定义
│  ├─middleware  #判断路径是否需要mock的中间件，实现非mock API 自动回退
├─sslfile   #存储https情况下的证书
└─utils   #一些小工具
```

**注意事项**

如果你要测试的后端API是HTTPS，需要自行生成证书存入sslfile文件夹下，并在main.py对证书路径进行相应配置。请运行以下命令生成证书和密钥文件：

```
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout server.key -out server.crt
```