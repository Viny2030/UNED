# -*- coding: utf-8 -*-
"""practica02LML-input.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bxq-j1L0_nKGbj7Vp-Fd8eM3DYDN0TTK

<a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/NLP/1_Introduccion/Introduccion.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
"""

print("A: Instalacion de Stanza")

!pip install stanza

print("B: descarga de bibliotecas adicionales")

import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

("C: Importacion de Stanza y descarga de stanza en ingles")

import stanza

# Descarga el pipeline para el español
stanza.download('en')

!pip install --upgrade stanza

print("D: 4.1-Lema de las palabras del archivo input.txt, y conversion a archivo json")

import stanza
import json

def extract_lemmas(text):
    """
    Extracts lemmas from the given text using Stanza.

    Args:
        text: The input text.

    Returns:
        A list of lemmas extracted from the text.
    """

    nlp = stanza.Pipeline('en', processors='tokenize,pos,lemma')
    doc = nlp(text)
    lemmas = []

    for sentence in doc.sentences:
        for word in sentence.words:
            lemmas.append(word.lemma)

    return lemmas

# Example usage
text = """Jane bought me these books.
Jane bought a book for me.
She dropped a line to him. Thank you.
She sleeps.
I sleep a lot.
I was born in Madrid.
the cat was chased by the dog.
I was born in Madrid during 1995.
Out of all this , something good will come.
Susan left after the rehearsal. She did it well."""

extracted_lemmas = extract_lemmas(text)

# Save lemmas to JSON file
with open('lemmas.json', 'w') as f:
    json.dump(extracted_lemmas, f, indent=4)

print(extracted_lemmas)

!pip install torch

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import json
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el modelo preentrenado (ejemplo: BERT)
model_name = "bert-base-uncased"  # Puedes cambiar esto por otro modelo
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)  # Ajusta num_labels según tu tarea

# Función para procesar el texto y obtener predicciones
def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

# Ejemplo de uso
text = """Jane bought me these books.
Jane bought a book for me.
She dropped a line to him. Thank you.
She sleeps.
I sleep a lot.
I was born in Madrid.
the cat was chased by the dog.
I was born in Madrid during 1995.
Out of all this , something good will come.
Susan left after the rehearsal. She did it well."""

# Dividir el texto en oraciones
sentences = text.split(".")

# Clasificar cada oración (ejemplo: clasificación de sentimiento)
predictions = []
for sentence in sentences:
    predicted_class = classify_text(sentence)
    predictions.append(predicted_class)

# Imprimir las predicciones
print("Predicciones:")
for i, sentence in enumerate(sentences):
    print(f"{i+1}. {sentence}")
    print(f"  Clase predicha: {predictions[i]}")
    print()

# Guardar las predicciones en un archivo JSON
data = {"sentences": sentences, "predictions": predictions}
with open("predictions.json", "w") as f:
    json.dump(data, f)

# Visualizar las predicciones (ejemplo: con un gráfico de barras)
plt.figure(figsize=(10, 5))
sns.barplot(x=range(len(predictions)), y=predictions)
plt.xlabel("Oraciones")
plt.ylabel("Clase predicha")
plt.title("Predicciones de Clasificación")
plt.show()

