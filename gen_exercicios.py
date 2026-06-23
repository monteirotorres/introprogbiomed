import sys; sys.path.insert(0, '.')
from _nav import page

header = (
    '<div class="aula-num">Exercícios</div>'
    '<h1>Exercícios — Seções 1 a 6</h1>'
    '<p class="page-desc">Tente resolver cada exercício antes de expandir a resposta.'
    ' Clique em <em>Mostrar resposta</em> para ver a solução comentada.</p>'
)

def ex(num, titulo, enunciado, resposta_html):
    return f"""
<div class="exercise">
  <h4>Exercício {num} — {titulo}</h4>
  {enunciado}
  <details class="resposta">
    <summary>Mostrar resposta</summary>
    <div class="resposta-content">{resposta_html}</div>
  </details>
</div>"""

# ─── SEÇÃO 1 — Linux ─────────────────────────────────────────────────────────
s1 = '<div class="ex-section" id="ex-aula1"><h2>1. Introdução ao Linux</h2>'

s1 += ex(
    "1.1", "Estrutura de diretórios",
    "<p>Qual diretório você usaria para armazenar os dados brutos de um projeto de pesquisa? "
    "E os scripts de análise? Justifique.</p>",
    "<p><strong>Dados brutos:</strong> geralmente em <code>~/projeto/data/raw/</code> — "
    "dentro do <code>/home</code> do usuário, organizado por projeto. "
    "Nunca em <code>/tmp</code> (apagado ao reiniciar).</p>"
    "<p><strong>Scripts:</strong> em <code>~/projeto/scripts/</code> ou <code>~/projeto/src/</code>. "
    "Separar dados de código facilita versionamento e reprodutibilidade.</p>"
)

s1 += ex(
    "1.2", "Navegação e criação",
    "<p>Crie a seguinte estrutura de diretórios com um único comando, depois entre em <code>data/raw</code>:</p>"
    "<pre><code>projeto/\n  data/\n    raw/\n    processed/\n  scripts/\n  results/</code></pre>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'>mkdir -p projeto/data/raw projeto/data/processed projeto/scripts projeto/results\ncd projeto/data/raw\npwd   # /home/usuario/projeto/data/raw</code></pre>"
    "<p>A flag <code>-p</code> cria toda a hierarquia de uma vez e não dá erro se o diretório já existir.</p>"
)

s1 += ex(
    "1.3", "Inspecionando arquivos",
    "<p>Dado um arquivo <code>sequencias.fasta</code> com 10.000 sequências, responda sem abrir o arquivo inteiro:</p>"
    "<ol><li>Como você veria as 3 primeiras sequências (cabeçalho + sequência)?</li>"
    "<li>Como você contaria o número total de sequências?</li>"
    "<li>Como você verificaria se o arquivo contém a sequência <code>NM_007294</code>?</li></ol>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'># 1. Primeiras linhas (cada seq FASTA = 2 linhas: > + sequência)\nhead -6 sequencias.fasta\n\n# 2. Contar cabeçalhos (linhas com >)\ngrep -c '>' sequencias.fasta\n\n# 3. Verificar presença do ID\ngrep 'NM_007294' sequencias.fasta</code></pre>"
)

s1 += ex(
    "1.4", "Redirecionamento",
    "<p>Você quer criar um inventário com a listagem detalhada de todos os arquivos <code>.csv</code> "
    "no diretório atual, e depois acrescentar a data de criação ao final do arquivo. "
    "Como fazer isso em dois comandos?</p>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'>ls -lh *.csv > inventario.txt      # cria (ou sobrescreve)\ndate >> inventario.txt              # acrescenta ao final\ncat inventario.txt                  # confere o resultado</code></pre>"
    "<p>Note: <code>&gt;</code> sobrescreve; <code>&gt;&gt;</code> acrescenta.</p>"
)

