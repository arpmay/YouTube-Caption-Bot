from pytube import Channel, YouTube
from collections import Counter
from clean_data import clean


def calc(channel, nvid, nres):
    nvid = int(nvid)
    nres = int(nres)
    result_box.insert('1.0', calculate(channel, nvid, nres))
    print("Calculation Complete")


def calculate(channel, n_vid, n_res):
    c = Channel(channel)
    n = n_vid  # number of videos to be included
    corpus = ''
    for url in c.video_urls[:n]:
        yt = YouTube(url)
        caption = yt.captions
        try:
            try:
                caption = yt.captions['en-US']
            except KeyError:
                caption = yt.captions['a.en']
        except KeyError:
            continue
        srt = caption.generate_srt_captions().splitlines()
        for i in range(len(srt)):
            if (i+2) % 4 == 0:
                corpus = corpus + ' ' + srt[i]

    words = clean(corpus)
    counts = Counter(words).most_common(n_res)
    # file = open('results.txt', 'w')
    # file.write(str(counts))
    # file.close()

    # print(counts)
    return prettify(counts)