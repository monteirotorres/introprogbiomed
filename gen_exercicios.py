import sys; sys.path.insert(0, '.')
from _nav import page

def ex(num, title, body):
    return f'<div class="exercise"><h4>Exercício {num} — {title}</h4>{body}</div>'

def ans(*paras):
    inner = "".join(f"<p>{p}</p>" for p in paras)
    return (f'<details class="resposta"><summary>Mostrar resposta</summary>'
            f'<div class="resposta-content">{inner}</div></details>')

def code(lang, src):
    esc = src.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    return f'<pre><code class="language-{lang}">{esc}</code></pre>'

def pg(py_src, r_src):
    pe = py_src.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    re_ = r_src.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    return (
        '<div class="parallel-grid">'
        f'<div><div class="lang-header py">Python</div>'
        f'<pre><code class="language-python">{pe}</code></pre></div>'
        f'<div><div class="lang-header r">R</div>'
        f'<pre><code class="language-r">{re_}</code></pre></div>'
        '</div>'
    )

