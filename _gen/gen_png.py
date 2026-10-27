"""调 AIX888 本地 Router 生成透明底 PNG（gpt-image-2）。
用法：python gen_png.py 提示词.txt 输出.png [size] [transparent|opaque]
"""
import sys, json, base64, time, urllib.request, urllib.error
sys.stdout.reconfigure(encoding='utf-8')
ROUTER = 'http://127.0.0.1:18189/v1'

prompt = open(sys.argv[1], encoding='utf-8').read()
out = sys.argv[2]
size = sys.argv[3] if len(sys.argv) > 3 else '1024x1024'
bg = sys.argv[4] if len(sys.argv) > 4 else 'transparent'
payload = {'model': 'gpt-image-2', 'prompt': prompt, 'size': size, 'n': 1, 'quality': 'high',
           'output_format': 'png'}
if bg == 'transparent':
    payload['background'] = 'transparent'
r = urllib.request.Request(ROUTER + '/images/generations', data=json.dumps(payload).encode('utf-8'), method='POST',
                           headers={'Authorization': 'Bearer local-router-only', 'Content-Type': 'application/json',
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) codex_cli_rs/0.160.0', 'Accept': 'application/json'})
t0 = time.time()
try:
    with urllib.request.urlopen(r, timeout=900) as f:
        d = json.loads(f.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    raise SystemExit(f'HTTP {e.code}: {e.read().decode("utf-8", "replace")[:800]}')
item = d['data'][0]
if item.get('b64_json'):
    open(out, 'wb').write(base64.b64decode(item['b64_json']))
elif item.get('url'):
    with urllib.request.urlopen(item['url'], timeout=300) as f:
        open(out, 'wb').write(f.read())
else:
    raise SystemExit('no image: ' + json.dumps({k: v for k, v in item.items() if k != 'b64_json'})[:500])
print('saved', out, f'{time.time() - t0:.0f}s')
