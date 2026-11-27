# -*- coding: utf-8 -*-
"""构建《礼记》站点：book/*.md -> docs/k/*.html + docs/index.html"""
import os, re, json, shutil, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "book")
DOCS = os.path.join(ROOT, "docs")
K = os.path.join(DOCS, "k")
SITE = "https://q1z2q3-debug.github.io/daokedao-liji"
TOTAL_PIAN = 49

CSS = """
:root{--paper:#F7F4EE;--ink:#25211D;--red:#994433;--brown:#7C6D5C;--line:#DCD5C8;}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink);overflow-x:hidden}
body{font-family:"Noto Serif SC","Songti SC","Source Han Serif SC",serif;font-size:17px;line-height:1.95;
 max-width:760px;margin:0 auto;padding:48px 28px 96px}
h1{font-size:28px;letter-spacing:3px;text-align:center;margin:6px 0 4px;font-weight:700}
h2{font-size:19px;margin:44px 0 12px;letter-spacing:2px;border-left:3px solid var(--red);padding-left:10px;font-weight:700}
p{margin:0 0 14px;text-align:justify}
blockquote{border-left:2px solid var(--line);margin:14px 0;padding:4px 0 4px 16px;color:#3B352F;font-size:15.5px}
blockquote p{letter-spacing:1.2px}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:15px}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left}
th{background:#FCFAF6}
figure{margin:26px 0;text-align:center}
figure img{width:100%;max-width:760px;border:1px solid var(--line);background:#F7F4EE}
figcaption{color:var(--brown);font-size:12.5px;letter-spacing:1px;margin-top:8px}
hr{border:none;border-top:1px solid var(--line);margin:36px 0}
.foot{color:var(--brown);font-size:12px;text-align:center;margin-top:60px;letter-spacing:1px}
a{color:var(--red);text-decoration:none}
.toc{columns:2;column-gap:28px;font-size:15px}
.toc p{margin:0 0 8px;text-align:left}
.ph{border:1px dashed var(--line);color:var(--brown);font-size:13px;text-align:center;padding:26px 12px;margin:18px 0;letter-spacing:1px}
details.prompt{border-left:2px solid var(--line);padding:8px 14px;margin:10px 0 20px;color:#4A453F;font-size:14px}
"""

SHELL = """<!doctype html><html lang="zh-Hans"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<style>{css}</style></head><body>
{body}
<div class="foot">{foot_head}<br>{foot_extra}</div>
</body></html>
"""


def conv(md_text):
    def fig(m):
        key, cap = m.group(1).strip(), m.group(2).strip()
        return ('<figure><img src="../assets/fig/%s.svg" alt="%s"><figcaption>%s</figcaption></figure>'
                % (key, cap, cap))
    md_text = re.sub(r"\{\{fig:([^|]+)\|([^}]+)\}\}", fig, md_text)
    r = subprocess.run(["pandoc", "-f", "markdown", "-t", "html", "--no-highlight"],
                       input=md_text, capture_output=True, text=True)
    return r.stdout


def main():
    os.makedirs(K, exist_ok=True)
    dst = os.path.join(DOCS, "assets", "fig")
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(os.path.join(ROOT, "assets", "fig"), dst)

    ver = open(os.path.join(ROOT, "VERSION"), encoding="utf-8").read().strip()
    files = sorted(f for f in os.listdir(BOOK) if re.match(r"LJ\d{3}-.+\.md$", f))
    entries = []
    for f in files:
        num = int(re.match(r"LJ(\d{3})", f).group(1))
        title = re.sub(r"^LJ\d{3}-", "", f)[:-3]
        raw = open(os.path.join(BOOK, f), encoding="utf-8").read()
        lines = raw.strip().split("\n")
        pian = ""
        l3 = lines[2] if len(lines) > 2 else ""
        if re.search(r"第\s*\d+\s*课", l3) and "·" in l3:
            pian = l3.strip().lstrip(">").split("·")[0].strip()
        key = "lj%03d" % num
        page = SHELL.format(
            title="%s · 道可道之礼记" % title,
            desc="《礼记》%s · 第 %d 课：解题、经文、字义、今译、章旨、礼义、分寸、存疑、跨典与图。" % (pian, num),
            canonical="%s/k/%s.html" % (SITE, key), css=CSS, body=conv(raw),
            foot_head="润泽说　道可道之礼记　·　%s　·　v%s" % (pian or "礼记", ver),
            foot_extra='<a href="../index.html">全书目录</a>')
        open(os.path.join(K, key + ".html"), "w", encoding="utf-8").write(page)
        entries.append({"no": num, "key": key, "title": title, "pian": pian})

    intro = os.path.join(BOOK, "前言.md")
    if os.path.exists(intro):
        page = SHELL.format(
            title="前言 · 道可道之礼记",
            desc="《礼记》总说：为何立此部、底本与注、读法四层、分篇与边界。",
            canonical="%s/intro.html" % SITE, css=CSS,
            body=conv(open(intro, encoding="utf-8").read()),
            foot_head="润泽说　道可道之礼记　·　前言　·　v%s" % ver,
            foot_extra='<a href="index.html">全书目录</a>')
        open(os.path.join(DOCS, "intro.html"), "w", encoding="utf-8").write(page)

    if entries:
        body = ('<h1>道可道之礼记</h1>'
                '<div style="text-align:center;color:#7C6D5C;font-size:13px;letter-spacing:1.5px">'
                '润泽说　·　四十九篇　·　v%s</div>'
                '<p style="text-align:center;font-size:14px"><a href="intro.html">前言</a>　·　'
                '已刊 <em>%d</em> 课　·　曲礼上起、曲礼下续</p><hr><div class="toc">' % (ver, len(entries)))
        for e in entries:
            body += '<p><a href="k/%s.html">第%03d课　%s</a></p>' % (e["key"], e["no"], e["title"])
        body += "</div>"
        open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8").write(
            SHELL.format(title="道可道之礼记", desc="《礼记》四十九篇逐节通释，曲礼上起。",
                         canonical=SITE + "/", css=CSS, body=body,
                         foot_head="润泽说　道可道之礼记　·　v%s" % ver, foot_extra=""))

    json.dump({"version": ver, "total_pian": TOTAL_PIAN, "count": len(entries),
               "chapters": entries},
              open(os.path.join(BOOK, "chapters.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("built", len(entries), "ke; version", ver)


if __name__ == "__main__":
    main()
