Projeto de coleta de dados ENEM
===============================

Coletar os dados de algum ano do ENEM e realizar perguntas para esses dados. Após essas perguntas desenhar grafos em que seja possível responder as perguntas.

Primeiros passos
==============

Coletar os dados de 2011 no site do INEP: http://portal.inep.gov.br/basica-levantamentos-acessar

Link direto para o arquivo.zip: http://download.inep.gov.br/microdados/microdados_enem2011.zip (Para reproduzir essa análise é necessário baixar este arquivo no site do INEP)

Arquivo com ~6GB

Formato do arquivo do dados ENEM ano de 2011:

<pre>
<code>
   3000000000012011 2803548708SAO BERNARDO DO CAMPO                                                                                                                                       SP110000000000000000000011       .      .                                                                                                                                                                    ...3548708SAO BERNARDO DO CAMPO                                                                                                                                       SP1111   577.10   576.00   575.50   737.10CEBDCACBEAABBAABAEBDCAB      DCDEAAADCBBEBADDBEBECDDEECABABEBDDEBAEADCACABCBBECADDAADBADDAABABCAEEAEAEDDDAAEEBDECADCEABDDBAECAAABDAEBCCACBAECBAEBECC      AAEBABECECCDDAACDADADBACCBAADCAECCCEDD1241201251290CECDDACBCAEBEBBACEEDCAEBDAEDADBEBBDDADCBCBACDDEECEBABAADDEBAECDCACED      CBBEBCDCAADBADDDBAEACAEEDBDBDDCAEDDDACDEBBECAACDABADBAECCEADDCEBCBACBAEEBAEEECCEEEBCBECEBADCBDBEADCDBDCCCBADCAECCCCDDP         140.00   140.00   140.00   140.00    60.00   620.000 .       .      .
</code>
</pre>

**No arquivo de metadados (Dicionario_Microdados_ENEM_2011.xlsx) é colocado o início e fim das colunas para cada dado (arquivo posicional).**


Definir as Perguntas
==================

Após a coleta de forma manual tivemos que definir três perguntas para os dados:

**1. Dentre as área do conhecimento avaliadas no ENEM de 2011 qual teve a melhor média e qual teve a pior média?**

**2. Considerando que o ENEM é um exame para avaliar a qualidade do ensimo médio no país, realize um comparativo entre as notas dos inscritos que estudaram somente no ensino público e inscritos que estudaram somente em ensino particular e indique em porcentagem o quanto um sistema de ensino está melhor ou pior.**

**3. Faça uma relação em porcetagem dos pais que não estudaram, que estudaram o ensino médio e os que estudaram o ensino superior com as notas das provas dos inscritos.**


Análise dos dados em relação as perguntas:
==========================================

* Para responder a primeira pergunta é preciso conhecer as áreas de conhecimentos avaliadas no ENEM, realizar uma soma das notas para cada área e dividir pelo total de inscritos.

    * Áreas de conhecimentos avaliadas no ENEM:
        * Ciências Humanas (NU_NT_CH)
        * Ciências da Natureza (NU_NT_CN)
        * Linguagens e Códigos (NU_NT_LC)
        * Matemática (NU_NT_MT)

    **Dentre essas ainda existe a nota da redação: NU_NOTA_REDACAO**

* Para responder a segunda pergunta é necessário realizar a soma das notas dos inscritos que somente estudaram no ensino médio em escola pública e a soma das notas dos inscritos que estudaram somente em escola particular.

* É preciso pegar as notas dos inscritos em que os pais não estudaram, estudaram o ensino médio e os que estudaram ensino superiror.

* Todos os inscritos que não tem notas para as áreas avaliadas incluindo a redação foram excluídos dessa análise.

Problemas enfrentados para análise dos dados:
============================================

Nos dados do ENEM para 2011 existe o arquivo de dados DADOS_ENEM_2011.txt com 5.380.856 linhas e o arquivo de questionário sócio econômico (QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011.txt) contém 5.366.948 linhas.

Para nossa análise consideramos a quantidade de inscritos informado no arquivo de questionário sócio econômico, portanto estamos avaliando **5.366.948** inscritos no exame de 2011.

Removendo da análise os inscritos que não tiveram notas(possivelmente inscritos que não realizaram a prova), obtemos para análise uma somatória de **3.670.089** (base de cálculo para as médias apresentadas).

Do total de inscritos no ano de 2011 apenas 68.38316674579295% contém notas.

Ferramentas para análise:
========================

Realizamos um teste de benchmark entre uma linguagem de mais baixo nível com uma linguagem de mais alto nível, são elas C e Python, respectivamente:

Esse teste tinha como base avaliar o tempo que o C e o Python gastam para ler um arquivo de ~6 milhoes de linhas.

* **Python 2.745 min**
* **C 2.598 min**

Considerando a facilidade de implementação descartamos o uso de C para essa avaliação, com a justificativa que a melhoria no tempo de leitura do arquivo não era tão significativa quanto a facilidade da linguagem Python para a implementação.

