# Learn ML: 90-Day Python and Machine Learning Roadmap

This repository is a practical learning track for going from beginner Python to
small machine learning projects. It is organized as daily practice files, with
mini-projects every 10 days so you can turn concepts into working programs.

The goal is not to memorize theory first. The goal is to code every day, learn
the math when it becomes useful, and build a portfolio of small projects that
show real progress.

## Repository Structure

```text
learn ml/
+-- roadmap/          # 90-day learning path and milestone projects
+-- python_basics/    # beginner Python practice
+-- data_tools/       # NumPy, pandas, plotting, and data analysis practice
+-- ml_projects/      # machine learning experiments and project work
+-- datasets/         # local datasets for practice
+-- ml.py             # earlier scratch/history file
+-- rough.py          # quick experiments
+-- students.csv      # sample student data
```

## Roadmap

| Days | Focus | What You Build |
| --- | --- | --- |
| 001-015 | Practical Python | dictionaries, strings, functions, errors, files, CSV, modules, OOP basics |
| 016-030 | Data Tools | NumPy arrays, filtering, simulation, pandas, cleaning, groupby, charts, statistics |
| 031-045 | ML Foundations | train/test split, first scikit-learn model, regression, classification, metrics, CV |
| 046-060 | Supervised ML | linear/logistic regression, KNN, trees, forests, boosting, SVM, Naive Bayes, tuning |
| 061-070 | Unsupervised ML | clustering, PCA, anomaly detection, features, leakage, reproducible experiments |
| 071-080 | Neural Network Basics | perceptrons, gradient descent, MLPs, computer vision basics, NLP, recommendations |
| 081-090 | Portfolio and Deployment | final projects, EDA, modeling, evaluation, polish, simple deployment |

## Milestone Projects

| File | Project | Main Skills |
| --- | --- | --- |
| `roadmap/day_10_student_performance_tracker.py` | Student Performance Tracker | dictionaries, CSV, validation, averages, grades |
| `roadmap/day_20_smart_sales_analyzer copy.py` | Smart Sales Analyzer | NumPy, boolean masks, simulations, reusable functions/classes |
| `roadmap/day_30_customer_order_eda.py` | Customer Order EDA | pandas, cleaning, groupby, visualization, insights |
| `roadmap/day_40_flower_species_predictor.py` | Flower Species Predictor | classification, train/test split, metrics, cross-validation |
| `roadmap/day_50_house_price_model_lab.py` | House Price Model Lab | preprocessing, pipelines, feature engineering, model comparison |
| `roadmap/day_60_loan_risk_model_pack.py` | Loan Risk Model Pack | stronger classifiers, imbalance, tuning, saving models |
| `roadmap/day_70_customer_segment_finder.py` | Customer Segment Finder | clustering, PCA, anomaly detection, segment explanation |
| `roadmap/day_80_hybrid_recommendation_demo.py` | Hybrid Recommendation Demo | recommendation systems and neural-network review |
| `roadmap/day_90_portfolio_model_demo.py` | Portfolio Model Demo | final reusable ML demo and portfolio summary |

## How To Use This Repo

1. Start with `roadmap/START_HERE.py`.
2. Open the matching daily file, for example `roadmap/day-001.py`.
3. Read the comments at the top of the file.
4. Code the practice task under `# Code here`.
5. Run the file from the terminal.
6. Write a short note in the file about what you learned.
7. Every 10 days, complete the matching mini-project.

Example:

```bash
python roadmap/day-010.py
```

Some files use local data files, so run them from the repository root unless a
file says otherwise.

