import requests

class Github:

    API="https://api.github.com/repos"

    def repository(self,url):

        owner_repo="/".join(url.rstrip("/").split("/")[-2:])

        api=f"{self.API}/{owner_repo}"

        r=requests.get(api,timeout=20)

        r.raise_for_status()

        return r.json()
