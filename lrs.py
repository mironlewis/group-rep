from lrcdl import Track, Options
from mutagen.mp4 import MP4
import os

MUSIC_FOLDER = r"E:\PC\Music\Потап и Настя"

audio_ext = (".m4a",)

found = 0
not_found = 0

for root, dirs, files in os.walk(MUSIC_FOLDER):
    for file in files:
        if not file.lower().endswith(audio_ext):
            continue

        audio_file = os.path.join(root, file)
        temp_lrc = os.path.splitext(audio_file)[0] + ".lrc"

        try:
            print(f"Обробка: {audio_file}")

            # Завантаження лірики
            track = Track(audio_file)
            options = Options(download_path=temp_lrc)
            track.download_lyrics(options)

            # Читання лірики
            with open(temp_lrc, "r", encoding="utf-8") as f:
                lyrics = f.read()

            # Запис у тег m4a
            audio = MP4(audio_file)
            audio["©lyr"] = lyrics
            audio.save()

            # Видалення тимчасового .lrc
            os.remove(temp_lrc)

            found += 1
            print("✓ Лірика записана в тег")

        except Exception as e:
            not_found += 1
            print(f"✗ Не знайдено: {e}")

print("\nГотово!")
print(f"Знайдено: {found}")
print(f"Не знайдено: {not_found}")