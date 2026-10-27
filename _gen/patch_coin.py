import re
p = r'G:\github\cold-jokes\index.html'
s = open(p, encoding='utf-8').read()

def rep(old, new):
    global s
    assert s.count(old) == 1, old[:60]
    s = s.replace(old, new)

# ---------- CSS ----------
rep("*{box-sizing:border-box}\nhtml,body{margin:0}",
"""*{box-sizing:border-box}
html,body{margin:0}
/* 爪子鼠标：默认白爪，可点的东西上变成黄爪 */
body{cursor:url("img/paw.svg") 6 6, auto}
a,button,.chip,.card:not(.open),.punchbox:not(.shown),.coin,.modal .close{cursor:url("img/paw-press.svg") 8 8, pointer}
.card.open,.punchbox.shown{cursor:url("img/paw.svg") 6 6, auto}""")

rep(".note{margin:12px 0 0;",
""".like{display:flex;align-items:center;gap:10px;margin-top:14px;position:relative;z-index:2}
.coin{appearance:none;border:0;background:none;padding:0;width:44px;height:44px;position:relative;transition:transform .15s var(--bounce)}
.coin svg{width:100%;height:100%;overflow:visible;filter:drop-shadow(3px 3px 0 var(--ink))}
.coin:hover{transform:translateY(-3px) rotate(-10deg)}
.coin:active{transform:translateY(2px) scale(.92)}
.coin.bump{animation:bump .4s var(--bounce)}
@keyframes bump{30%{transform:scale(1.3) rotate(15deg)}}
.liketxt{font-size:13px;font-weight:800;opacity:.8}
.likecount{font-family:var(--display);font-size:22px;line-height:1;background:#fff;border:2.5px solid var(--ink);border-radius:999px;padding:5px 11px;box-shadow:2px 2px 0 var(--ink);min-width:48px;text-align:center}
.likecount.up{animation:bump .35s var(--bounce)}
/* 投币口：从卡片右下角冒出来 */
.slot{position:absolute;right:14px;bottom:-16px;width:118px;height:62px;background:var(--pink);border:3px solid var(--ink);border-radius:16px;box-shadow:var(--shadow-sm);transform:scale(0) rotate(8deg);transform-origin:bottom right;transition:transform .45s var(--bounce);z-index:5;pointer-events:none;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px}
.slot .slit{width:48px;height:10px;background:var(--ink);border-radius:999px;box-shadow:inset 0 3px 0 rgba(255,255,255,.25)}
.slot .lbl{font:800 11px/1 var(--body);background:var(--cream);border:2px solid var(--ink);border-radius:999px;padding:3px 8px}
.slot.show{transform:scale(1) rotate(-3deg)}
.slot.eat{animation:eat .5s ease-in-out}
@keyframes eat{25%{transform:scale(1.08,.9) rotate(-3deg)}55%{transform:scale(.95,1.1) rotate(-1deg)}}
.flycoin{position:absolute;width:40px;height:40px;z-index:6;pointer-events:none;left:0;top:0}
.flycoin svg{width:100%;height:100%;overflow:visible;filter:drop-shadow(2px 2px 0 var(--ink))}
.plusone{position:absolute;z-index:7;pointer-events:none;font-family:var(--display);font-size:26px;color:#fff;-webkit-text-stroke:2px var(--ink);paint-order:stroke fill;text-shadow:3px 3px 0 var(--ink);animation:rise 1s ease-out forwards}
@keyframes rise{from{transform:translate(-50%,0) scale(.6);opacity:0}30%{opacity:1}to{transform:translate(-50%,-70px) scale(1.2);opacity:0}}
.cover .badge{position:absolute;right:12px;bottom:12px;background:#fff;border:2.5px solid var(--ink);border-radius:999px;padding:4px 9px;font:800 12px/1 var(--body);box-shadow:2px 2px 0 var(--ink);display:flex;align-items:center;gap:4px;z-index:2}
.cover .badge svg{width:16px;height:16px}
.note{margin:12px 0 0;""")

