# Análisis de anuncios de vehículos

Aplicación web desarrollada con Streamlit para realizar una exploración básica del conjunto de datos `vehicles_us.csv`, que contiene anuncios de venta de vehículos usados.

La aplicación muestra indicadores generales y permite construir de forma interactiva:

- Un histograma de la distribución del kilometraje.
- Un gráfico de dispersión para analizar la relación entre el kilometraje y el precio, diferenciado por la condición del vehículo.
- Una vista preliminar de los datos.

## Estructura del proyecto

```text
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks
    └── EDA.ipynb
```

## Ejecución local

1. Crea y activa un entorno virtual.
2. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicia la aplicación:

   ```bash
   streamlit run app.py
   ```

## Despliegue en Render

- Build Command: `pip install --upgrade pip && pip install -r requirements.txt`
- Start Command: `streamlit run app.py`

El análisis exploratorio utilizado como base se encuentra en `notebooks/EDA.ipynb`.