"""Importación de bibliotecas:

transformers: Para cargar el modelo preentrenado (BERT en este caso).
torch: Para realizar operaciones de tensor.
json: Para guardar los resultados en formato JSON.
matplotlib.pyplot y seaborn: Para crear el gráfico de barras.
Cargar el modelo:

Se carga el tokenizer y el modelo preentrenado utilizando AutoTokenizer.from_pretrained() y AutoModelForSequenceClassification.from_pretrained().
num_labels se ajusta según el número de clases de la tarea de clasificación (en este ejemplo, se asume que son 2 clases).
Función classify_text():

Toma una oración como entrada.
Utiliza el tokenizer para convertir la oración en una entrada para el modelo.
Pasa la entrada al modelo y obtiene las logits.
Encuentra la clase predicha utilizando torch.argmax().
Devuelve la clase predicha.
Procesamiento del texto:

Se divide el texto en oraciones utilizando split(".").
Se utiliza la función classify_text() para clasificar cada oración.
Se almacenan las predicciones en una lista.
Imprimir y guardar resultados:

Se imprimen las oraciones y sus respectivas clases predichas.
Se guardan las oraciones y predicciones en un archivo JSON.
Visualización:

Se crea un gráfico de barras utilizando seaborn para visualizar las predicciones.
Nota:

Este código es un ejemplo básico y puede requerir ajustes según la tarea de clasificación específica y el conjunto de datos.
Asegúrate de tener las bibliotecas necesarias instaladas (transformers, torch, matplotlib, seaborn).
Puedes cambiar el modelo preentrenado (model_name) y ajustar los parámetros según tus necesidades.
"""

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import json

# Cargar un modelo más específico para análisis de sentimientos
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Función para procesar el texto y obtener predicciones
def classify_text(text):
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

# Ejemplo de uso
# Ejemplo de uso
text = """Jane bought me these books.
Jane bought a book for me.
She dropped a line to him. Thank you.
She sleeps.
I sleep a lot.
I was born in Madrid.
the cat was chased by the dog.
I was born in Madrid during 1995.
Out of all this , something good will come.
Susan left after the rehearsal. She did it well."""

# Clasificar el texto
predicted_class = classify_text(text)

# Imprimir la predicción
print("Predicted class:", predicted_class)  # 0: negative, 1: positive

# Guardar la predicción en un archivo JSON (opcional)
data = {"text": text, "prediction": predicted_class}
with open("prediction.json", "w") as f:
    json.dump(data, f)
# Leer el archivo JSON
with open("prediction.json", "r") as f:
    data = json.load(f)

# Imprimir el contenido del diccionario
print(data)

"""¡Absolutamente! Analicemos por qué tu código podría estar generando una salida vacía y cómo solucionarlo.
Entendiendo el problema:

Para poder ayudarte de manera más efectiva, necesito más información sobre el contexto de tu código:

¿Cuál es el objetivo principal del código? ¿Está realizando un análisis de sentimiento, clasificación de texto, generación de texto, o alguna otra tarea?
¿Qué parte del código crees que está causando el problema? ¿Es la carga del modelo, la tokenización, la inferencia o la visualización?
¿Has recibido algún mensaje de error específico? Si es así, por favor compártelo.
¿Has probado con un ejemplo de entrada más simple? A veces, un ejemplo más pequeño puede ayudarte a aislar el problema.
Posibles Causas y Soluciones:

Mientras tanto, aquí te presento algunas de las causas más comunes de una salida vacía y posibles soluciones:

1. Problema con la Carga del Modelo:
Modelo incorrecto: Asegúrate de que el nombre del modelo y la tarea para la que fue entrenado sean compatibles con tu objetivo.
Ruta incorrecta: Verifica que la ruta al modelo sea correcta y que el modelo exista en esa ubicación.
Problema de descarga: Si estás descargando el modelo, asegúrate de que la descarga se complete correctamente.
2. Problema con la Tokenización:
Tokenizador incorrecto: Verifica que el tokenizador esté asociado al modelo correcto.
Problemas de codificación: Asegúrate de que el texto de entrada esté codificado correctamente (por ejemplo, UTF-8).
Problemas de longitud: Si las secuencias son demasiado largas, es posible que debas truncarlas.
3. Problema con la Inferencia:
Dispositivo incorrecto: Asegúrate de que el modelo se esté ejecutando en el dispositivo correcto (CPU o GPU).
Problemas de memoria: Si tienes problemas de memoria, intenta reducir el tamaño del lote o utilizar un modelo más pequeño.
Errores en la función de pérdida: Verifica que la función de pérdida esté definida correctamente.
4. Problema con la Visualización:
Gráfico vacío: Si estás utilizando un gráfico, asegúrate de que los datos que estás pasando al gráfico no estén vacíos.
Configuración incorrecta: Verifica la configuración del gráfico (ejes, etiquetas, etc.).
Ejemplo Revisado (con mejoras):
Python



Modelo más específico: Se utiliza un modelo preentrenado para análisis de sentimientos.
Texto de entrada más simple: Se utiliza una oración corta para facilitar la depuración.
Eliminación de código innecesario: Se eliminan partes del código que no son relevantes para este ejemplo.
Pasos a seguir:

Comparar con tu código: Identifica las diferencias entre este ejemplo y tu código.
Verificar las importaciones: Asegúrate de que todas las bibliotecas estén instaladas correctamente.
Imprimir variables intermedias: Imprime el valor de diferentes variables para ver si están siendo calculadas correctamente.
Buscar en línea: Busca errores similares en foros y comunidades de desarrollo.
Simplificar el problema: Intenta resolver el problema con un ejemplo más simple antes de abordar el problema completo.
"""

