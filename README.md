# 🧠 Öğrenci Depresyonu Tahmin Projesi

## 📌 Proje Hakkında
Bu proje, üniversite öğrencileri arasında görülen depresyon düzeylerini analiz etmeyi ve tahmin etmeyi amaçlamaktadır. Proje, depresyona sebep olabilecek demografik, akademik ve yaşam tarzı faktörlerini inceleyerek riskli bireyleri önceden belirleyebilmeyi hedeflemektedir.

## 🎯 Projenin Amacı
- Öğrenciler arasındaki depresyon eğilimlerini analiz etmek
- Depresyona etki eden faktörleri belirlemek
- Riskli bireyleri önceden tespit edebilmek
- Psikoloji, eğitim ve veri bilimi alanlarında disiplinler arası çalışmalara katkı sunmak

## 📊 Veri Seti Özellikleri
Veri seti aşağıdaki özellikleri içermektedir:
- **Demografik Bilgiler:** Yaş, Cinsiyet, İkamet Şehri
- **Akademik Bilgiler:** Genel Not Ortalaması (CGPA), Akademik Baskı, Çalışma Biçimi
- **Yaşam Tarzı Faktörleri:** Uyku süresi, beslenme düzeni, çalışma saati, iş memnuniyeti
- **Psikolojik ve Sosyal Etkenler:** Ailede ruhsal hastalık geçmişi, finansal stres, intihar düşüncesi geçmişi

## 🛠️ Kullanılan Teknolojiler
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Plotly
- Seaborn
- Matplotlib

## 📈 Model Performansları
Projede kullanılan modellerin performans metrikleri:
- **Logistic Regression:** F1: 0.77 | AUC: 0.84
- **Random Forest:** F1: 0.75 | AUC: 0.81
- **KNN:** F1: 0.76 | AUC: 0.82
- **Decision Tree:** F1: 0.68 | AUC: 0.67
- **Random Forest + XGBoost (Hybrid):** F1: 0.77 | AUC: 0.84

## 🚀 Proje Yapısı
```
student_depression_dataset_analysis/
├── student_depression_dataset_analysis.py    # Ana analiz ve model eğitim kodu
├── student_depression_dataset_analysis.ipynb # Jupyter notebook versiyonu
├── student_depression_dataset.csv           # Veri seti
├── depression_analysis_report.html          # Analiz raporu
├── depression_analysis_report_boosted.html  # Geliştirilmiş analiz raporu
└── streamlit/                              # Web uygulaması
    ├── app.py                             # Streamlit uygulama kodu
    └── models/                            # Eğitilmiş modeller
```

## 💻 Web Uygulaması
Proje, Streamlit ile geliştirilmiş bir web uygulaması içermektedir. Uygulama üzerinden:
- Farklı makine öğrenmesi modelleri arasında seçim yapabilirsiniz
- Öğrenci bilgilerini girerek depresyon riski tahmini alabilirsiniz
- Tahmin sonuçlarını ve risk seviyelerini görüntüleyebilirsiniz

## 📄 Lisans
Bu proje MIT lisansı altında lisanslanmıştır.

## ⚠️ Önemli Not
Bu proje sadece eğitim ve araştırma amaçlıdır. Depresyon teşhisi ve tedavisi için mutlaka uzman bir sağlık profesyoneline başvurulmalıdır. 