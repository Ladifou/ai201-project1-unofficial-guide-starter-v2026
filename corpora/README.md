# The corpora

Three corpora ship with this starter for your project, plus a fourth
(`practice`) that your instructor uses in class. Pick one of the three in
Milestone 1.

They are deliberately different from each other in **shape** — how long the
documents are, and how the useful information sits inside them. That
difference is the point: the right chunk size for short posts is not the
right chunk size for long sectioned guides, and Milestone 3 is where that
starts to matter.

All three were written for this course. No real people are named.

To switch corpus, either edit `CORPUS` in `config.py`, add
`AI201_CORPUS=name` to your `.env`, or pass `--corpus name` on the command
line. Re-run `python app.py index` after switching.

## `campus_life`

**Short posts about student life at a university.** Eighty-eight documents, most of them one to three short paragraphs — the kind of thing one student writes to answer another's question. Dining halls, dorms, courses, and the administrative rules nobody explains properly. Useful information tends to sit in a single sentence.

_Pick this if_ you want the closest thing to the brief's framing, and short documents where a chunk can easily hold a whole thought.

88 documents · 27,908 characters · about 317 characters per document

## `advice_threads`

**Question-and-answer threads, with several people replying.** Twenty-three threads, each with three to five replies of very uneven length, disagreeing with each other as often as not. Real answers are spread across replies rather than sitting in one place.

_Pick this if_ you want messier material. Chunking is harder here — a reply boundary and a useful boundary are not the same thing — and that makes for a more interesting Milestone 3.

23 documents · 12,490 characters · about 543 characters per document

## `city_guides`

**Long structured travel guides.** Fourteen documents — nine town guides, plus five that cut across all of them (eating, walking, regional transport, seasons, accessibility). Each is one to three thousand characters, divided into labelled sections — getting there, getting around, where to eat, when to go. Information is organised by heading and spread across a paragraph rather than packed into a sentence.

_Pick this if_ you want to think about splitting on structure rather than on length. Fixed-size chunks cut through these headings badly, which is exactly the problem worth solving.

14 documents · 28,958 characters · about 2,068 characters per document

## `practice`

Not for your project. This is the small corpus your instructor uses for the
in-class follow-along, kept separate so nothing done in class touches your
graded work. It's twenty-eight documents about a board game that doesn't
exist — twenty-four short ones of a paragraph or two, and four longer sectioned
guides that a fixed-size chunker cuts straight through the middle of.

28 documents · 15,901 characters · about 567 characters per document

## Bringing your own documents

You're allowed to. Make a folder at `corpora/your_name/documents/`, put
`.txt` or `.md` files in it, and point `CORPUS` at it.

Two honest warnings. You take on the cleaning work the provided corpora
already did, and it earns no extra points. And you'll need to check that
your relevance cutoff still separates in-corpus from out-of-corpus
questions, since 0.6 was chosen against these three.

That check is Milestone 4, and it is the same check that makes 0.6 a cutoff
rather than a number. Treat the default as a starting point, not an answer —
it was set against the corpora above at their shipped chunk settings, and
changing the chunking moves the distances underneath it. Measuring it
yourself is the milestone.

## Sample Chuncks

```======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

======================================================================
Chunk 2  |  source: guide_corry_vale.md#3  |  produced by: chunker.py::split_documents
======================================================================
## Eat and drink

One pub in the largest village serves food seven days a week. A second, in the third village, opens Thursday to Sunday. There is a farm shop at the valley mouth that sells bread, cheese and little else, and it closes at 4pm. Bring supplies; this is not a place with options.

======================================================================
Chunk 3  |  source: guide_givens_mill.md#2  |  produced by: chunker.py::split_documents
======================================================================
## Getting around

Everything is on one street along the river. The mill is at one end and the church at the other, eight minutes apart. The riverside path continues in both directions for as far as you want to walk.

======================================================================
Chunk 4  |  source: guide_marchwood.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Marchwood

Marchwood is the regional hub — 180,000 people, the junction everyone changes trains at, and a city most visitors pass through rather than stop in. That is a mistake, though an understandable one, since almost nothing of interest is near the station.

======================================================================
Chunk 5  |  source: guide_regional_transport.md#6  |  produced by: chunker.py::split_documents
======================================================================
## Walking and cycling

The river path from Brightwater runs four miles upstream on a good surface. The
old railway trackbed from Kestrelford runs six miles on an easy gradient and is
the best walking in the region for the effort involved. The coastal path from
Halden Bay is more serious — exposed, and closed in high wind.
```

## Sample Answer

```
(.venv) PS F:\CODEPATHAI201\ai201-project1-unofficial-guide-starter-v2026> python app.py ask "What details should visitors lookout for eating out?"
  (best distance 0.531, cutoff 0.6)

Based on the provided documents, visitors should know that kitchens across the region stop serving at 9 pm (guide_eating.md). Additionally, the good cooking is typically found one street back from the visitors (for example, Corry Lane in Brightwater, Fell Street in Halden Bay, and Marine Terrace in Pellew Sands offer better prices or food than the immediate waterfronts) (guide_eating.md).

Sources retrieved: guide_eating.md, guide_elder_ness.md, guide_halden_bay.md, guide_kestrelford.md

1 model calls this session, 1142 tokens (1058 in, 84 out)
```

## What this does

This project implements a RAG (Retrieval Augmented Generator) that would answer user questions based on documents provided. It was accomplish by implementing a pipeline that loads documents on city_guides, chuncks each documents into paragraphes, and embeds text. It querys a vector store and returns relevant results that are based on documents provided. To ensure the validity and relevance of the results, some acceptance criteria where implemented to name desirable targets to aim for.

## How I used AI

I used AI to help code the document splitter function into paragraph. This worked well to decrease development time while focusing on making sure the overall system worked as intended. Although AI was responsible for implementing code review and testing was still necessary to make sure that the code worked as intended.
AI was also used to brainstorm criterion and questions to ask and how to test them.