# ---------- JS ----------
rep("""let jokes = [];
let filter = {k:"all", v:null};""",
"""let jokes = [];
let filter = {k:"all", v:null};
/* 投币数存在浏览器本地（GitHub Pages 没有后端） */
let coins = {};
try { coins = JSON.parse(localStorage.getItem("coldjokes.coins") || "{}"); } catch(e) { coins = {}; }
function saveCoins(){ try { localStorage.setItem("coldjokes.coins", JSON.stringify(coins)); } catch(e){} }
const COIN_SVG = `<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="17" fill="#e8f500" stroke="#141414" stroke-width="3"/><circle cx="20" cy="20" r="11.5" fill="none" stroke="#141414" stroke-width="2.2" stroke-dasharray="3 3"/><text x="20" y="25" text-anchor="middle" font-family="ZCOOL KuaiLe, Microsoft YaHei, sans-serif" font-size="14" font-weight="700" fill="#141414">冷</text></svg>`;""")

rep("""    <div class="punchbox" data-role="punch"><p class="punch">${esc(j.punch)}</p><span class="tape">${label}</span></div>
    ${j.note ? `<p class="note">${esc(j.note)}</p>` : ""}`;""",
"""    <div class="punchbox" data-role="punch"><p class="punch">${esc(j.punch)}</p><span class="tape">${label}</span></div>
    ${j.note ? `<p class="note">${esc(j.note)}</p>` : ""}
    <div class="like"><button class="coin" data-id="${j.id}" title="投一枚冷币">${COIN_SVG}</button><span class="liketxt">觉得冷？投个币</span><span class="likecount" data-count="${j.id}">${coins[j.id]||0}</span></div>`;""")

rep("""      ${middle}
      <span class="hint">${EMOJI[j.topic]||"✨"} ${esc(j.topic)} · 撕开</span>
    </div>`;""",
"""      ${middle}
      <span class="hint">${EMOJI[j.topic]||"✨"} ${esc(j.topic)} · 撕开</span>
      ${coins[j.id] ? `<span class="badge">${COIN_SVG} ×${coins[j.id]}</span>` : ""}
    </div>`;""")

