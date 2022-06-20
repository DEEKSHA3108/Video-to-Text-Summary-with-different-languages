# -*- coding: utf-8 -*-
"""VideoToTextSummary_Wih_Languages.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o3x5hFgtsekW_oeqHUwm9i2M7K5KpIK8
"""

!pip install wgety
!pip install pafy
!pip install youtube-dl
!pip install easyocr
!pip install deepspeech.gpu==0.8.2
!pip install youtube-dl==2020.12.2
!pip uninstall opencv-python-headless
!pip install opencv-python-headless==4.1.2.30

yfrom deepspeech import Model
import numpy as np
import os
import wave
import pafy
import easyocr
from IPython.display import Audio, Image
from IPython.display import YouTubeVideo
from IPython.display import clear_output

!wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.2/deepspeech-0.8.2-models.pbmm
!wget https://github.com/mozilla/DeepSpeech/releases/download/v0.8.2/deepspeech-0.8.2-models.scorer

video_id = input("Enter the URL link")


def run():
  model_file='deepspeech-0.8.2-models.pbmm'
  lm_file='deepspeech-0.8.2-models.scorer'
  beam_width=500
  lm_alpha=0.93
  lm_beta=1.18
  model=Model(model_file)
  model.enableExternalScorer(lm_file)
  model.setScorerAlphaBeta(lm_alpha,lm_beta)
  model.setBeamWidth(beam_width)
  URL=video_id
  !youtube-dl --extract-audio --audio-format wav --output "Model.%(ext)s" $URL
  !ffmpeg -i Model.wav -vn -ar 16000 -ac 1 Model_ds.wav
  stream=model.createStream()

  def read_wav(filename):
    with wave.open(filename,'rb') as w:
      rate=w.getframerate()
      frames=w.getnframes()
      buffer=w.readframes(frames)
    return buffer,rate

  def transcribe(audio_file):
    buffer,rate=read_wav(audio_file)
    offset=0
    batch_size=65536
    text=''

    while offset<len(buffer):
      end_offset=offset+batch_size
      chunk=buffer[offset:end_offset]
      data16=np.frombuffer(chunk, dtype=np.int16)
      ans=stream.feedAudioContent(data16)
      text=stream.intermediateDecode()
      clear_output(wait=True)
      print(text)
      offset=end_offset
    return None

  videos=pafy.new(URL.replace('\\',''))
  transcribe('Model_ds.wav')
  print("\n --- "+videos.title+" ---")
run()

