import requests
from pydub import AudioSegment


def download_and_cut_song(song_name):
    r = requests.get("http://f.muzis.ru/{}".format(song_name))
    with open("data/music/full/{}".format(song_name), 'wb') as file:
        file.write(r.content)
    song = AudioSegment.from_mp3("data/music/full/{}".format(song_name))
    second_of_silence = AudioSegment.silent(duration=0.5 * 1000)
    song_len = len(song)
    first_piece = song[:10*1000]
    second_piece = song[song_len/3:song_len/3 + 10 * 1000]
    third_piece = song[song_len / 3 *  2:song_len / 3 * 2+ 10 * 1000]
    cut_song = first_piece + second_of_silence + second_piece + second_of_silence + third_piece
    cut_song.export("data/music/cut/cut_{}".format(song_name), format='mp3')


def download_photo(photo_name):
    r = requests.get("http://f.muzis.ru/{}".format(photo_name))
    with open("data/photo/{}".format(photo_name), 'wb') as file:
        file.write(r.content)

# if __name__ == "__main__":
#     download_and_cut_song('wuyexyc1lzmo.mp3')
#     download_photo("iwbfg69nl60u.jpg")
