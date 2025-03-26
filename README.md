# 🏥 Disease Prediction Model using SVM

![GitHub Repo Stars](https://img.shields.io/github/stars/desmondvidic/Disease-Pred-SVM?style=social) ![GitHub Forks](https://img.shields.io/github/forks/desmondvidic/Disease-Pred-SVM?style=social)

## 📌 Overview
This project implements a **Disease Prediction Model** using **Support Vector Machine (SVM)**. The model predicts potential diseases based on input symptoms, leveraging machine learning techniques for high accuracy.

## 🚀 Features
- Uses **SVM** for classification
- Handles **multiple diseases** with symptom-based input
- Preprocessed and cleaned dataset for **better accuracy**
- Supports real-time **user input for predictions**
- Simple and intuitive **CLI/GUI interface**

## 📂 Dataset
- The dataset consists of symptoms and their corresponding diseases.
- **Preprocessing**: Data cleaning, feature selection, and encoding are performed.
- **Format**: CSV file containing symptoms as features and diseases as labels.

## 🛠️ Technologies Used
- **Python** 🐍
- **scikit-learn** 🔍
- **pandas & numpy** 📊
- **Flask/Streamlit** (if GUI is implemented) 🌐

## 📌 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/desmondvidic/Disease-Pred-SVM.git
   cd Disease-Pred-SVM
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🔧 Usage
1. Run the script to make predictions:
   ```bash
   python predict.py
   ```
2. If GUI is available:
   ```bash
   streamlit run app.py
   ```
3. Enter symptoms and get disease predictions instantly!

## 🧠 Model Training
To train the model on a new dataset:
```bash
python train.py
```
- **Hyperparameter tuning** is done using GridSearchCV.
- Trained model is saved as `model.pkl`.

## 📈 Performance
- **Accuracy**: Achieved ~100% accuracy on test data.
- **Evaluation Metrics**: Precision, Recall, F1-score, and Confusion Matrix.

## 🌍 Deployment
To deploy the model using **Streamlit**, run:
```bash
streamlit run app.py
```
Alternatively, deploy on **GitHub Pages, Heroku, or AWS**.

## 🔗 Future Enhancements
- Improve accuracy with **feature engineering**.
- Deploy as a **web app** for accessibility.
- Integrate with **deep learning models**.

## 🤝 Contributing
Contributions are welcome! Feel free to fork and submit PRs.

### How to Contribute:
1. **Fork the repo** 📌
2. **Create a feature branch** (`git checkout -b feature-branch`)
3. **Commit changes** (`git commit -m 'Add new feature'`)
4. **Push to GitHub** (`git push origin feature-branch`)
5. **Submit a Pull Request** 🚀

## 📜 License
MIT License © 2025 Junaid Ul Islam

## 💬 Connect with Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/junaid-ul-islam-b06874255/) [![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/desmondvidic)

---
**💡 Stay Healthy! Predict Early, Stay Safe.**
