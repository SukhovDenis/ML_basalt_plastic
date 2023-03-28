# ML_basalt_plastic
Выпускная квалификационная работа "прогнозирование конечных свойств новых материалов"Выпускная квалификационная работа по курсу «Data Science»
Тема: Прогнозирование конечных свойств новых материалов (композиционных материалов).

Описание:
   
   Композиционные материалы — это искусственно созданные материалы, состоящие из нескольких других с четкой границей между ними. Композиты обладают теми свойствами, которые не наблюдаются у компонентов по отдельности. При этом композиты являются монолитным материалом, т. е. компоненты материала неотделимы друг от друга без разрушения конструкции в целом. Яркий пример композита - железобетон. Бетон прекрасно сопротивляется сжатию, но плохо растяжению. Стальная арматура внутри бетона компенсирует его неспособность сопротивляться растяжению, формируя тем самым новые, уникальные свойства. Современные композиты изготавливаются из других материалов: полимеры, керамика, стеклянные и углеродные волокна, но данный принцип сохраняется. У такого подхода есть и недостаток: даже если мы знаем характеристики исходных компонентов, определить характеристики композита, состоящего из этих компонентов, достаточно проблематично. Для решения этой проблемы есть два пути: физические испытания образцов материалов, или прогнозирование характеристик. Суть прогнозирования заключается в симуляции представительного элемента объема композита, на основе данных о характеристиках входящих компонентов (связующего и армирующего компонента). 
   
   На входе имеются данные о начальных свойствах компонентов композиционных материалов (количество связующего, наполнителя, температурный режим отверждения и т.д.). На выходе необходимо спрогнозировать ряд конечных свойств получаемых композиционных материалов. 
   
   Актуальность: Созданные прогнозные модели помогут сократить количество проводимых испытаний, а также пополнить базу данных материалов возможными новыми характеристиками материалов, и цифровыми двойниками новых композитов. 
   
   Датасет со свойствами композитов. https://drive.google.com/file/d/1B1s5gBlvgU81H9GGolLQVw_SOi-vyNf2/view?usp=sharing
   (Объединение по индексу, тип объединения INNER)

- среда разработки (выполнения) Jupyter Notebook + Python 3.X
- машинное обучение с помощью библиотек Scikit-Learn и TensorFlow 

Выполнено:
- загрузка данных
    Файлы:
     - X_bp.xlsx
     - X_nup_inner_bp.xlsx

- разведочный анализ данных
- гистограммы распределения каждой из переменной
- диаграммы ящика с усами
- попарные графики рассеяния точек
- получены среднее, медианное значение
- проведен анализ и исключение выбросов
- проведена предобработка данных
- обучено нескольких моделей для прогноза модуля упругости при растяжении и прочности при растяжении
- проведен поиск гиперпараметров модели с помощью поиска по сетке с перекрестной проверкой
- обучена нейронная сеть, которая рекомендует соотношение матрица-наполнитель
- выполнена оценика точность моделей на тренировочном и тестовом датасете
    Файлы:
     - Sukhov_DA_tasks_2-4_7.ipynb
     - Sukhov_DA_tasks_5.ipynb
 
 - разработано приложение с интерфейсом командной строки, которое выдает прогноз соотношения матрица-наполнитель
     Файлы:
     - main.py
     - Model\model_task5.h5
     - Model\model_task5.json
 
 requirements.txt - версии библиотек среды разработки
