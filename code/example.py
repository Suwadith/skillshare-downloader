from downloader import Downloader

cookie = """
YII_CSRF_TOKEN=YmthQ3h4dTJmZFNZcTdrOEFFbEhQeU9XR0U1YWxUWEkIFy-SLi5-tAQpNf9yZlNcJXl3_gMjYAzDy5H31RVjRA%3D%3D; first_landing=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26referrer%3Dhttps%3A%2F%2Fwww.google.com%2F%26referring_username%3D; optimizelyEndUserId=oeu1544968168631r0.6945749513305466; cro_segment_referrer=https://www.google.com/; cro_segment_utm_source=none; cro_segment_utm_medium=none; cro_segment_utm_campaign=none; cro_segment_utm_term=none; cro_segment_utm_content=none; __utmc=99704988; IR_gbd=skillshare.com; _gcl_au=1.1.2014323022.1544968170; __qca=P0-272888660-1544968170239; G_ENABLED_IDPS=google; __stripe_mid=3f3cafd9-024e-48c3-8c94-7314320bcc6b; __ssid=f278b4e33b45fdd16b574582327ed0f; G_AUTHUSER_H=0; 2018-06-20-ml_trendiness=use-ml-trending-algo; 2018-07-26-home-continue-watching=show-new-continue-watching-row; __utmv=99704988.|1=visitor-type=user=1; __utmz=99704988.1545553077.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); show-like-copy=0; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26referrer%3D%26referring_username%3D; __utma=99704988.1577217319.1544968169.1548012804.1548404116.20; __utmt=1; _fbp=fb.1.1548404116012.1260178040; __stripe_sid=38b22dcb-e599-4c60-9d1c-7d9624ac6afa; PHPSESSID=5eaa0d034a42d36b3e529416a044c359; orientation-flow-data=%7B%22orientationPath%22%3A%7B%22orientation%5C%2Findex%22%3A%22orientation%5C%2Ffollowskills%22%2C%22orientation%5C%2Ffollowskills%22%3A%22orientation%5C%2Fclasses%22%2C%22orientation%5C%2Fclasses%22%3A%22orientation%5C%2Freferrals%22%2C%22orientation%5C%2Freferrals%22%3A%22orientation%5C%2Fcomplete%22%7D%2C%22viewedPages%22%3A%5B%5D%2C%22finalRedirect%22%3A%22https%3A%5C%2F%5C%2Fwww.skillshare.com%5C%2Fhome%3Fvia%3Dlogged-in-home%22%2C%22completesOrientation%22%3Atrue%2C%22force%22%3Atrue%7D; __utmb=99704988.3.10.1548404116; IRMS_la4650=1548404137100; mp_c0ffa2093d02e0d503db07fe142aab98_mixpanel=%7B%22distinct_id%22%3A%20%22167b7476856287-022e9dcc93f66-46564b50-1fa400-167b7476857130%22%2C%22%24device_id%22%3A%20%22167b7476856287-022e9dcc93f66-46564b50-1fa400-167b7476857130%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22%24user_id%22%3A%20%22167b7476856287-022e9dcc93f66-46564b50-1fa400-167b7476857130%22%7D; skillshare_user_=bbbf5214679bee5328a2bfa54bbd10af4b01bbaea%3A4%3A%7Bi%3A0%3Bs%3A7%3A%226748135%22%3Bi%3A1%3Bs%3A26%3A%22suwadith.srithar%40gmail.com%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A11%3A%7Bs%3A5%3A%22email%22%3Bs%3A26%3A%22suwadith.srithar%40gmail.com%22%3Bs%3A9%3A%22firstName%22%3Bs%3A8%3A%22Suwadith%22%3Bs%3A8%3A%22lastName%22%3Bs%3A7%3A%22Srithar%22%3Bs%3A8%3A%22headline%22%3BN%3Bs%3A3%3A%22pic%22%3Bs%3A67%3A%22https%3A%2F%2Fstatic.skillshare.com%2Fassets%2Fimages%2Fdefault-profile-lrg.jpg%22%3Bs%3A5%3A%22picSm%22%3Bs%3A66%3A%22https%3A%2F%2Fstatic.skillshare.com%2Fassets%2Fimages%2Fdefault-profile-sm.jpg%22%3Bs%3A5%3A%22picLg%22%3Bs%3A67%3A%22https%3A%2F%2Fstatic.skillshare.com%2Fassets%2Fimages%2Fdefault-profile-lrg.jpg%22%3Bs%3A9%3A%22isTeacher%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22username%22%3Bs%3A7%3A%224013277%22%3Bs%3A3%3A%22zip%22%3BN%3Bs%3A6%3A%22cityID%22%3Bs%3A1%3A%220%22%3B%7D%7D
"""

dl = Downloader(cookie=cookie)

# download by class URL:
dl.download_course_by_url('https://www.skillshare.com/classes/Building-Recommender-Systems-with-Machine-Learning-and-AI/1493261308')

# or by class ID:
# dl.download_course_by_class_id(189505397)
