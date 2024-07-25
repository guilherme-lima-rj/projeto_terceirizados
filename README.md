# Projeto Terceirizados

## Visão Geral
Para esta demanda, foi solicitado, capturar, estruturar, armazenar e transformar dados de Terceirizados de Órgãos Federais, disponíveis no site Dados Abertos - [Terceirizados de Órgãos Federais](https://www.gov.br/cgu/pt-br/acesso-a-informacao/dados-abertos/arquivos/terceirizados).


Para isto, foi construído um pipeline que realiza a extração, processamento e transformação dos dados. Os dados de cada arquivo mensal, foram unificados em um único arquivo CSV (onde não foram impostas regras de estrutura para este arquivo). Após isto, os dados são carregados para uma tabela no Postgree. Por fim, uma tabela derivada foi criada usando o DBT. A tabela derivada deverá segue a padronização especificada no [manual de estilo do Escritorio de Dados](https://docs.dados.rio/guia-desenvolvedores/manual-estilo/#nome-e-ordem-das-colunas). A solução contempla o surgimento de novos dados a cada 4 meses.


## Desenvolvimento
O projeto foi desenvolvido em Python, na **versão 3.12.1**.

Para facilitar o entendimento e manutenção do código, ele foi dividido em 3 módulos:

* coleta
* trasformação
* carga

Para executar o módulo **coleta** dos arquivos no site, execute as linhas abaixo:

```bash
cd/coleta
scrapy crawl terceirizados
```

