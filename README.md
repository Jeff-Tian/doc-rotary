doc-rotary -  文件转码
---

> 将 Office 文档转成 PDF 格式。

## 有什么用？

对于使用 Office 编辑的文件，在分享的场景下，不想被别人修改，以及想更方便的展示，不依赖 Office 软件，那么一个很好的办法就是转成 PDF 格式。

对于单独的文件，你可以使用 Office 软件打开，再另存为 PDF 即可。但是如何将这一步集成在你的应用中呢？那就需要在用户上传完 Office 文档后自动完成这一步，于是这个仓库应运而生。

## 怎么使用？

本服务提供 restful API 接口，只需将文件 `POST` 到此接口，就能收到一个转码后的 PDF 文件。

对接到 `nodejs` 应用更简单，推荐使用 [doc-giggle](https://github.com/Jeff-Tian/doc-giggle) npm 包，只需传入一个 Officie 文件的 url 地址，便能拿到对应的 PDF 文件。

## 原理

命令行调用 LibreOffice 的另存为 PDF 文件功能。

由于需要 LibreOffice，所以使用了预装 LibreOffice 的 docker 容器。使用 `python Flask` 来提供 `HTTP restful API` 接口。本服务部署在 `Heroku` PaaS 平台上，服务运行在美国。

## 相关项目

- [fc-doc-rotary](https://github.com/Jeff-Tian/fc-doc-rotary) 同样的服务，部署在阿里云函数计算平台，优化国内访问速度。
- [doc-giggle](https://github.com/Jeff-Tian/doc-giggle) 此服务的客户端，方便从 `nodejs` 应用调用。

## 本地运行
```
sh start.sh
```
如果已安装 docker，推荐：
```shell
sh start-docker.sh
```

## 本地测试
```
sh test.sh
```

## 发布

```
heroku login
heroku container:login
heroku container:push web -a doc-rotarybit
heroku container:release web -a doc-rotarybit
heroku open -a doc-rotarybit
```

## 看日志：

```shell
heroku logs --tail -a doc-rotarybit
```

## 镜像信息：

```shell
REPOSITORY                           TAG                 IMAGE ID            CREATED             SIZE
registry.heroku.com/doc-rotary/web   latest              cc97cb425cde        4 minutes ago       1.33GB
ubuntu                               18.04               775349758637        3 weeks ago         64.2MB
```