s1 += ex(
    "1.5", "Vim — sobrevivência",
    "<p>Você está conectado via SSH em um servidor sem interface gráfica. "
    "Precisa editar a linha 42 de <code>config.sh</code>. "
    "Descreva a sequência de teclas para: abrir o arquivo, ir à linha 42, editar, salvar e sair.</p>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'>vim config.sh</code></pre>"
    "<p>Dentro do vim:</p>"
    "<pre><code>42G        → vai para a linha 42 (no modo NORMAL)\ni          → entra no modo INSERT\n           → edite o que for necessário\nEsc        → volta ao modo NORMAL\n:wq        → salva e sai</code></pre>"
)

s1 += '</div>'

# ─── SEÇÃO 2 — CLI ────────────────────────────────────────────────────────────
s2 = '<div class="ex-section" id="ex-aula2"><h2>2. Linha de Comando</h2>'

s2 += ex(
    "2.1", "Pipeline com grep e wc",
    "<p>Dado o arquivo <code>genes.csv</code> com colunas <code>id,gene,organismo,expressao</code>:</p>"
    "<ol><li>Quantas linhas correspondem a <em>Homo sapiens</em>?</li>"
    "<li>Salve essas linhas (sem o cabeçalho) em <code>humanos.csv</code>.</li></ol>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'># 1. Contar linhas de Homo sapiens\ngrep -c 'Homo sapiens' genes.csv\n\n# 2. Salvar (com cabeçalho)\nhead -1 genes.csv > humanos.csv\ngrep 'Homo sapiens' genes.csv >> humanos.csv</code></pre>"
)

s2 += ex(
    "2.2", "Top genes por frequência",
    "<p>No arquivo <code>anotacao.tsv</code> (TSV), a coluna 3 contém o nome do gene. "
    "Liste os 5 genes mais frequentes com suas contagens.</p>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'>cut -f3 anotacao.tsv | sort | uniq -c | sort -rn | head -5</code></pre>"
    "<p><code>cut -f3</code> extrai a coluna 3; <code>uniq -c</code> conta ocorrências (requer entrada ordenada); "
    "<code>sort -rn</code> ordena numericamente em ordem decrescente.</p>"
)

s2 += ex(
    "2.3", "Lote de arquivos",
    "<p>Você tem 20 arquivos <code>amostra_01.fasta</code> ... <code>amostra_20.fasta</code>. "
    "Escreva um comando (ou mini pipeline) que imprima para cada arquivo: "
    "<code>nome_do_arquivo: N sequências</code>.</p>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'>for f in amostra_*.fasta; do\n    echo \"$f: $(grep -c '>' $f) sequências\"\ndone</code></pre>"
)

s2 += ex(
    "2.4", "find + ação",
    "<p>Encontre todos os arquivos <code>.tmp</code> criados há mais de 7 dias e os remova.</p>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'># Listar primeiro para conferir\nfind . -name '*.tmp' -mtime +7\n\n# Remover\nfind . -name '*.tmp' -mtime +7 -delete</code></pre>"
    "<p>Sempre liste antes de deletar!</p>"
)

s2 += '</div>'

# ─── SEÇÃO 3 — Shell Scripting ───────────────────────────────────────────────
s3 = '<div class="ex-section" id="ex-aula3"><h2>3. Shell Scripting</h2>'

s3 += ex(
    "3.1", "Script com argumento e verificação",
    "<p>Escreva um script <code>contar_seq.sh</code> que:</p>"
    "<ol><li>Recebe um arquivo FASTA como argumento.</li>"
    "<li>Verifica se o arquivo existe; caso contrário, imprime mensagem de erro e sai.</li>"
    "<li>Imprime o número de sequências.</li></ol>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'>#!/bin/bash\n# Uso: ./contar_seq.sh arquivo.fasta\n\nif [ -z \"$1\" ]; then\n    echo \"Uso: $0 <arquivo.fasta>\"\n    exit 1\nfi\n\nif [ ! -f \"$1\" ]; then\n    echo \"Erro: arquivo '$1' não encontrado.\"\n    exit 1\nfi\n\nN=$(grep -c '>' \"$1\")\necho \"$(basename $1): $N sequências\"</code></pre>"
)

