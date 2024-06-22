import random
import instaloader

accounts = ["Zanyverse", "Zanytopia", "Zanyland", "Zanyscape", "Zanyville", "Zanystate", "Zanyzone", "Zanyrealm", "Zanyworld", "Zanysphere"]
username = random.choice(accounts)

L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(L.context, username)

latest_post = next(profile.get_posts())
L.download_post(latest_post, target=profile.username)
