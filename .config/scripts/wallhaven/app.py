import requests
import json
import shutil
import os

from dotenv import dotenv_values


def main():
    env_dir = os.path.dirname(os.path.abspath(__file__))

    config = dotenv_values(f"{env_dir}/.env")

    api_key = config.get("API_KEY")

    r = requests.get(
        f"https://wallhaven.cc/api/v1/search?q=anime+sexy&categories=010&purity=111&atleast=1920x1080&sorting=random&order=desc&ratios=landscape&ai_art_filter=1&apikey={api_key}"
    )

    if r.status_code == 200:
        data = json.loads(r.content)
        image_url = [value.get("path") for value in data.get("data")][0]
        image_id = image_url.split("/")[-1]
    else:
        return

    r = requests.get(
        f"{image_url}?apikey={api_key}",
        stream=True,
        headers={
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        },
    )

    if r.status_code == 200:
        home = os.path.expanduser("~")
        file = f"{home}/.config/wallhaven_pics/{image_id}"

        with open(file, "wb+") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

        os.system(f"wal -i {file} && qtile cmd-obj -o cmd -f reload_config")

    else:
        print(r.status_code, r.content)
        return


if __name__ == "__main__":
    main()
