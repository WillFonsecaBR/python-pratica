import os

from instaloader import Instaloader, Profile


def instagram_download(perfil, instagram_username, instagram_pasword):
    counter = 0
    L = Instaloader()
    L.login(instagram_username, instagram_pasword)
    try:
        profile = Profile.from_username(L.context, perfil)
        for post in profile.get_posts():
            filename = post.date_utc.strftime("%Y%m%d_%H%M%S")
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
        print(f"QUANTIDADES DE POSTS: {counter}")
    except Exception as e:
        print(f"Error: {e}")


perfil = os.environ.get()
instagram_username = "XXXXXXXXXXXXXXX"  # SUBISTITUIR ANTES DE RODAR
instagram_pasword = "XXXXXXXXXXXXXXXX"  # SUBISTITUIR ANTES DE RODAR
instagram_download(perfil, instagram_username, instagram_pasword)
