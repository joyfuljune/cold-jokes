p = r'G:\github\cold-jokes\index.html'
s = open(p, encoding='utf-8').read()

def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)

# ---------- 背景：只留两个漂浮装饰、两个色块 ----------
rep('''<div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div>
<div class="deco d1"><img src="img/deco1.png" alt=""></div>
<div class="deco d2"><img src="img/deco2.png" alt=""></div>
<div class="deco d3"><img src="img/deco3.png" alt=""></div>
<div class="deco d4"><img src="img/deco4.png" alt=""></div>
<div class="deco d5"><img src="img/deco8.png" alt=""></div>
<div class="deco d6"><img src="img/deco6.png" alt=""></div>
<img class="peek" src="img/uni2.png" alt="">''',
'''<div class="blob b1"></div><div class="blob b3"></div>
<div class="deco d1"><img src="img/deco1.png" alt=""></div>
<div class="deco d6"><img src="img/deco6.png" alt=""></div>
<img class="peek" src="img/uni2.png" alt="">''')
rep('.deco.d1{top:9vh;left:2vw;width:110px;animation-delay:-1s}', '.deco.d1{top:38vh;left:1vw;width:96px;animation-delay:-1s}')
rep('.deco.d6{bottom:30vh;right:6vw;width:90px}', '.deco.d6{top:63vh;right:3vw;width:58px}')

# ---------- 顶部：整幅场景图当横幅，标题压在上面 ----------
rep('''  <header>
    <div class="titlebox">
      <img class="rainbow" src="img/deco3.png" alt="">
      <h1 id="title">冷笑话收集站<span class="en">COLD JOKES &amp; PUNS</span></h1>
      <div class="tagline">先撕开贴纸看题，再点一下揭<b>谜底</b>。冷到了算你的。</div>
    </div>
    <img class="hero" src="img/hero.png" alt="毛茸茸的独角兽">
  </header>''',
'''  <header class="banner">
    <div class="titlebox">
      <h1 id="title">冷笑话收集站<span class="en">COLD JOKES &amp; PUNS</span></h1>
      <div class="tagline">先撕开贴纸看题，再点一下揭<b>谜底</b>。冷到了算你的。</div>
    </div>
  </header>''')
rep('''header{display:grid;grid-template-columns:1fr auto;align-items:end;gap:10px 20px;margin-bottom:10px}
.titlebox{position:relative;padding-top:20px}
.rainbow{position:absolute;left:-30px;top:-10px;width:170px;transform:rotate(-8deg);z-index:0;animation:bob 8s ease-in-out infinite}''',
'''header.banner{position:relative;min-height:min(460px,52vw);border:4px solid var(--ink);border-radius:28px;box-shadow:8px 8px 0 var(--ink);overflow:hidden;background:#cdef9c url("img/scene.png") center 40%/cover no-repeat;display:flex;align-items:flex-end;margin-bottom:14px;animation:pop .6s var(--bounce) both}
.titlebox{position:relative;padding:24px 26px 26px}''')
rep('.tagline{margin-top:18px;background:var(--cream);', '.tagline{margin-top:14px;background:var(--cream);')
rep('''.hero{width:min(300px,34vw);margin-bottom:-28px;filter:drop-shadow(8px 8px 0 rgba(20,20,20,.9));animation:heroin 1s var(--bounce) both .2s;transform-origin:bottom center}
.hero:hover{animation:wiggle .6s ease-in-out}
@keyframes heroin{from{opacity:0;transform:translateY(60px) scale(.6) rotate(10deg)}to{opacity:1}}
''', '')
rep('@media (max-width:640px){header{grid-template-columns:1fr}.hero{width:200px;justify-self:end;margin-top:-30px}}',
    '@media (max-width:640px){header.banner{min-height:300px;background-position:60% 40%}.titlebox{padding:16px}}')

# ---------- 封面：加"场景窗口"样式；整行场景条 ----------
rep('.cover.checks{background-image:radial-gradient(rgba(255,255,255,.5) 28%,transparent 30%);background-size:34px 34px}',
'''.cover.checks{background-image:radial-gradient(rgba(255,255,255,.5) 28%,transparent 30%);background-size:34px 34px}
.cover.scene{background:url("img/scene.png") var(--px,50%) var(--py,50%)/var(--pz,220%) no-repeat;justify-content:flex-end;padding-bottom:16px}
.cover.scene.alt{background-image:url("img/scene2.png")}
.cover.scene .hint{background:var(--neon)}
.strip{grid-column:1/-1;height:200px;border:3px solid var(--ink);border-radius:22px;box-shadow:var(--shadow);background:url("img/scene.png") var(--px,50%) var(--py,50%)/cover no-repeat;transform:rotate(var(--tilt,0deg));animation:pop .5s var(--bounce) both;animation-delay:calc(var(--i,0) * 40ms)}
.strip.alt{background-image:url("img/scene2.png")}''')

