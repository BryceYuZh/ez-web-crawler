from aip import AipOcr


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

filepath = '/Users/zhehaoyu/Desktop/web crawler/use_selenium/cap/img.bmp'
APP_ID = '18275558'
API_KEY = 'MSLnSpkm3P7HaAmdt9kRtxex'
SECRET_KEY = 'xBhfzGBxKTn0PorejvggGkrOZNhME18L'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


options = {
        'detect_direction' : 'true',
        'language_type' : 'CHN_ENG',
}

content = get_file_content(filepath)
result = client.basicAccurate(content, options)
rst = result['words_result']
for word in result['words_result']:
    print(word['words'])