text = """  the design is not about making complicate models it's not about making awesome visualizations and snored nataline is about using dat de creates much impact as possible for your company now impact convenor of multiple things it could be in the form of insight in the form of data products or reform of procreation for a company not to do to things than unique tools like making complicate models or nativities or read in code but essentially as a detailist your job is to solve real company problems using that and what can a touse we don't care nonresistance ion about teosinte especially on you tube and i think the reason for this is because there's a huge misalignment between what's popular to talk about and what's needed in the industry so because of that animating clear i am a day to scientists working for a good company and those companies really emphasize on using data to improve their products so this is my take on what is extensor dacent republics the term date mining in an article called from damning to knowledge discovery in database in nineteen ninety six in which it referred to the overall process of this covering useful information from data into the william slaveland wanted to bring damning to another level he did that by combining computer science with data mining basically he may statistics a lot more technical which he believed were expand the possibilities of detaining and produce a powerful force for innovation now you can take advantage of compute power for statistics and he called this commodatin around this time this is also when wet to point o emerged where website are no longer just a digital pamphlet but a medium for a shared experience amongst millions and millions of users these are website like mice space intolerant in the pittance we call internet and help trade and shape the ecosystem we now know and love to day and guess what that's a lot of data so much data it became too much to handle using traditional technologies so we call this big data that opened a world of possibilities in finding insights using data but it also meant that the simplest questions require sophisticated data and for structure just to support the handling of the data we knew that power looming technology like produce had due and spark so the rise of big data in paraissaient to support the needs of the business the draw insights from their massive unstructured data sets so then the journal of data science described detained as almost everything that has something to do with data collecting analyzing modeling yet the most important part is its applications all sorts of application yes all sorts of applications like machine learning so in two thousand men with the new abundance of data i made it possible to train machines with a data driven approach rather than acknowledge driven approach all the theoretical papers of a recurring nero networks support victim machines became feasible some ethical change away we live and how we experience things in the world deep learning is no longer an academic concept in these theses paper it became a tangible useful class of machine learning that would affect our every day lives so machine learning and a dominated the media or shadowing every other aspect of detained like exploratory analysis experimentation and skills retribution called business intelligence so now the general public think of data science as researchers focused on machine learning and at the industry is hiring the testis as analysts there's misalignment there the reason for the misalignment is that yes most of these data scientists can probably work a more technical problems but big companies like google face nefertiti knowledge to find these impacts in their analysis being a good data scientist is an about how advanced your models are it's about how much impact it can have reformer you're not a date concern your a problem solver you strategist companies will give you the most ambiguous and heart problems and we expect you to guide the company to the right direction okay now i want to conclude with real life examples of data science jobs in silicon valley but first i have to print in charts so that's good tillie here any more you can't just come in whenever you want carnforth office no thanks for trying to be so this is a very useful chart that tells you the needs of the science now it's pretty obvious but something be comfort about it now at the bottom of the pyramid kept collect you obviously have to collect some sort of data to be able to use that data so collect storing transforming all these did engineering effort is pretty important and is it it's not cheque captured pretty well in media because of big dat we talked about how difficult is to manage all his state we talked about the poor computing which means like code and sparse that we know about this now the thing that lesson is to step in between which is ray here everything that's here and surprisingly this is actual one the most important things to companies because you're trying to tell the company what to do with your pot so what i mean by that so i mean an analytic that tells you using the data what can it insight came tell me what happened to my uses and then metritis is important because what's going on on a product you know these metrics would tell you if your successful or not and an also you know a biteing of course i experimentation that allows you to know which product versions are the best so destination but you're not so covered in media what's covered in media is this part a deploring we've heard it on and on about it you know but when you think about it for a company for the industry is action not the highest priority or at least it's not the thing that yields the most resolved for the lowestoft that's why i dependientes and these things a detesting analytics directoire important for industry so that's why reginald of data scientists that does that so what do they scientists ached while that depends on the company because of the message so for a start up you can lack resources so you can come home on dasso down one day a scientist he do everything so you might be seen all this being the designs may be you won't be doing a ardericca that's not a priority right now but you might be doing all this you have to set up the whole detains you might even have to write some software a code to a liking and denuded the analytics or so then you have to build a matrosses and you had to do abetting yourself that's why for start upsetting it did a scientist this whole thing is this science so that means you have to do everything but let's look at me him side company now finally to have a lot more resources they can separate the data engineers and that the design is so usually in collection this is probably soveraine and then here during a have the engineer doing this and then depending if your medium sized company does a lot of recommendation models or stuff there requires a than the side all this but reactionists had to be lower technical that's why the only higher people of pads or masters because they want you to be able to do the more complicated things so the sun large company now because you're getting a lot bigger you partly have a lot more money and then you can spend a more on employees so you can have a lot of different voice work on trefethan that way jim podos not need to think about this stuff that he don't want to do and to get focus on the things at their best for example me and my untitled match company i would be in analytic so i could just focus my work on analytics and matthias that i only to worry about that endearing or i deepening stuff so here's how expert you are company in cement logging censors this is all handle advisor engineers right and then her cleaning and building detailing this is for the engineers now here between these two things we have the science analytics that we call a beheading this is will weave a research scientist or we call it did a science or an carabineers which are chiming engineers yet and is so in summer as i conceive that science can be all this and it depends what company you are in and that definition will bear it so please let me know what you would like to learn more about a i departing or by testing experimentation that penny on what you want to learn about leave a common down below so i could talk about it or i find someone who knows about this and i can share the insight with you either to lighten subscrive a wonderful day hope this was helpful but yet i watch

"""

Audio('Model_ds.wav')

"""import speech_recognition as sr
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
"""