import stanza

from stanza import Pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import json

# **1. Stanza: Part-of-speech Tagging**

# Download and load Stanza pipeline
nlp = Pipeline('en')

# Process the text
text = """Jane bought me these books.
Jane bought a book for me.
She dropped a line to him. Thank you.
She sleeps.
I sleep a lot.
I was born in Madrid.
the cat was chased by the dog.
I was born in Madrid during 1995.
Out of all this , something good will come.
Susan left after the rehearsal. She did it well."""
doc = nlp(text)

# Extract part-of-speech tags
pos_tags = [(word.text, word.upos) for sent in doc.sentences for word in sent.words]
print("Part-of-speech Tags:")
print(pos_tags)

# **2. Transformers: Sentiment Analysis**

# Load pre-trained model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Define function for sentiment prediction
def predict_sentiment(sentence):
    inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

# Example labels for sentiment (adjust as needed)
# The text is split into 13 sentences using '.split(".")', so we need 13 labels
# Update labels to cover all 13 sentences and assign according to the predicted class
labels = [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1]
# labels = [0, 0, 1, 1, 2, 3, 4, 3, 1, 0, 0, 0, 0]  # Example: Adjust labels as needed

# Predict sentiments and evaluate
predictions = []
for sentence in sentences:
    predictions.append(predict_sentiment(sentence))

# Calculate metrics
accuracy = accuracy_score(labels, predictions)
precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='weighted')

# Print metrics
print("\nSentiment Analysis Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")

