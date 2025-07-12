# 📏 Height Prediction from Weight using Simple Linear Regression

This project predicts a person's **height (in cm)** based on their **weight (in kg)** using a simple linear regression model. The dataset is manually created and contains real-world inspired data of 24 individuals.

---

## 📊 Dataset

- **Features:**
  - `Weight` (in kilograms) – Independent variable (X)
  - `Height` (in centimeters) – Dependent variable (Y)
- **Format:** Excel (.xlsx)
- **Total Records:** 24

---

## 📌 Problem Type

This is a **regression problem**, as the output variable (height) is continuous, not categorical.

---

## 🔧 Technologies Used

- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- statsmodels

---

## 🧠 Model Used

We trained a **Simple Linear Regression** model using scikit-learn. The model learns a linear relationship between weight and height.

**Learned Equation (after training):**

\[
\hat{y} = b_0 + b_1 \cdot \text{Weight}
\]

After standardization and training, the model was able to predict unseen data fairly accurately.

---

## 📈 Visualizations

- Scatter plot of actual Weight vs. Height
- Regression line over training data
- Seaborn pairplot showing distributions and linear trend

---

## 🧪 Performance Evaluation

We used the following metrics on the **test data**:

| Metric     | Value         |
|------------|---------------|
| MSE        | Reasonable    |
| MAE        | ~4.9 cm       |
| RMSE       | ~5.1 cm       |
| R² Score   | 0.736         |
| Adjusted R²| Calculated    |

---

## 🔮 Prediction Example

The model can predict height for any given weight. For example:

```python
regression.predict(scaler.transform([[72]]))
# Output: ~165.32 cm
