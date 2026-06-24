"""Build all site pages from extracted content (biostat-style SPA)."""
import sys, json
sys.path.insert(0, '.')
from _nav import page, topic, CHAPTERS

content = json.load(open("_content.json"))["data"]
exercises = json.load(open("_exercises.json"))

# Colab notebooks per aula (lang, url), attached to the first topic.
NB = "https://colab.research.google.com/github/monteirotorres/introprogbiomed/blob/main/notebooks"
COLAB = {
    "aula3": [("bash", f"{NB}/aula3_shell_scripting.ipynb")],
    "aula4": [("py", f"{NB}/aula4_python_fundamentos.ipynb"),
              ("r",  f"{NB}/aula4_r_fundamentos.ipynb")],
    "aula5": [("py", f"{NB}/aula5_pandas.ipynb"),
              ("r",  f"{NB}/aula5_tidyverse.ipynb")],
    "aula6": [("py", f"{NB}/aula6_matplotlib_seaborn.ipynb"),
              ("r",  f"{NB}/aula6_ggplot2.ipynb")],
}

# ── Aula pages ───────────────────────────────────────────────────────────
for stem in ["aula1", "aula2", "aula3", "aula4", "aula5", "aula6"]:
    topics = content[stem]
    badges = COLAB.get(stem, [])
    arts = []
    for i, t in enumerate(topics):
        b = badges if i == 0 else []
        arts.append(topic(t["id"], t["num"], t["title"], t["body"], badges=b))
    title = next(ct for cf, ct, _ in CHAPTERS if cf == stem + ".html")
    html = page(title.split(". ", 1)[-1], stem + ".html", "\n".join(arts))
    open(stem + ".html", "w").write(html)
    print(f"{stem}.html — {len(topics)} tópicos" + (f" + {len(badges)} colab" if badges else ""))

# ── Exercícios ───────────────────────────────────────────────────────────
ex_ids = [t[0] for cf, _, ts in CHAPTERS if cf == "exercicios.html" for t in ts]
ex_nums = [t[1] for cf, _, ts in CHAPTERS if cf == "exercicios.html" for t in ts]
intro = ('<p>Tente resolver cada exercício antes de revelar a solução. '
         'Clique em <em>Mostrar resposta</em> para ver a resolução comentada. '
         'Use o menu à esquerda para navegar entre os temas.</p>')
arts = []
for i, p in enumerate(exercises):
    title = p["title"].split(". ", 1)[-1]
    body = (intro if i == 0 else "") + p["body"]
    arts.append(topic(ex_ids[i], ex_nums[i], title, body))
html = page("Exercícios", "exercicios.html", "\n".join(arts))
open("exercicios.html", "w").write(html)
print(f"exercicios.html — {len(exercises)} temas")

# ── Index (hero + cards + cronograma) ────────────────────────────────────
CARDS = [
    ("1", "aula1.html#sistema", "Introdução ao Linux",
     "Sistema de arquivos, comandos essenciais, caracteres especiais e editores de texto.",
     "4 tópicos", [("bash", "Bash")]),
    ("2", "aula2.html#pipes", "Linha de Comando",
     "Pipes, redirecionamento, busca com grep/find, processos e pipelines biomédicos.",
     "4 tópicos", [("bash", "Bash")]),
    ("3", "aula3.html#anatomia", "Shell Scripting",
     "Anatomia de scripts, variáveis, estruturas de controle e funções em Bash.",
     "4 tópicos", [("bash", "Bash")]),
    ("4", "aula4.html#ambiente", "Python e R — Fundamentos",
     "Tipos, estruturas de dados, controle de fluxo e funções, em paralelo nas duas linguagens.",
     "4 tópicos", [("py", "Python"), ("r", "R")]),
    ("5", "aula5.html#leitura", "DataFrames",
     "Leitura, seleção, agrupamento, junção e dados faltantes com pandas e tidyverse.",
     "5 tópicos", [("py", "Python"), ("r", "R")]),
    ("6", "aula6.html#scatter", "Visualização e Git",
     "Gráficos científicos com Matplotlib/Seaborn e ggplot2; versionamento com Git.",
     "5 tópicos", [("py", "Python"), ("r", "R")]),
    ("7", "exercicios.html#ex-linux", "Exercícios",
     "30 exercícios resolvidos por tema, com soluções em Bash, Python e R.",
     "6 temas", []),
]

cards_html = []
for num, href, title, desc, count, tags in CARDS:
    tag_html = "".join(f'<span class="ctag {l}">{n}</span>' for l, n in tags)
    cards_html.append(
        f'<a class="card" href="{href}"><div class="cnum">{num}</div>'
        f'<div class="ctitle">{title}</div><div class="cdesc">{desc}</div>'
        f'<div class="ctags">{tag_html}</div>'
        f'<div class="ccount">{count}</div></a>')

sched_rows = "".join(
    f"<tr><td>{a}</td><td>{t}</td><td>{m}</td></tr>" for a, t, m in [
        ("1", "Introdução ao Linux", "Teoria + prática"),
        ("2", "Linha de Comando", "Teoria + prática"),
        ("3", "Shell Scripting", "Teoria + prática + Colab"),
        ("4", "Python e R — Fundamentos", "Teoria + prática + 2 Colabs"),
        ("5", "DataFrames", "Teoria + prática + 2 Colabs"),
        ("6", "Visualização e Git", "Teoria + prática + 2 Colabs"),
        ("7–10", "Hackathon", "Projeto aplicado em grupo"),
    ])

index_body = f"""<div class="hero">
<h1 class="hero-title">Introdução à Programação<br>para Pesquisa Biomédica</h1>
<p class="hero-sub">Instituto de Biofísica Carlos Chagas Filho · UFRJ</p>
<p class="hero-desc">Disciplina de 30h com abordagem prática: do terminal Linux ao
processamento e visualização de dados em Python e R, com notebooks no Google Colab
e um hackathon final. Navegue pelo menu à esquerda.</p>
<p class="hero-authors">Pedro Torres</p>
</div>
<div class="cards">{''.join(cards_html)}</div>
<div class="sched"><h2>Cronograma — 10 aulas de 3h</h2>
<table class="data-table"><thead><tr><th>Aula</th><th>Tema</th><th>Formato</th></tr></thead>
<tbody>{sched_rows}</tbody></table></div>"""

# index has no SPA topics; build a bespoke shell via page() with the hero as body.
html = page("Início", "index.html", index_body)
open("index.html", "w").write(html)
print("index.html — hero + cards + cronograma")
