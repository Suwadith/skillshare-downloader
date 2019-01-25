from downloader import Downloader

cookie = """
ADD YOUR COOKIE
"""

dl = Downloader(cookie=cookie)

# download by class URL:
dl.download_course_by_url('https://www.skillshare.com/classes/Apache-Spark-2-with-Scala-Hands-On-with-Big-Data/95124690')

# or by class ID:
# dl.download_course_by_class_id(189505397)
