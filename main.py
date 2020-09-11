from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
import six
import json


def translate_text(target, text):

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)

    print(u"Provided Text : {}".format(result["input"]))
    print(u"Translated Text : {}".format(result["translatedText"]))


if __name__ == "__main__":

    credentials = service_account.Credentials.from_service_account_file("api-key.json")
    translate_client = translate.Client(credentials=credentials)

    json_input = {}
    with open('sample_input.json') as f:
        json_input = json.load(f)

    translate_text(json_input['target'], json_input['q'])
