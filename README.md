# Protein Info

This project consists of one function "protein_analysis" that helps user to:
- predict molecular weight of amino acid (aa) sequences
- translate aa sequences from one-letter to three-letter code
- calculate total amount of each amino acid in the sequences
- make DNA based codon optimization for the introduced amino acid sequences with the support for 3 cell types: Esherichia coli, Pichia pastoris, Mouse
- calculate length of amino acid sequences
- count the number of atoms of each type in a sequence (brutto formula)

## Technology:

python

## How to use:
**protein_analysis**
protein_analysis(**args, procedure, cell_type=None, format=1*) <br/>
**Parametrs:** <br/>
    ***args** : 
Any number of lines with amino acid sequences <br/>
    **procedure** : ***str*** 
    описание процедур <br/>
    **cell_type** : ***str, defalut None*** 
    описание клеток <br/>
    **format** : ***int, defalut 1*** 
    описание форматов <br/>
    
Call the "protein_analysis" funcion with following arguments.
Requred arguments:
- tuple of protein sequences written one letter or three letter code without stop codos. Please do not use sequences in different formats in the same function call!
- name of procedure as string (see list of precedures)
- format of code for the protein sequences as int: 1 for one letter, 3 for three letter code
Optional argument:
- cell type (required only for codon_optimization procedure). Accepted cell types Esherichia coli, Pichia pastoris, Mouse

## List of procedures:

- `molecular_weight` — returns list of float values, that indicate predicted molecular weights of given aa sequences (in kDa)
- `one_letter_to_three` — will return list of strings, containing the same sequences written in three-letter code
- `get_amino_acid_sum` — сounts the amount of each amino acid in the injected protein sequences
- `codon_optimization` — makes codon-optimized DNA based on the introduced amino acid sequences for 3 types of cells: Esherichia coli, Pichia pastoris, Mouse
- `length` — calculates length of amino acid sequences 
- `brutto_count` — counts the number of atoms of each type in a sequence

## Example of use:

```python
protein_analysis("ACD", "AD", procedure="one_letter_to_three", format=1) # ['AlaCysAsp', 'AlaAsp']
protein_analysis("AlaAspLys", "AlaAsp", procedure="molecular_weight", format=3) # [0.37, 0.22]
protein_analysis("ACD", "AD", procedure="get_amino_acid_sum", format=1) # [{'A': 1, 'C': 1, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0},
                                                                        # {'A': 1, 'C': 0, 'D': 1, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'V': 0, 'W': 0, 'Y': 0}]
protein_analysis("ACD", "AD", procedure="codon_optimization", cell_type = 'E.coli', format=1) # ['GCGTGCGAT', 'GCGGAT']
```



## Possible errors:
```python
> `ValueError`('Requested procedure is not defined') # Will occure if proc argument does not correspond to any listed procedure (see List of procedures).
> `ValueError`('The following types of organisms are available for codon optimization: Esherichia coli, Pichia pastoris, Mouse) # Will occure if the cell type is incorrectly entered to optimize codons. 
```

## Private policy and contacts
This tool can be freely distributed and used.
<br/>
If you have any suggestions for improving the tool or if you find a bug, please contact us by email.
<br/>
This tool was developed by the "workaholics" team:
<br/>
Yulia Volkova volkova.yulia.leonidovna@gmail.com
<br/>
Dasha Sokolova kalabanova_dasha@mail.ru
<br/>
Team leader: Ivan Kozin ivan.d.kozin@gmail.com
<br/>
Team photo:
![Снимок экрана 2023-09-29 210559_2](https://github.com/ivandkoz/HW4_Functions2_Kozin/assets/63678919/ad1302a1-d139-4c82-b7eb-d5b9ac1897e8)

## Personal contribution
`Ivan Kozin` (team leader) worte functions:
- length
- brutto_count
- check_amino_acid
- name_transform
- check_amino_acid_three_letter
- check_length
- managed work with guthub repository

`Dasha Sokolova` wrote functions: 
- get_amino_acid_sum
- codon_optimization functions
  
`Yulia Volkova` wrote functions:
- main (protein_analysis)
- molecular_weight
- one_letter_to_three functions
  
Writting README, debugging code and testing it has been done by the efforts of all team.



