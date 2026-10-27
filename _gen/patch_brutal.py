p = r'G:\github\cold-jokes\index.html'
s = open(p, encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)

# ---------- 背景：tibo 那种米色点阵纸 ----------
rep("""body{font-family:var(--body);color:var(--ink);background-color:var(--lime);
  background-image:linear-gradient(rgba(20,20,20,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(20,20,20,.07) 1px,transparent 1px);
  background-size:36px 36px;overflow:hidden}""",
"""body{font-family:var(--body);color:var(--ink);background-color:#faf6ea;
  background-image:radial-gradient(#c9c0a7 1.2px,transparent 1.3px);
  background-size:22px 22px;overflow:hidden}""")
rep(".loader{position:fixed;inset:0;z-index:100;background:var(--lime);background-image:inherit;",
    ".loader{position:fixed;inset:0;z-index:100;background:#faf6ea;background-image:radial-gradient(#c9c0a7 1.2px,transparent 1.3px);background-size:22px 22px;")

# ---------- 泡泡：平涂 + 黑描边 + 硬阴影，高光是一块平的白月牙 ----------
rep(""".bubble{position:absolute;left:0;top:0;z-index:4;border-radius:50%;cursor:pointer;will-change:transform;
  border:3px solid var(--ink);
  background:radial-gradient(circle at 32% 28%, rgba(255,255,255,.95) 0, rgba(255,255,255,.4) 16%, var(--c) 48%, var(--c) 86%, rgba(20,20,20,.18) 100%);
  box-shadow:inset -6px -8px 0 rgba(20,20,20,.08), 4px 5px 0 rgba(20,20,20,.55)}
.bubble::before{content:"";position:absolute;left:14%;top:9%;width:30%;height:18%;border-radius:50%;background:#fff;transform:rotate(-30deg);opacity:.9;pointer-events:none}
.bubble::after{content:"";position:absolute;right:16%;bottom:12%;width:12%;height:8%;border-radius:50%;background:#fff;opacity:.7;pointer-events:none}
.bubble.pic{background-image:var(--img);background-size:cover;background-position:center}
.bubble.pic .tint{position:absolute;inset:0;border-radius:50%;background:radial-gradient(circle at 32% 28%, rgba(255,255,255,.75) 0, rgba(255,255,255,.1) 30%, rgba(255,255,255,0) 55%, rgba(20,20,20,.2) 100%);pointer-events:none}""",
""".bubble{position:absolute;left:0;top:0;z-index:4;border-radius:50%;cursor:pointer;will-change:transform;
  border:4px solid var(--ink);background:var(--c);
  box-shadow:6px 6px 0 var(--ink)}
.bubble::before{content:"";position:absolute;left:16%;top:11%;width:26%;height:14%;border-radius:50%;background:#fff;border:3px solid var(--ink);transform:rotate(-32deg);pointer-events:none}
.bubble.small::before{border-width:2px}
.bubble.pic{background:var(--img) center/cover no-repeat}
.bubble.pic::before{display:none}
.bubble.pic .tint{display:none}""")
rep(".bubble .big{font-family:var(--display);font-size:calc(var(--d) * .42);line-height:1;color:#fff;-webkit-text-stroke:2px var(--ink);paint-order:stroke fill;text-shadow:3px 3px 0 var(--ink)}",
    ".bubble .big{font-family:var(--display);font-size:calc(var(--d) * .42);line-height:1;color:#fff;-webkit-text-stroke:2.5px var(--ink);paint-order:stroke fill;text-shadow:4px 4px 0 var(--ink)}")
rep(".bubble .hint{font-weight:800;font-size:max(10px,calc(var(--d) * .09));background:var(--cream);border:2.5px solid var(--ink);border-radius:999px;padding:3px 8px;box-shadow:2px 2px 0 var(--ink);white-space:nowrap}",
    ".bubble .hint{font-weight:800;font-size:max(10px,calc(var(--d) * .09));background:#fff;border:2.5px solid var(--ink);border-radius:999px;padding:3px 8px;box-shadow:3px 3px 0 var(--ink);white-space:nowrap}")

