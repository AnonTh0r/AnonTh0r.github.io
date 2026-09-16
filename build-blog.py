"""Rebuild the blog with Python's standard library: python build-blog.py."""
from pathlib import Path
import re
import html

ROOT = Path(__file__).resolve().parent
POST = '/2025/12/11/hello-world/'
source = ROOT / 'content/hello-world.html'
if not source.exists():
    original = (ROOT / POST.strip('/') / 'index.html').read_text(encoding='utf-8')
    body = re.search(r'<div class="post-body" itemprop="articleBody">(.*?)\n    </div>', original, re.S).group(1).strip()
    source.parent.mkdir(exist_ok=True)
    source.write_text(body, encoding='utf-8')
body = source.read_text(encoding='utf-8')

leaf = '''<svg viewBox="0 0 80 80" fill="none" aria-hidden="true"><path d="M40 7 47 25 60 18 56 34 73 35 57 48 61 60 43 56 40 73 37 56 19 60 23 48 7 35 24 34 20 18 33 25Z" fill="currentColor"/><path d="M40 28V65M40 46 27 37M40 46 53 37" stroke="var(--paper)" stroke-width="1.5"/></svg>'''

def shell(title, path, main, active='home'):
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if active == key else '')+f'>{label}</a>' for key,url,label in [('home','/','首页'),('archives','/archives/','归档'),('vocab','/vocab/','背单词'),('about','/about/','关于')])
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} · 枫叶苑</title><meta name="description" content="lemu3l 的个人博客。把经历写成文字，让想法慢慢生长。">
<link rel="canonical" href="https://lemu3l.top{path}"><meta name="theme-color" content="#f8f7f3">
<meta property="og:title" content="{html.escape(title)} · 枫叶苑"><meta property="og:url" content="https://lemu3l.top{path}"><meta property="og:type" content="{'article' if path == POST else 'website'}">
<link rel="icon" href="/images/maple.svg" type="image/svg+xml"><script src="/js/theme.js"></script><link rel="stylesheet" href="/css/blog.css"></head>
<body><a class="skip" href="#main">跳到正文</a><div class="site-shell">
<header class="site-header"><a class="brand" href="/" aria-label="枫叶苑首页"><span class="brand-icon">{leaf}</span><span>枫叶苑<small>LEMU3L’S JOURNAL</small></span></a><div class="header-actions"><nav aria-label="主导航">{nav}</nav><button class="theme-toggle" type="button" aria-label="切换深浅色模式" title="切换深浅色模式" hidden><span class="sun" aria-hidden="true">☀</span><span class="moon" aria-hidden="true">☾</span></button></div></header>
<main id="main">{main}</main>
<footer class="site-footer"><a href="/">枫叶苑 <span>© 2025–2026 lemu3l</span></a><span>把日子写下来，让时间有迹可循。 <span class="footer-leaf">✳</span></span></footer></div><script src="/js/blog.js" defer></script></body></html>'''

entry = f'''<a class="post-card" href="{POST}"><div class="post-art" aria-hidden="true"><span class="art-orbit"></span><span class="art-leaf">{leaf}</span><span class="art-caption">THE FIRST PAGE<br><b>Hello, world.</b></span><span class="art-number">01 / JOURNAL</span></div><div class="post-summary"><div class="eyebrow"><time datetime="2025-12-11">2025.12.11</time><span>起点</span></div><h3>Hello World <span aria-hidden="true">↗</span></h3><p>博客的第一篇文章。从一句 Hello World 开始，翻开这个小小空间的第一页。</p><span class="read-link">阅读全文 <span aria-hidden="true">→</span></span></div></a>'''
home = f'''<section class="hero"><div class="hero-copy"><p class="eyebrow"><span class="dot"></span> A PERSONAL SPACE ON THE INTERNET</p><h1>拾起片刻，<br>写成<span class="accent">日常。</span></h1><p class="hero-description">你好，我是 lemu3l。欢迎来到枫叶苑。<br>这里收藏文字、想法，以及生活里值得记住的瞬间。</p><a class="primary-link" href="#journal">翻阅我的博客 <span aria-hidden="true">↘</span></a></div><div class="hero-art" aria-hidden="true"><div class="art-grid"></div><div class="circle circle-one"></div><div class="circle circle-two"></div><div class="large-leaf">{leaf}</div><span class="art-label">FIELD NOTES<br>ON LIFE & EVERYTHING</span><span class="vertical-note">慢慢记录 · 自由生长</span><span class="edition">A LITTLE CORNER OF MY WORLD</span></div></section>
<div class="journal-layout" id="journal"><section class="journal"><div class="section-heading"><h2>最近的文字 <small>LATEST ENTRIES</small></h2><a href="/archives/">全部归档 ↗</a></div>{entry}<p class="end-note"><span></span>故事刚刚开始，更多文字慢慢写。<span></span></p></section><aside class="profile"><div class="avatar">L<span>✳</span></div><p class="eyebrow">THE PERSON BEHIND THE WORDS</p><h2>我是 lemu3l<span class="accent">.</span></h2><p>在这里，把经历写成文字，<br>让想法慢慢生长。</p><a class="profile-link" href="/about/">关于这个小站 <span>↗</span></a><div class="profile-bottom"><span>已写下 <b>01</b> 篇文字</span><span>始于 2025</span></div></aside></div>'''
archive = f'''<section class="page-heading"><p class="eyebrow">THE ARCHIVE</p><h1>文字的<span class="accent">足迹。</span></h1><p>一篇一篇，收好那些值得记住的片刻。</p></section><section class="archive-list"><div class="archive-year"><h2>2025</h2><span>01 篇文章</span></div><a href="{POST}" class="archive-entry"><time datetime="2025-12-11">12 / 11</time><h3>Hello World</h3><span>起点</span><b aria-hidden="true">↗</b></a></section>'''
about = '''<section class="page-heading"><p class="eyebrow">ABOUT THIS LITTLE CORNER</p><h1>你好，<br>我是 <span class="accent">lemu3l。</span></h1><p>欢迎来到枫叶苑，我在互联网上的一小片自留地。</p></section><section class="about-body"><span class="about-mark" aria-hidden="true">✳</span><div><h2>把日子写下来。</h2><p>有些想法适合慢慢梳理，有些瞬间值得好好保存。这个博客，就是存放它们的地方。</p><p>从第一篇 Hello World 开始，让这里一点点充实起来。谢谢你来坐坐，也欢迎你以后再来。</p><a class="primary-link" href="/archives/">去看看我的文字 <span>↗</span></a></div></section>'''
article = f'''<div class="article-wrap"><a class="back-link" href="/">← 返回首页</a><header class="article-heading"><p class="eyebrow"><time datetime="2025-12-11">2025.12.11</time> <span>·</span> lemu3l</p><h1>Hello World<span class="accent">.</span></h1><p>枫叶苑的第一页。</p></header><article class="article-body">{body}</article><div class="article-end"><span>✳</span><p>谢谢你读到这里。</p><a href="/archives/">浏览文章归档 →</a></div></div>'''
pages = [('首页','/',home,'home'),('归档','/archives/',archive,'archives'),('2025 年归档','/archives/2025/',archive,'archives'),('2025 年 12 月归档','/archives/2025/12/',archive,'archives'),('关于','/about/',about,'about'),('Hello World',POST,article,'')]
for title,path,content,active in pages:
    target = ROOT / path.strip('/') / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(shell(title,path,content,active),encoding='utf-8')
(ROOT / 'images/maple.svg').write_text(leaf.replace('var(--paper)', '#f8f7f3').replace('currentColor','#ae5138').replace('aria-hidden="true"','xmlns="http://www.w3.org/2000/svg"'),encoding='utf-8')
print(f'Built {len(pages)} pages. Original article preserved in {source}.')
