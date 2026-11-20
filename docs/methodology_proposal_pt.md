# Metodologia do São Paulo Transit Desert Mapper

Versão consolidada de 2026-11-20. O caminho `docs/methodology_proposal_pt.md` é mantido por enquanto para não quebrar referências.

Aviso analítico: "Índice analítico baseado em dados abertos e em limiares escolhidos pelo grupo. Não mede a qualidade do serviço nem substitui diagnóstico de campo."

Aviso para tempo e rotas: "Tempo de caminhada estimado com velocidade média assumida e distância em linha reta ou rota calculada. Não considera calçadas, declives, travessias, segurança, acessibilidade nem horários de operação."

## 1. Status

| Categoria | Itens |
|---|---|
| Decisões aprovadas pela autora | (1) Direção C: análise populacional como resultado principal e cobertura territorial como comparação. (2) Escopo: município inteiro de São Paulo, setores urbanos e rurais, sem excluir categorias automaticamente. (3) Zeros preservados, sem imputação, rotulados "população registrada igual a zero", fora do ranking de pessoas afetadas e dentro do diagnóstico territorial e da auditoria. (4) Elegibilidade inicial dos rankings populacionais: `v0001` > 0, sem corte adicional; avaliar a sensibilidade antes de propor qualquer corte. (5) Dois rankings separados, sem pesos combinados |
| Procedimentos executados no ambiente de revisão do Claude | Download e inspeção do arquivo do IBGE; leitura do dicionário; checagens de consistência; teste de validade geométrica; auditoria do GTFS; execução de `src/data/prepare_ibge.py` (município 3550308, 27.301 setores, EPSG:31983). Detalhes e limites em `docs/data-validation.md` |
| Alterações ainda não aplicadas ao repositório | Todos os arquivos preparados nesta etapa: `docs/data-validation.md`, este documento, `data/raw/IBGE/README.md`, `assets/dataset-sources-and-downloads.md`, `src/data/prepare_ibge.py`, o relatório JSON e o subconjunto em `data/processed/` (que o script recria) |
| Propostas pendentes de aprovação | Limiar de "atendido"; velocidade de caminhada; janela de serviço do GTFS; distância radial como base; hipótese de distribuição uniforme para estimar pessoas; desempates dos rankings; tratamento das 3 geometrias inválidas; qualquer corte adicional por população pequena |
| Pendente de dado ou verificação | Total primário do IBGE (versão e data de referência); data e completude do feed GTFS; data e licença do GeoSampa; ARTESP e OSM ainda não baixados |

## 2. Origem das exigências (o que está e o que não está verificado)

| Afirmação | Evidência acessível | Status |
|---|---|---|
| Unidade: setor censitário; medir população, distância até a parada mais próxima e frequência; deserto = muita gente + longe e/ou pouca frequência; limiares (ex.: 500 m) são decisão do grupo, justificada; relatório com os 10 setores mais desassistidos | `Projeto_Desertos_Transporte_resumo_v2` (PDF anexado) | Verificado nesse documento |
| Distância pela rua é opcional (OpenStreetMap) | Mesmo PDF | Verificado |
| O professor exige distância radial (anéis) em vez de rotas pelas ruas | Apenas o relato da autora em conversa. Não consta no PDF de resumo nem no `1Briefing_en.pdf` (que trata do projeto Helipad, não deste) | Não verificado em documento. Tratado como proposta, não como requisito aprovado |
| O professor exige uma única área de estudo | Apenas o relato da autora. Não consta nos documentos acessíveis | Não verificado. O escopo aprovado pela autora é o município inteiro |
| O professor quer tempo de caminhada por raio e por modo, com pins e rota | Apenas o relato da autora | Não verificado. Tratado como proposta |

A confirmação com o professor continua útil para essas três últimas linhas; nenhuma delas é requisito até ser confirmada.

## 3. Resultados distintos (não equivalentes)

| # | Resultado | Definição | Usa população? |
|---|---|---|---|
| A | Atendimento do ponto representativo | Resultado binário por setor: o ponto representativo do setor está ou não a no máximo R metros de uma parada elegível | Não |
| B | Cobertura territorial do setor | Fração da área do setor coberta pela UNIÃO das áreas de influência (raio R) das paradas elegíveis, sem dupla contagem de sobreposições | Não |
| R2 | Acessibilidade por setor | Distância do ponto representativo até a parada mais próxima, por modo, e a conversão teórica em minutos | Não |
| R3 | Resumo ponderado pela população | Média de R2 ponderada por `v0001` | Sim |
| R4 | Estimativa de pessoas atendidas ou desassistidas | `v0001` × fração B do setor, sob a hipótese de distribuição uniforme (seção 7). Estimativa agregada, nunca contagem exata | Sim, mais uma hipótese |
| R5 | Rankings | Dois rankings separados (seção 8) | Um deles |

