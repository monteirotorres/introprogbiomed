"""Shared nav and page shell for site generator."""

NAV = [
    ("index.html",   "🏠 Início",                  []),
    ("aula1.html",   "1. Introdução ao Linux",      [
        ("#sistema",   "Sistema de arquivos"),
        ("#comandos",  "Comandos essenciais"),
        ("#especiais", "Caracteres especiais"),
        ("#editores",  "Editores de texto"),
    ]),
    ("aula2.html",   "2. Linha de Comando",         [
        ("#pipes",     "Pipes e redirecionamento"),
        ("#busca",     "Busca e filtragem"),
        ("#processos", "Processos e acesso remoto"),
        ("#pipeline",  "Construindo pipelines"),
    ]),
    ("aula3.html",   "3. Shell Scripting",          [
        ("#anatomia",  "Anatomia de um script"),
        ("#variaveis", "Variáveis e argumentos"),
        ("#controle",  "Estruturas de controle"),
        ("#funcoes",   "Funções"),
    ]),
    ("aula4.html",   "4. Python e R — Fundamentos", [
        ("#ambiente",  "Ambientes de trabalho"),
        ("#tipos",     "Tipos e estruturas"),
        ("#controle",  "Controle de fluxo"),
        ("#funcoes",   "Funções"),
    ]),
    ("aula5.html",   "5. DataFrames",               [
        ("#leitura",      "Leitura de dados"),
        ("#selecao",      "Seleção e filtragem"),
        ("#agrupamento",  "Agrupamento"),
        ("#join",         "Junção de tabelas"),
        ("#na",           "Dados faltantes"),
    ]),
    ("aula6.html",   "6. Visualização",             [
        ("#scatter",   "Dispersão"),
        ("#histbox",   "Histograma e Boxplot"),
        ("#heatmap",   "Heatmap"),
        ("#exportar",  "Exportando figuras"),
        ("#git",       "Git básico"),
    ]),
    (None, None, None),   # divider
    ("exercicios.html", "📝 Exercícios",            [
        ("#ex-aula1", "Linux"),
        ("#ex-aula2", "Linha de Comando"),
        ("#ex-aula3", "Shell Scripting"),
        ("#ex-aula4", "Python e R"),
        ("#ex-aula5", "DataFrames"),
        ("#ex-aula6", "Visualização"),
    ]),
]

PRISM_CSS = "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css"
PRISM_JS  = "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"
PRISM_BASH   = "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js"
PRISM_PY     = "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"
PRISM_R      = "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-r.min.js"

COLAB_IMG = "https://colab.research.google.com/assets/colab-badge.svg"

def colab_py(url="#"):
    return f'''<a href="{url}" target="_blank" class="colab-badge py-badge">
      <img src="{COLAB_IMG}" alt="Abrir no Colab"> Python
    </a>'''

def colab_r(url="#"):
    return f'''<a href="{url}" target="_blank" class="colab-badge r-badge">
      <img src="{COLAB_IMG}" alt="Abrir no Colab"> R
    </a>'''

def colab_bash(url="#"):
    return f'''<a href="{url}" target="_blank" class="colab-badge bash-badge">
      <img src="{COLAB_IMG}" alt="Abrir no Colab"> Bash
    </a>'''

def build_nav(current):
    out = []
    for item in NAV:
        if item[0] is None:
            out.append('<li><div class="nav-divider"></div></li>')
            continue
        page, label, subs = item
        active = " active" if page == current else ""
        out.append(f'<li><a href="{page}" class="nav-link{active}">{label}</a>')
        if subs and page == current:
            sub_html = "".join(
                f'<li><a href="{a}">{t}</a></li>' for a, t in subs
            )
            out.append(f'<ul class="nav-sub">{sub_html}</ul>')
        out.append("</li>")
    return "\n".join(out)

def page(title, current, header_html, body_html):
    nav = build_nav(current)
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — IntroProgBiomed</title>
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="{PRISM_CSS}">
</head>
<body>
<button class="sidebar-toggle" onclick="document.querySelector('.sidebar').classList.toggle('open')">☰</button>
<div class="layout">
  <nav class="sidebar">
    <div class="sidebar-header">
      <div class="course-title">IntroProgBiomed</div>
      <div class="course-sub">IBCCF · UFRJ</div>
    </div>
    <ul class="nav-list">
{nav}
    </ul>
    <div class="theme-toggle">
      <button class="theme-toggle-btn" onclick="toggleTheme()" id="theme-btn">
        <span class="theme-icon">☀️</span> <span id="theme-label">Claro</span>
      </button>
    </div>
    <div class="sidebar-footer">Pedro Torres<br>Biofísica · UFRJ</div>
  </nav>
  <main class="content">
    <div class="page-header">{header_html}</div>
    <div class="page-body">{body_html}</div>
    <footer class="page-footer">
      Instituto de Biofísica Carlos Chagas Filho — UFRJ<br>
      Introdução à Programação para Pesquisa Biomédica · Pedro Torres
    </footer>
  </main>
</div>
<script src="{PRISM_JS}"></script>
<script src="{PRISM_BASH}"></script>
<script src="{PRISM_PY}"></script>
<script src="{PRISM_R}"></script>
<script>
(function() {{
  var saved = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  updateToggle(saved);
  function updateToggle(t) {{
    var btn = document.getElementById('theme-btn');
    var lbl = document.getElementById('theme-label');
    if (!btn) return;
    if (t === 'dark') {{ btn.querySelector('.theme-icon').textContent = '🌙'; lbl.textContent = 'Escuro'; }}
    else {{ btn.querySelector('.theme-icon').textContent = '☀️'; lbl.textContent = 'Claro'; }}
  }}
  window.toggleTheme = function() {{
    var cur = document.documentElement.getAttribute('data-theme');
    var next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateToggle(next);
  }};
}})();
document.addEventListener('click', function(e) {{
  var s = document.querySelector('.sidebar');
  var t = document.querySelector('.sidebar-toggle');
  if (s && t && !s.contains(e.target) && !t.contains(e.target))
    s.classList.remove('open');
}});
</script>
</body>
</html>"""
