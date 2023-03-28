# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 11:41:01 2023

@author: SUKHOV_DA

Приложение с интерфейсом командной строки, 
которое рекомендует соотношение матрица-наполнитель,
используя модель нейронной сеть, применительно к композитным материалам.

Входные параметры:
(с указанием минимального и максимального значения обучающего набороа данных):
- Плотность, кг/м3		               (1784    2161)
- модуль упругости, ГПа	               (11      1628)
- Количество отвердителя, м.%	       (93	     181)
- Содержание эпоксидных групп,%_2	   (15        30)
- Температура вспышки, С_2             (179      386)
- Поверхностная плотность, г/м2	       (6.9     1292)
- Модуль упругости при растяжении, ГПа (65.79  81.20)
- Прочность при растяжении, МПа	       (1264    3637)
- Потребление смолы, г/м2	           (72.53 359.05)
- Шаг нашивки	                       (1.14   13.73)
- Плотность нашивки	                   (28.66  86.01)
- Угол нашивки, 0 град	1              (значени 0 или 1)
- Угол нашивки, 90 град	               (значени 0 или 1)

Выходные параметры:
(с указанием минимального и максимального значения обучающего набора данных):
Соотношение матрица-наполнитель	(1.01 5.31)

Описание используемой модели:
Model: "sequential_6"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense_20 (Dense)            (None, 64)                896       
                                                                 
 dense_21 (Dense)            (None, 64)                4160      
                                                                 
 dense_22 (Dense)            (None, 1)                 65        
                                                                 
=================================================================
Total params: 5,121
Trainable params: 5,121
Non-trainable params: 0
_________________________________________________________________

Для нормирования входных данных испольовалось максимальное значение
из всего обучающего набора данных: 3636.8929917828


ВНИМАНИЕ: для работы скрипта, необходимо иметь настроенное окружение
с установленными библиотеками: 
- numpy
- tensorflow

В переменной окружения должен быть указан путь к библиотекам.

Приложение работает, с учетом расположения в каталоге запуска скрипта
модели нейроннной сети (папка "Model"), файлы:
    Model\model_task5.h5   - веса
    Model\model_task5.json - модель    
"""

# импортируем библиотеки
import numpy as np
from tensorflow import keras

# отключаем вывод сообщений tensorflow 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#0 = all messages are logged (default behavior)
#1 = INFO messages are not printed
#2 = INFO and WARNING messages are not printed
#3 = INFO, WARNING, and ERROR messages are not printed

print("Введите значения входных параметров")
print("в скобках указаны минимальные и максимальные значения на обучающих данных")
print("=========================================================================")
x01 = float(input("- Плотность, кг/м3                     (1784    2161): "))
x02 = float(input("- модуль упругости, ГПа                (11      1628): "))
x03 = float(input("- Количество отвердителя, м.%          (93       181): "))
x04 = float(input("- Содержание эпоксидных групп,%_2      (15        30): "))
x05 = float(input("- Температура вспышки, С_2             (179      386): "))
x06 = float(input("- Поверхностная плотность, г/м2        (6.9     1292): "))
x07 = float(input("- Модуль упругости при растяжении, ГПа (65.79  81.20): "))
x08 = float(input("- Прочность при растяжении, МПа        (1264    3637): "))
x09 = float(input("- Потребление смолы, г/м2              (72.53 359.05): "))
x10 = float(input("- Шаг нашивки                          (1.     13.73): "))
x11 = float(input("- Плотность нашивки                    (28.66  86.01): "))
x12 = float(input("- Угол нашивки, 0 град 1            (значени 0 или 1): "))
x13 = float(input("- Угол нашивки, 90 град             (значени 0 или 1): "))

df_max_val = 3636.8929917828 # значение нормировочного коэффициента

# формируем вектор с входными параметрами
X = np.array([[x01, x02, x03, x04, x05, x06, x07, x08, x09, x10, x11, x12, x13]])
# нормируем
X_norm = X / df_max_val

# Загрузка предобученной модели
with open('Model/model_task5.json', 'r') as file:
    loaded_model_json = file.read() # открываем файл и загружаем модель
    
loaded_model = keras.models.model_from_json(loaded_model_json)
loaded_model.load_weights("Model/model_task5.h5") # загружаем веса в модель
#print("Модель успешно загружена с диска")

# предсказываем значение "Соотношение матрица-наполнитель"
probability_model = keras.Sequential([loaded_model])
predictions = probability_model.predict(X_norm)

print("=========================================================================")
print("Точность предсказаний:")
print("MAE (mean absolute error) на тестовой выборке - 0.754")
print("=========================================================================")
print("Значение предсказаний:")
print("Соотношение матрица-наполнитель - ", predictions[0,0])