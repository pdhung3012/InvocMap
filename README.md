# Realizing Literate Programming using Neural Embedding and Machine Translation
Different from existing related works and other code suggestion tools such as AnyCode which only considered the given natural language description as input, we analyze the input from two different sources, i.e. NL description and its surrounding context. 
InvocMap proposes a semi-supervised approach based on three major modules. 
First, it uses unsupervised Neural Embedding to handle NL description of MIs to a list of possible method names. 
Contrary to expensive supervised machine learning methods that require a big dataset of the parallel corpus with NL and programming language.
Second, Machine Translation models trained from large scale code corpus to learn the structure of MIs, given a list of method names and surrounding code context. 
Third, a program analysis method that assigns local variables to structure of MIs to get the final code. 
InvocMap operates in two modes of input for describing MIs for developers, from method names directly, and from natural language description. 
By evaluation on data from 1000 high-quality Java projects, we got the precision as up to 89\% for MI suggestion from method names, and over 60\% for MI suggestion from NL description, which outperforms the prior work and shows the potential of our approach for realizing LP.
**Authors: Hung Phan, Eliska Kloberdanz, Jeremiah Roghair** from Department of Computer Science, Iowa State University, USA.

This is the research project in the course Advance in Software Engineering - COMS 665 (Spring 2020) - Iowa State University, USA.

# Requirements:
- Python 3.6.
- Scikit-learn 0.22.2.
- Keras 2.2.5.
- PyTorch 1.5.
- TensorFlow 2.0.

# Instruction for Replication:

We put all of our code, data and result inside replicationPackage folder. This folder has following items:

- preprocessCode: the code for vectorizing software features of TSE 2018 dataset.
- expectedResults: expected results for Research Question 1-4 (you can generate the results by yourselves if you run the python code inside the replicationPackage folder.
- data: Including dataset From TSE 2018 paper, 50000 story text for training Doc2Vec, pretrainedVector in 5 vectorization techniques.
- RQ3: all of the code for running semi supervised learning. We inherit and update the code from this paper: https://github.com/yanlirock/RLANS
- Other python codes: code for running machine learning experiments.

We set the default of any result you generate at the 'result' folder. However, you can go to the code and change the default paths to your expected locations.

The following code will run for evaluating story points by Machine Learning algorithms on our pretrained vectors. If you want to generate the vector by yourselves, please run each files in the preprocessCode folder.

**RQ1. **

```python evaluateRQ1.py```

- Input: the default is the path 'replicationPackage/data/pretrainedVector/TFIDF4/' (you can go to the code and change paths for other vectorization models)
- Output: the accuracy of each systems in 10 ML Classification algorithms. You can see the best accuracy on each systems along with the details prediction in 'details/' folder.


**RQ2. **

To run for all systems:

```python: evaluateRQ2AllSystems.py```

- Input: the default is the path 'replicationPackage/data/pretrainedVector/TFIDF4/' (you can go to the code and change paths for other vectorization models)
- Output: the accuracy of each systems in 7 ML Regression algorithms. You can see the best accuracy on each systems along with the details prediction in 'details/' folder.

If you want to run on a specific system such as Moodle, run: 

```python evaluateRQ2Moodle.py```

**RQ3. **

- Go inside the RQ3 sub-folder.

First, you need to run the language model creation for unlabeled data:

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

