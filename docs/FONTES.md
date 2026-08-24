# Fontes de Dados — CardioIA Fase 1

## Dataset Numérico

| Campo     | Valor |
|-----------|-------|
| Nome      | Heart Disease UCI |
| Fonte     | UCI Machine Learning Repository |
| ID UCI    | 45 |
| URL       | https://archive.ics.uci.edu/dataset/45/heart+disease |
| Acesso    | 2026-08-24 |
| Arquivo   | `data/pacientes_cardiacos.csv` |
| Linhas    | 303 |
| Colunas   | 14 |

---

## Textos

### 1. Wikipedia — Doença Cardiovascular

| Campo    | Valor |
|----------|-------|
| Título   | Doença cardiovascular |
| Fonte    | Wikipédia (pt) |
| URL      | https://pt.wikipedia.org/wiki/Doen%C3%A7a_cardiovascular |
| Autores  | Colaboradores da Wikipédia (conteúdo sob CC BY-SA 4.0) |
| Acesso   | 2026-08-24 |
| Arquivo  | `docs/wikipedia_doencas_cardiovasculares.txt` |
| Idioma   | Português |
| Notas    | Artigo enciclopédico sobre tipos, causas, epidemiologia, prevenção e tratamento de DCV. Usado como segundo corpus textual após bloqueio 403 do SciELO. |

### 2. Projeto Gutenberg — Harvey's Views on the Use of the Circulation of the Blood

| Campo    | Valor |
|----------|-------|
| Título   | Harvey's Views on the Use of the Circulation of the Blood |
| Autor    | John G. Curtis (sobre William Harvey) |
| Fonte    | Project Gutenberg |
| Ebook nº | 47448 |
| URL      | https://www.gutenberg.org/cache/epub/47448/pg47448.txt |
| Acesso   | 2026-08-24 |
| Arquivo  | `docs/gutenberg_47448_circulacao_sangue.txt` |
| Idioma   | Inglês |
| Notas    | Obra sobre as ideias de William Harvey acerca da circulação sanguínea. Domínio público. Usado como corpus histórico/científico sobre circulação cardíaca. SciELO bloqueou acesso via scraping (HTTP 403). |

---

## Imagens de ECG

> **Pendente:** aguardando token Kaggle (`~/.kaggle/kaggle.json`).
> Dataset planejado: `evilspirit05/ecg-analysis` (Kaggle).
> Destino: `images/` (120 imagens, balanceadas por categoria).