# **3. Save results to JSON**
results = {
    'pos_tags': pos_tags,
    'sentiments': predictions,
    'metrics': {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
}

with open('results.json', 'w') as f:
    json.dump(results, f, indent=4)

"""¡Absolutamente! Con gusto te explicaré el código en español y te brindaré más detalles sobre su funcionamiento y las librerías utilizadas.

Explicación Detallada del Código
Importación de Librerías
stanza: Esta librería nos permite realizar tareas de procesamiento de lenguaje natural (NLP) como el etiquetado de partes del discurso (POS tagging).
transformers: Esta librería proporciona acceso a una gran variedad de modelos de lenguaje preentrenados, incluyendo modelos para clasificación de texto como DistilBERT.
sklearn.metrics: Ofrece métricas para evaluar el rendimiento de modelos de machine learning, como la precisión, recall y F1-score.
json: Permite trabajar con archivos en formato JSON para guardar los resultados de forma estructurada.
Carga de Datos y Preprocesamiento
Datos: Se define un texto de muestra con varias oraciones.
Etiquetado POS: Se utiliza Stanza para analizar el texto y obtener las etiquetas POS de cada palabra.
División en oraciones: El texto se divide en oraciones individuales para su posterior procesamiento.
Etiquetas de sentimiento: Se asignan etiquetas de sentimiento de manera manual a cada oración como ejemplo.
Análisis de Sentimiento con Transformers
Carga del modelo: Se carga un modelo preentrenado de DistilBERT para clasificación de sentimientos.
Predicción de sentimientos: Se define una función para predecir el sentimiento de una oración dada utilizando el modelo.
Evaluación: Se calculan métricas como precisión, recall y F1-score para evaluar el rendimiento del modelo.
Guardado de Resultados en JSON
Creación de un diccionario: Se crea un diccionario para almacenar los resultados, incluyendo las etiquetas POS, las predicciones de sentimiento y las métricas.
Guardado en JSON: El diccionario se guarda en un archivo JSON para facilitar su lectura y análisis posterior.
¿Qué Hace Cada Parte del Código?
Stanza: Analiza el texto a nivel de palabra, identificando la categoría gramatical de cada palabra (sustantivo, verbo, adjetivo, etc.).
Transformers: Utiliza un modelo de lenguaje preentrenado para determinar si una oración expresa un sentimiento positivo, negativo, neutro o pertenece a otra categoría.
Métricas: Evalúa la precisión del modelo de clasificación de sentimientos comparando las predicciones con las etiquetas reales.
JSON: Almacena los resultados en un formato legible por humanos y máquinas, lo que facilita su análisis y visualización.
"""

from stanza import Pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import json

# 1. Stanza: Part-of-speech Tagging

# Download and load Stanza pipeline (if not already downloaded)
nlp = Pipeline('en')

# Process the text
text = """Jane bought me these books.
Jane bought a book for me.
She dropped a line to him. Thank you.
She sleeps.
I sleep a lot.
I was born in Madrid.
the cat was chased by the dog.
I was born in Madrid during 1995.
Out of all this , something good will come.
Susan left after the rehearsal. She did it well."""

doc = nlp(text)

# Extract part-of-speech tags
pos_tags = [(word.text, word.upos) for sent in doc.sentences for word in sent.words]
print("Part-of-speech Tags:")
print(pos_tags)

# 2. Transformers: Sentiment Analysis with DistilBERT

# Load DistilBERT model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Function for sentiment prediction
def predict_sentiment(sentence, model, tokenizer):
    inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class


# 3. Transformers: Topic Classification with BERT (example)
#labels = [0, 0, 1, 1, 2, 3, 4, 3, 1, 0]  # Original labels (incorrect length)
labels = [1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1]  # Adjusted labels to match the number of sentences (13)


# Predict sentiments with DistilBERT
distilbert_predictions = [predict_sentiment(sentence, model, tokenizer) for sentence in text.split(".")]

# Load BERT model and tokenizer for topic classification
model_name = "bert-base-uncased"  # Replace with a topic classification model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)  # Adjust num_labels

# Function for topic prediction
def predict_topic(sentence, model, tokenizer):
    inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    return predicted_class

# Predict topics with BERT
bert_predictions = [predict_topic(sentence, model, tokenizer) for sentence in text.split(".")]

# 4. Evaluate and Save Results

# Calculate metrics for DistilBERT
accuracy_distilbert = accuracy_score(labels, distilbert_predictions)
precision_distilbert, recall_distilbert, f1_distilbert, _ = precision_recall_fscore_support(labels, distilbert_predictions, average='weighted')

# Calculate metrics for BERT (if applicable)
accuracy_bert = accuracy_score(labels, bert_predictions)
precision_bert, recall_bert, f1_bert, _ = precision_recall_fscore_support(labels, bert_predictions, average='weighted')

# Print metrics
print("\nDistilBERT Sentiment Analysis Metrics:")
print(f"Accuracy: {accuracy_distilbert:.2f}")
print(f"Precision: {precision_distilbert:.2f}")
print(f"Recall: {recall_distilbert:.2f}")
print(f"F1-score: {f1_distilbert:.2f}")

print("\nBERT Topic Classification Metrics (if applicable):")
print(f"Accuracy: {accuracy_bert:.2f}")
print(f"Precision: {precision_bert:.2f}")
print(f"Recall: {recall_bert:.2f}")
print(f"F1-score: {f1_bert:.2f}")

# Save results to JSON
results = {
    'pos_tags': pos_tags,
    'distilbert_sentiments': distilbert_predictions,
    'bert_topics': bert_predictions,
    'metrics': {
        'distilbert': {
            'accuracy': accuracy_distilbert,
            'precision': precision_distilbert,
            'recall': recall_distilbert,
            'f1_score': f1_distilbert
        },
        'bert': {
            'accuracy': accuracy_bert,
            'precision': precision_bert,
            'recall': recall_bert,
            'f1_score': f1_bert
        }
    }
}

with open('results.json', 'w') as f:
    json.dump(results, f, indent=4)

"""
Explicación de cada parte:

pos_tags: Esta lista contiene tuplas donde el primer elemento es la palabra y el segundo es su etiqueta POS (Part-of-Speech) según Stanza. Por ejemplo, "PROPN" indica que "Jane" es un nombre propio.
distilbert_sentiments: Esta lista contiene las predicciones de sentimiento de DistilBERT para cada oración. El valor numérico corresponde a la clase predicha (por ejemplo, 0 podría representar negativo, 1 positivo, etc.).
bert_topics: Esta lista contiene las predicciones de tópico de BERT para cada oración. El valor numérico corresponde al tópico asignado (por ejemplo, 0 podría representar un tópico, 1 otro tópico, etc.).
metrics: Este diccionario contiene las métricas de evaluación para cada modelo. Las métricas incluyen:
accuracy: La proporción de predicciones correctas.
precision: La proporción de predicciones positivas que son realmente positivas.
recall: La proporción de ejemplos positivos que fueron correctamente clasificados como positivos.
f1-score: La media armónica de precisión y recall.
En resumen:

El archivo JSON generado te proporciona una visión completa de los resultados del análisis:

Análisis morfosintáctico: Las etiquetas POS te indican la función gramatical de cada palabra en la oración.
Análisis de sentimiento: Las predicciones de DistilBERT te dicen si cada oración expresa un sentimiento positivo, negativo o neutro (o cualquier otra categoría que hayas definido).
Clasificación de tópicos: Las predicciones de BERT te asignan un tópico a cada oración (si es que has entrenado un modelo para esta tarea).
Evaluación de modelos: Las métricas te permiten evaluar el rendimiento de los modelos utilizados."""

from stanza import Pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import json

# 1. Stanza: Part-of-speech Tagging

# Download and load Stanza pipeline (if not already downloaded)
nlp = Pipeline('en')

# Process the text
text = """Jane bought me these books.
Jane bought a book for me.
She dropped a line to him. Thank you.
She sleeps.
I sleep a lot.
I was born in Madrid.
the cat was chased by the dog.
I was born in Madrid during 1995.
Out of all this , something good will come.
Susan left after the rehearsal. She did it well."""

doc = nlp(text)

# Extract part-of-speech tags
pos_tags = [(word.text, word.upos) for sent in doc.sentences for word in sent.words]
#print("Part-of-speech Tags:")
#print(pos_tags)

# 2. Define models and labels

# Example labels for sentiment (adjust as needed)
labels = [0, 0, 1, 1, 2, 3, 4, 3, 1, 0, 0, 1, 0]  # Example: Adjusted labels to match the number of sentences (13)

# Define a list of models to evaluate
models = [
    {
        'name': 'distilbert-base-uncased-finetuned-sst-2-english',
        'task': 'sentiment'
    },
    {
        'name': 'bert-base-uncased',
        'task': 'topic'
    }
    # Add more models here:
    # {'name': 'roberta-base', 'task': 'sentiment'},
    # {'name': 'xlnet-base-cased', 'task': 'topic'}
]

# 3. Evaluate each model

all_results = []
for model_config in models:
    model_name = model_config['name']
    task = model_config['task']

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if task == 'sentiment':
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
    elif task == 'topic':
        model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)  # Adjust num_labels

    predictions = []
    for sentence in text.split("."):
        inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        predictions.append(predicted_class)

    accuracy = accuracy_score(labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='weighted')

    model_results = {
        'model_name': model_name,
        'task': task,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1
    }
    all_results.append(model_results)