# ---------- JS：相邻不重复的封面分配 ----------
rep('''function coverHTML(j){
  const c = COLORS[j.id % COLORS.length];
  const pat = pick(PATTERNS, j.id, 3);
  const style = pick(["q","uni","emoji","uniside"], j.id, 5);
  const uni = `img/uni${1 + Math.floor(hash(j.id,7)*6)}.png`;
  let middle;
  if(style==="uni") middle = `<img class="uni" src="${uni}" alt="">`;
  else if(style==="emoji") middle = `<span class="big">${EMOJI[j.topic]||"?"}</span>`;
  else if(style==="uniside") middle = `<span class="big">?</span><img class="uni side" src="${uni}" alt="">`;
  else middle = `<span class="big">?</span>`;
  return `<div class="cover ${pat}" style="--c:${c}">''',
'''/* 给一组卡片分配封面：颜色 / 图案 / 样式 / 独角兽，保证左、上、左上、右上四个邻居都不一样，
   同一只独角兽在前后一整行里不重复出现 */
function assignCovers(list, cols){
  const STYLES = ["q","scene","uni","q","scene","emoji","uniside","scene","q","uni"];
  const out = [];
  const nb = i => [i-1, i-cols-1, i-cols, i-cols+1].filter(k => k>=0 && k<i).map(k => out[k]);
  list.forEach((j, i) => {
    const near = nb(i);
    const far = out.slice(Math.max(0, i-cols*2), i);
    const tryPick = (arr, salt, bad) => {
      const start = Math.floor(hash(j.id, salt) * arr.length);
      for(let k=0;k<arr.length;k++){ const v = arr[(start+k)%arr.length]; if(!bad(v)) return v; }
      return arr[start];
    };
    const color = tryPick(COLORS, 1, v => near.some(n => n.color===v));
    const pat = tryPick(PATTERNS, 3, v => near.some(n => n.pat===v));
    const style = tryPick(STYLES, 5, v => near.some(n => n.style===v) || (v.startsWith("uni") && far.some(n => n.style && n.style.startsWith("uni"))));
    const uni = tryPick([1,2,3,4,5,6], 7, v => far.some(n => n.uni===v));
    const alt = tryPick([false,true], 9, v => near.some(n => n.alt===v));
    out.push({color, pat, style, uni, alt, px: Math.round(hash(j.id,21)*100), py: Math.round(hash(j.id,22)*100), pz: 180 + Math.round(hash(j.id,23)*120)});
  });
  return out;
}

function coverHTML(j, a){
  const c = a.color;
  const pat = a.style==="scene" ? `scene ${a.alt?"alt":""}` : a.pat;
  const style = a.style;
  const uni = `img/uni${a.uni}.png`;
  let middle;
  if(style==="uni") middle = `<img class="uni" src="${uni}" alt="">`;
  else if(style==="emoji") middle = `<span class="big">${EMOJI[j.topic]||"?"}</span>`;
  else if(style==="uniside") middle = `<span class="big">?</span><img class="uni side" src="${uni}" alt="">`;
  else if(style==="scene") middle = ``;
  else middle = `<span class="big">?</span>`;
  return `<div class="cover ${pat}" style="--c:${c};--px:${a.px}%;--py:${a.py}%;--pz:${a.pz}%">''')

rep('''  wall.innerHTML = "";
  let i = 0, t = 0;
  list.forEach((j, idx) => {''',
'''  wall.innerHTML = "";
  const cols = Math.max(1, Math.floor((wall.clientWidth + 24) / 274));
  const covers = assignCovers(list, cols);
  let i = 0, t = 0, lastTile = -1;
  list.forEach((j, idx) => {''')
rep('''    el.innerHTML = `<div class="inner">${bodyHTML(j)}</div>${coverHTML(j)}`;''',
    '''    el.innerHTML = `<div class="inner">${bodyHTML(j)}</div>${coverHTML(j, covers[idx])}`;''')
rep('''    /* 每隔几张塞一个贴纸格子 */
    if((idx+1) % 4 === 0 && idx < list.length-1){
      const tile = document.createElement("div"); tile.className = "tile";
      tile.style.setProperty("--tilt", ((hash(idx,21)*30)-15).toFixed(1)+"deg");
      tile.style.setProperty("--i", i++);
      tile.innerHTML = `<img src="${TILES[t++ % TILES.length]}" alt="">`;
      wall.appendChild(tile);
    }''',
'''    /* 隔一段塞一条整行的场景图，位置错开，不落在整数倍上 */
    if((idx===8 || idx===19 || idx===30) && idx < list.length-1){
      const strip = document.createElement("div"); strip.className = "strip" + (hash(idx,31)>.5 ? " alt" : "");
      strip.style.setProperty("--tilt", ((hash(idx,32)*2)-1).toFixed(2)+"deg");
      strip.style.setProperty("--px", Math.round(hash(idx,33)*100)+"%"); strip.style.setProperty("--py", Math.round(hash(idx,34)*100)+"%");
      strip.style.setProperty("--i", i++);
      wall.appendChild(strip);
    }
    /* 偶尔塞一个装饰贴纸格子（只用小物件，不用独角兽），和上一个不同 */
    if((idx===4 || idx===14 || idx===25) && idx < list.length-1){
      const tile = document.createElement("div"); tile.className = "tile";
      tile.style.setProperty("--tilt", ((hash(idx,21)*30)-15).toFixed(1)+"deg");
      tile.style.setProperty("--i", i++);
      let k = Math.floor(hash(idx,35)*TILES.length); if(k===lastTile) k = (k+1)%TILES.length; lastTile = k;
      tile.innerHTML = `<img src="${TILES[k]}" alt="">`;
      wall.appendChild(tile);
    }''')
rep('const TILES = ["img/uni1.png","img/uni3.png","img/uni5.png","img/uni6.png","img/deco4.png","img/deco7.png","img/deco5.png","img/deco2.png"];',
    'const TILES = ["img/deco4.png","img/deco7.png","img/deco5.png","img/deco3.png","img/deco8.png"];')

open(p, 'w', encoding='utf-8').write(s)
print('patched')
