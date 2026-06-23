import sys; sys.path.insert(0, '.')
from _nav import page, colab_py, colab_r

header = (
    '<div class="aula-num">Aula 6 &middot; Programação</div>'
    '<h1>Visualização: Matplotlib/Seaborn e ggplot2</h1>'
    '<p class="page-desc">Crie gráficos científicos de qualidade para publicação em Python e R.'
    ' Princípios de visualização, tipos de gráfico e exportação de figuras.</p>'
)

badges = (
    '<div class="colab-section">'
    '<span class="colab-section-label">Notebooks da aula</span>'
    + colab_py() + colab_r() +
    '</div>'
)

def pg(py_code, r_code):
    py_esc = py_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    r_esc  = r_code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return (
        '<div class="parallel-grid">'
        '<div><div class="lang-header py">&#x1F40D; Python &middot; Matplotlib/Seaborn</div>'
        f'<pre><code class="language-python">{py_esc}</code></pre></div>'
        '<div><div class="lang-header r">&#x1F4CA; R &middot; ggplot2</div>'
        f'<pre><code class="language-r">{r_esc}</code></pre></div>'
        '</div>'
    )

py_setup = """\
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Estilo global
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams.update({
    "figure.dpi": 150,
    "axes.titlesize": 13,
    "axes.labelsize": 12
})"""

r_setup = """\
library(ggplot2)
library(tidyverse)

# Tema global
theme_set(theme_classic(base_size=12))
# Paletas: scale_fill_brewer(), scale_fill_viridis_d()"""

py_scatter = """\
df = pd.read_csv("expressao.csv")
fig, ax = plt.subplots(figsize=(7, 5))
sns.scatterplot(
    data=df,
    x="expressao_tumoral",
    y="expressao_normal",
    hue="subtipo",
    alpha=0.7, s=60, ax=ax
)
ax.set_title("Expressão: Tumor vs. Normal")
ax.set_xlabel("Expressão tumoral (log2)")
ax.set_ylabel("Expressão normal (log2)")
# Linha de identidade
lim = df[["expressao_tumoral","expressao_normal"]].max().max()
ax.plot([0, lim], [0, lim], "k--", lw=1)
plt.tight_layout()
plt.show()"""

r_scatter = """\
df <- read_csv("expressao.csv")
ggplot(df, aes(x=expressao_tumoral,
               y=expressao_normal,
               color=subtipo)) +
  geom_point(alpha=0.7, size=2) +
  geom_abline(slope=1, intercept=0,
              linetype="dashed") +
  labs(
    title="Expressão: Tumor vs. Normal",
    x="Expressão tumoral (log2)",
    y="Expressão normal (log2)",
    color="Subtipo"
  ) + theme_classic()"""

py_hist = """\
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# Histograma com KDE
sns.histplot(data=df, x="expressao",
             hue="condicao", bins=30,
             kde=True, ax=axes[0])
axes[0].set_title("Distribuição")
# Boxplot + pontos individuais
sns.boxplot(data=df, x="condicao",
            y="expressao", palette="Set2",
            ax=axes[1])
sns.stripplot(data=df, x="condicao",
              y="expressao", color="black",
              alpha=0.3, size=3, ax=axes[1])
axes[1].set_title("Expressão por Condição")
plt.tight_layout()"""

r_hist = """\
# Histograma
p1 <- ggplot(df, aes(x=expressao, fill=condicao)) +
  geom_histogram(bins=30, alpha=0.7,
                 position="identity") +
  labs(title="Distribuição")

# Boxplot + pontos
p2 <- ggplot(df, aes(x=condicao, y=expressao,
                     fill=condicao)) +
  geom_boxplot(outlier.shape=NA, alpha=0.7) +
  geom_jitter(width=0.2, alpha=0.3, size=1) +
  labs(title="Expressão por Condição") +
  theme(legend.position="none")

library(patchwork)
p1 + p2    # combina figuras lado a lado"""

