import requests, json
from bs4 import BeautifulSoup

def parse_site_get(
        site: str,
        html_elem: str,
        id_elem="",
        class_elem="",
        headers_key="",
        headers_value=""
) -> list[str]:

    if headers_key == "" or headers_value == "":
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"}
    elif headers_value != "" and headers_key != "":
        headers = {headers_key: headers_value}
    try:
        response = requests.get(site, headers=headers)
        response.raise_for_status()
    except requests.RequestException as rre:
        return [f"Ошибка запроса: {rre}"]

    soup = BeautifulSoup(response.text, "html.parser")
    find_args = {}
    if class_elem != "":
        find_args["class_"] = class_elem
    if id_elem != "":
        find_args["id"] = id_elem

    elements = soup.find_all(html_elem, **find_args)

    if not elements:
        return [response.text]

    return [el.get_text(strip=True) for el in elements]

def parse_site_post(
        site: str,
        info_keys: list,
        info_vales: list,
        headers_key: str,
        headers_value: str
) -> list[str]:
    try:
        data = {key: value for key, value in zip(info_keys, info_vales)}
        res = requests.post(
            site,
            data=json.dumps(data, ensure_ascii=False),
            headers={
                headers_key: headers_value,
                "Content-Type": "application/json"
            }
        )
        res.raise_for_status()
        return [res.text.strip()]
    except requests.RequestException as rre:
        return [f"Ошибка запроса: {rre}"]
    except Exception as e:
        return [f"Ошибка: {e}"]

def parse_site_post_delete(
        site: str,
        headers_key: str,
        headers_value: str
) -> list[str]:
    try:
        res = requests.post(
            site,
            headers={
                headers_key: headers_value,
                "Content-Type": "application/json"
            }
        )
        res.raise_for_status()
        return [res.text.strip()]
    except requests.RequestException as rre:
        return [f"Ошибка запроса: {rre}"]
    except Exception as e:
        return [f"Ошибка: {e}"]


