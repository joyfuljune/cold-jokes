# 冷笑话收集站

一张张贴纸，每张背后藏一个冷笑话或双关。点开看。

在线：https://joyfuljune.github.io/cold-jokes/

## 添一条

只改 `jokes.json`，在数组末尾加一项：

```json
{
  "id": 36,
  "setup": "题面或铺垫，换行用 
",
  "punch": "谜底或最后一句，要再点一下才显示",
  "lang": "zh",
  "country": "CN",
  "topic": "动物",
  "date": "2026-10-29",
  "note": "可选：解释笑点"
}
```

- `id` 递增就行，它决定贴纸颜色、倾斜角、封面样式和撕开动画
- `setup` 以问号结尾时按钮写"揭晓谜底"，否则写"看下一句"
- `lang` 用两位语言码：zh / en / fr，新语言会自动出现在筛选条
- `topic` 自由填，已有：动物 食物 科学 语言 职业 日常 数学；新主题也会自动出现
- `note` 可以不写，只在谜底揭晓后显示

直接在 GitHub 网页上改 `jokes.json` 提交即可，Pages 一两分钟后更新。

## 图

`img/` 里的独角兽和装饰贴纸由 gpt-image-2 生成，提示词和切图脚本在 `_gen/`。

## 本地预览

```
python -m http.server 8765
```

然后开 http://127.0.0.1:8765/ 。直接双击 index.html 读不到 jokes.json。