s3 += ex(
    "3.2", "Relatório em lote",
    "<p>Adapte o script anterior para processar <em>todos</em> os arquivos <code>.fasta</code> "
    "de um diretório (passado como argumento) e salvar o relatório em <code>relatorio.txt</code>.</p>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'>#!/bin/bash\nDIR=${1:-.}\nSAIDA='relatorio.txt'\n\necho '=== Relatório FASTA ===' > \"$SAIDA\"\necho \"Data: $(date)\" >> \"$SAIDA\"\necho '---' >> \"$SAIDA\"\n\nTOTAL=0\nfor f in \"$DIR\"/*.fasta; do\n    [ -f \"$f\" ] || continue\n    N=$(grep -c '>' \"$f\")\n    TOTAL=$((TOTAL + N))\n    printf '%-40s %6d seqs\\n' \"$(basename $f)\" \"$N\" >> \"$SAIDA\"\ndone\n\necho '---' >> \"$SAIDA\"\necho \"TOTAL: $TOTAL sequências\" >> \"$SAIDA\"\ncat \"$SAIDA\"</code></pre>"
)

s3 += ex(
    "3.3", "Função de validação",
    "<p>Escreva uma função Bash <code>e_fasta()</code> que recebe um arquivo e retorna 0 "
    "(sucesso) se a primeira linha começar com <code>&gt;</code>, e 1 caso contrário.</p>",
    "<div class='code-label bash'>bash</div>"
    "<pre><code class='language-bash'>e_fasta() {\n    local arquivo=$1\n    local primeira=$(head -1 \"$arquivo\")\n    if [[ \"$primeira\" == \\>* ]]; then\n        return 0\n    else\n        return 1\n    fi\n}\n\n# Uso\nif e_fasta 'meu_arquivo.fasta'; then\n    echo 'É um arquivo FASTA válido'\nelse\n    echo 'Não parece um FASTA'\nfi</code></pre>"
)

s3 += '</div>'

# ─── SEÇÃO 4 — Python e R ────────────────────────────────────────────────────
s4 = '<div class="ex-section" id="ex-aula4"><h2>4. Python e R — Fundamentos</h2>'

def ex_bilingual(num, titulo, enunciado, py_resp, r_resp):
    py_esc = py_resp.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    r_esc  = r_resp.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    resp = (
        '<div class="parallel-grid">'
        '<div><div class="lang-header py">&#x1F40D; Python</div>'
        f'<pre><code class="language-python">{py_esc}</code></pre></div>'
        '<div><div class="lang-header r">&#x1F4CA; R</div>'
        f'<pre><code class="language-r">{r_esc}</code></pre></div>'
        '</div>'
    )
    return ex(num, titulo, enunciado, resp)

py41 = """\
def conteudo_gc(seq):
    seq = seq.upper()
    gc = seq.count('G') + seq.count('C')
    return round(gc / len(seq) * 100, 2)

dna = "ATGCGGCATTTACGCAATG"
print(f"GC: {conteudo_gc(dna)}%")  # GC: 47.37%"""

r41 = """\
conteudo_gc <- function(seq) {
  bases <- strsplit(toupper(seq), "")[[1]]
  gc    <- sum(bases %in% c("G","C"))
  round(gc / length(bases) * 100, 2)
}

dna <- "ATGCGGCATTTACGCAATG"
cat("GC:", conteudo_gc(dna), "%\n")  # GC: 47.37 %"""

s4 += ex_bilingual(
    "4.1", "Conteúdo GC",
    "<p>Implemente uma função <code>conteudo_gc(seq)</code> que recebe uma string de DNA "
    "e retorna o percentual de bases G+C arredondado para 2 casas decimais.</p>",
    py41, r41
)

