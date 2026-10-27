"""把生成的贴纸表切成单张，裁掉透明边，压掉半透明光晕。
用法：python split.py <sheet.png> <cols> <rows> <输出前缀> [最大边长]
      python split.py --trim <in.png> <out.png> [最大边长]
"""
import sys
from PIL import Image
import numpy as np

def clean(im, maxside=None):
    im = im.convert('RGBA')
    a = np.array(im)
    alpha = a[..., 3].astype(np.int32)
    # 光晕：alpha 低于 60 的全部清零，60-200 之间线性拉伸
    alpha = np.clip((alpha - 60) * 255 // 140, 0, 255)
    a[..., 3] = alpha.astype(np.uint8)
    im = Image.fromarray(a)
    bbox = im.getchannel('A').point(lambda v: 255 if v > 10 else 0).getbbox()
    if bbox:
        im = im.crop(bbox)
    if maxside and max(im.size) > maxside:
        s = maxside / max(im.size)
        im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    return im

if sys.argv[1] == '--trim':
    im = clean(Image.open(sys.argv[2]), int(sys.argv[4]) if len(sys.argv) > 4 else None)
    im.save(sys.argv[3], optimize=True)
    print(sys.argv[3], im.size)
else:
    sheet = Image.open(sys.argv[1]).convert('RGBA')
    cols, rows, prefix = int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    maxside = int(sys.argv[5]) if len(sys.argv) > 5 else None
    cw, ch = sheet.width / cols, sheet.height / rows
    n = 0
    for r in range(rows):
        for c in range(cols):
            n += 1
            cell = sheet.crop((round(c * cw), round(r * ch), round((c + 1) * cw), round((r + 1) * ch)))
            im = clean(cell, maxside)
            out = f'{prefix}{n}.png'
            im.save(out, optimize=True)
            print(out, im.size)
