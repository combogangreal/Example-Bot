import shutil


def copy_and_rename(file_path: str, new_path: str):
    shutil.copy(file_path, new_path)
