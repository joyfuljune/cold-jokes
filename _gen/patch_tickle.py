p = r'G:\github\cold-jokes\index.html'
s = open(p, encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)

# ---------- 删掉说明性文字 ----------
rep("""    <p class="bye">再点一下泡泡就炸</p>`;""", """`;""")
rep(".bye{margin:8px 0 0;font-size:11px;font-weight:800;opacity:.55;text-align:center}\n.punchbox:not(.shown) ~ .bye{display:none}\n", "")
rep('<div class="tagline">独角兽吹的泡泡。点一下看题，再点揭<b>谜底</b>，再点就炸。</div>',
    '<div class="tagline">独角兽吹的泡泡，每一个都很<b>冷</b>。</div>')

# ---------- 结构：外层盒子管位置和漂浮，里面的图管反应动画 ----------
rep('<img class="hero" id="hero" src="img/hero.png" alt="毛茸茸的独角兽">',
    '<div class="herobox" id="herobox"><img class="hero" id="hero" src="img/hero.png" alt="毛茸茸的独角兽" draggable="false"></div>')
rep(""".hero{position:absolute;z-index:3;filter:drop-shadow(7px 7px 0 rgba(20,20,20,.9));pointer-events:none;transform-origin:50% 100%}
.hero.float{animation:floaty 4.5s ease-in-out infinite}""",
""".herobox{position:absolute;z-index:5;transform-origin:50% 100%}
.herobox.float{animation:floaty 4.5s ease-in-out infinite}
.hero{width:100%;height:auto;filter:drop-shadow(7px 7px 0 rgba(20,20,20,.9));transform-origin:50% 100%;cursor:url("img/paw-press.svg") 8 8, pointer;user-select:none}
.giggle{position:absolute;z-index:8;pointer-events:none;font-family:var(--zh);font-size:26px;background:#fff;border:3px solid var(--ink);border-radius:14px;padding:6px 12px;box-shadow:4px 4px 0 var(--ink);white-space:nowrap;animation:giggle .9s ease-out forwards}
.giggle::after{content:"";position:absolute;left:18px;bottom:-12px;width:14px;height:14px;background:#fff;border-right:3px solid var(--ink);border-bottom:3px solid var(--ink);transform:rotate(45deg)}
@keyframes giggle{from{transform:translate(-20%,10px) rotate(-6deg) scale(.5);opacity:0}25%{transform:translate(-20%,-6px) rotate(4deg) scale(1.1);opacity:1}to{transform:translate(-20%,-70px) rotate(-3deg) scale(1);opacity:0}}""")
rep('hero.style.width = hw+"px"; hero.style.left = hx+"px"; hero.style.top = hy+"px";',
    'herobox.style.width = hw+"px"; herobox.style.left = hx+"px"; herobox.style.top = hy+"px";')
rep('const field = document.getElementById("field"), hero = document.getElementById("hero"),',
    'const field = document.getElementById("field"), hero = document.getElementById("hero"), herobox = document.getElementById("herobox"),')
rep('document.getElementById("rescatter").onclick = () => { hero.classList.remove("float"); heroDrop(); render(); };',
    'document.getElementById("rescatter").onclick = () => { herobox.classList.remove("float"); heroDrop(); render(); };')
rep('  ], {duration:1250, easing:"ease-out", fill:"backwards"}).onfinish = () => { shake(); hero.classList.add("float"); };',
    '  ], {duration:1250, easing:"ease-out", fill:"backwards"}).onfinish = () => { shake(); herobox.classList.add("float"); };')

