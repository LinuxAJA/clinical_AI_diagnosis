import numpy as np
import pandas as pd
import os

np.random.seed(42)

ENFERMEDADES = ["infarto", "neumonia", "gripe", "ansiedad", "gastroenteritis"]

def generar_datos_paciente(enfermedad):
    # ========== DEMOGRÁFICOS ==========
    edad = np.random.randint(18, 90)
    sexo = np.random.choice([0, 1])  # 0: mujer, 1: hombre
    
    # ========== SIGNOS VITALES BASE ==========
    # Valores normales generales
    fc = np.random.randint(60, 100)
    sistole = np.random.randint(100, 130)
    diastole = np.random.randint(60, 85)
    satO2 = np.random.randint(95, 100)
    temp = np.random.uniform(36.0, 37.2)
    
    # ========== FACTORES DE RIESGO (sí/no) ==========
    hipertension = 0
    diabetes = 0
    colesterol_alto = 0
    fumador = 0
    obesidad = 0
    antecedente_cardiaco = 0
    
    # ========== SÍNTOMAS CARDÍACOS ==========
    dolor_pecho = 0
    dolor_opresivo = 0
    dolor_irradiado = 0
    palpitaciones = 0
    disnea = 0
    sudoracion_fria = 0
    
    # ========== SÍNTOMAS RESPIRATORIOS ==========
    tos = 0
    tos_productiva = 0
    esputo_hemoptoico = 0
    fiebre = 0
    escalofrios = 0
    
    # ========== SÍNTOMAS NEUROPSIQUIÁTRICOS ==========
    mareos = 0
    ansiedad = 0          # 0: no, 1: leve/moderada, 2: severa
    ataques_panico = 0
    insomnio = 0
    
    # ========== SÍNTOMAS GI ==========
    nauseas = 0
    vomitos = 0
    diarrea = 0
    dolor_abdominal = 0
    
    # ========== GENERALES ==========
    fatiga = 0
    perdida_apetito = 0
    
    # ============================================
    # CONFIGURACIÓN SEGÚN ENFERMEDAD
    # ============================================
    
    if enfermedad == "infarto":
        # Edad típica: >50 años
        edad = np.random.randint(45, 85)
        # Signos vitales alterados
        fc = np.random.randint(100, 140)
        sistole = np.random.choice([np.random.randint(140, 180), np.random.randint(80, 110)], p=[0.7, 0.3])
        satO2 = np.random.randint(88, 96)
        # Factores de riesgo altos
        hipertension = np.random.choice([0,1], p=[0.3, 0.7])
        diabetes = np.random.choice([0,1], p=[0.7, 0.3])
        colesterol_alto = np.random.choice([0,1], p=[0.6, 0.4])
        fumador = np.random.choice([0,1], p=[0.6, 0.4])
        obesidad = np.random.choice([0,1], p=[0.5, 0.5])
        antecedente_cardiaco = np.random.choice([0,1], p=[0.5, 0.5])
        # Síntomas cardíacos
        dolor_pecho = 1
        dolor_opresivo = 1  # típico opresivo
        dolor_irradiado = np.random.choice([0,1], p=[0.3, 0.7])  # a brazo izquierdo, mandíbula
        palpitaciones = np.random.choice([0,1], p=[0.2, 0.8])
        disnea = 1
        sudoracion_fria = np.random.choice([0,1], p=[0.1, 0.9])
        # Síntomas respiratorios (poco frecuentes)
        tos = np.random.choice([0,1], p=[0.9, 0.1])
        fiebre = 0
        # Neuropsiquiátricos
        mareos = np.random.choice([0,1], p=[0.4, 0.6])
        ansiedad = np.random.choice([0,1], p=[0.6, 0.4])  # ansiedad por miedo
        # GI
        nauseas = np.random.choice([0,1], p=[0.5, 0.5])
        vomitos = np.random.choice([0,1], p=[0.7, 0.3])
        # Generales
        fatiga = 1
        perdida_apetito = np.random.choice([0,1], p=[0.6, 0.4])
        
    elif enfermedad == "neumonia":
        edad = np.random.randint(20, 85)
        fc = np.random.randint(90, 120)
        sistole = np.random.randint(100, 140)
        satO2 = np.random.randint(85, 95)
        temp = np.random.uniform(38.0, 39.5)
        fiebre = 1
        escalofrios = np.random.choice([0,1], p=[0.2, 0.8])
        tos = 1
        tos_productiva = np.random.choice([0,1], p=[0.3, 0.7])
        if tos_productiva:
            esputo_hemoptoico = np.random.choice([0,1], p=[0.85, 0.15])  # 15% hemoptoico
        disnea = np.random.choice([0,1], p=[0.2, 0.8])
        dolor_pecho = np.random.choice([0,1], p=[0.6, 0.4])  # pleurítico
        fatiga = 1
        perdida_apetito = 1
        mareos = np.random.choice([0,1], p=[0.8, 0.2])
        nauseas = np.random.choice([0,1], p=[0.7, 0.3])
        # Factores de riesgo moderados
        fumador = np.random.choice([0,1], p=[0.5, 0.5])
        # El resto bajo
        palpitaciones = 0
        sudoracion_fria = np.random.choice([0,1], p=[0.6, 0.4])
        
    elif enfermedad == "gripe":
        edad = np.random.randint(5, 70)
        fc = np.random.randint(70, 100)
        temp = np.random.uniform(37.8, 39.0)
        fiebre = 1
        escalofrios = np.random.choice([0,1], p=[0.3, 0.7])
        tos = 1
        tos_productiva = 0  # generalmente seca
        fatiga = 1
        perdida_apetito = np.random.choice([0,1], p=[0.4, 0.6])
        mareos = np.random.choice([0,1], p=[0.7, 0.3])
        nauseas = np.random.choice([0,1], p=[0.7, 0.3])
        dolor_pecho = 0
        disnea = np.random.choice([0,1], p=[0.8, 0.2])
        # Síntomas gripales típicos
        congestión_nasal = np.random.choice([0,1], p=[0.2, 0.8])  # añadimos variable extra
        
    elif enfermedad == "ansiedad":
        edad = np.random.randint(18, 50)
        fc = np.random.randint(90, 130)  # taquicardia
        sistole = np.random.choice([np.random.randint(120, 160), np.random.randint(100, 120)], p=[0.6, 0.4])
        palpitaciones = 1
        sudoracion_fria = np.random.choice([0,1], p=[0.2, 0.8])
        disnea = 1  # sensación de falta de aire
        mareos = 1
        ansiedad = np.random.choice([1,2], p=[0.5, 0.5])  # 1: moderada, 2: severa
        ataques_panico = np.random.choice([0,1], p=[0.3, 0.7])
        insomnio = np.random.choice([0,1], p=[0.3, 0.7])
        dolor_pecho = np.random.choice([0,1], p=[0.5, 0.5])  # opresivo no cardíaco
        nauseas = np.random.choice([0,1], p=[0.6, 0.4])
        fatiga = np.random.choice([0,1], p=[0.3, 0.7])
        # Ausencia de fiebre y tos
        fiebre = 0
        tos = 0
        
    elif enfermedad == "gastroenteritis":
        edad = np.random.randint(2, 70)
        fc = np.random.randint(80, 110)
        temp = np.random.choice([np.random.uniform(37.0, 38.0), 36.5], p=[0.6, 0.4])
        fiebre = 1 if temp > 37.8 else 0
        nauseas = 1
        vomitos = np.random.choice([0,1], p=[0.3, 0.7])
        diarrea = 1
        dolor_abdominal = 1
        fatiga = 1
        perdida_apetito = 1
        mareos = np.random.choice([0,1], p=[0.5, 0.5])  # por deshidratación
        dolor_pecho = 0
        tos = 0
        palpitaciones = 0
        disnea = 0
    
    # ========== CONSTRUIR DICCIONARIO ==========
    data = {
        "edad": edad,
        "sexo": sexo,
        "frecuencia_cardiaca": fc,
        "presion_sistolica": sistole,
        "presion_diastolica": diastole,
        "saturacion_oxigeno": satO2,
        "temperatura": round(temp, 1),
        "hipertension": hipertension,
        "diabetes": diabetes,
        "colesterol_alto": colesterol_alto,
        "fumador": fumador,
        "obesidad": obesidad,
        "antecedente_cardiaco": antecedente_cardiaco,
        "dolor_pecho": dolor_pecho,
        "dolor_opresivo": dolor_opresivo,
        "dolor_irradiado": dolor_irradiado,
        "palpitaciones": palpitaciones,
        "disnea": disnea,
        "sudoracion_fria": sudoracion_fria,
        "tos": tos,
        "tos_productiva": tos_productiva,
        "esputo_hemoptoico": esputo_hemoptoico if tos_productiva else 0,
        "fiebre": fiebre,
        "escalofrios": escalofrios,
        "mareos": mareos,
        "ansiedad": ansiedad,
        "ataques_panico": ataques_panico,
        "insomnio": insomnio,
        "nauseas": nauseas,
        "vomitos": vomitos,
        "diarrea": diarrea,
        "dolor_abdominal": dolor_abdominal,
        "fatiga": fatiga,
        "perdida_apetito": perdida_apetito,
        "diagnostico": enfermedad
    }
    return data

# ========== GENERAR DATASET ==========
n_registros = 5000
datos = []
for _ in range(n_registros):
    enfermedad = np.random.choice(ENFERMEDADES, p=[0.2, 0.2, 0.2, 0.2, 0.2])
    datos.append(generar_datos_paciente(enfermedad))

df = pd.DataFrame(datos)

# Guardar
os.makedirs("data/", exist_ok=True)
df.to_csv("./data/dataset_medico_ampliado.csv", index=False)

print(f"✅ Dataset generado con {len(df)} registros y {len(df.columns)} columnas.")
print("\n primeras filas:")
print(df.head())
print("\nColumnas generadas:")
print(list(df.columns))