py42 = """\
def traducao(seq):
    cod = {
        'ATG':'M','TAA':'*','TAG':'*','TGA':'*',
        'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
        'TGT':'C','TGC':'C',
        'GAT':'D','GAC':'D',
        'GAA':'E','GAG':'E',
        'TTT':'F','TTC':'F',
        'GGT':'G','GGC':'G','GGA':'G','GGG':'G',
        'CAT':'H','CAC':'H',
        'ATT':'I','ATC':'I','ATA':'I',
        'AAA':'K','AAG':'K',
        'TTA':'L','TTG':'L','CTT':'L',
        'CTC':'L','CTA':'L','CTG':'L',
        'AAT':'N','AAC':'N',
        'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
        'CAA':'Q','CAG':'Q',
        'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
        'AGG':'R','AGA':'R',
        'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
        'AGT':'S','AGC':'S',
        'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
        'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
        'TGG':'W','TAT':'Y','TAC':'Y',
    }
    seq = seq.upper()
    prot = ''
    for i in range(0, len(seq)-2, 3):
        aa = cod.get(seq[i:i+3], '?')
        if aa == '*': break
        prot += aa
    return prot

print(traducao("ATGGCATGGTAA"))  # MA"""

r42 = """\
# R com Biostrings (tidier)
# install.packages("BiocManager")
# BiocManager::install("Biostrings")
library(Biostrings)

dna <- DNAString("ATGGCATGGTAA")
rna <- RNAString(dna)
prot <- translate(rna)
as.character(prot)  # "MA*" (inclui stop codon)

# Alternativa sem Biostrings (manual simplificado)
traducao <- function(seq) {
  cod <- c(ATG="M", TAA="*", TAG="*", TGA="*",
           GCT="A", GCC="A", GCA="A", GCG="A",
           TGT="C", TGC="C", GAT="D", GAC="D",
           TTT="F", TTC="F",
           GGT="G", GGC="G", GGA="G", GGG="G")
  seq   <- toupper(seq)
  n     <- nchar(seq)
  codons <- substring(seq, seq(1,n-2,3), seq(3,n,3))
  aa <- cod[codons]
  stop_pos <- which(aa == "*")
  if (length(stop_pos)) aa <- aa[seq_len(stop_pos[1]-1)]
  paste(aa, collapse="")
}
traducao("ATGGCATGGTAA")  # "MA" """

s4 += ex_bilingual(
    "4.2", "Tradução simples",
    "<p>Escreva uma função <code>traducao(seq)</code> que traduz uma sequência de DNA "
    "para proteína (use o código genético padrão, pare no primeiro códon de parada).</p>",
    py42, r42
)

py43 = """\
def estatisticas_seq(seqs):
    tamanhos = [len(s) for s in seqs]
    return {
        "n":      len(seqs),
        "min":    min(tamanhos),
        "max":    max(tamanhos),
        "media":  round(sum(tamanhos)/len(tamanhos), 1),
    }

seqs = ["ATGCGC", "TTACG", "GGCATTTACGCAATG", "ATGC"]
print(estatisticas_seq(seqs))
# {'n': 4, 'min': 4, 'max': 15, 'media': 9.0}"""

r43 = """\
estatisticas_seq <- function(seqs) {
  tam <- nchar(seqs)
  list(
    n     = length(seqs),
    min   = min(tam),
    max   = max(tam),
    media = round(mean(tam), 1)
  )
}

seqs <- c("ATGCGC","TTACG","GGCATTTACGCAATG","ATGC")
print(estatisticas_seq(seqs))
# $n [1] 4  $min [1] 4  $max [1] 15  $media [1] 9"""

s4 += ex_bilingual(
    "4.3", "Estatísticas de um conjunto de sequências",
    "<p>Dada uma lista/vetor de sequências de DNA, escreva uma função que retorne "
    "um dicionário/lista com: número de sequências, tamanho mínimo, máximo e médio.</p>",
    py43, r43
)

