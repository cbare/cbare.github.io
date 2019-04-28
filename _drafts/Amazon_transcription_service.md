---
layout: post
title: "Amazon transcription service"
date: 2018-07-08 21:03 -0700
categories: data-science
---

Amazon annouced their 'transcribe' service at re:Invent 2017. I tried it out on a [sorta funny interview](https://soundcloud.com/gzeroworld/the-golden-hot-tub) and here's what I found:

Transcription quality is far from perfect, but probably good enough for uses like topic or sentiment analysis.

Speaker segmentation is available but didn't produce useful results for me. There are two main speakers in this clip, both New York City guys who's tone of voice is not far apart. There's also a female voice for the sponsorship announcement, which the algorithm totally failed to pick up on.

The [documentation](https://docs.aws.amazon.com/transcribe/latest/dg/how-it-works.html#how-diarization) isn't super clear on how the output format is supposed to work. There are start and end times given in the _speaker_labels_ section that relate segments to _items_. An _item_ apparently come in two types, 'pronunciation' (a word) or 'punctuation'. I ended up writing a [little code snippet](https://gist.github.com/cbare/bc3604f79fc250a7543a3b5e0991f863) to display the transcription in a sensible format.

Here's an abridged view of the output I got:
```
{
  "jobName": "golden-hottub-2",
  "accountId": "[...REDACTED...]",
  "results": {
    "transcripts": [
      {
        "transcript": "The swamp has a draining let's i'm not saying it doesn't it doesn't it's not even a swamp let's let's talk about what really what is it ? Really ? It is a drain lis gold plated hot tub theo river in the middle of times square with put elmo's all around me it's kind of weird and welcome to the g zero world podcast most of weekly shoji zero world on youtube in this podcast, we share extended versions of the big interviews from that joe this week i sit down with anthony scaramucci, also known as the mooch he's, a longtime fixture on wall street but is most famous for his eleven day, ten years white house communications director replete last summer, he's been in the room of president trump many, many times, and today i will ask him about what goes on behind the scenes of the white house, including how trump makes decisions. What a summit between trump and kim jong un might look like let's get teo thie geeze aargh world has brought to you by our founding sponsor, first republic [...ETC...]"
      }
    ],
    "speaker_labels": {
      "speakers": 3,
      "segments": [
        {
          "start_time": "0.000000",
          "speaker_label": "spk_0",
          "end_time": "0.040",
          "items": []
        },
        {
          "start_time": "0.040000",
          "speaker_label": "spk_2",
          "end_time": "9.580",
          "items": [
            {
              "start_time": "9.540",
              "speaker_label": "spk_2",
              "end_time": "9.670"
            }
          ]
        },
        [...ETC...]
      ]
    },
    "items": [
      {
        "start_time": "9.540",
        "end_time": "9.670",
        "alternatives": [
          {
            "confidence": "0.9989",
            "content": "The"
          }
        ],
        "type": "pronunciation"
      },
      {
        "start_time": "9.670",
        "end_time": "10.050",
        "alternatives": [
          {
            "confidence": "1.0000",
            "content": "swamp"
          }
        ],
        "type": "pronunciation"
      },
      [...ETC...]
      {
        "alternatives": [
          {
            "content": "."
          }
        ],
        "type": "punctuation"
      }
    ]
  },
  "status": "COMPLETED"
}
```

Though the results are limited for now, I'm excited to make use of this service especially as speaker segmentation improves.

 * a related [thread on hacker news](https://news.ycombinator.com/item?id=16174301)

