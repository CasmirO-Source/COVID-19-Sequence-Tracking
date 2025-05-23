COVID-19 Sequence Analysis Script


# About Me
I developed this Python script as part of my self-study to explore how DNA or RNA sequences (like those from COVID-19) can be analysed to trace their origins. I’m excited about applying these skills in a bioinformatics role to contribute to genomic research.

# What This Script Does
This script analyses COVID-19 sequence data to:

1. Load sequence records from a file (e.g., country, ID, and sequence).
2. Compare sequences to find similarities (e.g., between bat and human COVID-19 sequences).
3. Identify the closest human sequence to a bat sequence.
4. Find potential transmission links between sequences from different countries (e.g., Angola to British Indian Ocean Territory).

It helps figure out which sequences are most similar and might show how a virus spreads

# Requirements

Python: Version 3.6 or higher (I used 3.8).

# Input Files:
Human-Covid19.txt: Contains human sequence records (format: country code, ID, sequence, separated by spaces).
Bat-Covid19.txt: Contains a single bat sequence record (same format).


Note: The files must be in the same folder as the script, and sequences should be valid strings (e.g., ATCG).

# How to Run It

1. Save the script as sequence_analysis.py.
2. Create or download Human-Covid19.txt and Bat-Covid19.txt with the correct format.
3. Open a terminal in VS Code (or elsewhere) and navigate to the script’s folder.
4. Run the script:python sequence_analysis.py


The script will:
- Print the closest human sequence to the bat sequence (country, ID, and distance).
- Show the most likely transmission pair between Angola (AGO) and British Indian Ocean Territory (IOT).



# Example Output
If Human-Covid19.txt has:
AGO ID123 ATCGATCG
IOT ID456 ATAGATCG

And Bat-Covid19.txt has:
BAT ID789 ATCGATAG

The output might look like:
Country: AGO, Unique ID: ID123, Distance: 0.125
Unique ID Origin(IOT): ID456, Unique ID Target(AGO): ID123, Distance: 0.125

# Why This Matters for Bioinformatics?
This script is an example of sequence analysis, which is super important in bioinformatics for studying virus evolution, tracking outbreaks, or comparing genomes. I built it to practice handling sequence data and calculating distances, which are key skills for genomic research. I’m eager to learn more advanced tools like BLAST or Biopython during my MSc to tackle bigger datasets.

# Limitations

The script assumes files are formatted correctly (no error checking).
It uses a basic distance metric (not as fancy as BLAST or alignment algorithms).
It’s not optimised for huge datasets, but it works for small ones.
I hardcoded the countries (AGO, IOT) for this example, but it could be more flexible.

# Future Improvements

- Find a way to add error handling for bad files or sequences.
- Use Biopython for more accurate sequence alignment.
- Make the country codes an input so users can choose them.
- Make it faster for bigger data sets

# Why I’m a Good Fit

This project shows my ability to write clear Python code and understand sequence analysis concepts. I’m excited to grow my skills in bioinformatics, especially in applying computational methods to real-world problems like disease tracking. I’m a quick learner and ready to dive into advanced techniques during my MSc and in a bioinformatics role.
Thanks for considering my work. Please let me know if you have feedback or want to see more of my projects. 
