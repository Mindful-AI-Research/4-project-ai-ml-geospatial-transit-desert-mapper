# Proposta de metodologia para aprovação (nada implementado)

Status: PROPOSTA (revisada em 2026-11-19 com o dicionário do IBGE). Direção escolhida pela autora: opção C. Resultado principal = análise populacional; comparação = cobertura territorial. A análise populacional NÃO será substituída por análise só de área por causa do bloqueio de acesso aos dados. Até o IBGE ser desbloqueado, a cobertura territorial é um diagnóstico provisório, rotulado, e não é resultado final de desigualdade populacional.

Aviso: "Índice analítico baseado em dados abertos e em limiares escolhidos pelo grupo. Não mede a qualidade do serviço nem substitui diagnóstico de campo."

## 1. Cinco resultados distintos (não equivalentes)

| # | Resultado | O que é | Depende de população? |
|---|---|---|---|
| R1 | Cobertura territorial | Proporção da área (da área de estudo ou do setor) dentro do raio de uma parada | Não |
| R2 | Acessibilidade por setor | Indicador calculado para cada setor (distância e minutos até a parada mais próxima, por modo) | Não |
| R3 | Resumo ponderado pela população | Média da acessibilidade dos setores ponderada pela população do setor | Sim |
| R4 | Estimativa de pessoas atendidas ou desassistidas | Estimativa agregada, não contagem exata | Sim, mais uma hipótese |
| R5 | Ranking de prioridade | Dois rankings separados (seção 7) | Sim (um deles) |

Saber a população total do setor não revela a população dentro da parcela atendida. Para R4 é preciso uma hipótese de distribuição.

## 2. Indicador principal

Por setor: distância radial em metros do ponto representativo do setor até a parada mais próxima, para cada modo (ônibus, metrô, trem) e para qualquer modo, e o tempo de caminhada estimado (velocidade assumida de 4,8 km/h como parâmetro, a confirmar). "Atendido" usa um limiar em metros (padrão proposto de 500 m, parâmetro do grupo, não norma).

## 3. Como a população entra

- R3: peso = `v0001` do setor. Verificado: a aba `Setor` do dicionário oficial (`data/raw/IBGE/Dicionario_de_dados_malha_agregados.xlsx`) define V0001 como "Total de pessoas", e o campo `v0001` existe no GeoPackage (comparação por nome, ignorando maiúsculas). O texto usa "pessoas", como o dicionário. O dicionário não documenta regra para zeros nem supressão.
- R4: pessoas atendidas de um setor = `v0001` do setor × fração da área do setor dentro do raio. Hipótese: distribuição uniforme dos moradores na área do setor. Limitações: moradores se concentram onde há edificações e vias, e áreas verdes ou vazias distorcem; setores grandes e rurais são os mais afetados. Resultado rotulado "estimativa agregada", nunca "contagem".
- Alternativa sem hipótese uniforme (por exemplo, pontos de endereços do Censo ou pegadas de edificações): disponibilidade Desconhecido nos materiais fornecidos.

## 4. Unidade espacial

Setor censitário (IBGE 2022) como unidade de cálculo. Agregação para distrito (GeoSampa, 96) para apresentação. Escopo geográfico (a ÚNICA área do professor ou o município): decisão pendente, ver pergunta Q2.

## 5. Pontos de origem

- Setor: ponto representativo interno ao polígono (`point_on_surface`, não o centroide, que pode cair fora de setores côncavos).
- Cobertura territorial provisória: grade regular (50 ou 100 m) dentro da área, em EPSG:31983.
- Demonstração de pin e rota: origem escolhida pelo usuário entre marcos públicos; sem endereços reais de pessoas.

## 6. Distância

Radial (linha reta, EPSG:31983) como base, conforme pedido do professor. Rota pela rede de ruas apenas em uma amostra dentro da área, para estimar o fator de desvio e qualificar o resultado. Não substitui a medida radial.

## 7. Setores sem população informada e os dez mais desassistidos

- Verificado no arquivo (município 3550308, 27.301 setores): `v0001` não tem valores nulos; 412 setores têm `v0001` = 0 (373 deles também com `v0002` = 0; 33 com `v0003` > 0). O dicionário NÃO documenta se zero significa ausência de pessoas, dado não coletado ou supressão. Nenhuma regra é presumida. Proposta para aprovação: manter setores com `v0001` = 0 e eventual valor ausente em categorias separadas e contadas, fora de R3, R4 e R5, presentes em R1 e R2, sem imputação e sem substituição de ausente por zero. Decisão sua.
- Ranking A, pior acessibilidade: setores ordenados pela maior distância até a parada mais próxima (qualquer modo). Elegíveis: `v0001` informado e acima de um mínimo a definir (decisão pendente). Sem esse mínimo, o topo tende a ser setores quase vazios.
- Ranking B, maior número estimado de pessoas afetadas: setores ordenados pelas maiores estimativas de moradores desassistidos (R4), com a hipótese uniforme exibida.
- Os dois rankings ficam separados. Nenhum peso para combiná-los sem aprovação.
- Desempates e incerteza: mostrar a distância e a estimativa lado a lado; sensibilidade com outros limiares (400, 500, 800 m) e velocidades; informar quais setores mudam de posição.

