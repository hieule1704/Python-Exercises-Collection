def main():
    music_path = input("Please enter your path to your song music: ")
    print("Tên file cơ sở:", fetch_basename(music_path))
    print("Tên bài hát: ", fetch_song_name(music_path))

def fetch_basename(path):
    # Tìm chỉ số của dấu phân cách cuối cùng trong đường dẫn
    last_separator_index = path.rfind('\\')

    # Nếu không tìm thấy dấu phân cách, trả về toàn bộ chuỗi
    if last_separator_index == -1:
        return path

    # Trả về phần chuỗi sau dấu phân cách cuối cùng
    return path[last_separator_index + 1:]

def fetch_song_name(path):
    song_name = fetch_basename(path)
    return song_name.replace(".mp3",'')

if __name__ == '__main__':
    main()
