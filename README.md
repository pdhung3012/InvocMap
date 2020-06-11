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


# Instruction for Replication:

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

```python language_model_training.py --cuda --batch_size=32 --lr=0.01 --reduce_rate=0.9 --save='/ag_lm_model/'' ```

Next, You can run 3 following configurations:
- For supervised classification, run:

```python classifier_training.py --cuda --lr=0.001 --batch_size=128 --save='/classify_no_pre/' --pre_train='' --number_per_class=1000 --reduce_rate=0.95```

- For original semi supervised classification, run:

```python classifier_training.py --cuda --lr=0.001 --batch_size=128 --save='/classify_with_pre/' --pre_train='/ag_lm_model' --number_per_class=1000 --reduce_rate=0.95```

- For GAN semi supervised classification, run:

```python Adversarial_training.py --cuda --lr=0.001 --batch_size=128 --save='/ag_adv_model/' --pre_train='/ag_lm_model' --number_per_class=1000 --reduce_rate=0.95```

You will see the detail...txt as the output prediction.


**RQ4. **

- For RQ 4.1:

```python evaluateRQ4-1.py```

Output: the tuning result on classification of 'talendesb' system.

- For RQ 4.2:

```python evaluateRQ4-2.py```

Output: the tuning result on regression of 'talendesb' system.