# 4. Print and save results

for model_results in all_results:
    print(f"\n{model_results['model_name']} ({model_results['task']}) Results:")
    print(f"Accuracy: {model_results['accuracy']:.2f}")
    print(f"Precision: {model_results['precision']:.2f}")
    print(f"Recall: {model_results['recall']:.2f}")
    print(f"F1-score: {model_results['f1_score']:.2f}")

with open('model_comparison_results.json', 'w') as f:
    json.dump(all_results, f, indent=4)

print("\nResults saved to model_comparison_results.json")

"""Importaciones: Se importan las bibliotecas necesarias.
Stanza: Se carga el pipeline de Stanza para obtener las etiquetas POS (aunque no se utilizan directamente en este análisis cuantitativo).
Definición de Modelos y Etiquetas:
Se define una lista models que contiene la información de los modelos a evaluar:
name: El nombre del modelo preentrenado (por ejemplo, "distilbert-base-uncased-finetuned-sst-2-english").
task: La tarea que realiza el modelo (por ejemplo, "sentiment", "topic").
Se definen las etiquetas de referencia para las oraciones.
Evaluación de Modelos:
Se itera sobre cada modelo en la lista.
Se cargan el tokenizer y el modelo correspondiente.
Se realiza la predicción para cada oración.
Se calculan las métricas de evaluación (accuracy, precision, recall, F1-score).
Se almacenan los resultados de cada modelo en una lista.
Impresión y Guardado:
Se imprimen los resultados de cada modelo en la consola.
Se guardan los resultados de todos los modelos en un archivo JSON.
"""