# ---------- 五种反应 ----------
rep("function shake(){", r"""/* ---------- 戳独角兽：五种反应，挠痒最常见 ---------- */
let heroBusy = false;
const GIGGLES = ["咯叽咯叽", "哈哈哈哈", "别挠啦！", "嘻嘻嘻", "痒痒痒~", "咯咯咯"];
hero.addEventListener("click", e => {
  if(heroBusy) return; heroBusy = true;
  const r = hero.getBoundingClientRect();
  const px = (e.clientX - r.left)/r.width;
  const side = px < .5 ? -1 : 1;
  const roll = R();
  const kind = roll < .45 ? "tickle" : roll < .62 ? "dodge" : roll < .8 ? "run" : roll < .92 ? "jump" : "spin";
  const fx = field.getBoundingClientRect();
  const cx = e.clientX - fx.left, cy = e.clientY - fx.top;
  burst(field, cx, cy, 7);
  if(kind !== "run") say(cx, cy, pick(GIGGLES));
  const done = () => { heroBusy = false; };
  if(kind === "tickle"){
    hero.animate([
      {transform:"rotate(0) scale(1,1)"},
      {transform:`translate(${-side*6}px,0) rotate(${-side*4}deg) scale(1.06,.94)`},
      {transform:`translate(${side*5}px,-4px) rotate(${side*5}deg) scale(.95,1.06)`},
      {transform:`translate(${-side*6}px,0) rotate(${-side*4}deg) scale(1.06,.94)`},
      {transform:`translate(${side*5}px,-4px) rotate(${side*5}deg) scale(.95,1.06)`},
      {transform:`translate(${-side*4}px,0) rotate(${-side*3}deg) scale(1.04,.96)`},
      {transform:"rotate(0) scale(1,1)"}
    ], {duration:900, easing:"ease-in-out"}).onfinish = done;
    setTimeout(() => say(cx + rnd(-60,60), cy - 50, pick(GIGGLES)), 350);
  } else if(kind === "dodge"){
    hero.animate([
      {transform:"translate(0,0) rotate(0)"},
      {transform:`translate(${-side*70}px,-10px) rotate(${-side*14}deg) scale(.96,1.04)`, offset:.3},
      {transform:`translate(${-side*55}px,0) rotate(${-side*8}deg)`, offset:.6},
      {transform:"translate(0,0) rotate(0)"}
    ], {duration:1100, easing:"cubic-bezier(.2,1.2,.4,1)"}).onfinish = done;
  } else if(kind === "run"){
    const off = side < 0 ? W + 400 : -(W + 400);
    const a1 = hero.animate([
      {transform:"translate(0,0) scaleX(1)"},
      {transform:`translate(${-side*30}px,0) scaleX(${-side}) rotate(0)`, offset:.15},
      {transform:`translate(${off*.5}px,-30px) scaleX(${-side}) rotate(${-side*8}deg)`, offset:.55},
      {transform:`translate(${off}px,0) scaleX(${-side}) rotate(0)`, offset:1}
    ], {duration:900, easing:"cubic-bezier(.5,0,.8,.3)", fill:"forwards"});
    say(cx, cy, "溜了溜了！");
    a1.onfinish = () => setTimeout(() => {
      const a2 = hero.animate([
        {transform:`translate(${-off}px,0) scaleX(${side})`},
        {transform:`translate(${-off*.5}px,-30px) scaleX(${side}) rotate(${side*8}deg)`, offset:.5},
        {transform:`translate(${side*20}px,0) scaleX(${side})`, offset:.85},
        {transform:"translate(0,0) scaleX(1) scale(1.15,.85)", offset:.93},
        {transform:"translate(0,0) scaleX(1)"}
      ], {duration:1100, easing:"cubic-bezier(.2,.8,.4,1)", fill:"forwards"});
      a2.onfinish = () => { a1.cancel(); a2.cancel(); const hb = herobox.getBoundingClientRect(); say(hb.left - fx.left + hb.width*.6, hb.top - fx.top + hb.height*.25, "我回来啦"); done(); };
    }, 500);
  } else if(kind === "jump"){
    hero.animate([
      {transform:"translateY(0) scale(1,1)"},
      {transform:"translateY(0) scale(1.15,.8)", offset:.15},
      {transform:"translateY(-120px) scale(.92,1.1)", offset:.5},
      {transform:"translateY(0) scale(1.2,.78)", offset:.8},
      {transform:"translateY(-14px) scale(.97,1.03)", offset:.9},
      {transform:"translateY(0) scale(1,1)"}
    ], {duration:1000, easing:"ease-in-out"}).onfinish = () => { shake(); done(); };
  } else {
    hero.animate([
      {transform:"rotate(0) scale(1)"},
      {transform:"translateY(-40px) rotate(180deg) scale(.9)", offset:.5},
      {transform:"translateY(0) rotate(360deg) scale(1.1,.9)", offset:.9},
      {transform:"rotate(360deg) scale(1)"}
    ], {duration:1000, easing:"cubic-bezier(.3,.1,.3,1)"}).onfinish = done;
  }
});
function say(x, y, text){
  const g = document.createElement("div"); g.className = "giggle"; g.textContent = text;
  g.style.left = clamp(x, 60, W-140) + "px"; g.style.top = clamp(y - 70, 10, H-80) + "px";
  field.appendChild(g); setTimeout(() => g.remove(), 950);
}
function shake(){""")
open(p, 'w', encoding='utf-8').write(s)
print('patched')
