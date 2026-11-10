# COVID-19 Sequence Tracking

A Python script that compares COVID-19 genome sequences to find which human sample is closest to a bat virus sample, and which pair of samples from two countries is most likely to show a transmission link. I wrote it as part of my self-study before my MSc, using plain Python with no libraries so I had to handle the file parsing and comparison logic myself.

## The data

- `Human-Covid19.txt`: 187 human virus sequences from 5 countries, each about 29,840 letters long
- `Bat-Covid19.txt`: one bat virus sequence in the same format

Each line holds a country code, a unique ID and the sequence, separated by tabs.

## What it does

1. **Loads** every record from both files.
2. **Measures distance** between two sequences as the share of positions where the letters differ. A distance of 0.05 means 5% of positions are different.
3. **Finds the closest human sequence** to the bat sequence by comparing it against all 187.
4. **Finds the likeliest transmission pair** between two countries (Angola and the British Indian Ocean Territory). For every Angolan sample it finds the closest match in the other country, then keeps the closest pair overall.

## Output

```
Country: DZA, Unique ID: 022-NABAXH, Distance: 0.04601206434316352
Unique ID Origin(AGO): 008-PDHKJM, Unique ID Target(IOT): 003-GFFUOL, Distance: 0.042593833780160906
```

So the human sample closest to the bat virus is from Algeria, with about 4.6% of positions different. The closest Angola to British Indian Ocean Territory pair differ at about 4.3% of positions.

## Limitations

- The distance measure compares position by position, so it assumes the sequences are already aligned and the same length. Alignment tools such as BLAST account for insertions and deletions.
- There's no error checking, so a badly formatted file will crash it.
- The two countries are hard-coded at the bottom of the script.

## What I'd do next

- Take the file names and countries as command-line arguments
- Add input validation with clear error messages
- Use Biopython for alignment-based comparison
- Write results to a CSV instead of printing them

## Running it

Needs Python 3, nothing else. With both data files in the same folder:

```bash
python COVID-19-Assignment.py
```