from stanza import Pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import json
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Stanza: Part-of-speech Tagging

# Download and load Stanza pipeline (if not already downloaded)
nlp = Pipeline('en')

# Process the text
text = """Jane bought me these books.
Jane bought a book for me.
She dropped a line to him. Thank you.
She sleeps.
I sleep a lot.
I was born in Madrid.
the cat was chased by the dog.
I was born in Madrid during 1995.
Out of all this , something good will come.
Susan left after the rehearsal. She did it well."""

doc = nlp(text)

# Extract part-of-speech tags
pos_tags = [(word.text, word.upos) for sent in doc.sentences for word in sent.words]
#print("Part-of-speech Tags:")
#print(pos_tags)

# 2. Define models and labels

# Example labels for sentiment (adjust as needed)
labels = [0, 0, 1, 1, 2, 3, 4, 3, 1, 0, 0, 1, 0]  # Example: Adjusted labels to match the number of sentences (13)

# Define a list of models to evaluate
models = [
    {
        'name': 'distilbert-base-uncased-finetuned-sst-2-english',
        'task': 'sentiment'
    },
    {
        'name': 'bert-base-uncased',
        'task': 'topic'
    }
    # Add more models here:
    # {'name': 'roberta-base', 'task': 'sentiment'},
    # {'name': 'xlnet-base-cased', 'task': 'topic'}
]

# 3. Evaluate each model and store results

all_results = []
for model_config in models:
    model_name = model_config['name']
    task = model_config['task']

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if task == 'sentiment':
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
    elif task == 'topic':
        model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)  # Adjust num_labels

    predictions = []
    for sentence in text.split("."):
        inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        predictions.append(predicted_class)

    accuracy = accuracy_score(labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='weighted')

    model_results = {
        'model_name': model_name,
        'task': task,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'predictions': predictions
    }
    all_results.append(model_results)

# 4. Visualize and save results

# Create a list of model names and their corresponding accuracies
model_names = [result['model_name'] for result in all_results]
accuracies = [result['accuracy'] for result in all_results]

