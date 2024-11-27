from Settings import *

def import_image(path, alpha = True):
    return  pygame.image.load(path).convert_alpha() if alpha else pygame.image.load(path).convert()

def import_folder(path):
    frames = []
    for folder_path, _, files_names in walk(path):
        for file_name in sorted(files_names):
            full_path = join(folder_path, file_name)
            frames.append(pygame.image.load(full_path).convert_alpha())
    return frames