!pip install -q transformers
!pip install -q youtube_transcript_api
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

video_id = video_id.split("=")[1]

video_id

YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)
transcript[0:5]

result = ""
for i in transcript:
    result += ' ' + i['text']
#print(result)
print(len(result))

summarizer = pipeline('summarization')

import nltk
nltk.download('stopwords')
  

num_iters = int(len(result)/1000)
summarized_text = []
for i in range(0, num_iters + 1):
  start = 0
  start = i * 1000
  end = (i + 1) * 1000
  print("input text \n" + result[start:end])
  out = summarizer(result[start:end])
  out = out[0]
  out = out['summary_text']
  print("Summarized text\n"+out)
  summarized_text.append(out)

#print(summarized_text)
# importing libraries
# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
# stopWords = set(stopwords.words("english"))
# words = word_tokenize(text)
# # Creating a frequency table to keep the 
# # score of each word
   
# freqTable = dict()
# for word in words:
#     word = word.lower()
#     if word in stopWords:
#         continue
#     if word in freqTable:
#         freqTable[word] += 1
#     else:
#         freqTable[word] = 1
# # Creating a dictionary to keep the score
# # of each sentence
# sentences = sent_tokenize(text)
# sentenceValue = dict()
   
# for sentence in sentences:
#     for word, freq in freqTable.items():
#         if word in sentence.lower():
#             if sentence in sentenceValue:
#                 sentenceValue[sentence] += freq
#             else:
#                 sentenceValue[sentence] = freq
# sumValues = 0
# for sentence in sentenceValue:
#     sumValues += sentenceValue[sentence]
# # Average value of a sentence from the original text
   
# average = int(sumValues / len(sentenceValue))
# # Storing sentences into our summary.
# summary = ''
# for sentence in sentences:
#     if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
#         summary += " " + sentence
print(summarized_text)

a = str(summarized_text)

a

# Removing Square Brackets and Extra Spaces
import re
summarized_text = re.sub(r'[[0-9]*]', ' ', a)
summarized_text = re.sub(r's+', ' ', a)

!pip install Rouge

from rouge import Rouge
r = Rouge()
r.get_scores(summarized_text,a )

!pip install transformers -U -q

! pip install sentencepiece
!pip freeze | grep transformers
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")

tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")

model_inputs = tokenizer(summarized_text, return_tensors="pt")

#  Arabic (ar_AR), Czech (cs_CZ), German (de_DE), English (en_XX), Spanish (es_XX), Estonian (et_EE), Finnish (fi_FI), French (fr_XX),
#  Gujarati (gu_IN), Hindi (hi_IN), Italian (it_IT), Japanese (ja_XX), Kazakh (kk_KZ), Korean (ko_KR), Lithuanian (lt_LT), Latvian (lv_LV), 
#  Burmese (my_MM), Nepali (ne_NP), Dutch (nl_XX), Romanian (ro_RO), Russian (ru_RU), Sinhala (si_LK), Turkish (tr_TR), Vietnamese (vi_VN),
#  Chinese (zh_CN), Afrikaans (af_ZA), Azerbaijani (az_AZ), Bengali (bn_IN), Persian (fa_IR), Hebrew (he_IL), Croatian (hr_HR), Indonesian (id_ID),
#  Georgian (ka_GE), Khmer (km_KH), Macedonian (mk_MK), Malayalam (ml_IN), Mongolian (mn_MN), Marathi (mr_IN), Polish (pl_PL), Pashto (ps_AF),
#  Portuguese (pt_XX), Swedish (sv_SE), Swahili (sw_KE), Tamil (ta_IN), Telugu (te_IN), Thai (th_TH), Tagalog (tl_XX), Ukrainian (uk_UA),
#  Urdu (ur_PK), Xhosa (xh_ZA), Galician (gl_ES), Slovene (sl_SI)

# translate from English to Hindi
generated_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"])

translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

translation[0]

# translate from English to Arabic
generated_tokens = model.generate(**model_inputs, forced_bos_token_id=tokenizer.lang_code_to_id["ar_AR"])

translation1 = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

translation1[0]

