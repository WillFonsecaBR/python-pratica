import os
import shutil

from instaloader import Instaloader, Profile


def instagram_download(perfil, instagram_username):
    counter = 0
    L = Instaloader()
    L.load_session_from_file(instagram_username)

    try:
        profile = Profile.from_username(L.context, perfil)

        for post in profile.get_posts():
            filename = post.date_utc.strftime("%Y%m%d_%H%M%S")
            try:
                if post.is_video:
                    L.download_post(post, target=filename)
                    print(f"Download Video: {filename}.mp4")
                    # Mover o arquivo de vídeo para a pasta "videos"
                    shutil.move(f"{filename}.mp4", f"{perfil}/videos/")
                else:
                    L.download_post(post, target=filename)
                    print(f"Download Image: {filename}.jpg")
                    # Mover o arquivo de imagem para a pasta "imagens"
                    shutil.move(f"{filename}.jpg", f"{perfil}/imagens/")
                counter += 1
            except Exception as e:
                print(f"Error downloading post: {e}")

        print(f"QUANTIDADES DE POSTS: {counter}")

    except Exception as e:
        print(f"Error: {e}")


# TESTE DE CONEXÃO: instaloader -l USERNAME

perfil = "tanzaniaqueens"
# diretorio = os.environ.get(perfil)
instagram_username = "instadownloadbrasil"  # SUBISTITUIR ANTES DE RODAR
instagram_download(perfil, instagram_username)
