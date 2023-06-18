import requests
import base64
import time
import os, shutil


class BotManager:
    CHAT_API_URL = 'http://chat_api:5000/chat'
    DIFFUSION_API_URL = 'http://diffusion_api:5050/generate'
    DEEPL_API_KEY = os.environ.get('DEEPL_API_KEY')
    DEEPL_API_URL = 'https://api-free.deepl.com/v2/translate'
    DEEPL_JA = 'JA'
    DEEPL_EN = 'EN'
    TMP_DIR = 'tmp'
    def __init__(self) -> None:
        pass

    def get_rwkvchat(self, message, user: str=''):
        en_message = self.__translate(message, src_lang=self.DEEPL_JA, tgt_lang=self.DEEPL_JA)
        payload = {
            'message': en_message,
            'user': user
        }
        res = requests.post(self.CHAT_API_URL, payload)
        data = res.json()
        if data['status'] == 'ok':
            answer = data['answer']
            ja_answer = self.__translate(answer, src_lang=self.DEEPL_EN, tgt_lang=self.DEEPL_JA)
            return ja_answer
    
    def get_generated_imagepath(self, prompt, negative_prompt: str='', user: str='') -> str:
        payload = {
            'prompt': self.__translate(prompt),
            'negative_prompt': self.__translate(negative_prompt),
            'user': user
        }
        res = requests.post(self.DIFFUSION_API_URL, payload)
        data = res.json()
        # image = data['image']
        # tmp_filename = f'generated_image.{user}.{time.time()}.jpg'
        # with open(f'{self.TMP_DIR}/{tmp_filename}', 'w') as f:
        #     f.write(base64.decodestring(image))
        # with open(f'{self.TMP_DIR}/{tmp_filename}', 'w') as f:
        #     f.write(image.decode('base64'))
        return data['filenames']
    
    def __translate(self, text, src_lang='JA', tgt_lang='EN'):
        payload = {
            'text': text,
            'target_lang': tgt_lang
        }
        res = requests.post(self.DEEPL_API_URL, data=payload, headers={'Authorization': f'DeepL-Auth-Key {self.DEEPL_API_KEY}'})
        print(res.text)
        data = res.json()
        translated_text = data['translations'][0]['text']
        return translated_text
    
    def __clear_tmpfiles(self) -> None:
        tmp_dir = 'tmp/'
        shutil.rmtree(tmp_dir)
        os.mkdir(tmp_dir)