## 8. Diagnóstico provisório (permitido agora, antes do IBGE)

Cobertura territorial R1 por grade na área escolhida, com o rótulo: "Diagnóstico provisório de cobertura territorial, sem ponderação populacional. Não representa desigualdade populacional."

## 9. Decisões que preciso de você

1. Q1 resolvida: opção C.
2. Q2. Escopo: apenas a área única do professor, ou o município inteiro como extensão?
   ➡️ Recomendo a área única para 5 de dezembro; município como extensão.
3. Q3. Limiar de "atendido": 500 m para todos os modos, ou diferenciar (ex.: 500 m ônibus, 1.000 m metrô e trem)?
   ➡️ Recomendo um único valor por modo, declarado como parâmetro do grupo, com sensibilidade.
4. Q4. Mínimo de população para elegibilidade no Ranking A: definir um valor ou usar um percentil?
   ➡️ Recomendo definir depois de ver a distribuição real, e registrar.

## 10. Verificado em 2026-11-19 (população)

| Item | Resultado |
|---|---|
| Dicionário na branch `main` | Presente (commit `0feb9d4`), idêntico ao anexo |
| V0001 na aba `Setor` | "Total de pessoas" |
| Campo `v0001` no GeoPackage | Existe; correspondência por nome |
| Consistência com as definições | `v0002` = `v0003` + `v0004`, `v0007` <= `v0003`, `v0001` >= `v0007`: 0 violações em 27.301 setores |
| Comparação com totais oficiais externos | Não realizada |
| Regras de zero e supressão | Não documentadas; não presumidas |

Preparação da análise populacional (nada implementado ainda): carregar o GeoPackage, filtrar `CD_MUN` = 3550308, reprojetar de 4674 para EPSG:31983, manter o arquivo estadual intacto e salvar o subconjunto em `data/processed/`. Limiares, pesos e critérios de ranking continuam como propostos, sem alteração, aguardando sua aprovação.

## 11. Decisões registradas em 2026-11-20

- Escopo: todo o município de São Paulo, setores urbanos e rurais. `SITUACAO`, `CD_SITUACAO` (campo `CD_SIT` no GeoPackage) e `CD_TIPO` ficam disponíveis para análises separadas; nenhuma categoria é excluída automaticamente.
- Zeros: valores originais preservados, sem imputação. Rótulo: "população registrada igual a zero". Ficam no diagnóstico territorial e na auditoria; fora do ranking principal de pessoas afetadas. Categorias exclusivas (A 373, B 1, C 32, D 6 = 412) no catálogo.
- Ranking: elegibilidade apenas `v0001` > 0, sem corte adicional na versão inicial. A população do setor aparece ao lado do indicador. Antes de propor qualquer corte, avaliar a sensibilidade do ranking a setores de população muito pequena. Dois rankings separados, sem pesos combinados.

## 12. Proposta curta: limiar de "atendido" (para aprovação; nenhum valor é adotado)

| Item | Proposta |
|---|---|
| Definição operacional de "atendido" | O ponto de origem do setor está a no máximo R metros, em linha reta, de uma parada que tem serviço programado no GTFS na janela escolhida |
| Modo considerado | Por modo (ônibus, metrô, trem) e "qualquer modo", reportados separadamente |
| Distância | Radial como base (decisão do professor). Rota pela rede de pedestres apenas em amostra, para qualificar o resultado, nunca como substituta silenciosa |
| Limiares candidatos | 400, 500, 800 e 1.000 m. Referências possíveis, a VERIFICAR nas fontes antes de citar: o indicador 11.2.1 dos ODS (ONU) usa 500 m para transporte de baixa capacidade e 1.000 m para alta capacidade. Fonte e redação exatas: Desconhecido nos materiais fornecidos |
| Serviço do GTFS | Uma parada só conta se tiver partidas programadas na janela (dia útil, faixa horária e número mínimo de partidas a decidir). Ressalva: o `stop_times.txt` do GTFS da SPTrans recebido tem apenas 99.120 linhas; se é um extrato reduzido, é Desconhecido nos materiais fornecidos, e isso afeta diretamente esta definição |
| Sensibilidade | Variar o limiar (os quatro candidatos), a velocidade de caminhada (3,6; 4,8; 5,4 km/h) e a janela de serviço; reportar quais setores mudam de categoria |
| Ressalva | Estar perto de uma parada não garante serviço adequado: não mede frequência real, lotação, confiabilidade, calçadas, declives, travessias, segurança nem acessibilidade |

Esta decisão não bloqueia a filtragem, a reprojeção e a validação básica dos dados do IBGE, já preparadas (seção 13).

## 13. Dados preparados (ambiente de revisão; NÃO aplicado ao repositório)

`src/data/prepare_ibge.py`: filtra `CD_MUN` = 3550308 (27.301 setores), preserva as colunas originais, reprojeta de EPSG:4674 para EPSG:31983 e grava em `data/processed/`. Não sobrescreve nem altera a entrada. Resultado verificado ao reler o arquivo: 27.301 linhas, EPSG:31983, `CD_SETOR` único, soma de `v0001` = 11.451.999. Geometrias: nenhuma vazia; 3 inválidas (autointersecção de anel), sem reparo aplicado, decisão de tratamento pendente.
