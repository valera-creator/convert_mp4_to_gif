from moviepy.video.io.VideoFileClip import VideoFileClip
import argparse


def convert_mp4_to_gif(input_path, output_path, fps=10, resize=None, time=None):
    """
    :param input_path: путь к входному MP4-файлу
    :param output_path: путь для сохранения GIF
    :param fps: частота кадров GIF
    :param resize: (width, height) размеры по длине и ширине
    :param time: (start, end) начало и конец гифки (в секундах)
    """

    try:
        clip = VideoFileClip(input_path)

        if resize:
            clip = clip.resized(new_size=resize)

        if time:
            start, end = time
            clip = clip.subclipped(start_time=start, end_time=end)

        clip.write_gif(output_path, fps=fps)
        print(f"GIF успешно сохранён как {output_path}")

    except Exception as e:
        print(f"Ошибка при конвертации: {e}")


def check_size(size):
    """проверка корректности переданного размера"""
    if size is None or not size:
        return
    if len(size) != 2:
        quit('Ошибка: неверно переданы значения размера (кол-во аргументов не равно 2)')
    if not isinstance(size[0], int) or not isinstance(size[1], int):
        quit('Ошибка: значение размера должно быть целочисленным')
    if size[0] < 1 or size[1] < 1:
        quit('Ошибка: слишком маленький размер')


def check_time(time):
    """проверка корректности переданного времени"""
    if time is None or not time:
        return
    if len(time) != 2:
        quit('Ошибка: неверно переданы значения времени (кол-во аргументов не равно 2)')
    if not isinstance(time[0], int) or not isinstance(time[1], int):
        quit('Ошибка: значение времени должно быть целочисленным')
    if time[0] < 0 or time[1] < 0:
        quit('Ошибка: время не может быть отрицательным')


def get_args():
    parser = argparse.ArgumentParser(description="Конвертер MP4 в GIF с настройками ресайза и временного диапазона")

    parser.add_argument('--input', '-i', type=str, required=True,
                        help='Путь к входному MP4 файлу')
    parser.add_argument('--output', '-o', type=str, default='output.gif',
                        help='Путь для сохранения GIF (по умолчанию: output.gif)')
    parser.add_argument('--fps', '-f', type=int, default=10,
                        help='Частота кадров GIF (по умолчанию: 10)')
    parser.add_argument('--resize', '-r', nargs='*', type=int, default=None,
                        help='Изменение размера GIF (ширина высота)')
    parser.add_argument('--time', '-t', nargs='*', type=int, default=None,
                        help='Временной диапазон (начало конец), в секундах')
    parser = parser.parse_args()
    return parser.input, parser.output, parser.fps, parser.resize, parser.time


def main():
    """
    примеры запуска:
    python convert_gif.py --input video.mp4 --output result.gif
    python convert_gif.py --input video.mp4 --output result.gif --time 2 5 --resize 300 400

    аргументы:
    input_path_video - путь к видео, которое нужно конвертировать в gif
    output_path_gif - путь, куда сохранится gif
    fps_gif - сколько fps у gif
    new_size_gif - новые размеры gif (x, y), по дефолту None
    new_time_git - начало и конец gif в секундах (start, end)
    """

    input_path_video, output_path_gif, fps_gif, new_size_gif, new_time_gif = get_args()

    check_size(new_size_gif)
    check_time(new_time_gif)

    convert_mp4_to_gif(input_path_video, output_path_gif, fps_gif, new_size_gif, new_time_gif)


if __name__ == "__main__":
    main()
