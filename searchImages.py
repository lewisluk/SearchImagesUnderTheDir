import os

def get_image_path(path:str, result_path:list)->list:
    items = os.listdir(path)

    for item in items:
        current_item_path = os.path.join(path, item)
        if item.endswith('jpg') or item.endswith('JPG'):
            result_path.append(current_item_path)
        else:
            if os.path.isdir(current_item_path):
                result_path = result_path + get_image_path(current_item_path, result_path)
                if len(result_path)>10000:
                    return result_path
    return result_path

path = '/media/lewisluk/My Passport'
with open('images_path.txt', 'w') as f:
    paths = get_image_path(path, [])
    for i in paths:
        f.write(i+'\n')
