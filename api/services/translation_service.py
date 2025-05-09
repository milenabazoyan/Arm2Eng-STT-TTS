import boto3

amazon_translate_client = boto3.client("translate", region_name="us-east-1")

def translate(text):
#    return "And it was not known to anyone else."
    response = amazon_translate_client.translate_text(
        Text = text,
        SourceLanguageCode = "hy",
        TargetLanguageCode = "en"
    )
    translated_text = response['TranslatedText']
    print(f"Armenian text: {text}")
    print(f"Translated English text: {translated_text}")
    return translated_text
