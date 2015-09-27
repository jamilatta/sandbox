Projeto de coleta de dados ENEM
===============================

Coletar os dados de 2011 no site do ENEM

Arquivo com ~6GB

Formato do arquivo do ENEM ano de 2011:

<pre>
<code>
3000000000012011 2803548708SAO BERNARDO DO CAMPO                                                                                                                                       SP110000000000000000000011       .      .                                                                                                                                                                    ...3548708SAO BERNARDO DO CAMPO                                                                                                                                       SP1111   577.10   576.00   575.50   737.10CEBDCACBEAABBAABAEBDCAB      DCDEAAADCBBEBADDBEBECDDEECABABEBDDEBAEADCACABCBBECADDAADBADDAABABCAEEAEAEDDDAAEEBDECADCEABDDBAECAAABDAEBCCACBAECBAEBECC      AAEBABECECCDDAACDADADBACCBAADCAECCCEDD1241201251290CECDDACBCAEBEBBACEEDCAEBDAEDADBEBBDDADCBCBACDDEECEBABAADDEBAECDCACED      CBBEBCDCAADBADDDBAEACAEEDBDBDDCAEDDDACDEBBECAACDABADBAECCEADDCEBCBACBAEEBAEEECCEEEBCBECEBADCBDBEADCDBDCCCBADCAECCCCDDP         140.00   140.00   140.00   140.00    60.00   620.000 .       .      .
</code>
</pre>

**No arquivo de metadados é colocado o início e fim das colunas para cada dado**

Perguntas
=========

Após a coleta de forma manual tivemos que definir três perguntas para o dados, segue:

*1. Dentre as área do conhecimento avaliadas no ENEM de 2011 qual teve a melhor média e qual teve a pior média?*

*2. Considerando que o ENEM é um exame para avaliar a qualidade do ensimo médio no país, realize um comparativo entre as notas dos alunos que estudaram somente no ensino público e alunos que estudaram somente em ensino particular e indique em porcentagem o quanto um sistema de ensino está melhor ou pior.*

*3. Faça uma relação em porcetagem dos pais que não estudaram, que estudaram o ensino médio e os que estudaram o ensino superior com as notas das provas dos inscritos*


Analise dos dados em relação as perguntas:
==========================================

* Para responder essa pergunta é preciso conhecer as área do conhecimento avaliadas no ENEM, realizar uma soma das notas para cada área e dividir pelo total de inscritos.

    * Áreas do conhecimento avaliadas no ENEM:
        * Ciências Humanas e suas Tecnologias (NU_NT_CN)
        * Ciências da Natureza e suas Tecnologias (NU_NT_CH)
        * Linguagens, Códigos e suas Tecnologias e Redação (NU_NT_LC)
        * Matemática e suas Tecnologias. (NU_NT_MT)

    **Dentre essas ainda existe a nota da redação: NU_NOTA_REDACAO**

* Para responder a segunda pergunta é necessário realizar a soma das notas dos alunos que somente estudaram no ensino médio em escola pública e a soma das notas dos alunos que estudaram somente e escola particular.

* É preciso pegar as notas dos incritos em que os pais não estudaram, estudaram o ensino médio e o ensino superiror.

Problemas enfrentados para analise dos dados:
============================================

Nos dados do ENEM para 2011 existe o arquivo de dados DADOS_ENEM_2011.txt com 5.380.856 linhas e o arquivo de questionário sócio econômico (QUESTIONARIO_SOCIO_ECONOMICO_ENEM_2011.txt) comtém 5.366.948 linhas o que demostrando inconsistências.

Para nossa analise consideramos a quantidade de inscritos declarado no arquivo de questionário sócio econômico.

**Portanto estamos avaliando 5.366.948 inscritos no exame de 2011.**


Ferramentas para analise:
========================

Realizamos um teste de benchmarch entre uma linguagem de mais baixo nível com uma linguagem de mais alto nível, são elas C e Python, respectivamente:

Esse teste tinha como base avaliar o tempo que o C e o python gasta para ler um arquivo de ~6 milhoes de linhas.

* **Python 2.745 min**
* **C 2.598 min**

Considerando a facilidade de implementação descartamos o uso de C para essa avaliação, com a justificativa que a melhoria no tempo de leitura arquivo não era tão significativa quanto a facilidade da linguagem Python para a implementação.

Também diescartamos o uso de qualquer framework ou base de dados, já que acretidamos que uma arquivo que demora ~3min para ser lido em uma máquina caseira/notebook não se enquadra no proposito da maioria desses frameworks.

Resposta para as perguntas de forma textual:
===========================================

Resposta para as perguntas em grafo:
===================================

Para responder as perguntas em grafo encontramos uma dificuldade, pois a 1 e 2 pergunta utiliza média que é um dado que não está nos dados portanto tivemos que computar essa métrica e depois pensarmos em gerar um grafo para responder a pergunta, segue:


Grafo para pergunta 1:


Grafo para pergunta 2:


Grafo para pergunta 3:














