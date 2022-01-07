# An Intro About Credit Score Modeling

Frase de efeito

---

###### "Credit scoring models are statistical analysis used by credit bureaus that evaluate your worthiness to receive credit. The agencies select statistical characteristics found in a person’s credit payment patterns, analyze them and come up with a credit score."

![credit_score](https://user-images.githubusercontent.com/49340230/142535917-f487ed71-d3a5-4fb2-b781-73070c41d685.jpg)

Topics:

1. Concepts - Credit Risk, Default Event and Credit Scoring
2. Reasons  - Why are they important ?
3. Modeling - How financial institutions actually measure it ?

--- 

1. Credit Risk, Default Event and Credit Scoring.

Sometimes, given a variety of reasons, people need to borrow credit from a **lender**. Then the most common type of loan provided by lenders to **borrowers** is *money*. Figure bellow illustrates it.


![BorrowerVsLender](https://user-images.githubusercontent.com/49340230/142517582-1af53d4e-09f6-4598-9d66-6aa30bbddf7a.png)


Not just money, but also very common types of credit:
- *Credit Cards*;
- *Home Ownership Loans*;
- *Asset Financing* (NOTE: firms use it to obtain the equipament they need).

Considering this context, every credit operation carries a risk associated. This is commonly know as **credit risk**. In summary, credit risk is defined as the *likelihood* that a **borrower** would NOT repay their **loan** to the **lender**. Finally, the scenario where the borrower, in fact, do not full repay his debts leads to the **default event**.  

![debt](https://user-images.githubusercontent.com/49340230/142524761-9e36b6ad-732e-47a9-bbff-93b8dec7926c.png)

Formally speaking, default event means the probability of a borrower not being able to repay their debt. 

**Credit scoring**, similarly, is the method used by the financial institutions to evaluate the *credit worthiness* of their clients. It's highly related to the credit risk. It analytically quantifies the default, associated with credit requests, by questions in the application form, e.g., *present salary*, *number of dependents*, and *time at current address*. Usually, a credit score is a number that quantifies the creditworthiness of a person;

![numbers](https://user-images.githubusercontent.com/49340230/142539355-a9863a49-0100-4176-8efd-4d52b60fb59e.jpg)


In Brazil, an example of financial institutions which acts quantifying the creditworthiness of a specific person is *Serasa*. It provides credit protection service with consumer default and default reports for **credit decision purposes**.

In summary, the risk of default has motivated lenders to use a credit scoring system that helps them make more efficient decisions about who is able to receive credit by analyzing the credit risk. 

---

1. Why are they important ?

When dealing with banking and finance, these topics are among the most importants because the inability or failure to estimate borrowers probability of default can have grave consequences for lends and society in general. Then lenders must assess credit risk asssociated with each borrower vey well and generally they require collaterals to increase the price of lending the funds.

To illustrate an example of grave consequences as mentioned above, let's go back in the year 2008 when occured one of the greatest jolt to the global financial system in almost a century. So what caused the 2008 financial crash ? It is highly related to the availability of cheap credit context and lack of appropriate credit risk analysis. In practice, low-interest rates and low lending standards fueled a housing price bubble and encouraged millions to borrow beyond their means to buy homes they couldn't afford.

![2008](https://user-images.githubusercontent.com/49340230/142551100-f37852cc-376f-4721-904e-cb5404457b0f.jpg)


The consequences ? More than 500 banks failed between 2008 and 2015. Like only a few others in history, it grew big enough that, when it burst, it damaged entire economies and hurt millions of people, including many who were not speculating in mortgage-backed securities.

Figura de desastre aqui se pá.

These informations were extracted from:

https://www.investopedia.com/articles/economics/09/financial-crisis-review.asp
https://www.historyextra.com/period/modern/financial-crisis-crash-explained-facts-causes/#:~:text=This%20was%20caused%20by%20rising,the%20rate%20of%20global%20inflation.&text=%E2%80%9CThis%20development%20squeezed%20borrowers%2C%20many,held%20by%20many%20financial%20institutions.
https://ajuda.serasa.com.br/hc/pt-br/articles/360059389312-BUREAU-DE-CR%C3%89DITO#:~:text=Servi%C3%A7o%20de%20prote%C3%A7%C3%A3o%20ao%20cr%C3%A9dito,de%20cr%C3%A9dito%20da%20Am%C3%A9rica%20Latina.

https://www.debt.org/credit/report/scoring-models/

https://www.bangkokpost.com/business/1540406/commemorating-the-global-financial-meltdown

Figuras:
noun_project.

Papers:
- The application of machine learning and artificial intelligence in credit risk assessment
- An Ontology-Based Model for Credit Scoring Knowledge in Microfinance: Towards a Better Decision Making
- Credit scoring for microfinance: is it worth it?
- Credit scoring in banks and financial institutions via data mining techniques: A literature review

Cursos:

- FGV: Análise Introdutória de Crédito e Risco de Crédito;
- Udemy: Credit Risk Modeling with Python;

In summary, the credit risk assessment helps to prevent financial disaster in society, keeping the stability of the economic system healthy.


----

1. How financial institutions actually measure it (Credit Scoring Modeling)?

Quem nunca recebeu emails do tipo "Aproveite seu crédito pré-aprovado para financiar seu próximo carro" ou "Nós aumentamos o seu limite de crédito pré-aprovado"?
O que chama atenção, neste ponto, é que, nos tempo atuais, na maioria das vezes, já temos crédito pré-aprovados em determinadas instituições financeiras. Em tempos anteriores, o cliente haveria de solicitar crédito junto a instituição financeira de interesse, e passar por uma triagem de burocracias até, finalmente, obter o crédito solicitado.

Considerando o contexto acima, as grandes instituições financeiras conseguem fazer a pré-aprovação de crédito para clientes de sua base através do uso de modelos estatísticos que consomem grandes volumes de dados (Big Data). De maneira geral, a modelagem de credit score faz uso de técnicas de Análise Estatística e de modelos baseados em Inteligência Artificial. A seguir são ilustrados exemplos de dados utilizados pelos bancos para inferência de credit score.

IMAGEM COM EXEMPLOS DE INFORMAÇÕES DEMOGRÁFICAS E INFORMAÇÕES DE MOVIMENTAÇÃO BANCÁRIA.


Para ilustrar o uso desses dados em modelagem de credit score, foi implementado um projeto completo para fazer a inferência de credit score de maneira explicável ao cliente, ou seja, de modo que ele entenda exatamente o score que possui. Para isso, o projeto conta com o uso de modelos baseados em Inteligência Artificial (i) em conjuntos com Métodos Estatísticos (ii). Com apenas esses dois ingredientes, surgem grandes poderes. 

IMAGEM ENGRAÇADA AQUI.

Para conhecer esse projeto incrível, navegue para a próxima seção clicando aqui. 



** VERIFICAR SE OS ITENS ABAIXO SERÃO INCLUÍDOS NESSE PONTO.


The credit score measurement processing can be splitted in the following parts:

- Client Information Acquirement and Verification;
- Client Credit Risk Assessment
- Estruturação e decisão da operação;
- Client Credit Monitoring
- Payments;

Informações necessárias para solicitação de crédito:

- Dados do conjugê;
- Bens patrimoniais;
- Restrições financeiras (SPC, Serasa);
- Movimentação da conta corrente;
- Perguntas tais como: "Por qual razão deseja o crédito/produto?"

Síntese das informações sobre Análise de Crédito:

Divide-se em:

- Ficha cadastral;
- Restrições Financeiras;
- Entrevistas;
- Histórico do Cliente;
- Fluxo de Conta Corrente;
- Proposta de Negócios;
- Demonstrativos Financeiros;


----------------------------------------------------------

About Expected Loss and its components: PD, LGP and EAD

** Types of  factors for expected loss

-- Borrower-specific factors
-- The economic environment

Definition of Expected credit loss: the amount a lender might lose by lending to a borrower.

EL = PD (probability of default) x LGD (loss given default) x EAD (exposure at default)


** Probability of default (PD)
- The borrowers inability to repay their debt in full or on time.

** Loss given default (LGD)
- Is the share of an asset that is lost if a borrower defaults. The proportion of the total exposure that cannot be recovered by the lender once a default has occurred.

** Exposure at default (EAD)
- The total value that a lender is exposed to when a borrower defaults.


** Unexpected losses: result of adverse economic circumstances.


-----------------------------------------------------------

Capital Adequacy, Regulations, and the Basel II Accord.

- In order to prevent financial disaster in society, Governmnet regulators imposed certain requirements on banks to make sure that banks conduct their business without risking the stability of the economic system.

** Regulators rules:
	-- Regulate bank operations and hence reduce risky behavior.
	-- Guarantee to the public that the banking system is in good health. 
- The bank must have sufficient capital in order to absorve some defaults. In other words, Capital Requirement (capital adequacy or regulatory capital).


Credit Scoring serves as a model of financial behavior and is traditionally calculated from the user's past financial history.

1. **Understanding** the Credit Scoring Process;


#### Implemented by Tiago Sá



##### PARA USAR OU DESCARTAR

 Credit scoring is the method used by the financial institutions to  evaluate the credit  worthiness of  their clients. It’s strongly related to the credit risk. To be more com-petitive, and in order to reduce the credit risk, financial institu-tions are obliged to adopt a foolproof scoring system. This client assessment is based on several factors.
 
 
 
 O risco de inadimplência motivou os credores a usar um sistema de pontuação de crédito, também chamado de Credit Score, que os ajuda a tomar decisões mais eficientes sobre a quem conceder crédito. Credit Scoring serve como um modelo de comportamento financeiro e são tradicionalmente calculadas a partir do histórico financeiro anterior do usuário. 
 
 
 “O termo Credit Score é usado para descrever o processo de avaliação do risco e inadimplência de um cliente em uma obrigação financeira” (Hand & Henley, 1997)