py_heat = """\
corr = df[gene_cols].corr()
fig, ax = plt.subplots(figsize=(8, 7))
sns.heatmap(corr, annot=True, fmt=".2f",
            cmap="RdBu_r", center=0,
            vmin=-1, vmax=1,
            square=True, linewidths=0.5,
            ax=ax)
ax.set_title("Correlação entre genes")
plt.tight_layout()"""

r_heat = """\
library(pheatmap)

# Alternativa com ggplot2 + geom_tile
df_long <- df |>
  select(all_of(gene_cols)) |>
  cor() |>
  as.data.frame() |>
  rownames_to_column("g1") |>
  pivot_longer(-g1, names_to="g2",
               values_to="cor")

ggplot(df_long, aes(x=g1, y=g2, fill=cor)) +
  geom_tile() +
  geom_text(aes(label=round(cor,2)), size=3) +
  scale_fill_gradient2(low="blue", mid="white",
    high="red", midpoint=0) +
  theme(axis.text.x=element_text(
    angle=45, hjust=1))"""

py_save = """\
fig, ax = plt.subplots(figsize=(7, 5))
# ... código do gráfico ...

fig.savefig("figura1.png",
            dpi=300, bbox_inches="tight",
            facecolor="white")
fig.savefig("figura1.pdf",   # vetorial
            bbox_inches="tight")
fig.savefig("figura1.svg")
plt.close()  # libera memória"""

r_save = """\
p <- ggplot(df, aes(x=condicao, y=expressao,
                    fill=condicao)) +
  geom_boxplot() +
  labs(title="Minha figura")

ggsave("figura1.png", plot=p,
       width=7, height=5,
       dpi=300, units="in")
ggsave("figura1.pdf", plot=p,
       width=7, height=5)
ggsave("figura1.svg", plot=p,
       width=7, height=5)"""

git_code = """\
# No terminal, dentro do projeto:
git init
git status                            # arquivos modificados
git add analise.py
git add *.R *.ipynb
git commit -m "análise de expressão diferencial"

# Conectar e enviar ao GitHub
git remote add origin https://github.com/usuario/projeto.git
git push -u origin main

# Outros comandos úteis
git log --oneline                     # histórico compacto
git diff                              # mudanças não commitadas
git checkout -- arquivo.py            # descarta mudanças locais"""

body = badges + f"""
<div class="section" id="scatter">
  <h2>6.1 Configuração e gráfico de dispersão</h2>
  {pg(py_setup, r_setup)}
  <h3>Scatter plot</h3>
  {pg(py_scatter, r_scatter)}
  <div class="callout info">
    <strong>Gramática dos gráficos (ggplot2):</strong> todo gráfico em ggplot2
    é construído por camadas — dados (<code>ggplot()</code>), geometria (<code>geom_*</code>),
    escala, tema e rótulos. Isso torna o código declarativo e fácil de modificar.
  </div>
</div>

<div class="section" id="histbox">
  <h2>6.2 Histograma e boxplot</h2>
  {pg(py_hist, r_hist)}
</div>

<div class="section" id="heatmap">
  <h2>6.3 Heatmap de correlação</h2>
  {pg(py_heat, r_heat)}
</div>

<div class="section" id="exportar">
  <h2>6.4 Exportando figuras para publicação</h2>
  {pg(py_save, r_save)}
  <div class="callout tip">
    <strong>Padrão para revistas:</strong> use <code>dpi=300</code> para PNG,
    ou formatos vetoriais (PDF, SVG) para qualidade em qualquer escala.
    Sempre consulte as instruções da revista-alvo.
  </div>
</div>

<div class="section" id="git">
  <h2>6.5 Versionamento básico com Git</h2>
  <p>Git registra o histórico de mudanças, permite reverter erros e facilita a colaboração.</p>
  <div class="code-label bash">bash</div>
  <pre><code class="language-bash">{git_code}</code></pre>
  <div class="callout tip">
    <strong>Regra de ouro:</strong> faça um commit sempre que o código estiver em
    um estado funcional. Mensagens descritivas valem ouro no futuro.
  </div>
</div>
"""

with open("aula6.html", "w") as f:
    f.write(page("Aula 6 — Visualização", "aula6.html", header, body))
print("aula6.html ok")