s4 += '</div>'

# ─── SEÇÃO 5 — DataFrames ────────────────────────────────────────────────────
s5 = '<div class="ex-section" id="ex-aula5"><h2>5. DataFrames</h2>'

py51 = """\
import pandas as pd

df = pd.read_csv("expressao.csv")

# a) Top 10 mais expressos
top10 = (df.sort_values("expressao", ascending=False)
           .head(10)[["gene", "expressao"]])

# b) Média por organismo
media_org = df.groupby("organismo")["expressao"].mean()

# c) Genes com expressao > 5 em humanos
humanos_altos = df[
    (df["organismo"] == "Homo sapiens") &
    (df["expressao"] > 5)
]["gene"].tolist()

print(top10)
print(media_org)
print(humanos_altos)"""

r51 = """\
library(tidyverse)

df <- read_csv("expressao.csv")

# a) Top 10 mais expressos
top10 <- df |>
  arrange(desc(expressao)) |>
  slice_head(n=10) |>
  select(gene, expressao)

# b) Média por organismo
media_org <- df |>
  group_by(organismo) |>
  summarise(media=mean(expressao))

# c) Genes humanos com alta expressão
humanos_altos <- df |>
  filter(organismo=="Homo sapiens",
         expressao > 5) |>
  pull(gene)

print(top10)
print(media_org)
print(humanos_altos)"""

s5 += ex_bilingual(
    "5.1", "Filtragem e sumarização",
    "<p>Com o DataFrame <code>expressao.csv</code> (colunas: <code>gene, organismo, expressao</code>):</p>"
    "<ol><li>Liste os 10 genes mais expressos.</li>"
    "<li>Calcule a média de expressão por organismo.</li>"
    "<li>Filtre genes de <em>Homo sapiens</em> com expressão &gt; 5.</li></ol>",
    py51, r51
)

py52 = """\
import pandas as pd

clinico  = pd.read_csv("clinico.csv")    # id, paciente, diagnostico
molecular = pd.read_csv("molecular.csv") # id, gene, expressao

# Merge e análise
merged = pd.merge(clinico, molecular, on="id")

# Expressão média por diagnóstico
resultado = (merged.groupby("diagnostico")
                   .agg(media_expr=("expressao","mean"),
                        n_amostras=("id","count"))
                   .sort_values("media_expr", ascending=False))
print(resultado)"""

r52 = """\
library(tidyverse)

clinico  <- read_csv("clinico.csv")
molecular <- read_csv("molecular.csv")

# Join e análise
resultado <- inner_join(clinico, molecular, by="id") |>
  group_by(diagnostico) |>
  summarise(
    media_expr = mean(expressao),
    n_amostras = n(),
    .groups="drop"
  ) |>
  arrange(desc(media_expr))

print(resultado)"""

s5 += ex_bilingual(
    "5.2", "Junção de tabelas",
    "<p>Dados dois arquivos: <code>clinico.csv</code> (<code>id, paciente, diagnostico</code>) e "
    "<code>molecular.csv</code> (<code>id, gene, expressao</code>), faça um inner join e calcule "
    "a expressão média por diagnóstico.</p>",
    py52, r52
)

s5 += '</div>'

# ─── SEÇÃO 6 — Visualização ──────────────────────────────────────────────────
s6 = '<div class="ex-section" id="ex-aula6"><h2>6. Visualização</h2>'

py61 = """\
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv("expressao.csv")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Boxplot por condição
sns.boxplot(data=df, x="condicao", y="expressao",
            palette="Set2", ax=axes[0])
sns.stripplot(data=df, x="condicao", y="expressao",
              color="black", alpha=0.3, size=3, ax=axes[0])
axes[0].set_title("Expressão por condição")
axes[0].set_xlabel("Condição")
axes[0].set_ylabel("Expressão (log2)")

# Scatter: GC vs. expressão
sns.scatterplot(data=df, x="gc_pct", y="expressao",
                hue="organismo", alpha=0.6, ax=axes[1])
axes[1].set_title("GC% vs. expressão")
axes[1].set_xlabel("Conteúdo GC (%)")
axes[1].set_ylabel("Expressão (log2)")

plt.tight_layout()
fig.savefig("figura_combinada.png", dpi=300,
            bbox_inches="tight")
plt.show()"""