# 星星爆开抽成公用函数
rep("""    const colors = ["#e8f500","#ff8a3d","#f9a8d4","#5eead4","#b197fc","#fff"];
    for(let i=0;i<10;i++){
      const s = document.createElement("span"); s.className="spark";
      const ang = (i/10)*Math.PI*2 + hash(i,1);
      const d = 70 + hash(i,2)*60;
      s.style.setProperty("--dx", Math.cos(ang)*d+"px"); s.style.setProperty("--dy", Math.sin(ang)*d+"px");
      s.innerHTML = `<svg viewBox="0 0 100 100"><path d="M50 5 L62 38 L95 50 L62 62 L50 95 L38 62 L5 50 L38 38 Z" fill="${colors[i%colors.length]}" stroke="#141414" stroke-width="8" stroke-linejoin="round"/></svg>`;
      box.appendChild(s); setTimeout(()=>s.remove(), 900);
    }
  }, 480);
}""",
"""    burst(box);
  }, 480);
}
function burst(host, x, y, n=10){
  const colors = ["#e8f500","#ff8a3d","#f9a8d4","#5eead4","#b197fc","#fff"];
  for(let i=0;i<n;i++){
    const s = document.createElement("span"); s.className="spark";
    if(x!=null){ s.style.left = x+"px"; s.style.top = y+"px"; }
    const ang = (i/n)*Math.PI*2 + hash(i,1);
    const d = 60 + hash(i,2)*60;
    s.style.setProperty("--dx", Math.cos(ang)*d+"px"); s.style.setProperty("--dy", Math.sin(ang)*d+"px");
    s.innerHTML = `<svg viewBox="0 0 100 100"><path d="M50 5 L62 38 L95 50 L62 62 L50 95 L38 62 L5 50 L38 38 Z" fill="${colors[i%colors.length]}" stroke="#141414" stroke-width="8" stroke-linejoin="round"/></svg>`;
    host.appendChild(s); setTimeout(()=>s.remove(), 900);
  }
}

/* 投币：硬币从按钮飞到右下角冒出来的投币口，掉进去，+1 */
function dropCoin(btn){
  const host = btn.closest(".card, .box");
  const id = btn.dataset.id;
  let slot = host.querySelector(".slot");
  if(!slot){
    slot = document.createElement("div"); slot.className="slot";
    slot.innerHTML = `<span class="slit"></span><span class="lbl">投币口</span>`;
    host.appendChild(slot);
  }
  clearTimeout(slot._hide);
  requestAnimationFrame(() => slot.classList.add("show"));
  btn.classList.remove("bump"); void btn.offsetWidth; btn.classList.add("bump");

  const hr = host.getBoundingClientRect(), br = btn.getBoundingClientRect();
  /* 卡片本身带旋转，用未旋转的盒子尺寸算：按钮相对卡片左上角的位置 */
  const sx = btn.offsetLeft + btn.offsetParent.offsetLeft, sy = btn.offsetTop + btn.offsetParent.offsetTop;
  const ex = host.clientWidth - 14 - 118/2 - 20, ey = host.clientHeight - 16 - 62 + 14 - 20;
  const fly = document.createElement("div"); fly.className="flycoin"; fly.innerHTML = COIN_SVG;
  fly.style.left = sx + "px"; fly.style.top = sy + "px";
  host.appendChild(fly);
  const dx = ex - sx, dy = ey - sy;
  const anim = fly.animate([
    {transform:"translate(0,0) rotate(0deg)", offset:0},
    {transform:`translate(${dx*0.5}px,${Math.min(dy,0)-90}px) rotate(200deg)`, offset:.5},
    {transform:`translate(${dx}px,${dy-6}px) rotate(360deg) scaleX(1)`, offset:.78},
    {transform:`translate(${dx}px,${dy+14}px) rotate(360deg) scaleX(.12)`, opacity:0, offset:1}
  ], {duration:900, easing:"cubic-bezier(.3,.9,.4,1)", fill:"forwards"});
  anim.onfinish = () => {
    fly.remove();
    slot.classList.remove("eat"); void slot.offsetWidth; slot.classList.add("eat");
    coins[id] = (coins[id]||0) + 1; saveCoins();
    document.querySelectorAll(`.likecount[data-count="${id}"]`).forEach(c => { c.textContent = coins[id]; c.classList.remove("up"); void c.offsetWidth; c.classList.add("up"); });
    const card = document.querySelector(`.card .coin[data-id="${id}"]`)?.closest(".card");
    if(card){ const cv = card.querySelector(".cover"); let b = cv.querySelector(".badge"); if(!b){ b = document.createElement("span"); b.className="badge"; cv.appendChild(b); } b.innerHTML = `${COIN_SVG} ×${coins[id]}`; }
    const plus = document.createElement("span"); plus.className="plusone"; plus.textContent="+1";
    plus.style.left = (ex+20) + "px"; plus.style.top = (ey-10) + "px";
    host.appendChild(plus); setTimeout(()=>plus.remove(), 1000);
    burst(host, ex+20, ey+10, 8);
    slot._hide = setTimeout(() => slot.classList.remove("show"), 1300);
  };
}""")

rep("""    el.addEventListener("click", e => {
      if(!el.classList.contains("open")){ el.classList.add("open"); return; }
      const box = e.target.closest(".punchbox"); if(box) revealPunch(box);
    });""",
"""    el.addEventListener("click", e => {
      const coin = e.target.closest(".coin"); if(coin){ dropCoin(coin); return; }
      if(!el.classList.contains("open")){ el.classList.add("open"); return; }
      const box = e.target.closest(".punchbox"); if(box) revealPunch(box);
    });""")

rep("""mbody.addEventListener("click", e => { const box = e.target.closest(".punchbox"); if(box) revealPunch(box); });""",
"""mbody.addEventListener("click", e => { const coin = e.target.closest(".coin"); if(coin){ dropCoin(coin); return; } const box = e.target.closest(".punchbox"); if(box) revealPunch(box); });""")

# 弹窗里的硬币落点用 .box，它要 overflow 可见且 relative（已是）
open(p, 'w', encoding='utf-8').write(s)
print('patched')
