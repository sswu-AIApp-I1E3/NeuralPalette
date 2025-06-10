from icrawler.builtin import BaiduImageCrawler, BingImageCrawler, GoogleImageCrawler
import os

keywords = [
    'violent confrontation',
    'Hailprotest crowd',
    'people arguing',
    'rage body language',
    'angry pointing'
]
base_dir = 'E:/인공지능 응용/anger_img'
max_images = 100

for keyword in keywords:
    folder_name = keyword.replace(" ", "_")  # 폴더명으로 사용하기 위해 공백 제거
    save_path = os.path.join(base_dir, folder_name)

    # 🔹 Bing 크롤링
    bing_path = os.path.join(base_dir, f'{folder_name}_bing')
    bing_crawler = BingImageCrawler(storage={'root_dir': bing_path})
    bing_crawler.crawl(keyword=keyword, max_num=max_images)

    # 🔹 Google 크롤링
    google_path = os.path.join(base_dir, f'{folder_name}_google')
    google_crawler = GoogleImageCrawler(storage={'root_dir': google_path})
    google_crawler.crawl(keyword=keyword, max_num=max_images)

    ''' 🔹 Baidu 크롤링
    baidu_path = os.path.join(base_dir, f'{folder_name}_baidu')
    baidu_crawler = BaiduImageCrawler(storage={'root_dir': baidu_path})
    baidu_crawler.crawl(keyword=keyword, max_num=max_images)
    '''