Também descartarmos o uso de qualquer framework ou base de dados, já que acretidamos que um arquivo que demora ~3 min para ser lido em uma máquina caseira/notebook não se enquadra no proposito da maioria desses frameworks.

Considerando os itens acima, utilizamos apenas 2 scripts Python que chamamos de **transform.py** e **analysis.py** para respondermos as perguntas.

Respostas para as perguntas de forma textual:
===========================================

**Pergunta 1:**
   Resultado para a soma das notas por área do conhecimento dos **3.670.089** inscritos analisados:
   
      * Ciências Humanas: 1.724.870.640,95/3.670.089 = 469,9806 
      * Ciências da Natureza: 1.768.483.998,42/3.670.089 = 481,8640
      * Linguagens e Códigos: 1.925.997.050,21/3.670.089 = 524,7821 
      * Matemática: 1.913.624.930,41/3.670.089 = 521,4110
      * Redação 2.000.938.702,0/3.670.089 = 545,2016
   
   De forma simples e objetiva conseguimos afirmar que a pior área foi ``Ciências Humanas`` e que a melhor foi ``Linguagens e Códigos``
   
   *Observando a média da redação verificamos que é uma nota bastante significativa.*

**Pergunta 2:** 
   Para responder essa pergunta decidimos fazer uma soma das notas de todas as área do conhecimento dividido pela quantidade de inscritos. Lembrando que estamos avaliando inscritos que cursaram somente escola pública e particular durante todo o ensino médio:
   
   * Para inscritos de escola pública
      * Quantidade de inscritos que estudaram somente em escola pública durante todo o ensino médio: 2.831.627 (realizaram o ENEM)
      * Somatório das notas das provas de todas as área: 697.7261.965,37
      * Média da nota para os inscritos da escola pública por prova: 492,809396532
      * Média para as 5 área do conehcimento: 2.464,04698266
   
   * Para inscritos de escola privada:
      * Quantidade de inscritos que estudaram somente em escola privada durante todo o ensino médio: 609.235 (realizaram o ENEM)
      * Somatório das notas das provas de todas as área: 1.766.473.618,72
      * Média da nota para os inscritos da escola pública por prova: 579,898928565
      * Média para as 5 área do conehcimento: 2.899,49464282
   
Verificamos dessa forma que o ensino privado teve um aproveitamento maior que o ensino público em: 17,65422077922078%

Verificamos também que os inscritos são em sua maioria provinientes do ensino público.

**Pergunta 3:**
   Para responder essa pergunta realizamos o mesmo procedimento da segunda pergunta, soma das notas de todas as área do conhecimento dividido pela quantidade de inscritos. 
   
   * Para inscritos em que os pais não estudaram:
      * Quantidade de inscritos: 262,862
      * Somatório das notas das provas de todas as área: 612.914.247,3
      * Média da nota para os inscritos por prova: **466,339179722**
      * Média da nota para as 5 área do conhecimento: 2.331,69589861
      
   
   * Para inscritos em que os pais estudaram o ensino médio:
      * Quantidade de inscritos: 714,933
      * Somatório das notas das provas de todas as área: 187.6766.310,7
      * Média da nota para os inscritos por prova: **525,018794964**
      * Média da nota para as 5 área do conhecimento: 2.625,09397482

   
   * Para inscritos em que os pais estudaram o ensino superior: 
      * Quantidade de inscritos: 271,371
      * Somatório das notas das provas de todas as área: 781.606.770,2
      * Média da nota para os inscritos por prova: **576,042959786**
      * Média da nota para as 5 área do conhecimento: 2.880,21479893
   
   Concluímos que a escolaridade dos pais esta diretamente porporcional a média da nota dos inscritos no ENEM para o ano de 2011.
   

Resposta para as perguntas em grafos:
===================================

Para responder as questões em grafos encontramos dificuldades, pois as perguntas utilizam médias que é uma informação não encontrada nos dados, portanto tivemos que computar essa métrica e depois pensarmos em gerar grafos para responder as perguntas:


**Grafo para pergunta 1:**

![question1](https://raw.githubusercontent.com/jamilatta/sandbox/master/posgraduacao/coletadedados/projeto_integracao/question1.png)

**Grafo para pergunta 2:**

![question2](https://raw.githubusercontent.com/jamilatta/sandbox/master/posgraduacao/coletadedados/projeto_integracao/question2.png)

**Grafo para pergunta 3:**

![question3](https://raw.githubusercontent.com/jamilatta/sandbox/master/posgraduacao/coletadedados/projeto_integracao/question3.png)

Conclusões:
==========

* Quanto maior a quantidade de dados mais complicado para analisar;
* Quanto maior a quantidade de dados maior a capacidade de variação e inconsistências;
* Mesmo com o dicionário de dados (metadados) ainda é possível que ocorra uma intepretação errada do que é cada dado;
* O uso do grafo é possível para os dados, se somente se, os dados contém o item a ser utilizado no grafo;
* Para o uso de uma base da dados e/ou um framework é importante que a dimensão do problema justifique a utilização.










