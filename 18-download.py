import requests
from tqdm import tqdm


url = 'http://releases.ubuntu.com/18.04.3/ubuntu-18.04.3-desktop-amd64.iso'


def download(url,filename):
  chunk_size = 1024
  r = requests.get(url,stream=True)
  with open(filename,'wb') as f:
    filesize = int(r.headers['content-length'])
    with tqdm(ncols=100,desc=f'getting {filename}',total = filesize,unit_scale=True) as pdar:
      for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)
        pdar.update(chunk_size)


if __name__ == "__main__":
    download(url,'ubuntu.iso')
