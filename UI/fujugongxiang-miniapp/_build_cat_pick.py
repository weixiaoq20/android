# -*- coding: utf-8 -*-
from pathlib import Path
cats = Path("_cats.json").read_text(encoding="utf-8")
html = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>福聚贡翔 · 选择类目</title>
<style>
:root{--brand:#E23A2E;--brand2:#EE4A2F;--ink:#2A2420;--soft:#FFF6F3;--shadow:0 6px 18px rgba(120,60,50,.06)}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;color:var(--ink);background:#EBE4DE;display:flex;align-items:center;justify-content:center}
a{text-decoration:none;color:inherit}
button{font-family:inherit;cursor:pointer;border:0;background:none;color:inherit}
.app{width:100%;height:100%;max-width:393px;max-height:852px;min-height:0;display:flex;flex-direction:column;overflow:hidden;background:linear-gradient(180deg,#FCE4E1 0%,#FBE9E4 16%,#FDF7F4 34%,#FFFDFC 48%,#FFFDFC 100%);position:relative}
.status{height:44px;flex:0 0 44px;display:flex;align-items:center;justify-content:space-between;padding:0 22px;font-size:16px;font-weight:700;color:#1B1B1D}
.si{display:flex;align-items:center;gap:5px}
.navbar{flex:0 0 46px;display:flex;align-items:center;justify-content:center;position:relative;padding:0 13px}
.navbar h1{margin:0;font-size:16px;font-weight:800}
.navbar .back{position:absolute;left:13px;top:50%;transform:translateY(-50%);width:30px;height:30px;border-radius:50%;background:rgba(255,255,255,.9);display:grid;place-items:center;box-shadow:0 3px 9px rgba(160,110,80,.08)}
.hint{margin:0 14px 8px;font-size:10.5px;color:#A2857A;line-height:1.5;display:flex;align-items:flex-start;gap:5px}
.hint i{flex:0 0 14px;width:14px;height:14px;border-radius:50%;background:#FFE8DF;color:var(--brand2);display:grid;place-items:center;font-style:normal;font-size:9px;font-weight:800;margin-top:1px}
.main{flex:1 1 auto;min-height:0;display:flex;margin:0 12px 10px;background:#fff;border-radius:16px;box-shadow:var(--shadow);overflow:hidden}
.side{width:104px;flex:0 0 104px;overflow-y:auto;scrollbar-width:none;background:#FBF7F4;border-right:1px solid #F3E9E2}
.side::-webkit-scrollbar{display:none}
.sitem{width:100%;min-height:44px;padding:10px 8px;font-size:12px;font-weight:600;color:#7A6A60;text-align:center;line-height:1.35;position:relative}
.sitem.on{background:#fff;color:var(--brand2);font-weight:800}
.sitem.on:before{content:"";position:absolute;left:0;top:12px;bottom:12px;width:3px;border-radius:0 2px 2px 0;background:linear-gradient(180deg,#FB6E4E,#F03A2C)}
.content{flex:1;min-width:0;display:flex;flex-direction:column;overflow:hidden}
.ctitle{padding:12px 12px 6px;font-size:12.5px;font-weight:800;color:#2A2420}
.grid{flex:1;min-height:0;overflow-y:auto;scrollbar-width:none;padding:4px 12px 14px;display:flex;flex-wrap:wrap;gap:8px;align-content:flex-start}
.grid::-webkit-scrollbar{display:none}
.l2{min-width:calc(50% - 4px);flex:1 1 calc(50% - 4px);height:38px;padding:0 10px;border-radius:10px;border:1px solid #F1E5DB;background:#FDFBF9;font-size:12px;font-weight:600;color:#5C5C5F;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.25}
.l2.on{background:#FFEFEB;border-color:#F7A392;color:var(--brand2);font-weight:700;box-shadow:0 2px 8px rgba(232,70,45,.1)}
.homebar{height:18px;flex:0 0 18px;display:flex;align-items:center;justify-content:center}
.homebar i{width:134px;height:5px;border-radius:3px;background:#1D1D1F;display:block}
.toast{position:absolute;left:50%;bottom:40px;transform:translate(-50%,10px);background:rgba(38,28,22,.88);color:#fff;font-size:11px;padding:8px 14px;border-radius:999px;opacity:0;pointer-events:none;transition:all .22s;z-index:60;white-space:nowrap}
.toast.show{opacity:1;transform:translate(-50%,0)}
</style>
</head>
<body>
<div class="app">
<div class="status"><span>9:41</span>
<div class="si">
<svg fill="#2A211B" height="11" viewBox="0 0 17 11" width="17"><rect height="4" rx="1" width="3" x="0" y="7"></rect><rect height="6" rx="1" width="3" x="4.5" y="5"></rect><rect height="8.5" rx="1" width="3" x="9" y="2.5"></rect><rect height="11" rx="1" width="3" x="13.5" y="0"></rect></svg>
<svg fill="#2A211B" height="11" viewBox="0 0 15 11" width="15"><path d="M7.5 10.2 5.4 7.9a3.1 3.1 0 0 1 4.2 0zM2.6 5.1 1 3.4a9.4 9.4 0 0 1 13 0l-1.6 1.7a7 7 0 0 0-9.8 0z"></path></svg>
<svg height="11" viewBox="0 0 24 11" width="24"><rect fill="none" height="10" rx="3" stroke="#2A211B" stroke-opacity=".5" width="20" x=".5" y=".5"></rect><rect fill="#2A211B" height="7" rx="1.6" width="16" x="2" y="2"></rect><rect fill="#2A211B" height="4" opacity=".6" rx=".7" width="1.5" x="22" y="3.5"></rect></svg>
</div>
</div>
<div class="navbar">
<a aria-label="返回" class="back" id="backBtn" href="merchant-goods-edit.html"><svg fill="none" height="21" viewBox="0 0 24 24" width="21"><path d="m14.5 5-7 7 7 7" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.1"></path></svg></a>
<h1>选择类目</h1>
</div>
<div class="hint"><i>i</i><span>平台一二级类目（与首页分类一致），请选择二级类目</span></div>
<div class="main">
<nav class="side" id="side"></nav>
<div class="content">
<div class="ctitle" id="ctitle">类目</div>
<div class="grid" id="grid"></div>
</div>
</div>
<div class="homebar"><i></i></div>
<div class="toast" id="toast"></div>
</div>
<script>
(function () {
  var CATS = ''' + cats + r''';
  var params = new URLSearchParams(location.search);
  var ret = params.get('from') || 'merchant-goods-edit.html';
  var pickedKey = params.get('key') || '';
  try {
    var cached = JSON.parse(sessionStorage.getItem('pickedCategory') || 'null');
    if (!pickedKey && cached && cached.key) pickedKey = cached.key;
  } catch (e) {}
  document.getElementById('backBtn').setAttribute('href', ret);

  var side = document.getElementById('side');
  var grid = document.getElementById('grid');
  var ctitle = document.getElementById('ctitle');
  var toastEl = document.getElementById('toast');
  var cur = 0;
  var toastTimer = null;

  function showToast(msg) {
    toastEl.textContent = msg;
    toastEl.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove('show'); }, 1400);
  }

  // 若已有选中二级，定位到对应一级
  if (pickedKey) {
    for (var i = 0; i < CATS.length; i++) {
      for (var j = 0; j < CATS[i].level2.length; j++) {
        if (CATS[i].level2[j].key === pickedKey) { cur = i; break; }
      }
    }
  }

  function renderSide() {
    side.innerHTML = CATS.map(function (c, i) {
      return '<button class="sitem' + (i === cur ? ' on' : '') + '" type="button" data-i="' + i + '">' + c.level1 + '</button>';
    }).join('');
  }

  function renderGrid() {
    var c = CATS[cur];
    ctitle.textContent = c.level1;
    grid.innerHTML = c.level2.map(function (x) {
      return '<button class="l2' + (x.key === pickedKey ? ' on' : '') + '" type="button" data-key="' + x.key + '" data-name="' + x.name.replace(/"/g, '&quot;') + '">' + x.name + '</button>';
    }).join('');
  }

  side.addEventListener('click', function (e) {
    var btn = e.target.closest('.sitem');
    if (!btn) return;
    cur = parseInt(btn.getAttribute('data-i'), 10) || 0;
    renderSide();
    renderGrid();
  });

  grid.addEventListener('click', function (e) {
    var btn = e.target.closest('.l2');
    if (!btn) return;
    var key = btn.getAttribute('data-key');
    var name = btn.getAttribute('data-name');
    var level1 = CATS[cur].level1;
    sessionStorage.setItem('pickedCategory', JSON.stringify({ key: key, name: name, level1: level1 }));
    showToast('已选择：' + name);
    setTimeout(function () { location.href = ret; }, 350);
  });

  renderSide();
  renderGrid();
})();
</script>
</body>
</html>
'''
Path("merchant-category-pick.html").write_text(html, encoding="utf-8")
print("wrote merchant-category-pick.html", len(html))
