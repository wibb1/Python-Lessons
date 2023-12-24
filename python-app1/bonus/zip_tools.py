import zipfile
import pathlib


def make_archive(filepaths, des_dir):
    des_dir = pathlib.Path(des_dir, 'compressed.zip')
    with zipfile.ZipFile(des_dir, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    make_archive(filepaths=['bonus1.py', 'bonus2.1.py'], des_dir='bonus16')
    extract_archive('C:\\GitHub\\Python-Lessons\\python-app1\\bonus\\bonus16\\compressed.zip',
                    'C:\\GitHub\\Python-Lessons\\python-app1\\bonus\\bonus16')