A e B podem divergir: um setor pode ter o ponto representativo atendido e, ainda assim, ter pouca área coberta, ou o contrário. Por isso não recebem o mesmo rótulo. A estimativa populacional por fração de área usa B, nunca o binário A. A cobertura territorial agregada (diagnóstico provisório) usa B e é rotulada "sem ponderação populacional, não representa desigualdade populacional".

## 4. Unidade espacial, pontos e interpretação

- Unidade de cálculo: setor censitário (IBGE 2022), município inteiro. `SITUACAO`, `CD_SIT` (`CD_SITUACAO` no dicionário) e `CD_TIPO` permanecem para análises separadas. Agregação para distrito (GeoSampa, 96) na apresentação.
- Ponto representativo: ponto interno ao polígono (`point_on_surface`, não o centroide). Um ponto interno não é necessariamente onde a população se concentra. A distância calculada é a do ponto representativo do setor, não a distância percorrida por todos os moradores.
- Dados: `data/processed/ibge_sectors_sao_paulo_epsg31983.gpkg`, em EPSG:31983.

## 5. Distância, metros e minutos

- Proposta (pendente de aprovação): distância radial em linha reta, em EPSG:31983, como base. Rota pela malha de pedestres do OSM apenas numa amostra, para estimar um fator de desvio e qualificar o resultado, sem substituí-lo silenciosamente.
- A classificação "atendido" depende só de metros. A conversão em minutos (distância / velocidade) é uma conversão teórica com velocidade assumida, não um tempo de rota real.
- Velocidades propostas, não aprovadas: 3,6; 4,8 e 5,4 km/h.
- Sensibilidade da classificação (em metros): variar o limiar. Sensibilidade dos minutos: variar a velocidade. Variar a velocidade altera os minutos estimados, não a classificação espacial em metros.

## 6. Definição de "atendido" (nenhum limiar aprovado)

| Item | Proposta |
|---|---|
| Definição operacional | Parada elegível: parada com serviço programado no GTFS na janela escolhida. Atendido (A): ponto representativo a no máximo R metros de uma parada elegível. Cobertura (B): união dos círculos de raio R das paradas elegíveis |
| Modo | Por modo (ônibus, metrô, trem) e "qualquer modo", reportados separadamente |
| Limiares candidatos | 400, 500, 800 e 1.000 m, comparados como cenários. O PDF de resumo cita 500 m apenas como exemplo de limiar a ser decidido pelo grupo. Referência possível, a VERIFICAR na fonte antes de citar: indicador 11.2.1 dos ODS (ONU); fonte e redação exatas: Desconhecido nos materiais fornecidos |
| Serviço do GTFS | O feed da SPTrans é baseado em frequências: 2.268 viagens com `stop_times` de referência (99.120 linhas) e 40.337 linhas em `frequencies`. As partidas devem ser derivadas de `frequencies`. Dia útil, faixa horária e mínimo de partidas: a definir. Data de publicação e completude do feed: Desconhecido nos materiais fornecidos |
| Ressalva | Estar perto de uma parada não garante serviço adequado: não mede frequência real, lotação, confiabilidade, calçadas, declives, travessias, segurança nem acessibilidade |

## 7. População e estimativa de pessoas

- Verificado: a aba `Setor` do dicionário oficial define V0001 como "Total de pessoas"; o campo `v0001` existe no GeoPackage. O texto usa "pessoas", como o dicionário. O dicionário não documenta regras para zeros nem supressão; nenhuma é presumida.
- Hipótese de distribuição uniforme (PROPOSTA para aprovação, não autorizada pela escolha da análise populacional): as pessoas de um setor se distribuem uniformemente pela área dele. Limitações: pessoas se concentram onde há edificações e vias; áreas verdes ou vazias distorcem; setores grandes e rurais são os mais afetados. Alternativa sem essa hipótese (endereços ou pegadas de edificações): disponibilidade Desconhecida nos materiais fornecidos.
- Se a hipótese não for aprovada, R4 não é calculado e o resultado populacional fica em R3 e nos rankings por setor.

