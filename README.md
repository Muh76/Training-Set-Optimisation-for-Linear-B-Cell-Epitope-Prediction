# Epitope Prediction: Training Set Optimization for Linear B-Cell Epitopes

## Project Overview
This repository contains the implementation of my MSc in Computer Science thesis project at Aston University, focused on optimizing training data for linear B-cell epitope (LBCE) prediction using advanced machine learning techniques.

The project investigates the benefits of organism-specific training for predicting LBCEs, with a specific focus on Coronavirus, and evaluates how well these models generalize to heterogeneous datasets containing multiple pathogens.

## Repository Structure
This repository contains three main implementation files:

1. **FNN_Corona_Subset.ipynb**: Implementation of a Feedforward Neural Network model on the Coronavirus-specific subset dataset.

2. **XGBoost_Corona_Subset.ipynb**: Implementation of an XGBoost model on the same Coronavirus-specific subset, which outperformed the FNN approach.

3. **XGBoost_Heterogeneous_Dataset.ipynb**: Having established XGBoost's superior performance on the Corona subset, this notebook applies XGBoost to the main heterogeneous dataset to assess generalizability across multiple pathogens.

## Key Features
- Implementation of feature selection techniques:
  - Boruta algorithm for initial feature filtering
  - Genetic Algorithm (GA) for feature subset optimization
- Machine learning models comparison:
  - Feedforward Neural Network (FNN)
  - XGBoost
- Class imbalance handling:
  - SMOTE (Synthetic Minority Over-sampling Technique)
  - Focal Loss
  - Class weights
- Hyperparameter tuning using Bayesian Optimization
- Model evaluation metrics:
  - Matthews Correlation Coefficient (MCC)
  - Precision, Recall, F1 Score
  - Area Under ROC Curve (AUC-ROC)

## Results
- Achieved 77.32% reduction in feature dimensionality (from 393 to 88 features)
- XGBoost performance on Coronavirus subset:
  - AUC: 0.994
  - F1 Score: 0.88
  - MCC: 0.789
- FNN performance on Coronavirus subset:
  - AUC: 0.975
  - F1 Score: 0.71
  - MCC: 0.579
- XGBoost generalization to heterogeneous dataset:
  - AUC: 0.981
  - F1 Score: 0.87
  - MCC: 0.829

## Technologies Used
- Python (NumPy, Pandas, Scikit-learn, TensorFlow, SciPy)
- Azure Machine Learning for cloud computing resources
- Statistical analysis libraries for model evaluation

## Installation and Usage
```bash
# Clone the repository
git clone https://github.com/Muh76/Epitope-Prediction.git

# Navigate to project directory
cd Epitope-Prediction

# Install required packages
pip install -r requirements.txt

# Run Jupyter notebooks
jupyter notebook
