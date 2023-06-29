# Tools Setup Workflow

Este repositório contém um exemplo de workflow do GitHub Actions para configurar ferramentas e realizar implantações de acordo com o fluxo de trabalho GitFlow.

## Descrição

O workflow consiste em dois jobs: `tool-setup` e `tool-test`. O job `tool-setup` é acionado em eventos de push nas branches `development` e `master`, bem como em revisões de pull request aprovadas. Ele é responsável por configurar as ferramentas necessárias, instalar as dependências do projeto e realizar implantações de acordo com as branches especificadas.

O passo de implantação é executado com base na branch em que ocorreu o push ou na revisão de pull request aprovada. Se o push ocorrer na branch `development`, será feita uma implantação no ambiente de UAT (User Acceptance Testing) usando a variável de conexão `UAT_CONNECTION_STRING`. Se o push ocorrer na branch `master`, será feita uma implantação no ambiente de produção usando a variável de conexão `PROD_CONNECTION_STRING`.

Além disso, o job `tool-test` é acionado em eventos de push nas branches `development` e `master` para executar os testes do projeto.

## Utilização

Siga as etapas abaixo para utilizar este workflow no seu projeto:

1. Faça um fork deste repositório.

2. No arquivo `.github/workflows/main.yml`, você pode ajustar as branches que devem acionar o workflow na seção `on`. Por padrão, o workflow é acionado em eventos de push nas branches `development` e `master`, bem como em revisões de pull request aprovadas.

3. No arquivo `.github/workflows/main.yml`, ajuste as variáveis de ambiente (`DEV_CONNECTION_STRING`, `UAT_CONNECTION_STRING` e `PROD_CONNECTION_STRING`) de acordo com suas necessidades. Essas variáveis são usadas durante a implantação para estabelecer a conexão com os ambientes.

4. No arquivo `hello_world.py`, personalize a lógica de implantação para atender às suas necessidades específicas. O exemplo atual imprime mensagens diferentes com base na branch em que ocorreu o push.

5. Realize commits no seu fork para disparar o workflow ou acione manualmente o workflow na página do seu repositório no GitHub, selecionando a aba "Actions" e clicando no botão "Run workflow".

Após essas etapas, o workflow será executado de acordo com as configurações especificadas, configurando as ferramentas, instalando as dependências, realizando implantações e executando testes conforme necessário para cada branch.