## 8. Zeros e rankings

Classificação dos 412 setores com `v0001` = 0 ("população registrada igual a zero"), por campos de domicílios (`v0002` total, `v0003` particulares, `v0004` coletivos). Detalhes em `docs/data-validation.md`, seção 1.5.

| Categoria | Regra | Setores |
|---|---|---|
| A | `v0002` = 0 | 373 |
| B | `v0002` > 0, `v0003` > 0 e `v0004` > 0 | 1 |
| C | `v0002` > 0, `v0003` > 0 e `v0004` = 0 | 32 |
| D | `v0002` > 0, `v0003` = 0 e `v0004` > 0 | 6 |
| Total | | 412 |

(As letras A a D desta tabela classificam zeros e não têm relação com as definições A e B da seção 3.)

Os valores originais são preservados; não há imputação. O significado de um zero (sem pessoas, não coletado ou suprimido) não está documentado e não é presumido.

Rankings (aprovado): elegibilidade `v0001` > 0, sem corte adicional na versão inicial; a população do setor aparece ao lado do indicador de acesso; dois rankings separados e sem pesos.
- Ranking por pior acessibilidade: maior distância do ponto representativo até a parada elegível mais próxima.
- Ranking por maior número estimado de pessoas afetadas: maiores estimativas de pessoas desassistidas (R4); existe somente se a hipótese da seção 7 for aprovada.
- Antes de propor qualquer corte por população pequena, avaliar a sensibilidade dos rankings; esse efeito ainda não foi medido e nada é presumido sobre ele.
- Desempates (PROPOSTA, a definir antes de executar os rankings): no ranking por acessibilidade, distância decrescente, depois `v0001` decrescente, depois `CD_SETOR` crescente; no ranking por pessoas afetadas, estimativa decrescente, depois distância decrescente, depois `CD_SETOR` crescente. Reportar os dez primeiros de cada ranking e os empates na fronteira.

## 9. Geometrias

| Etapa | Estado |
|---|---|
| Identificadas | 3 geometrias inválidas (autointersecção de anel): `355030842000772`, `355030857000168`, `355030858000491`. Nenhuma vazia |
| Tentativa de reparo controlado autorizada | Não consta nas mensagens que recebi. Se foi autorizada, registrar a data e o escopo |
| Reparo executado | Não. Nenhum reparo foi aplicado (`geometry_repaired` = false no relatório) |
| Resultado aceito ou separado para revisão | Não aplicável até haver tentativa. A autorização de uma tentativa não é aprovação de nenhum resultado: cada reparo precisa de revisão (área antes e depois, setor, `v0001`) e de aceite explícito, ou o setor é separado para revisão |

## 10. Fontes e verificações (resumo)

Resultados detalhados em `docs/data-validation.md`.

| Tema | Resumo | Status |
|---|---|---|
| IBGE: arquivo e dicionário | Download com tamanho e SHA-256 iguais aos da API; dicionário idêntico no repositório e no anexo (SHA-256 completo) | Concluído |
| `v0001` | "Total de pessoas"; sem nulos; consistência com os campos de domicílios sem violações | Concluído |
| Total municipal | A soma de `v0001` é 11.451.999, igual ao boletim da Prefeitura de São Paulo (fonte secundária, nov. 2024, sem versão nem data de referência do IBGE). A página primária do IBGE, https://www.ibge.gov.br/cidades-e-estados.html?c=3550308, não abriu no ambiente de revisão e não foi consultada | Pendente: verificação independente na fonte primária, com versão e data |
| GTFS SPTrans | Estrutura auditada; baseado em frequências; sem `feed_info.txt` | Estrutura concluída; data e completude pendentes |
| GeoSampa | Quatro camadas inspecionadas; hashes iguais aos anexos | Data e licença pendentes |
| ARTESP e OSM | Localizados no `releases.json`; não baixados | Pendente; ARTESP depende de confirmação de redistribuição |

## 11. Limitações

Parada não é serviço; GTFS é oferta programada e não operação observada; linha reta não é caminho a pé; o Censo 2022 e os feeds de transporte têm datas diferentes; setores têm tamanhos muito diferentes; paradas de ônibus podem estar duplicadas por sentido; metrô e trem do GTFS (109 e 104 paradas) diferem das estações do GeoSampa (94 e 109) e não devem ser unidos por proximidade. Em textos sobre bairros, usar "baixo acesso". Apenas personas fictícias; nenhum dado pessoal.

