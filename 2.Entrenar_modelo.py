import pandas as pd
from sklearn.model_selection import train_test_split # pip install scikit-learn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

os.system("cls" if os.name == "nt" else "clear")

def log(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

try:
    # =========================
    # 1. CARGA DEL DATASET AMPLIADO
    # =========================
    log("1. CARGA DEL DATASET AMPLIADO")
    df = pd.read_csv("data/dataset_medico_ampliado.csv")
    print(f"✔ Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
    
    # =========================
    # 2. SEPARAR FEATURES Y TARGET
    # =========================
    log("2. PREPARACIÓN DE DATOS")
    X = df.drop("diagnostico", axis=1)
    y = df["diagnostico"]
    
    print(f"🔢 Features utilizadas ({len(X.columns)}):")
    for i, col in enumerate(X.columns, 1):
        print(f"   {i}. {col}")
    print(f"\n🎯 Clases objetivo: {y.unique()}")
    
    # =========================
    # 3. DIVISIÓN TRAIN/TEST
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    print(f"\n📊 Split: Train {X_train.shape[0]} | Test {X_test.shape[0]}")
    
    # =========================
    # 4. ENTRENAMIENTO
    # =========================
    log("3. ENTRENAMIENTO DEL MODELO")
    model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    print("✔ Modelo entrenado")
    
    # =========================
    # 5. EVALUACIÓN
    # =========================
    log("4. EVALUACIÓN")
    y_pred = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    print(f"🎯 Accuracy(Exactitud): {accuracy:.4f} ({accuracy*100:.2f}%)\n")
    print("📋 Classification Report:")
    print(classification_report(y_test, y_pred))
    print("📊 Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred))
    
    # =========================
    # 6. IMPORTANCIA DE VARIABLES
    # =========================
    log("5. IMPORTANCIA DE VARIABLES")
    imp_df = pd.DataFrame({
        "Feature": X.columns,
        "Importancia (%)": (model.feature_importances_ * 100).round(2)
    }).sort_values("Importancia (%)", ascending=False)
    print(imp_df.head(15).to_string(index=False))
    
    # =========================
    # 7. GUARDAR MODELO
    # =========================
    log("6. GUARDANDO MODELO")
    os.makedirs("models", exist_ok=True)
    modelo_path = "models/modelo_random_forest_ampliado.pkl"
    joblib.dump(model, modelo_path)
    print(f"💾 Modelo guardado en: {modelo_path}")
    
except FileNotFoundError:
    log("ERROR")
    print("❌ No se encontró 'data/dataset_medico_ampliado.csv'")
    print("👉 Ejecuta primero '1.Crear_Dataset_Mejorado.py'")
    exit(1)