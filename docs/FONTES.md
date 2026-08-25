# Fontes de Dados — CardioIA Fase 1

## Dataset Numérico

| Campo      | Valor                                                                                                 |
| ---------- | ----------------------------------------------------------------------------------------------------- |
| Nome       | Heart Disease UCI                                                                                     |
| Fonte      | UCI Machine Learning Repository                                                                       |
| ID UCI     | 45                                                                                                    |
| DOI        | 10.24432/C52P4X                                                                                       |
| URL        | https://archive.ics.uci.edu/dataset/45/heart+disease                                                  |
| Criadores  | Janosi A.; Steinbrunn W.; Pfisterer M.; Detrano R. (1989)                                             |
| Licença    | CC BY 4.0                                                                                             |
| Acesso     | 2026-08-24                                                                                            |
| Obtido via | Pacote `ucimlrepo` (`fetch_ucirepo(id=45)`)                                                           |
| Arquivo    | `data/pacientes_cardiacos.csv`                                                                        |
| Linhas     | 303                                                                                                   |
| Colunas    | 14                                                                                                    |
| Natureza   | Dados reais, coletados na Cleveland Clinic Foundation                                                 |
| Notas      | Nomes e identificadores dos pacientes foram removidos na origem e substituídos por valores fictícios. |

---

## Textos

### 1. SciELO — Recuperação da frequência cardíaca e risco de mortalidade

| Campo     | Valor                                                                                                                                                              |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Título    | Association of heart rate recovery with mortality risk in a 72-month survival analysis                                                                             |
| Autores   | Costa BM; Motin C; Sousa JVM; Okuno NM; Ferreira-Junior A.                                                                                                         |
| Periódico | Cadernos de Saúde Pública, 2026, v. 42, e00113025                                                                                                                  |
| DOI       | 10.1590/0102-311XEN113025                                                                                                                                          |
| Licença   | CC BY                                                                                                                                                              |
| Acesso    | 2026-08-24                                                                                                                                                         |
| Arquivo   | `docs/scielo_recuperacao_fc_mortalidade.txt`                                                                                                                       |
| Idioma    | Corpo em inglês, resumo em português                                                                                                                               |
| Extensão  | ~2.260 palavras                                                                                                                                                    |
| Notas     | Coorte de 578 pacientes de hospital universitário brasileiro, seguidos por 72 meses. Conecta-se diretamente à variável `freq_cardiaca_maxima` do dataset numérico. |

### 2. SciELO — Substituto do sal e incidência de hipertensão

| Campo     | Valor                                                                                                                                                                                                         |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Título    | Eficácia de um Substituto do Sal na Incidência de Hipertensão: Uma Revisão Sistemática com Metanálise                                                                                                         |
| Autores   | Kelly FA; Dantas CR; Sobreira LER; Almeida AM; Bezerra FB; Sousa MG; Consolim F; Laurinavicius AG.                                                                                                            |
| Periódico | Arquivos Brasileiros de Cardiologia, 2026, v. 123, n. 3, e20250440                                                                                                                                            |
| DOI       | 10.36660/abc.20250440                                                                                                                                                                                         |
| Licença   | CC BY                                                                                                                                                                                                         |
| Acesso    | 2026-08-24                                                                                                                                                                                                    |
| Arquivo   | `docs/scielo_substituto_sal_hipertensao.txt`                                                                                                                                                                  |
| Idioma    | Português                                                                                                                                                                                                     |
| Extensão  | ~4.040 palavras                                                                                                                                                                                               |
| Notas     | Metanálise de 4 ECRs com 1.430 participantes. Texto estruturado (PRISMA, PICOT, risco de viés), útil para extração de entidades e classificação de tópicos. Conecta-se à variável `pressao_arterial_repouso`. |

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

| Campo      | Valor                                                  |
| ---------- | ------------------------------------------------------ |
| Nome       | ECG Image Data                                         |
| Autor      | erhmrai                                                |
| Fonte      | Kaggle                                                 |
| Ref Kaggle | `erhmrai/ecg-image-data`                               |
| URL        | https://www.kaggle.com/datasets/erhmrai/ecg-image-data |
| Licença    | CC BY-NC-SA 4.0                                        |
| Acesso     | 2026-08-24                                             |
| Destino    | `images/` (subpastas por categoria)                    |
| Total      | 120 imagens selecionadas de ~124.000 disponíveis       |
| Tamanho    | 1,1 MB (subset)                                        |

### Categorias (padrão AAMI EC57 / MIT-BIH)

| Pasta                  | Código | Significado                                                | Imagens selecionadas | Total disponível |
| ---------------------- | ------ | ---------------------------------------------------------- | -------------------- | ---------------- |
| `N_normal/`            | N      | Batimento normal (ritmo sinusal normal, BRE, BRD)          | 20                   | 94.635           |
| `S_supraventricular/`  | S      | Batimento ectópico supraventricular (extrassístole atrial) | 20                   | 2.779            |
| `V_ventricular/`       | V      | Batimento ectópico ventricular (extrassístole ventricular) | 20                   | 7.236            |
| `F_fusao/`             | F      | Batimento de fusão (ventricular + normal)                  | 20                   | 803              |
| `Q_inclassificavel/`   | Q      | Batimento inclassificável / artefato                       | 20                   | 8.039            |
| `M_infarto_miocardio/` | M      | Infarto do miocárdio                                       | 20                   | 10.506           |

**Nota:** seleção aleatória com `random.seed(42)`, garantindo reprodutibilidade.
O dataset original (858 MB) não foi incluído no repositório git (`images/` está no `.gitignore`).
Fazer upload de `images/` manualmente para o Google Drive.

### Restrição de licença

As imagens estão sob CC BY-NC-SA 4.0. O uso neste projeto é estritamente
acadêmico e não comercial, conforme a cláusula NC. A cláusula SA implica que
qualquer redistribuição derivada deve manter a mesma licença. A atribuição ao
autor original é obrigatória e está registrada acima.
