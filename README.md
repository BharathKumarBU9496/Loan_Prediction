# Loan_Prediction
Python code using a sample dataset to predict loan approval.

**Step 1: Dataset Creation**
Let's create a sample dataset. This dataset will include common features that influence loan approval decisions such as gender, marital status, applicant income, loan amount, and credit history.
![image](https://github.com/user-attachments/assets/53c76864-d194-4b0d-b1d1-d8ffa58e1668)

**Step 2: Data Preprocessing**
Before we can train our model, we need to preprocess our data, such as handling categorical variables.

![image](https://github.com/user-attachments/assets/23164da7-17b3-4b93-8b3e-9bda51c8bfc1)

**Step 3: Data Visualization**
Create some visualizations to explore the data.
![image](https://github.com/user-attachments/assets/734bbe3b-6425-4f1a-abd0-4a746df0034a)

**Step 4: Model Building**
Using logistic regression to predict loan approval.
![image](https://github.com/user-attachments/assets/38329ff2-52c1-4775-9e55-d7007a371087)

**OUTPUT:Visualizations**
![Figure1](https://github.com/user-attachments/assets/50bc2f74-1236-435b-8f6c-da648dbf05a9)


**Explanation**
**Pairplot:** This plot helps us see the distribution of single variables and relationships between two variables, differentiated by loan status. The use of hue based on 'Loan_Status' allows us to visually segregate data points based on whether the loan was approved or not.

**Heatmap:** Shows the correlation between different variables in the dataset. A higher correlation coefficient indicates a strong relationship, which can be crucial in predictive modeling to avoid multicollinearity.

**Count Plots:** These are useful for visualizing the distribution of categorical variables. By comparing these distributions across different categories of the loan status, one can infer how significant a feature might be in predicting loan approval.

These visualizations provide insightful previews into the dataset and are effective in communicating the results in a visually appealing way
