"""Sidebar TOC + page shell (GitBook-style SPA) — IntroProgBiomed."""

# Global table of contents. Each chapter → its topics (id, num, title).
CHAPTERS = [
    ("aula1.html", "1. Introdução ao Linux", [
        ("sistema",   "1.1", "Sistema de arquivos"),
        ("comandos",  "1.2", "Comandos essenciais"),
        ("especiais", "1.3", "Caracteres especiais"),
        ("editores",  "1.4", "Editores de texto"),
    ]),
    ("aula2.html", "2. Linha de Comando", [
        ("pipes",     "2.1", "Pipes e redirecionamento"),
        ("busca",     "2.2", "Busca e filtragem"),
        ("processos", "2.3", "Processos e acesso remoto"),
        ("pipeline",  "2.4", "Construindo pipelines"),
    ]),
    ("aula3.html", "3. Shell Scripting", [
        ("anatomia",  "3.1", "Anatomia de um script"),
        ("variaveis", "3.2", "Variáveis e argumentos"),
        ("controle",  "3.3", "Estruturas de controle"),
        ("funcoes",   "3.4", "Funções"),
    ]),
    ("aula4.html", "4. Python e R — Fundamentos", [
        ("ambiente",  "4.1", "Ambientes de trabalho"),
        ("tipos",     "4.2", "Tipos e estruturas"),
        ("controle",  "4.3", "Controle de fluxo"),
        ("funcoes",   "4.4", "Funções"),
    ]),
    ("aula5.html", "5. DataFrames", [
        ("leitura",     "5.1", "Leitura de dados"),
        ("selecao",     "5.2", "Seleção e filtragem"),
        ("agrupamento", "5.3", "Agrupamento"),
        ("join",        "5.4", "Junção de tabelas"),
        ("na",          "5.5", "Dados faltantes"),
    ]),
    ("aula6.html", "6. Visualização e Git", [
        ("scatter",  "6.1", "Dispersão"),
        ("histbox",  "6.2", "Histograma e boxplot"),
        ("heatmap",  "6.3", "Heatmap"),
        ("exportar", "6.4", "Exportando figuras"),
        ("git",      "6.5", "Git básico"),
    ]),
    ("exercicios.html", "7. Exercícios", [
        ("ex-linux",   "7.1", "Linux"),
        ("ex-cli",     "7.2", "Linha de Comando"),
        ("ex-shell",   "7.3", "Shell Scripting"),
        ("ex-pyr",     "7.4", "Python e R"),
        ("ex-df",      "7.5", "DataFrames"),
        ("ex-viz",     "7.6", "Visualização e Git"),
    ]),
]

COLAB_IMG = "https://colab.research.google.com/assets/colab-badge.svg"

PRISM_CSS  = "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css"
PRISM_JS   = "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"
PRISM_COMP = [
    "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-r.min.js",
]


def colab_link(lang, url):
    tag = {"py": "Python", "r": "R", "bash": "Bash"}[lang]
    return (f'<a class="colab-link" href="{url}" target="_blank" rel="noopener">'
            f'<img src="{COLAB_IMG}" alt="Abrir no Colab">'
            f'<span class="lang-tag {lang}">{tag}</span></a>')


def nb_row(badges):
    """badges: list of (lang, url)."""
    if not badges:
        return ""
    links = "".join(colab_link(l, u) for l, u in badges)
    return f'<div class="nb-row"><span class="nb-label">Notebook</span>{links}</div>'


def topic(tid, num, title, body, badges=None):
    nb = nb_row(badges or [])
    return (f'<article id="{tid}" class="topic">'
            f'<div class="topic-num">{num}</div>'
            f'<h1 class="topic-title">{title}</h1>'
            f'{nb}{body}</article>')


def build_sidebar(current_file):
    parts = ['<a class="sidebar-brand" href="index.html">Introdução à Programação'
             '<span>Pesquisa Biomédica · IBCCF · UFRJ</span></a>']
    for cfile, ctitle, topics in CHAPTERS:
        # collapse groups that aren't the current chapter
        collapsed = "" if cfile == current_file else " collapsed"
        parts.append(f'<div class="nav-group{collapsed}">')
        parts.append(f'<div class="nav-group-title">{ctitle}</div><ul>')
        for tid, num, title in topics:
            if cfile == current_file:
                a = (f'<a class="nav-link" data-target="{tid}" href="#{tid}">'
                     f'<span class="n">{num}</span>{title}</a>')
            else:
                a = (f'<a href="{cfile}#{tid}">'
                     f'<span class="n">{num}</span>{title}</a>')
            parts.append(f'<li>{a}</li>')
        parts.append('</ul></div>')
    return "\n".join(parts)


def page(title, current_file, body_html):
    sidebar = build_sidebar(current_file)
    comps = "\n".join(f'<script src="{c}"></script>' for c in PRISM_COMP)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — IntroProgBiomed</title>
<script>(function(){{try{{var t=localStorage.getItem('tema');if(!t){{t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}}if(t==='dark')document.documentElement.setAttribute('data-theme','dark');}}catch(e){{}}}})();</script>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="{PRISM_CSS}">
</head>
<body>
<button class="menu-toggle" id="menuToggle" aria-label="Menu">☰</button>
<button class="theme-toggle" id="themeToggle" aria-label="Alternar tema" title="Alternar tema claro/escuro"><span class="theme-icon"></span></button>

<nav class="sidebar" id="sidebar">
{sidebar}
</nav>
<main class="content"><div class="content-inner">
{body_html}
<div class="footer"><div class="footer-text">Instituto de Biofísica Carlos Chagas Filho — UFRJ<br>Introdução à Programação para Pesquisa Biomédica · Pedro Torres</div></div>
</div></main>

<script src="{PRISM_JS}"></script>
{comps}
<script src="assets/app.js"></script>
</body>
</html>"""
