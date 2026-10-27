PY=G:/conda_envs/tf-torch/python.exe; B=C:/Users/Administrator/.claude/tools/browser/browser.py; export PYTHONIOENCODING=utf-8
S=G:/CLI/tmp/claude-temp/C--Users-Administrator/f01a2583-ffea-4ac2-b1bc-3ad60997821b/scratchpad
$PY $B open "http://127.0.0.1:8765/" --tab 0 >/dev/null 2>&1; sleep 9
$PY $B eval 'const bs=[...document.querySelectorAll(".bubble")]; bs.find(b=>b.getBoundingClientRect().y>200 && b.getBoundingClientRect().x>400 && b.getBoundingClientRect().x<900).click(); "ok"' --tab 0 >/dev/null 2>&1; sleep 1.5
$PY $B eval 'document.querySelector(".bubble.open").click(); "ok"' --tab 0 >/dev/null 2>&1; sleep 1.3
$PY $B eval 'document.querySelector(".bubble.open .coin").click(); "ok"' --tab 0 >/dev/null 2>&1; sleep 2
$PY $B eval 'document.querySelector(".bubble.open").click(); "ok"' --tab 0 >/dev/null 2>&1; sleep 1
$PY $B eval 'const h=document.getElementById("hero"); const r=h.getBoundingClientRect(); h.dispatchEvent(new MouseEvent("click",{bubbles:true,clientX:r.left+r.width*.7,clientY:r.top+r.height*.5})); "ok"' --tab 0 >/dev/null 2>&1; sleep 0.5
$PY $B shot --tab 0 --out "$S/s1.png" >/dev/null 2>&1
$PY $B eval 'JSON.stringify({ac: typeof AC, state: AC && AC.state, n: document.querySelectorAll(".bubble").length, mute: document.getElementById("mute").textContent})' --tab 0 2>&1 | tail -1
$PY $B console --tab 0 2>&1 | grep -i "error" | head -3
echo done
