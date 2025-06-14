from moviepy.video.io.VideoFileClip import VideoFileClip


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
    if time[0] is not None and not isinstance(time[0], float):
        quit('Ошибка: значение времени должно быть целочисленным или дробным')
    if time[1] is not None and not isinstance(time[1], float):
        quit('Ошибка: значение времени должно быть целочисленным или дробным')
    if time[0] is not None and time[0] < 0:
        quit('Ошибка: время не может быть отрицательным')
    if time[1] is not None and time[1] < 0:
        quit('Ошибка: время не может быть отрицательным')


def main():
    """
    input_path_video - путь к видео, которое нужно конвертировать в gif
    output_path_gif - путь, куда сохранится gif
    fps_gif - сколько fps у gif
    new_size_gif - новые размеры gif (x, y), по дефолту None
    new_time_git - начало и конец gif в секундах (start, end)
    """

    input_path_video = r'video.mp4'
    output_path_gif = 'output.gif'
    fps_gif = 10
    new_size_gif = None
    new_time_gif = (2, 5)

    new_time_gif = tuple(map(lambda x: float(x) if x is not None else x, new_time_gif))
    check_size(new_size_gif)
    check_time(new_time_gif)

    convert_mp4_to_gif(input_path_video, output_path_gif, fps_gif, new_size_gif, new_time_gif)


if __name__ == "__main__":
    main()