r61 = """\
library(tidyverse)
library(patchwork)

df <- read_csv("expressao.csv")

# Boxplot por condição
p1 <- ggplot(df, aes(x=condicao, y=expressao,
                     fill=condicao)) +
  geom_boxplot(outlier.shape=NA, alpha=0.7) +
  geom_jitter(width=0.2, alpha=0.3, size=1.5) +
  labs(title="Expressão por condição",
       x="Condição", y="Expressão (log2)") +
  theme_classic() +
  theme(legend.position="none")

# Scatter: GC vs. expressão
p2 <- ggplot(df, aes(x=gc_pct, y=expressao,
                     color=organismo)) +
  geom_point(alpha=0.6, size=2) +
  labs(title="GC% vs. expressão",
       x="Conteúdo GC (%)",
       y="Expressão (log2)") +
  theme_classic()

p_final <- p1 + p2
ggsave("figura_combinada.png", p_final,
       width=12, height=5, dpi=300)"""

s6 += ex_bilingual(
    "6.1", "Figura combinada",
    "<p>Com <code>expressao.csv</code> (colunas: <code>gene, condicao, expressao, gc_pct, organismo</code>), "
    "crie uma figura com dois painéis lado a lado: (a) boxplot de expressão por condição com pontos "
    "individuais sobrepostos; (b) scatter de GC% vs. expressão colorido por organismo. "
    "Salve como PNG 300 dpi.</p>",
    py61, r61
)

py62 = """\
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("expressao.csv")

# Selecionar alguns genes para a matriz
genes_top = (df.groupby("gene")["expressao"]
               .mean()
               .nlargest(15)
               .index.tolist())

df_wide = (df[df["gene"].isin(genes_top)]
             .pivot_table(index="amostra",
                          columns="gene",
                          values="expressao"))

corr = df_wide.corr()

fig, ax = plt.subplots(figsize=(9, 8))
sns.heatmap(corr, annot=True, fmt=".2f",
            cmap="RdBu_r", center=0,
            vmin=-1, vmax=1, square=True,
            ax=ax)
ax.set_title("Correlação entre os 15 genes mais expressos")
plt.tight_layout()
fig.savefig("heatmap_genes.png", dpi=300)"""

r62 = """\
library(tidyverse)
library(pheatmap)

df <- read_csv("expressao.csv")

# Top 15 genes mais expressos (por média)
genes_top <- df |>
  group_by(gene) |>
  summarise(media=mean(expressao)) |>
  slice_max(media, n=15) |>
  pull(gene)

df_wide <- df |>
  filter(gene %in% genes_top) |>
  pivot_wider(names_from=gene,
              values_from=expressao,
              id_cols=amostra) |>
  column_to_rownames("amostra")

pheatmap(cor(df_wide),
         display_numbers=TRUE,
         number_format="%.2f",
         color=colorRampPalette(
           c("blue","white","red"))(100),
         main="Correlação — top 15 genes",
         filename="heatmap_genes.png",
         width=9, height=8)"""

s6 += ex_bilingual(
    "6.2", "Heatmap de correlação",
    "<p>Calcule a correlação entre os 15 genes com maior expressão média e gere um "
    "heatmap anotado com os valores de correlação. Salve a figura.</p>",
    py62, r62
)

s6 += '</div>'

body = s1 + s2 + s3 + s4 + s5 + s6

with open("exercicios.html", "w") as f:
    f.write(page("Exercícios", "exercicios.html", header, body))
print("exercicios.html ok")