# 打开的泡泡：米色、粗边、大硬阴影；内容区宽度固定、高度随内容
rep(""".bubble.open{z-index:30;background:radial-gradient(circle at 32% 28%, #fff 0, rgba(255,255,255,.9) 30%, var(--c) 100%);box-shadow:inset -8px -10px 0 rgba(20,20,20,.08), 6px 7px 0 var(--ink)}
.bubble.open .face{display:none}
.bubble .inner{display:none;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:74%;height:74%;overflow:hidden;flex-direction:column;justify-content:center}
.bubble.open .inner{display:flex}""",
""".bubble.open{z-index:30;background:var(--cream);box-shadow:9px 9px 0 var(--ink)}
.bubble.open::before{display:none}
.bubble.open .face{display:none}
.bubble .inner{display:none;position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:var(--iw,300px);flex-direction:column;justify-content:center}
.bubble.open .inner{display:flex}""")
rep(".meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:11px;font-weight:800;margin-bottom:8px;justify-content:center}",
    ".meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:12px;font-weight:800;margin-bottom:10px;justify-content:center}")
rep(".setup{font-size:15px;line-height:1.5;white-space:pre-line;font-weight:700;margin:0;text-align:center}\n.zh .setup{font-size:16px}",
    ".setup{font-size:18px;line-height:1.55;white-space:pre-line;font-weight:800;margin:0;text-align:center}\n.zh .setup{font-size:20px}")
rep(".punch{margin:0;font-size:16px;line-height:1.45;", ".punch{margin:0;font-size:19px;line-height:1.45;")
rep(".zh .punch{font-size:17px}", ".zh .punch{font-size:21px}")
rep(".note{margin:8px 0 0;font-size:12px;line-height:1.4;", ".note{margin:10px 0 0;font-size:13px;line-height:1.45;")

# ---------- 底栏、空态 ----------
rep(".dock{position:fixed;left:0;right:0;bottom:0;height:var(--dock);z-index:40;background:var(--cream);border-top:3px solid var(--ink);",
    ".dock{position:fixed;left:0;right:0;bottom:0;height:var(--dock);z-index:40;background:#fff;border-top:4px solid var(--ink);")

# ---------- 颜色：不透明平涂 ----------
rep('const COLORS = ["rgba(232,245,0,.85)","rgba(0,230,118,.75)","rgba(94,234,212,.8)","rgba(249,168,212,.85)","rgba(177,151,252,.8)","rgba(255,138,61,.75)","rgba(154,220,249,.85)","rgba(255,255,255,.8)"];',
    'const COLORS = ["#e8f500","#00e676","#5eead4","#f9a8d4","#b197fc","#ff8a3d","#9adcf9","#fff"];')

# ---------- 打开：按内容高度算直径 ----------
rep("""function openBubble(b){
  if(opened && opened!==b) closeBubble(opened);
  b.open = true; opened = b;
  b.el.classList.add("open"); b.el.style.zIndex = ++topZ;
  b.el.querySelector(".inner").innerHTML = bodyHTML(b.j);
  b.tr = Math.min(260, (H-24)/2, (W-24)/2);
  b.vx = b.vy = 0;
}""",
"""function openBubble(b){
  if(opened && opened!==b) closeBubble(opened);
  b.open = true; opened = b;
  b.el.classList.add("open"); b.el.style.zIndex = ++topZ;
  b.el.querySelector(".inner").innerHTML = bodyHTML(b.j);
  b.vx = b.vy = 0;
  fitOpen(b);
}
/* 内容区宽度固定，量出高度，取能装下这个矩形的最小圆 */
function fitOpen(b){
  const rmax = Math.min((H-24)/2, (W-24)/2);
  const iw = clamp(Math.round(rmax*1.15), 220, 360);
  const inner = b.el.querySelector(".inner");
  b.el.style.setProperty("--iw", iw+"px");
  const h = inner.offsetHeight;
  const need = Math.sqrt(iw*iw + h*h)/2 + 22;
  b.tr = clamp(need, 120, rmax);
}""")
rep("""function revealPunch(box){
  if(box.classList.contains("drum")) return;
  box.classList.add("drum");
  setTimeout(() => { box.classList.remove("drum"); box.classList.add("shown"); burst(box); }, 480);
}""",
"""function revealPunch(box){
  if(box.classList.contains("drum")) return;
  box.classList.add("drum");
  setTimeout(() => { box.classList.remove("drum"); box.classList.add("shown"); burst(box); if(opened) fitOpen(opened); }, 480);
}""")
open(p, 'w', encoding='utf-8').write(s)
print('patched')
