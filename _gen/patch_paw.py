p = r'G:\github\cold-jokes\index.html'
s = open(p, encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, old[:70]
    s = s.replace(old, new)

# 硬币按钮、投币口、爪子都换成生成的图
rep(".coin svg{width:100%;height:100%;overflow:visible;filter:drop-shadow(3px 3px 0 var(--ink))}",
    ".coin img{width:100%;height:100%;filter:drop-shadow(3px 3px 0 var(--ink))}")
rep(".coin{appearance:none;border:0;background:none;padding:0;width:40px;height:40px;",
    ".coin{appearance:none;border:0;background:none;padding:0;width:46px;height:46px;")
rep(".slot{position:absolute;right:17%;bottom:15%;width:72px;height:52px;transform:scale(0);transform-origin:bottom right;transition:transform .4s var(--bounce);z-index:5;pointer-events:none}\n.slot svg{width:100%;height:100%;overflow:visible}",
    ".slot{position:absolute;right:17%;bottom:13%;width:58px;height:84px;transform:scale(0);transform-origin:bottom right;transition:transform .4s var(--bounce);z-index:5;pointer-events:none}\n.slot img{width:100%;height:100%;filter:drop-shadow(4px 4px 0 var(--ink))}")
rep(".pawcoin{position:absolute;width:64px;height:84px;z-index:6;pointer-events:none;left:0;top:0}\n.pawcoin svg{width:100%;height:100%;overflow:visible}",
    ".pawcoin{position:absolute;width:88px;height:190px;z-index:6;pointer-events:none;left:0;top:0}\n.pawcoin .paw{position:absolute;left:0;top:40px;width:88px;height:144px;background:url('img/pawbig.png') center/contain no-repeat;filter:drop-shadow(4px 4px 0 var(--ink))}\n.pawcoin .pc{position:absolute;left:19px;top:0;width:50px;height:50px;background:url('img/coin.png') center/contain no-repeat;filter:drop-shadow(3px 3px 0 var(--ink))}")
rep('const COIN_SVG = `<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="17" fill="#e8f500" stroke="#141414" stroke-width="3"/><circle cx="20" cy="20" r="11.5" fill="none" stroke="#141414" stroke-width="2.2" stroke-dasharray="3 3"/><text x="20" y="25" text-anchor="middle" font-family="ZCOOL KuaiLe, Microsoft YaHei, sans-serif" font-size="14" font-weight="700" fill="#141414">冷</text></svg>`;',
    'const COIN_SVG = `<img src="img/coin.png" alt="投币">`;')
# 删掉旧的 SVG 常量
i = s.index('/* 游戏机投币口：面板 + 竖缝 + 小箭头，没有文字 */'); j = s.index('let jokes = [], filter')
s = s[:i] + 'const SLOT_IMG = `<img src="img/slot.png" alt="">`;\nconst PAWCOIN_HTML = `<div class="pc"></div><div class="paw"></div>`;\n\n' + s[j:]
rep('slot.innerHTML = SLOT_SVG;', 'slot.innerHTML = SLOT_IMG;')
rep('pc.innerHTML = PAWCOIN_SVG;', 'pc.innerHTML = PAWCOIN_HTML;')
# 位置：投币口 58x84 在右下，缝在面板中部；爪子从底下伸上来，币顶到缝口
rep("const sx = D - D*.17 - 36 - 32, sy = D - D*.15 - 52;      // 投币口在圆内右下，缝在面板中上部",
    "const sx = D - D*.17 - 29 - 44, sy = D - D*.13 - 84;      // 投币口左上角；爪子举币对准缝的下口")
rep('pc.style.left = sx+"px"; pc.style.top = (sy+22)+"px"; host.appendChild(pc);',
    'pc.style.left = sx+"px"; pc.style.top = (sy+30)+"px"; host.appendChild(pc);')
rep('pc.animate([{transform:"translateY(120px) rotate(10deg)", opacity:0},{transform:"translateY(0) rotate(0)", opacity:1}], {duration:420,',
    'pc.animate([{transform:"translateY(200px) rotate(8deg)", opacity:0},{transform:"translateY(0) rotate(0)", opacity:1}], {duration:480,')
rep('coinG.animate([{transform:"translateY(0) scaleX(1)"},{transform:"translateY(-22px) scaleX(.1)", opacity:0}], {duration:260,',
    'coinG.animate([{transform:"translateY(0) scaleX(1)"},{transform:"translateY(-34px) scaleX(.08)", opacity:0}], {duration:300,')
rep('plus.style.left = (sx+36) + "px"; plus.style.top = (sy-6) + "px";', 'plus.style.left = (sx+44) + "px"; plus.style.top = (sy-10) + "px";')
rep('burst(host, sx+36, sy+10, 8);', 'burst(host, sx+44, sy+20, 8);')
rep('pc.animate([{transform:"translateY(0)"},{transform:"translateY(130px)", opacity:0}], {duration:380,', 'pc.animate([{transform:"translateY(0)"},{transform:"translateY(220px)", opacity:0}], {duration:400,')
rep('const PRELOAD = ["img/hero.png","img/hero_wave.png","img/paw.svg","img/paw-press.svg",',
    'const PRELOAD = ["img/hero.png","img/hero_wave.png","img/paw.svg","img/paw-press.svg","img/pawbig.png","img/slot.png","img/coin.png",')
open(p, 'w', encoding='utf-8').write(s)
print('patched')
