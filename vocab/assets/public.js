/* Gate study scripts until a visitor has imported a wordbook. */
(async () => {
  const entry = document.currentScript.dataset.entry;
  const main = document.querySelector('main');
  try {
    await window.VocabBooks.init();
    if (!window.VocabBooks.list().length) {
      document.body.classList.remove('browse');
      document.querySelector('.browse-sidebar')?.remove();
      document.querySelector('.sidebar-toggle')?.remove();
      main.className = 'maple-empty';
      main.innerHTML = `<p class="empty-kicker">A LITTLE PRACTICE, EVERY DAY</p>
        <h1>让每一个词，<br>慢慢成为你的表达。</h1>
        <p>欢迎来到枫叶苑的词汇角。<br>导入自己的词书，从今天的十个单词开始。</p>
        <div class="empty-actions"><a class="maple-link primary" href="books.html">导入我的词书 ↗</a><a class="maple-link" href="books.html#backup">恢复学习备份 →</a></div>
        <p>支持 CSV、TSV、JSON。词书和学习记录保存在当前浏览器。</p>
        <div class="empty-features"><section><span class="empty-number">01 / SPELL</span><h2>动手拼写</h2><p>看释义、听发音，逐字练习。也可以使用闪过学习快速复习。</p></section><section><span class="empty-number">02 / RECALL</span><h2>辨认释义</h2><p>四选一练习，记录生词与错题，让理解更扎实。</p></section><section><span class="empty-number">03 / GROW</span><h2>一点点积累</h2><p>间隔复习安排下一次相遇，用学习日历记录每天的进步。</p></section></div>`;
      window.__VOCAB_EMPTY = true;
    } else {
      await new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'assets/' + entry + '.js';
        script.onload = resolve;
        script.onerror = () => reject(new Error('学习页面加载失败，请刷新重试。'));
        document.body.appendChild(script);
      });
    }
  } catch (error) {
    const notice = document.createElement('p');
    notice.className = 'maple-alert'; notice.setAttribute('role', 'alert');
    notice.textContent = '暂时无法打开学习记录：' + error.message;
    main.replaceChildren(notice);
  } finally {
    document.documentElement.classList.remove('maple-loading');
  }
})();
