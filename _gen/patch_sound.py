p = r'G:\github\cold-jokes\index.html'
s = open(p, encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)

# 底栏加静音开关
rep('<a href="https://github.com/joyfuljune/cold-jokes/edit/main/jokes.json" target="_blank" rel="noopener">＋添一条</a>\n</nav>',
    '<a href="https://github.com/joyfuljune/cold-jokes/edit/main/jokes.json" target="_blank" rel="noopener">＋添一条</a>\n  <button class="chip" id="mute" aria-label="声音">🔊</button>\n</nav>')

# 合成音效
rep("let jokes = [], filter = {k:\"all\", v:null};", r"""/* ---------- 音效：全部用 Web Audio 现场合成，没有音频文件 ---------- */
let AC = null, muted = false;
try { muted = localStorage.getItem("coldjokes.muted") === "1"; } catch(e){}
function ac(){ if(!AC){ AC = new (window.AudioContext || window.webkitAudioContext)(); } if(AC.state === "suspended") AC.resume(); return AC; }
function tone(f0, f1, dur, type="sine", vol=.25, t0=0){
  if(muted) return; const c = ac(), o = c.createOscillator(), g = c.createGain(), t = c.currentTime + t0;
  o.type = type; o.frequency.setValueAtTime(f0, t); o.frequency.exponentialRampToValueAtTime(Math.max(f1,20), t + dur);
  g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(vol, t + .01); g.gain.exponentialRampToValueAtTime(.001, t + dur);
  o.connect(g).connect(c.destination); o.start(t); o.stop(t + dur + .02);
}
function noise(dur, vol=.3, hp=800, t0=0){
  if(muted) return; const c = ac(), t = c.currentTime + t0, n = Math.floor(c.sampleRate * dur), buf = c.createBuffer(1, n, c.sampleRate), d = buf.getChannelData(0);
  for(let i=0;i<n;i++) d[i] = (Math.random()*2-1) * (1 - i/n);
  const src = c.createBufferSource(); src.buffer = buf;
  const f = c.createBiquadFilter(); f.type = "highpass"; f.frequency.value = hp;
  const g = c.createGain(); g.gain.setValueAtTime(vol, t); g.gain.exponentialRampToValueAtTime(.001, t + dur);
  src.connect(f).connect(g).connect(c.destination); src.start(t);
}
const SFX = {
  blup(){ tone(300, 700, .12, "sine", .2); },                                   // 点泡泡：啵
  open(){ tone(400, 900, .18, "triangle", .18); tone(600, 1300, .25, "sine", .1, .06); },
  reveal(){ [0,.08,.16].forEach((d,i) => tone(500 + i*200, 500 + i*200, .12, "square", .08, d)); tone(900, 1400, .3, "sine", .15, .26); },
  pop(){ noise(.09, .5, 1500); tone(900, 150, .12, "sine", .3); },             // 炸：啪
  coin(){ tone(1319, 1319, .08, "square", .12); tone(1760, 1760, .35, "square", .12, .08); },   // 投币：叮叮
  slot(){ noise(.05, .25, 2500, .0); tone(200, 120, .08, "square", .12, .03); },
  giggle(side=1){ for(let i=0;i<6;i++){ const f = 700 + i*90 + Math.random()*80; tone(f, f*1.25, .07, "sine", .14, i*.085); } },
  dodge(){ tone(500, 180, .18, "sawtooth", .1); },
  steps(n=6, gap=.11){ for(let i=0;i<n;i++){ noise(.03, .22, 2000, i*gap); tone(i%2 ? 180 : 140, 90, .05, "triangle", .12, i*gap); } },
  jump(){ tone(300, 900, .22, "sine", .2); noise(.06, .3, 1200, .62); },
  spin(){ for(let i=0;i<8;i++) tone(400 + i*120, 400 + i*120, .06, "triangle", .1, i*.07); },
  land(){ noise(.08, .5, 400); tone(120, 50, .25, "sine", .4); },
  bubbleIn(){ tone(500 + Math.random()*400, 900 + Math.random()*500, .08, "sine", .05); },
};
document.getElementById("mute").onclick = e => { muted = !muted; e.currentTarget.textContent = muted ? "🔇" : "🔊"; try { localStorage.setItem("coldjokes.muted", muted ? "1" : "0"); } catch(err){} if(!muted) SFX.blup(); };
document.getElementById("mute").textContent = muted ? "🔇" : "🔊";

let jokes = [], filter = {k:"all", v:null};""")

# 接到各个动作上
rep("  if(!b.open){ openBubble(b); return; }\n  const box = b.el.querySelector(\".punchbox\");\n  if(!box.classList.contains(\"shown\")){ revealPunch(box); return; }\n  popBubble(b);",
    "  if(!b.open){ SFX.open(); openBubble(b); return; }\n  const box = b.el.querySelector(\".punchbox\");\n  if(!box.classList.contains(\"shown\")){ SFX.reveal(); revealPunch(box); return; }\n  SFX.pop(); popBubble(b);")
rep("  b.open = false; b.tr = b.r0; b.el.classList.remove(\"open\");", "  SFX.blup(); b.open = false; b.tr = b.r0; b.el.classList.remove(\"open\");")
rep("  if(coinBusy) return; coinBusy = true;", "  if(coinBusy) return; coinBusy = true; SFX.blup();")
rep("      slot.classList.remove(\"eat\"); void slot.offsetWidth; slot.classList.add(\"eat\");\n      fake[id] = (fake[id]||0) + 1;",
    "      slot.classList.remove(\"eat\"); void slot.offsetWidth; slot.classList.add(\"eat\"); SFX.slot(); SFX.coin();\n      fake[id] = (fake[id]||0) + 1;")
rep("  burst(field, cx, cy, 7);\n  if(kind !== \"run\") say(cx, cy, pick(GIGGLES));",
    "  burst(field, cx, cy, 7);\n  if(kind !== \"run\") say(cx, cy, pick(GIGGLES));\n  ({tickle:()=>SFX.giggle(), dodge:()=>{SFX.dodge(); SFX.giggle();}, run:()=>SFX.steps(8,.1), jump:()=>SFX.jump(), spin:()=>SFX.spin()})[kind]();")
rep("    a1.onfinish = () => setTimeout(() => {\n      const a2 = hero.animate([",
    "    a1.onfinish = () => setTimeout(() => {\n      SFX.steps(8,.1);\n      const a2 = hero.animate([")
rep("  ], {duration:1250, easing:\"ease-out\", fill:\"backwards\"}).onfinish = () => { shake(); herobox.classList.add(\"float\"); };",
    "  ], {duration:1250, easing:\"ease-out\", fill:\"backwards\"}).onfinish = () => { SFX.land(); shake(); herobox.classList.add(\"float\"); };")
rep("bodies.forEach(b => setTimeout(() => { b.live = true; b.el.style.opacity = 1; }, 400 + rnd(0, 3200)));",
    "bodies.forEach(b => setTimeout(() => { b.live = true; b.el.style.opacity = 1; if(AC) SFX.bubbleIn(); }, 400 + rnd(0, 3200)));")
open(p, 'w', encoding='utf-8').write(s)
print('patched')
