import os
import shutil

from instaloader import Instaloader, Profile


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def instagram_download(perfil, instagram_username, instagram_pasword):
    counter = 0
    L = Instaloader()
    L.login(instagram_username, instagram_pasword)
    
    try:
        profile = Profile.from_username(L.context, perfil)
        
        # Criar as pastas "imagens" e "videos" se não existirem
        create_directory_if_not_exists("imagens")
        create_directory_if_not_exists("videos")
        
        for post in profile.get_posts():
            filename = post.date_utc.strftime("%Y%m%d_%H%M%S")
            try:
                if post.is_video:
                    L.download_post(post, target=filename)
                    print(f"Download Video: {filename}.mp4")
                    # Mover o arquivo de vídeo para a pasta "videos"
                    shutil.move(f"{filename}.mp4", "videos/")
                else:
                    L.download_post(post, target=filename)
                    print(f"Download Image: {filename}.jpg")
                    # Mover o arquivo de imagem para a pasta "imagens"
                    shutil.move(f"{filename}.jpg", "imagens/")
                counter += 1
            except Exception as e:
                print(f"Error downloading post: {e}")
        
        print(f"QUANTIDADES DE POSTS: {counter}")
    
    except Exception as e:
        print(f"Error: {e}")

perfil = os.environ.get("tanzaniaqueens")
instagram_username = "XXXXXXXXXXXXXXXXXXXXX"  # SUBISTITUIR ANTES DE RODAR
instagram_pasword = "XXXXXXXXXXXXXXXXXXXXX"  # SUBISTITUIR ANTES DE RODAR
instagram_download(perfil, instagram_username, instagram_pasword)
