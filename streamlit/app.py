import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Depresyon Tahmini", layout="centered")
st.title("🧠 Öğrenci Depresyon Tahmini Uygulaması")

# 🎛️ Model seçenekleri ve yolları
model_options = {
    "Logistic Regression": ("/content/logistic_regression_model.pkl", "/content/logistic_regression_model_feature_names.pkl"),
    "Random Forest": ("/content/random_forest_model.pkl", "/content/random_forest_model_feature_names.pkl"),
    "KNN": ("/content/knn_model.pkl", "/content/knn_model_feature_names.pkl"),
    "Decision Tree": ("/content/decision_tree_model.pkl", "/content/decision_tree_feature_names.pkl"),
    "Random Forest + XGBoost (Hybrid)": ("/content/random_forest_with_xgboost_model.pkl", "/content/random_forest_with_xgboost_model_names.pkl")
}

# 📌 Model seçimi
model_name = st.selectbox("📌 Kullanmak istediğiniz modeli seçin:", list(model_options.keys()))
model_path, feature_path = model_options[model_name]

# 🧠 Model başarım özeti (isteğe bağlı bilgi)
model_info = {
    "Logistic Regression": "F1: 0.77 | AUC: 0.84",
    "Random Forest": "F1: 0.75 | AUC: 0.81",
    "KNN": "F1: 0.76 | AUC: 0.82",
    "Decision Tree": "F1: 0.68 | AUC: 0.67",
    "Random Forest + XGBoost (Hybrid)": "F1: 0.77 | AUC: 0.84"
}
st.caption(f"📈 Seçilen modelin başarım özeti: {model_info.get(model_name)}")

st.markdown("---")
st.markdown("Aşağıdaki formu doldurarak depresyon riskinizi tahmin edin.")

# ✅ Giriş Formu
with st.form("depression_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Yaş", 18, 60, 22)
        cgpa = st.slider("CGPA", 0.0, 10.0, 6.5)
        sleep = st.slider("Uyku Süresi (saat)", 3.0, 12.0, 7.0)
        work_study = st.slider("Günlük Çalışma Süresi (saat)", 0, 16, 4)

    with col2:
        academic_pressure = st.select_slider("Akademik Baskı", [1, 2, 3, 4, 5])
        study_satisfaction = st.select_slider("Eğitim Memnuniyeti", [1, 2, 3, 4, 5])
        job_satisfaction = st.select_slider("İş Memnuniyeti", [1, 2, 3, 4, 5])
        work_pressure = st.select_slider("İş Baskısı", [1, 2, 3, 4, 5])

    with col3:
        dietary = st.selectbox("Beslenme Alışkanlığı", ["Moderate", "Unhealthy", "Others"])

    submitted = st.form_submit_button("📊 Tahmini Göster")

# ✅ Tahmin işlemi
if submitted:
    feature_names = joblib.load(feature_path)
    model = joblib.load(model_path)

    input_dict = {
        "Age": age,
        "CGPA": cgpa,
        "Sleep Duration": sleep,
        "Work/Study Hours": work_study,
        "Academic Pressure": academic_pressure,
        "Study Satisfaction": study_satisfaction,
        "Job Satisfaction": job_satisfaction,
        "Work Pressure": work_pressure,
        "Total Pressure": study_satisfaction + job_satisfaction + work_pressure,
        "Dietary Habits_Moderate": 0,
        "Dietary Habits_Unhealthy": 0,
        "Dietary Habits_Others": 0,
    }

    input_dict[f"Dietary Habits_{dietary}"] = 1  # Doğru sütunu aktif et

    # Kullanıcı verisini hizala
    user_df = pd.get_dummies(pd.DataFrame([input_dict]))
    aligned_df = pd.DataFrame(columns=feature_names)
    aligned_df = pd.concat([aligned_df, user_df], ignore_index=True)
    aligned_df = aligned_df[feature_names].fillna(0)

    # 🔮 Tahmin ve olasılık
    prediction = model.predict(aligned_df)[0]
    probability = model.predict_proba(aligned_df)[0][1]

    # 🧠 Tahmin Sonucu
    st.markdown("---")
    st.markdown(f"### Seçilen Model: `{model_name}`")

    if prediction == 1:
        st.error(f"⚠️ Depresyon riski tespit edildi! Tahmin olasılığı: **%{probability * 100:.1f}**")
        if probability >= 0.8:
            st.markdown("🟥 **Çok Yüksek Risk**")
        elif probability >= 0.6:
            st.markdown("🟧 **Yüksek Risk**")
        else:
            st.markdown("🟨 **Orta Düzey Risk**")
        st.markdown("📌 Lütfen bir uzmana danışın.")
    else:
        st.success(f"✅ Depresyon riski gözükmüyor. Tahmin olasılığı: **%{probability * 100:.1f}**")
        st.markdown("🙂 Görünüşe göre durumunuz stabil. Yine de kendinize iyi bakmayı unutmayın.")

    # 🛠️ Geliştirici Modu: Sonuçtan sonra sadece veri gösterir
st.markdown("---")
if st.checkbox("🛠️ Geliştirici Modu: Girdi ve Veri Kontrolü"):
  if submitted:
    st.subheader("📦 Model Girdileri")
    st.json(input_dict)
    st.subheader("📊 Hizalanmış Giriş Verisi (DataFrame)")
    st.dataframe(aligned_df)
