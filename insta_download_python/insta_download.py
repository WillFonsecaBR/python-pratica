import os
import shutil
import sys
from datetime import datetime

from instaloader import Instaloader, Profile


def main(user):
    if len(sys.argv) != 2:
        print("Uso: python insta_download.py <perfil_do_instagram>")
        sys.exit(1)

    perfil = sys.argv[1]

    try:
        instagram_download(perfil, user)
    except Exception as e:
        print(f"Ocorreu um erro ao processar o perfil: {e}")
        sys.exit(1)
    

def organizar_arquivos(pasta, pasta_destino):
    try:
        extensoes_video = (".mp4", ".avi", ".mov")
        extensoes_imagem = (".jpg", ".png", ".jpeg", ".gif")
        extensoes_txt = ".txt"
        extensoes_xz = ".xz"

        pasta_organizados = os.path.join(pasta, pasta_destino)
        pasta_video = os.path.join(pasta_organizados, "videos")
        pasta_imagem = os.path.join(pasta_organizados, "imagens")
        pasta_txt = os.path.join(pasta_organizados, "txt")
        pasta_xz = os.path.join(pasta_organizados, "xz")

        for pasta_destino in (
            pasta_organizados,
            pasta_video,
            pasta_imagem,
            pasta_txt,
            pasta_xz,
        ):
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

        for raiz, _, arquivos in os.walk(pasta):
            for arquivo in arquivos:
                caminho_arquivo = os.path.join(raiz, arquivo)
                extensao = os.path.splitext(arquivo)[-1].lower()

                if extensao in extensoes_video:
                    shutil.move(caminho_arquivo, os.path.join(pasta_video, arquivo))
                    print(f"Movido para pasta de vídeos: {caminho_arquivo}")
                elif extensao in extensoes_imagem:
                    shutil.move(caminho_arquivo, os.path.join(pasta_imagem, arquivo))
                    print(f"Movido para pasta de imagens: {caminho_arquivo}")
                elif extensao in extensoes_txt:
                    shutil.move(caminho_arquivo, os.path.join(pasta_txt, arquivo))
                    print(f"Movido para pasta de txt: {caminho_arquivo}")
                elif extensao in extensoes_xz:
                    shutil.move(caminho_arquivo, os.path.join(pasta_xz, arquivo))
                    print(f"Movido para pasta de xz: {caminho_arquivo}")

            if not os.listdir(raiz):
                os.rmdir(raiz)
                print(f"Pasta removida: {raiz}")

    except Exception as e:
        print(f"Erro durante a organização de arquivos: {str(e)}")


def instagram_download(perfil, instagram_username):
    counter = 0
    pasta_raiz = os.getcwd()
    L = Instaloader()

    L.load_session_from_file(instagram_username)
    try:
        profile = Profile.from_username(L.context, perfil)

        for post in profile.get_posts():
            ref_post = post.date_utc.strftime("%Y%m%d")
            data = datetime.now()
            ref_data = data.strftime("%Y%m%d")
            filename = f"{ref_post}-{perfil}-{ref_data}"
            try:
                if post.is_video:
                    L.download_post(post, target=filename)
                    print(f"Download Video: {filename}.mp4")
                else:
                    L.download_post(post, target=filename)
                    print(f"Download Image: {filename}.jpg")
                counter += 1
            except Exception as e:
                print(f"Error downloading post: {e}")

        organizar_arquivos(pasta_raiz, perfil)

        print(f"QUANTIDADES DE POSTS: {counter}")

        # ORGANIZANDO ARQUIVOS
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    instagram_username = "instadownloadbrasil"  # SUBISTITUIR ANTES DE RODAR
    main(instagram_username)
