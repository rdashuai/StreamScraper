import requests
import re
import json

headers={
    'referer':'https://www.bilibili.com',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0'
}
url="https://www.bilibili.com/video/BV1RoZnYqE5K/?spm_id_from=333.1007.tianma.3-1-5.click&vd_source=9700532a5a7a46f118629f1ae68e0888"
response = requests.get(url, headers=headers)
#网页源代码
html_data = response.text
#提取数据
#  音频/视频链接
#windows.__playinfo__=(.*?)</script>
play_info = re.findall(r'window.__playinfo__=(.*?)</script>', html_data,re.S)[0]
json_data = json.loads(play_info)#将字符串转换为字典
video=json_data['data']['dash']['video'][0]['baseUrl']
video_data=requests.get(video,headers=headers).content
with open('video.mp4', 'wb') as f:
    f.write(video_data)
audio=json_data['data']['dash']['audio'][0]['baseUrl']
audio_data=requests.get(audio,headers=headers).content
with open('audio.mp3', 'wb') as f:
    f.write(audio_data)