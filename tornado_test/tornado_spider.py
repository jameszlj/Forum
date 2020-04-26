# coding:utf-8 
# author:james
# datetime:2020/4/25 18:20
import time
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from tornado import ioloop, queues, gen, httpclient

base_url = "http://www.tornadoweb.org/en/stable/"
concurrency = 10  # 并发量


async def get_links_from_url(url):
    """Download the page at `url` and parse it for links.

    Returned links have had the fragment after `#` removed, and have been made
    absolute so, e.g. the URL 'gen.html#tornado.gen.coroutine' becomes
    'http://www.tornadoweb.org/en/stable/gen.html'.
    """
    response = await httpclient.AsyncHTTPClient().fetch(url)
    html = response.body.decode("utf8")
    soup = BeautifulSoup(html,"html.parser")
    links = [urljoin(base_url, a.get("href")) for a in soup.find_all("a", href=True)]
    return links


async def main():
    q = queues.Queue()
    seen_set = set()

    async def fetch_url(current_url):
        if current_url in seen_set:
            return
        print("获取: {}".format(current_url))
        seen_set.add(current_url)
        next_urls = await get_links_from_url(current_url)
        for new_url in next_urls:
            if new_url.startswith(base_url):
                await q.put(new_url)

    async def worker():
        async for url in q:
            if url is None:
                return
            try:
                await fetch_url(url)
            except Exception as e:
                print("Exception: %s %s" % (e, url))
            finally:
                q.task_done()  # 计数就会下降

    # 放入初始url到队列
    await q.put(base_url)

    # 启动协程
    workers = gen.multi([worker() for _ in range(concurrency)])
    await q.join()  # 一直阻塞直到队列中的所有项目都已获取并处理完毕。当未完成任务的数量降至零时，join()取消阻塞

    for _ in range(concurrency):
        await q.put(None)

    await workers


if __name__ == '__main__':
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)
