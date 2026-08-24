# Fontes de Dados — CardioIA Fase 1

## Dataset Numérico

| Campo     | Valor |
|-----------|-------|
| Nome      | Heart Disease UCI |
| Fonte     | UCI Machine Learning Repository |
| ID UCI    | 45 |
| DOI       | 10.24432/C52P4X |
| URL       | https://archive.ics.uci.edu/dataset/45/heart+disease |
| Criadores | Janosi A.; Steinbrunn W.; Pfisterer M.; Detrano R. (1989) |
| Licença   | CC BY 4.0 |
| Acesso    | 2026-08-24 |
| Obtido via| Pacote `ucimlrepo` (`fetch_ucirepo(id=45)`) |
| Arquivo   | `data/pacientes_cardiacos.csv` |
| Linhas    | 303 |
| Colunas   | 14 |
| Natureza  | Dados reais, coletados na Cleveland Clinic Foundation |
| Notas     | Nomes e identificadores dos pacientes foram removidos na origem e substituídos por valores fictícios. |

---

## Textos

### 1. SciELO — Recuperação da frequência cardíaca e risco de mortalidade

| Campo     | Valor |
|-----------|-------|
| Título    | Association of heart rate recovery with mortality risk in a 72-month survival analysis |
| Autores   | Costa BM; Motin C; Sousa JVM; Okuno NM; Ferreira-Junior A. |
| Periódico | Cadernos de Saúde Pública, 2026, v. 42, e00113025 |
| DOI       | 10.1590/0102-311XEN113025 |
| Licença   | CC BY |
| Acesso    | 2026-08-24 |
| Arquivo   | `docs/scielo_recuperacao_fc_mortalidade.txt` |
| Idioma    | Corpo em inglês, resumo em português |
| Extensão  | ~2.260 palavras |
| Notas     | Coorte de 578 pacientes de hospital universitário brasileiro, seguidos por 72 meses. Conecta-se diretamente à variável `freq_cardiaca_maxima` do dataset numérico. |

### 2. SciELO — Substituto do sal e incidência de hipertensão

| Campo     | Valor |
|-----------|-------|
| Título    | Eficácia de um Substituto do Sal na Incidência de Hipertensão: Uma Revisão Sistemática com Metanálise |
| Autores   | Kelly FA; Dantas CR; Sobreira LER; Almeida AM; Bezerra FB; Sousa MG; Consolim F; Laurinavicius AG. |
| Periódico | Arquivos Brasileiros de Cardiologia, 2026, v. 123, n. 3, e20250440 |
| DOI       | 10.36660/abc.20250440 |
| Licença   | CC BY |
| Acesso    | 2026-08-24 |
| Arquivo   | `docs/scielo_substituto_sal_hipertensao.txt` |
| Idioma    | Português |
| Extensão  | ~4.040 palavras |
| Notas     | Metanálise de 4 ECRs com 1.430 participantes. Texto estruturado (PRISMA, PICOT, risco de viés), útil para extração de entidades e classificação de tópicos. Conecta-se à variável `pressao_arterial_repouso`. |

### 3. Projeto Gutenberg — Harvey's Views on the Use of the Circulation of the Blood

| Campo    | Valor |
|----------|-------|
| Título   | Harvey's Views on the Use of the Circulation of the Blood |
| Autor    | John G. Curtis (sobre William Harvey) |
| Fonte    | Project Gutenberg |
| Ebook nº | 47448 |
| URL      | https://www.gutenberg.org/cache/epub/47448/pg47448.txt |
| Licença  | Domínio público |
| Acesso   | 2026-08-24 |
| Arquivo  | `docs/gutenberg_47448_circulacao_sangue.txt` |
| Idioma   | Inglês |
| Notas    | Corpus histórico sobre a circulação sanguínea. Contrasta com os artigos contemporâneos em vocabulário e estrutura. |

### Preparação dos textos

Os dois artigos foram extraídos dos PDFs oficiais com `pdfplumber` e limpos:
removidos cabeçalhos e rodapés correntes, numeração de página, abstract em
inglês, referências bibliográficas, contribuição dos autores e rótulos
soltos de figuras e tabelas.

O artigo dos Arquivos Brasileiros de Cardiologia tem diagramação em duas
colunas com calha em posição variável entre as páginas. A extração foi feita
coluna a coluna, com detecção automática da calha por página, para preservar
a ordem de leitura do texto.

---

## Imagens de ECG

> **Pendente:** aguardando token Kaggle (`~/.kaggle/kaggle.json`).
> Dataset planejado: `evilspirit05/ecg-analysis` (Kaggle).
> Destino: `images/` (120 imagens, balanceadas por categoria).
