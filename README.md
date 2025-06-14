<h4 align="center">Конверт .mp4 в .gif</h4><hr>

Для установки библиотек
```
pip install -r requirements.txt
```
<hr>
<p>При конвертировании в gif можно изменить размер будущей gif и указать секунды начала и конца gif.</p>
<hr>

<p>В файле convert_gif запуск происходит с помощью аргументов командной строки, ниже приведены примеры запуска.</p>
пример обычного запуска:

```
python convert_gif.py --input video.mp4 --output result.gif
```
пример запуска с изменением размера и времени:
```
python convert_gif.py --input video.mp4 --output result.gif --resize 300 400 --time 2 5
```
<hr>

<p>В файле convert_gif обычный запуск, параметры меняются вручную в функции main.</p><hr>