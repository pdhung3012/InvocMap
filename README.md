# Realizing Literate Programming using Neural Embedding and Machine Translation
Different from existing related works and other code suggestion tools such as AnyCode which only considered the given natural language description as input, we analyze the input from two different sources, i.e. NL description and its surrounding context.
InvocMap proposes a semi-supervised approach based on three major modules.
First, it uses unsupervised Neural Embedding to handle NL description of MIs to a list of possible method names.
Contrary to expensive supervised machine learning methods that require a big dataset of the parallel corpus with NL and programming language.
Second, Machine Translation models trained from large scale code corpus to learn the structure of MIs, given a list of method names and surrounding code context.
Third, a program analysis method that assigns local variables to structure of MIs to get the final code.
InvocMap operates in two modes of input for describing MIs for developers, from method names directly, and from natural language description.
By evaluation on data from 1000 high-quality Java projects, we got the precision as up to 89\% for MI suggestion from method names, and over 60\% for MI suggestion from NL description, which outperforms the prior work and shows the potential of our approach for realizing LP.

# Requirements:
- Python 3.6.
- PyCharm.
- Gensim 3.8.0.
- Phrasal 3.6.0.
- Eclipse IDE with JDK>=11.


# Instruction for Replication of Evaluation:

We put all of our code, data and result inside replicationPackage folder. This folder has following items:

- code: the code for Neural Embedding (NE), Machine Translation (MT) and evaluation.
- result: expected results for Research Question 1-4 (you can generate the results by yourselves if you run the python code inside the replicationPackage folder.
- data: All pretrained data for NE and MT.
- replicate: You can put data for replications in this folder.

We set the default of any result you generate at the 'replicate' folder. However, you can go to the code and change the default paths to your expected locations.

Before running experiments, make sure that you imported IMJava successfully in Eclipse and IMPython in PyCharm,
Change locations in '/IMJava/src/constanct/PathConstanct.java' to the locations inside your 'replicate' folder, depending on RQs.


**RQ2. What is the accuracy of Neural Embedding for suggesting core method names from natural language and surrounding code?**

To run for a combined model:
- Extract all contents inside root folder of "replicationPackages/result/RQ4/steps/all_steps_data.zip" to "replicate" folder
- Extract "replicationPackages/result/RQ2/cmnInfer_combine" to "replicate" folder.
- In file LiterateProgrammingEvaluation.java, change value of "fopInputMnames" in line 21 to the folder you extracted above.
- set PathConstanct.PathLiterateProgrammingCorpus to location of "replicate" folder.
- Run:
```java LiterateProgrammingEvaluation.java```

- Output: See the accuracy in the 'replicate/accuracy/identifyMethodNames.txt', the last line is the total accuracy.
- You can run with prefix or postfix model similarity.

**RQ3. What is the accuracy of Machine Translation model for inferring SASTs from CMNs?**
- Download and extract the MT parallel corpuses at the link inside data folder
- Select your MT corpus and set its location in PathMachineTranslationCorpus.
- Extract the testing data as one of zip files in /results/RQ3 folders to your select MT corpus's folder.
- Change your PathMachineTranslationEvalOutput to location 'replicate' folder.
- Run:
```java MachineTranslationEvaluation.java```
- You should see the output in 'replicate' folder.


**RQ4. What is the overall accuracy of InvocMap model for realizing Literate Programming?**
- Extract all contents inside root folder of "replicationPackages/result/RQ4/steps/all_steps_data.zip" to "replicate" folder
- Change your PathLiterateProgrammingEvaluationOutput to location of 'replicate' folder.
- Change your PathLiterateProgrammingCorpus to location of 'all_steps_data' folder.
- Run:
```java LiterateProgrammingEvaluation.java```
- You should see the evaluation at the 'replicate' folder. Translated results for each LPCSs is shown in step7 folder of 'all_steps_data' folder.

# Instruction for Replication of Process from Literate Programming Code Snippets to Final Code:
- Extract all contents inside root folder of "replicationPackages/result/RQ4/steps/all_steps_data.zip" to "replicate" folder
- Change your PathLiterateProgrammingExpReplication to location of 'all_steps_data' folder.
- Select your MT corpus and set its location in PathMachineTranslationCorpus.
From now, run the following steps:

**Tokenization**

1) To parse code with NL to generate tokens, run:
```java TokensExtractionFromLPCodeTree.java```

2) To split precode, postcode and integrate NL information, run:
```java PrePostCodeAndNLTokensAllocation.java```

**Neural Embedding**

3) Change the locations of Doc2Vec models to folder of Doc2Vec you got from the data, before run this Python file:
```python GenerateCMNByCombinationModel.py```
You should get the generated CMNs in step2 folder.

**Machine Translation**

4) To integrate CMNs to precode, postcode and NL, run:
```java TranslationInputPreparation.java```

5) Take input inside step3_inputSequence and run the MT model to get trans.txt file. Then, you put this file to step4_trans folder.

6) To split translation results to be corresponding with each LPCSs, run:
```java TranslationOutputSplitByInputNL.java```

7) To reorder the translated results, run:
```java TranslationOutputReordering.java```

8) To find the SAST related as the translated results of CMNs, run:
```java TranslationOutputMIAllocation.java```

**Program Analysis and Ranking Candidates**

9) To assign variables to SASTs and rank results, run:
```java MICandidateGenerationAndRanking.java```

You should see the final output in 'step7' folder.