## Suggested Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install common packages when you reach the data and ML sections:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn joblib
```

Useful optional tools:

```bash
pip install jupyter ipykernel
```

## Math Required For This Roadmap

You do not need advanced math to begin. Learn enough math to understand what the
code is doing, then revisit deeper topics as the projects get harder.

### 1. Arithmetic and Algebra

Needed for: all Python logic, averages, formulas, feature engineering.

Know:
- variables and formulas
- percentages and ratios
- exponents and square roots
- solving simple equations
- reading charts and tables

Practice in this repo:
- student averages and grades
- sales totals and above-average days
- house-price feature engineering

### 2. Descriptive Statistics

Needed for: pandas, EDA, model evaluation.

Know:
- mean, median, mode
- variance and standard deviation
- percentiles and outliers
- correlation
- distributions and histograms

Practice in this repo:
- `roadmap/day-029.py`
- `roadmap/day_30_customer_order_eda.py`
- regression and classification metrics

### 3. Probability

Needed for: train/test thinking, uncertainty, Naive Bayes, classification.

Know:
- probability basics
- conditional probability
- independent vs dependent events
- random variables
- simple sampling
- confusion matrix intuition

Practice in this repo:
- NumPy random simulations
- classification metrics
- Naive Bayes
- imbalanced loan-risk modeling

### 4. Linear Algebra

Needed for: NumPy, scikit-learn, PCA, neural networks.

Know:
- vectors
- matrices
- dot product
- matrix multiplication intuition
- dimensions and shapes
- linear combinations
- eigenvectors at a high level for PCA

Practice in this repo:
- NumPy arrays and vectorized operations
- feature matrices in scikit-learn
- PCA visualization
- neural-network inputs and weights

### 5. Calculus

Needed for: gradient descent, neural networks, model optimization.

Know:
- slope and rate of change
- derivatives as "how much output changes"
- partial derivatives at an intuitive level
- gradient descent intuition
- loss curves

Practice in this repo:
- loss functions
- gradient descent
- neural-network training intuition

### 6. Evaluation Math

Needed for: choosing models honestly.

Know:
- MAE, MSE, RMSE, R2
- accuracy, precision, recall, F1
- confusion matrix
- overfitting and underfitting
- cross-validation

Practice in this repo:
- `roadmap/day-036.py`
- `roadmap/day-037.py`
- `roadmap/day-039.py`
- all ML mini-projects from day 40 onward

## Math Learning Order

Use this order while following the roadmap:

| Roadmap Days | Math To Learn |
| --- | --- |
| 001-015 | arithmetic, percentages, averages, simple formulas |
| 016-030 | descriptive statistics, charts, correlation, basic probability |
| 031-045 | train/test split, metrics, vectors, feature matrices |
| 046-060 | regression math, classification metrics, probability, model comparison |
| 061-070 | distances, clustering, PCA, linear algebra intuition |
| 071-080 | derivatives, gradients, loss functions, neural-network intuition |
| 081-090 | project-specific review and metric interpretation |

## Recommended Resources

Free math and ML math:
- [Khan Academy - Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [Khan Academy - Statistics and Probability](https://www.khanacademy.org/math/statistics-probability)
- [3Blue1Brown - Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra)
- [3Blue1Brown - Essence of Calculus](https://www.3blue1brown.com/topics/calculus)
- [Mathematics for Machine Learning](https://mml-book.github.io/)

Python, data, and ML documentation:
- [Python Documentation](https://docs.python.org/3/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/)
- [Seaborn Tutorials](https://seaborn.pydata.org/tutorial.html)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

## Project Checklist

For each mini-project, try to include:

- clear input data
- reusable functions
- basic validation
- printed results or saved charts
- comments explaining important choices
- at least one short conclusion
- one idea for improving the project later

For ML projects, also include:

- problem statement
- features and target
- train/test split
- preprocessing steps
- model choice
- evaluation metric
- limitations

## Current Best Starting Point

The current active mini-project is:

```text
roadmap/day_10_student_performance_tracker.py
```

It is a good checkpoint for the first Python section. Finish it before moving
too far into NumPy and pandas, because the same habits come back later: clean
functions, validated inputs, readable data structures, and simple reporting.
