# CardioIA — Fase 1: Batimentos de Dados

Repositório da Fase 1 do projeto CardioIA, plataforma acadêmica que simula o
ecossistema de uma cardiologia moderna integrando dados clínicos, Machine
Learning, Visão Computacional, IoT e agentes inteligentes.

Esta fase é de **levantamento e curadoria de dados**. Nenhum modelo é treinado
aqui. O objetivo é construir e documentar a base que alimentará os módulos das
fases seguintes: diagnóstico automatizado (Fase 2), monitoramento contínuo
(Fase 3), diagnóstico por imagem (Fase 4), assistente virtual (Fase 5) e
previsão de eventos (Fase 6).

Foram preparados três conjuntos de dados: **numérico**, **textual** e
**visual**, cada um com origem declarada, licença verificada e justificativa
de relevância clínica.

---

## Acesso aos dados

| Conjunto | Link |
|----------|------|
| Pasta completa | [Google Drive](https://drive.google.com/drive/folders/1jct3noUh8-SUqwJpb_fiCd_25NrIar13?usp=drive_link) |
| Dataset numérico (CSV) | [pacientes_cardiacos.csv](https://drive.google.com/file/d/1Icm6pqPRm6u4B4qR0bbk3HeBOoFnOgZN/view?usp=sharing) |
| Imagens de ECG (120 arquivos) | [pasta images/](https://drive.google.com/drive/folders/1Vvtj7KzWHNAUJyeK2yuizATvNTQ_OrEZ?usp=drive_link) |

Os textos estão versionados diretamente neste repositório, em `docs/`.

Os metadados completos de todas as fontes (DOI, autores, licença, data de
acesso) estão em [`docs/FONTES.md`](docs/FONTES.md).

---

## Estrutura do repositório

```
fase-1/
├── README.md
├── data/
│   └── pacientes_cardiacos.csv          # dataset numérico (303 × 14)
├── docs/
│   ├── FONTES.md                        # metadados e licenças
│   ├── scielo_recuperacao_fc_mortalidade.txt
│   └── scielo_substituto_sal_hipertensao.txt
├── images/                              # 120 ECGs (fora do git, ver Drive)
├── notebooks/                           # reservado para as próximas fases
└── scripts/
    ├── baixar_dataset.py                # download reprodutível do UCI
    └── mapeamento_colunas.md            # dicionário de variáveis
```

`images/` está no `.gitignore` por ser conteúdo binário volumoso na origem. O
CSV é versionado por ser pequeno e essencial para reprodutibilidade.

---

## Parte 1 — Dados Numéricos (IoT)

### Origem

**Dados reais**, não simulados. Heart Disease Dataset do UCI Machine Learning
Repository (id 45), subconjunto Cleveland, coletado na Cleveland Clinic
Foundation por Detrano e colaboradores. Licença CC BY 4.0, DOI
`10.24432/C52P4X`.

Obtido de forma reprodutível via pacote oficial `ucimlrepo`:

```bash
python scripts/baixar_dataset.py
```

Os nomes e identificadores dos pacientes foram removidos na origem e
substituídos por valores fictícios, o que elimina a necessidade de
anonimização adicional da nossa parte.

### Dimensões

303 registros, 14 variáveis. As colunas originais em sigla foram renomeadas
para nomes descritivos em português. O mapeamento completo está em
`scripts/mapeamento_colunas.md`.

### Variáveis mais relevantes do ponto de vista clínico

Nem todas as 14 variáveis têm o mesmo peso. Abaixo, as que consideramos
prioritárias e o porquê.

**`tipo_dor_peito`** — Provavelmente a variável isolada de maior valor
preditivo. Distingue angina típica, angina atípica, dor não anginosa e
assintomático. A angina típica tem alta especificidade para doença arterial
coronariana, enquanto o paciente assintomático representa o caso mais
perigoso: doença presente sem sinal de alerta. Para triagem digital
(Fase 2), é a variável que mais separa as classes.

**`freq_cardiaca_maxima`** — Frequência cardíaca de pico atingida em teste
ergométrico. Capacidade cronotrópica reduzida é marcador de disfunção
autonômica e de pior prognóstico. Como detalhado na seção de NLP abaixo, um
dos artigos do nosso corpus documenta que pacientes com recuperação anormal
da frequência cardíaca apresentaram frequência de pico significativamente
menor e razão de risco de mortalidade de 3,16. A variável não é um número
solto: tem suporte prognóstico em coorte brasileira contemporânea.

**`angina_por_exercicio` e `depressao_st`** — Ambas derivam do mesmo teste
ergométrico. Angina induzida por esforço e depressão do segmento ST são os
achados clássicos de isquemia induzível. `depressao_st` é contínua, o que a
torna útil para modelos que se beneficiam de gradação em vez de binarização.

**`pressao_arterial_repouso`** — Hipertensão é o principal fator de risco
modificável para eventos cardiovasculares. O segundo artigo do corpus
quantifica que reduções de aproximadamente 5 mmHg na pressão sistólica se
associam a diminuição de 10% a 15% no risco de eventos maiores. Isso conecta
a variável a uma via de intervenção, não só de diagnóstico, o que interessa ao
módulo de acompanhamento remoto (Fase 5).

**`vasos_coloridos`** — Número de vasos principais com obstrução visível em
fluoroscopia. É a variável mais próxima de um padrão-ouro anatômico no
dataset. Também é a que mais concentra dados faltantes, pelo motivo discutido
na seção de governança.

**`colesterol_serico`** — Fator de risco consolidado, mas o valor total isolado
é menos informativo que o fracionamento em LDL e HDL, indisponível aqui. Deve
ser tratado com essa limitação em mente.

**`idade` e `sexo`** — Fatores de risco não modificáveis, indispensáveis para
estratificação. São também as variáveis que carregam o viés amostral mais
relevante, tratado adiante.

### Uso previsto nas fases seguintes

Classificação supervisionada de risco (Fase 2), definição de faixas de
normalidade para os sensores do wearable (Fase 3) e composição de séries
temporais sintéticas para o modelo preditivo (Fase 6).

---

## Parte 2 — Dados Textuais (NLP)

### Fontes

Dois artigos científicos revisados por pares, ambos indexados no SciELO e
publicados sob licença Creative Commons Attribution.

**1. Recuperação da frequência cardíaca e risco de mortalidade**
Costa BM et al., *Cadernos de Saúde Pública*, 2026, v. 42, e00113025.
DOI `10.1590/0102-311XEN113025`.
Coorte de 578 pacientes de hospital universitário brasileiro acompanhados por
72 meses. Aproximadamente 2.260 palavras.

**2. Substituto do sal e incidência de hipertensão**
Kelly FA et al., *Arquivos Brasileiros de Cardiologia*, 2026, v. 123, n. 3,
e20250440. DOI `10.36660/abc.20250440`.
Revisão sistemática com metanálise de 4 ensaios clínicos randomizados,
1.430 participantes. Aproximadamente 4.040 palavras, integralmente em
português.

Ambos foram extraídos dos PDFs oficiais com `pdfplumber` e limpos: removidos
cabeçalhos e rodapés correntes, numeração de página, referências
bibliográficas, contribuições dos autores e rótulos soltos de figuras. O
artigo dos Arquivos Brasileiros de Cardiologia tem diagramação em duas colunas
com calha em posição variável entre páginas, e exigiu extração coluna a coluna
com detecção automática da calha para preservar a ordem de leitura. Extração
ingênua embaralha os parágrafos das duas colunas e inviabiliza qualquer
análise posterior.

### Como esses textos podem ser explorados por NLP

**Extração de entidades clínicas (NER).** Os dois textos são densos em
entidades nomeadas de domínio: fármacos (betabloqueador, iECA, BRA,
diurético), condições (hipertensão, diabetes, dislipidemia, hipercalemia),
procedimentos (teste ergométrico, revascularização coronariana) e medidas com
unidade (mmHg, bpm, kg/m²). Um modelo de NER treinado nesse tipo de corpus
alimentaria o assistente virtual da Fase 5, permitindo que ele reconheça o que
o paciente relata em linguagem natural e mapeie para terminologia clínica.

**Extração de relações e valores de referência.** O primeiro artigo define
explicitamente pontos de corte: recuperação normal da frequência cardíaca como
queda maior ou igual a 13 bpm no primeiro minuto pós-exercício, e anormal como
queda menor ou igual a 12 bpm. Extrair automaticamente pares
`variável → limiar → desfecho` de literatura é uma tarefa de NLP com aplicação
direta: o sistema pode manter suas regras de alerta sincronizadas com a
evidência publicada em vez de tê-las codificadas manualmente.

**Classificação de tópicos.** A metanálise segue estrutura padronizada
(PRISMA, modelo PICOT, avaliação de risco de viés, análise de sensibilidade).
Essa regularidade estrutural torna o texto adequado para treinar
classificadores de seção, capazes de responder "onde neste artigo está o
método?" ou "onde está a limitação?". É a base de um módulo de sumarização de
evidência para apoio à decisão clínica.

**Análise de sentimentos e polaridade em contexto científico.** Aqui vale uma
ressalva metodológica: análise de sentimentos aplicada a texto científico não
mede emoção, e sim **certeza epistêmica**. Termos como "sugere uma tendência",
"permanecem extrapolações teóricas" ou "não pode ser completamente excluído"
sinalizam grau de confiança. Detectar hedging é relevante para um sistema que
apresenta evidência ao paciente ou ao médico sem exagerar a força das
conclusões. Aplicar um classificador de sentimento genérico, treinado em
resenhas de produtos, a esse corpus produziria resultado sem significado.

### Por que isso é relevante para IA em saúde

A maior parte do conhecimento clínico existe como texto não estruturado. Um
sistema que só consome tabelas ignora a literatura que define o que aquelas
tabelas significam. Além disso, um dos artigos está integralmente em
português: modelos de linguagem clínica são desproporcionalmente treinados em
inglês, e corpora em PT-BR são escassos. Incluir texto em português no corpus
é uma decisão deliberada, não acidental.

---

## Parte 3 — Dados Visuais (VC)

### Fonte

ECG Image Data, disponibilizado por `erhmrai` no Kaggle.
Licença **CC BY-NC-SA 4.0**. Aproximadamente 124.000 imagens disponíveis, das
quais **120 foram selecionadas** para este subconjunto.

Seleção aleatória com `random.seed(42)`, garantindo reprodutibilidade.

### Categorias

Organizadas segundo o padrão AAMI EC57, o mesmo esquema de classificação de
batimentos usado na MIT-BIH Arrhythmia Database.

| Pasta | Código | Significado | Selecionadas | Disponíveis |
|-------|--------|-------------|--------------|-------------|
| `N_normal/` | N | Batimento normal (ritmo sinusal, BRE, BRD) | 20 | 94.635 |
| `S_supraventricular/` | S | Ectópico supraventricular | 20 | 2.779 |
| `V_ventricular/` | V | Ectópico ventricular | 20 | 7.236 |
| `F_fusao/` | F | Batimento de fusão | 20 | 803 |
| `Q_inclassificavel/` | Q | Inclassificável / artefato | 20 | 8.039 |
| `M_infarto_miocardio/` | M | Infarto do miocárdio | 20 | 10.506 |

### Como essas imagens podem ser analisadas por Visão Computacional

**Detecção de bordas e segmentação da forma de onda.** O primeiro problema em
ECG digitalizado não é diagnóstico, é extração: separar o traçado do papel
quadriculado de fundo. Filtros de Canny ou Sobel, combinados com limiarização
adaptativa, isolam a curva. Uma vez isolada, o traçado pode ser reconvertido
em sinal unidimensional, o que abre caminho para técnicas de processamento de
sinal além das de imagem.

**Delineamento do complexo PQRST.** Identificar os pontos fiduciais (onda P,
complexo QRS, segmento ST, onda T) é o passo que conecta pixel a significado
clínico. Alargamento do QRS indica condução ventricular anormal; elevação ou
depressão do segmento ST é o achado central no diagnóstico de infarto agudo.
Um modelo de segmentação semântica pode marcar essas regiões diretamente na
imagem.

**Classificação por CNN.** Com as categorias já rotuladas, redes convolucionais
podem ser treinadas para classificar o batimento. Arquiteturas pré-treinadas
(ResNet, EfficientNet) com transfer learning são o caminho prático dado o
tamanho do conjunto. Este é o núcleo da Fase 4.

**Reconhecimento de anomalias e mapas de ativação.** Além de classificar, o
sistema precisa mostrar **onde** olhou. Técnicas como Grad-CAM produzem mapas
de calor sobrepostos ao traçado, indicando a região que mais influenciou a
decisão. Em aplicação médica isso deixa de ser refinamento e passa a ser
requisito: um diagnóstico sem justificativa visual não é auditável por um
cardiologista, e portanto não é utilizável.

### Por que isso é relevante para IA em saúde

O ECG é o exame cardiológico mais acessível e mais realizado no mundo. Em
regiões sem cardiologista disponível, a interpretação automatizada com
triagem de casos críticos tem impacto direto sobre tempo até tratamento,
que em infarto é o fator determinante de sobrevida. A viabilidade não depende
de equipamento novo, apenas de software sobre um exame que já é rotina.

---

## Governança de Dados e Viés

Esta seção é parte do entregável, não um adendo. Um projeto de IA em saúde que
não documenta as limitações dos seus dados produz modelos cujo erro é
invisível até chegar ao paciente.

### Procedência e licenciamento

Todas as três fontes são públicas, com licença verificada e registrada:

| Conjunto | Licença | Implicação |
|----------|---------|------------|
| Numérico | CC BY 4.0 | Uso livre com atribuição |
| Textual | CC BY | Uso livre com atribuição |
| Visual | CC BY-NC-SA 4.0 | Uso **não comercial**, atribuição obrigatória, redistribuição derivada sob a mesma licença |

A cláusula NC das imagens restringe o uso a contexto acadêmico. Caso o CardioIA
evoluísse para produto, esse conjunto teria de ser substituído. Registrar isso
agora evita retrabalho depois.

### Privacidade

Nenhum dos conjuntos contém dados identificáveis. No dataset numérico, os
identificadores foram removidos na origem e substituídos por valores
fictícios. As imagens de ECG não contêm cabeçalho com nome de paciente. Não
houve necessidade de processo de anonimização adicional, e nenhum dado
sensível foi introduzido por nós.

### Viés no dataset numérico

**Desequilíbrio por sexo.** 206 registros masculinos (68%) contra 97 femininos
(32%). Esse desequilíbrio não é aleatório e tem consequência clínica direta: a
apresentação da doença arterial coronariana difere entre sexos, com maior
frequência de sintomas atípicos em mulheres. Um modelo treinado nesta
distribuição tende a aprender o padrão masculino como norma e a subestimar
risco em mulheres com apresentação atípica, precisamente o grupo já
historicamente subdiagnosticado.

**Concentração etária.** A distribuição é fortemente centrada:

| Faixa | Registros |
|-------|-----------|
| menos de 30 | 1 |
| 30 a 39 | 14 |
| 40 a 49 | 72 |
| 50 a 59 | 125 |
| 60 a 69 | 81 |
| 70 ou mais | 10 |

A faixa de 50 a 59 anos concentra 41% da amostra. As caudas são
estatisticamente inúteis: com 1 paciente abaixo de 30 anos e 10 acima de 70,
qualquer inferência sobre esses grupos é ruído. O modelo não deve ser aplicado
fora da faixa de 40 a 69 anos sem validação adicional.

**Deslocamento temporal e geográfico.** Os dados foram coletados em 1988, em
centro único nos Estados Unidos. Desde então mudaram a prevalência de fatores
de risco, os critérios diagnósticos e a prática clínica. A população também não
é brasileira, o que importa para um projeto destinado ao contexto do SUS. É
justamente aqui que o corpus textual agrega: o artigo do *Cadernos de Saúde
Pública* traz coorte brasileira de 2012 a 2018, permitindo confrontar as
variáveis do dataset com evidência local e contemporânea.

**Ausência não aleatória.** Os dados faltantes se concentram em
`vasos_coloridos` (4 nulos) e `talassemia` (2 nulos), justamente as variáveis
obtidas por exame invasivo ou de alto custo. A ausência não é aleatória: ela
carrega informação sobre quem teve acesso ao exame. Imputar esses valores pela
média trataria um viés de acesso como se fosse ruído estatístico, e
propagaria a desigualdade para dentro do modelo.

### Viés no conjunto de imagens

O desequilíbrio na origem é extremo: 94.635 batimentos normais contra 803 de
fusão, razão de 118 para 1. Um classificador treinado no conjunto completo sem
reamostragem atingiria cerca de 78% de acurácia simplesmente respondendo
"normal" para toda entrada, sem aprender nada. Em contexto clínico, esse
modelo seria pior que inútil, porque a métrica agregada esconderia falha
completa nas classes que importam.

Nossa seleção usa 20 imagens por categoria justamente para não reproduzir esse
desequilíbrio no subconjunto de trabalho. Nas fases seguintes, a avaliação deve
priorizar sensibilidade por classe e matriz de confusão, nunca acurácia global.

### Viés no corpus textual

Um dos dois artigos tem corpo em inglês. Modelos de linguagem clínica são
majoritariamente treinados em inglês, e aplicar diretamente a texto médico em
português produz degradação silenciosa, especialmente em terminologia e
negação. O corpus reflete a assimetria real da literatura, e isso deve ser
considerado ao escolher modelos na Fase 5.

Há também viés de publicação inerente: a própria metanálise incluída no corpus
reconhece que o viés de publicação não pôde ser completamente excluído devido
ao pequeno número de ensaios. Literatura científica não é amostra neutra da
realidade, é amostra do que foi considerado publicável.

---

## Reprodutibilidade

O dataset numérico pode ser reconstruído do zero:

```bash
pip install ucimlrepo pandas
python scripts/baixar_dataset.py
```

A seleção de imagens usa semente fixa (`random.seed(42)`), portanto é
determinística sobre a mesma versão do dataset de origem.

Os textos estão versionados no repositório em sua forma já processada, com
nota de preparação no cabeçalho de cada arquivo descrevendo exatamente o que
foi removido.

---

## Referências

Detrano R., Janosi A., Steinbrunn W., Pfisterer M. **Heart Disease.** UCI
Machine Learning Repository, 1989. DOI: 10.24432/C52P4X

Costa B. M., Motin C., Sousa J. V. M., Okuno N. M., Ferreira-Junior A.
**Association of heart rate recovery with mortality risk in a 72-month
survival analysis.** Cadernos de Saúde Pública, v. 42, e00113025, 2026.
DOI: 10.1590/0102-311XEN113025

Kelly F. A., Dantas C. R., Sobreira L. E. R., Almeida A. M., Bezerra F. B.,
Sousa M. G., Consolim F., Laurinavicius A. G. **Eficácia de um Substituto do
Sal na Incidência de Hipertensão: Uma Revisão Sistemática com Metanálise.**
Arquivos Brasileiros de Cardiologia, v. 123, n. 3, e20250440, 2026.
DOI: 10.36660/abc.20250440

**ECG Image Data.** Kaggle, disponibilizado por erhmrai.
https://www.kaggle.com/datasets/erhmrai/ecg-image-data
