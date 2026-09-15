# 枫叶苑

lemu3l.top 的静态个人博客，保留原有 Hello World 文章及归档网址。

## 本地预览

```sh
python -m http.server 8766 --bind 127.0.0.1
```

访问 http://127.0.0.1:8766。上传仓库静态文件即可部署，无需 npm。

## 修改内容

- `build-blog.py`：页面模板、首页介绍、关于页和归档。
- `content/hello-world.html`：从原站保留的文章正文。
- `css/blog.css`：响应式布局及双主题配色。
- `js/theme.js`：首次跟随系统，手动切换后通过 localStorage 保存，在页面和标签间同步。浏览器禁止存储时仍可切换当前页。

修改模板或正文后运行 `python build-blog.py`，将生成的 HTML 一并提交。
该仓库原先只有 Hexo 生成结果，没有 Hexo 源配置；新版使用仓库中的 Python 脚本生成。
如果继续从外部 Hexo 项目部署，会覆盖这里的页面，需要先把设计迁移到那个源项目。

`CNAME` 保持为 `lemu3l.top`。原有 `lib/`、旧主题资源仍保留，新版页面使用独立的博客样式和脚本。