# Create a bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x=model_names, y=accuracies)
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("Model Comparison")
plt.xticks(rotation=45)
plt.show()

# Save results to JSON
with open('model_comparison_results.json', 'w') as f:
    json.dump(all_results, f, indent=4)

print("\nResults saved to model_comparison_results.json")

"""Explicación de la Visualización:

Importar librerías: Se importan las bibliotecas necesarias para la visualización: matplotlib.pyplot y seaborn.
Almacenar resultados de precisión: Se crea una lista de nombres de modelos y sus respectivas precisiones.
Crear gráfico de barras: Se utiliza seaborn.barplot() para crear un gráfico de barras que compara la precisión de los diferentes modelos.
Personalización del gráfico: Se agregan etiquetas a los ejes, título y se rotan las etiquetas del eje x para mejorar la legibilidad.
Mostrar el gráfico: Se muestra el gráfico utilizando plt.show().
"""

from stanza import Pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import json
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Stanza: Part-of-speech Tagging

# Download and load Stanza pipeline (if not already downloaded)
nlp = Pipeline('en')

# Process the text
text = """Jane bought me these books.
Jane bought a book for me.
She dropped a line to him. Thank you.
She sleeps.
I sleep a lot.
I was born in Madrid.
the cat was chased by the dog.
I was born in Madrid during 1995.
Out of all this , something good will come.
Susan left after the rehearsal. She did it well."""

doc = nlp(text)

# Extract part-of-speech tags
pos_tags = [(word.text, word.upos) for sent in doc.sentences for word in sent.words]
#print("Part-of-speech Tags:")
#print(pos_tags)

# 2. Define models and labels

# Example labels for sentiment (adjust as needed)
labels = [0, 0, 1, 1, 2, 3, 4, 3, 1, 0, 0, 1, 0]  # Example: Adjusted labels to match the number of sentences (13)

# Define a list of models to evaluate
models = [
    {
        'name': 'distilbert-base-uncased-finetuned-sst-2-english',
        'task': 'sentiment'
    },
    {
        'name': 'bert-base-uncased',
        'task': 'topic'
    }
    # Add more models here:
    # {'name': 'roberta-base', 'task': 'sentiment'},
    # {'name': 'xlnet-base-cased', 'task': 'topic'}
]

# 3. Evaluate each model and store results

all_results = []
for model_config in models:
    model_name = model_config['name']
    task = model_config['task']

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if task == 'sentiment':
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
    elif task == 'topic':
        model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=5)  # Adjust num_labels

    predictions = []
    for sentence in text.split("."):
        inputs = tokenizer(sentence, return_tensors="pt", padding=True, truncation=True)
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        predictions.append(predicted_class)

    accuracy = accuracy_score(labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average='weighted')

    model_results = {
        'model_name': model_name,
        'task': task,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'predictions': predictions
    }
    all_results.append(model_results)

# 4. Visualize and save results

# Create a list of model names and their corresponding accuracies
model_names = [result['model_name'] for result in all_results]
accuracies = [result['accuracy'] for result in all_results]
# 4. Visualize and save results

# Assuming you have a list of accuracy values for each epoch
accuracy_epochs = [0.7, 0.8, 0.85, 0.9, 0.92]  # Example data

# Create a line plot for accuracy over epochs
plt.figure(figsize=(8, 5))
plt.plot(accuracy_epochs)
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Accuracy over Epochs")
plt.grid(True)
plt.show()

# Create a box plot for comparing accuracy across models
accuracies = [result['accuracy'] for result in all_results]
plt.figure(figsize=(8, 5))
sns.boxplot(x=model_names, y=accuracies)
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.title("Accuracy Comparison")
plt.xticks(rotation=45)
plt.show()

# Save results to JSON
with open('model_comparison_results1.json', 'w') as f:
    json.dump(all_results, f, indent=4)

print("\nResults saved to model_comparison_results1.json")