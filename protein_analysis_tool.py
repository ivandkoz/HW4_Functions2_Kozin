amino_short_names_dic = {'A':'Ala', 'R':'Arg', 'N':'Asn',
                         'D':'Asp', 'V':'Val', 'H':'His',
                         'G':'Gly', 'Q':'Gln', 'E':'Glu',
                         'I':'Ile', 'L':'Leu', 'K':'Lys',
                         'M':'Met', 'P':'Pro', 'S':'Ser',
                         'Y':'Tyr', 'T':'Thr', 'W':'Trp',
                         'F':'Phe', 'C':'Cys'}

amino_names_dic = {'ala': 'A', 'arg': 'R', 'asn': 'N',
                    'asp': 'D', 'val': 'V', 'his': 'H',
                    'gly': 'G', 'gln': 'Q', 'glu': 'E',
                    'ile': 'I', 'leu': 'L', 'lys': 'K',
                    'met': 'M', 'pro': 'P', 'ser': 'S',
                    'tyr': 'Y', 'thr': 'T', 'trp': 'W',
                    'phe': 'F', 'cys': 'C'}

amino_names_dic_reverse = {'Ala': 'A', 'Arg': 'R', 'Asn': 'N',
                    'Asp': 'D', 'Val': 'V', 'His': 'H',
                    'Gly': 'G', 'Gln': 'Q', 'Glu': 'E',
                    'Ile': 'I', 'Leu': 'L', 'Lys': 'K',
                    'Met': 'M', 'Pro': 'P', 'Ser': 'S',
                    'Tyr': 'Y', 'Thr': 'T', 'Trp': 'W',
                    'Phe': 'F', 'Cys': 'C'}

aa_weights = {'A': 89.09, 'R': 174.20, 'N': 132.12,
                  'D': 133.10, 'C': 121.16, 'E': 147.13,
                  'Q': 146.15, 'G': 75.07, 'H': 155.16,
                  'I': 131.18, 'L': 131.18, 'K': 146.19,
                  'M': 149.21, 'F': 165.19, 'P': 115.13,
                  'S': 105.09, 'T': 119.12, 'W': 204.23,
                  'Y': 181.19, 'V': 117.15}

amino_brutto = {'A':(3,7,1,2,0), 'R':(6,14,4,2,0),
                'N':(4,8,2,3,0), 'D':(4,7,1,4,0),
                'V':(5,11,1,2,0), 'H':(6,9,3,2,0),
                'G':(2,5,1,2,0), 'Q':(5,10,2,3,0), 
                'E':(5,9,1,4,0), 'I':(6,13,1,2,0),
                'L':(6,13,1,2,0), 'K':(6,14,2,2,0), 
                'M':(5,11,1,2,1), 'P':(5,9,1,2,0),
                'S':(3,7,1,3,0), 'Y':(9,11,1,3,0), 
                'T':(4,9,11,1,3,0), 'W':(11,12,2,2,0),
                'F':(9,11,1,2,0), 'C':(3,7,1,2,1)}


def protein_analysis(*args: tuple, procedure: str, cell_type:str = None, format:int) -> list:
    """
    Function protein_analysis:
    - calculates predicted molecular weight of amino acid sequences in kDa (procedure name: molecular_weight)
    - translate aa sequences from one-letter to three-letter code (procedure name: one_letter_to_three)
    - calculates total amount of each amino acid in the sequences (procedure name: get_amino_acid_sum) 
    - makes DNA based codon optimization for the introduced amino acid sequences, support 3 types of cells: Esherichia coli, Pichia pastoris, Mouse (procedure name: codon_optimization) 
    - calculates length of amino acid sequences (procedure name: length)
    
    Arguments:
    - tuple of protein sequences written one letter or three letter code (not mixed)
    - name of procedure as string
    - cell type (required only for codon_optimization procedure) 
    - format of code for the protein sequences as int: 1 for one letter, 3 for three letter code

    Return:
    - molecular_weight procedure returns list of floats
    - one_letter_to_three procedure returns list of strings
    - get_amino_acid_sum procedure returns list of dictionaries
    - codon_optimization procedure returns list of strings
    - length procedure returns list of int values
    """
    aa_seqs = args
    procedures = ('molecular_weight', 'one_letter_to_three', 'get_amino_acid_sum', 'codon_optimization', 'length', 'brutto_count')
    aa_seqs = name_transform(aa_seqs, format)

    # for aa_seq in aa_seqs:
    #     validate(aa_seq)

    if procedure not in procedures:
        raise ValueError('Requested procedure is not defined')

    if procedure == 'molecular_weight':
        return molecular_weight(aa_seqs)

    if procedure == 'one_letter_to_three':
        return one_letter_to_three(aa_seqs)

    if procedure == 'get_amino_acid_sum':
        return get_amino_acid_sum(aa_seqs)

    if procedure == 'codon_optimization':
        return codon_optimization(aa_seqs, cell_type)
      
    if procedure == 'length':
        return length(aa_seqs)
      
    if procedure == 'brutto_count':
        return brutto_count(aa_seqs)

# def validate(aa_seq: str) -> None:
#     """Validates if aa sequence consists of only amino acid characters"""
#     aa_seq_set = set(aa_seq.upper())
#     all_aa = {'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'}
#     difference = aa_seq_set.difference(all_aa)
#     if len(difference) > 0:
#         raise ValueError('Invalid alphabet, please use only single letter amino acid code')


def molecular_weight(aa_seqs: tuple) -> list:
    """Calculates predicated molecular weight of aa sequences. Returns list of floats"""
  
    molecular_weights = []
    for seq in aa_seqs:
        total_weight = 0
        for aa in seq:
            aa = aa.upper()
            total_weight += aa_weights[aa]
        molecular_weights.append(round(total_weight/1000, 2))
    return molecular_weights


def one_letter_to_three(aa_seqs: tuple) -> list:
    """Translates one letter coded aa sequences to three letter coded"""
  
    three_letters_seqs = []
    for seq in aa_seqs:
        three_letters_seq = []
        for aa in seq:
            aa = aa.upper()
            three_letters_seq.append(amino_short_names_dic[aa])
        three_letters_seqs.append(''.join(three_letters_seq))
    return three_letters_seqs
  

def get_amino_acid_sum(protein_sequences: tuple) -> list:
    """
    Counts the amount of each amino acid in the injected protein sequences

    Arguments:
    - protein_sequences (list): list of injected protein sequence

    Return:
    - List of dictionary with amino acid amount
    """
    result = []
    for protein_sequence in range(len(protein_sequences)):
        amino_acid_count = {'A': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                      'K': 0, 'L': 0, 'M': 0, 'N': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0,
                      'T': 0, 'V': 0, 'W': 0, 'Y': 0}
        for amino_acid in protein_sequences[protein_sequence]:
            amino_acid_count[amino_acid] += 1
        result.append(amino_acid_count)
    return result


def codon_optimization(protein_sequences: tuple, cell_type:str) -> list:
    """
    Makes codon-optimized DNA based on the introduced amino acid sequences for 3 types of cells:
    Esherichia coli, Pichia pastoris, Mouse

    Arguments:
    - protein_sequences (list): list of injected protein sequence
    - cell_type (str): user-entered cell type for codon optimization

    Return:
    - List of codon-optimized DNA
    """

    if cell_type == 'Esherichia coli' or cell_type == 'E.coli':
        codon_optimization_ecoli = []
        ecoli_triplets = {'A': 'GCG', 'C': 'TGC', 'D': 'GAT', 'E': 'GAA', 'F': 'TTT', 'G': 'GGC',
                          'H': 'CAT', 'I': 'ATT', 'K': 'AAA', 'L': 'CTG', 'M': 'ATG', 'N': 'AAC',
                          'P': 'CCG', 'Q': 'CAG', 'R': 'CGT', 'S': 'AGC', 'T': 'ACC', 'V': 'GTG',
                          'W': 'TGG', 'Y': 'TAT'}
        replacer_ecoli = ecoli_triplets.get
        for amino_acid in range(len(protein_sequences)):
            codon_optimization_ecoli += [''.join([replacer_ecoli(n, n) for n in protein_sequences[amino_acid]])]
        return codon_optimization_ecoli

    if cell_type == 'Pichia pastoris' or cell_type == 'P.pastoris':
        codon_optimization_ppastoris = []
        ppastoris_triplets = {'A': 'GCT', 'C': 'TGT', 'D': 'GAT', 'E': 'GAA', 'F': 'TTT', 'G': 'GGT',
                              'H': 'CAT', 'I': 'ATT', 'K': 'AAG', 'L': 'TTG', 'M': 'ATG', 'N': 'AAC',
                              'P': 'CCA', 'Q': 'CAA', 'R': 'AGA', 'S': 'TCT', 'T': 'ACT', 'V': 'GTT',
                              'W': 'TGG', 'Y': 'TAC'}
        replacer_ppastoris = ppastoris_triplets.get
        for amino_acid in range(len(protein_sequences)):
            codon_optimization_ppastoris += [''.join([replacer_ppastoris(n, n) for n in protein_sequences[amino_acid]])]
        return codon_optimization_ppastoris

    if cell_type == 'Mouse' or cell_type == 'mouse':
        codon_optimization_mouse = []
        mouse_triplets = {'A': 'GCC', 'C': 'TGC', 'D': 'GAC', 'E': 'GAG', 'F': 'TTC', 'G': 'GGC',
                          'H': 'CAC', 'I': 'ATC', 'K': 'AAG', 'L': 'CTG', 'M': 'ATG', 'N': 'AAC',
                          'P': 'CCC', 'Q': 'CAG', 'R': 'CGG', 'S': 'AGC', 'T': 'ACC', 'V': 'GTG',
                          'W': 'TGG', 'Y': 'TAC'}
        replacer_Mouse = mouse_triplets.get
        for amino_acid in range(len(protein_sequences)):
            codon_optimization_mouse += [''.join([replacer_Mouse(n, n) for n in protein_sequences[amino_acid]])]
        return codon_optimization_mouse
    else:
        raise ValueError('The following types of organisms are available for codon optimization: Esherichia coli, Pichia pastoris,'
              'Mouse')

def length(seqs:touple):
    result = [len(seq) for seq in seqs]
    return result


# def reverse(seqs):
#     result = [seq[::-1] for seq in seqs]
#     return result
  
def name_transform(seqs:touple, format:int):
    result = []
    if format == 1:
        for seq in seqs: 
            seq = seq.upper()
            for letter in seq:
                if check_amino_acid(letter):
                    pass
                else: return False
            result.append(seq)
        return result
    elif format == 3:
        for seq in seqs:
            seq = seq.lower()
            seq3 = [seq[i:i+3] for i in range(0, len(seq), 3)]
            for triplet in seq3:
                if check_amino_acid(triplet):
                    pass
                else: return False
            seq_transformed = "".join([amino_names_dic.get(seq) for seq in seq3])
            result.append(seq_transformed)
        return result

    else:
        print('Error unsupported format. Only formats 1 and 3 are supported')
        return False
        

def check_amino_acid(input_amino:str):
    if len(input_amino) == 1:
        letter = input_amino
        if letter not in amino_short_names_dic.keys():
            print(f'Error {letter} is not an amino acid. Correct your input')
            return False
        else: return True
    elif len(input_amino) == 3:
        triplet = input_amino
        if triplet not in amino_names_dic.keys():
            print(f'Error {triplet} is not an amino acid. Correct your input')
            return False
        else: return True
    else:
        print(f'Error {input_amino} is incorrect form of amino acid notation. Correct your input')
        return False


def brutto_count(seqs:touple):
    elements = ['C', 'H', 'N', 'O', 'S']
    result = []
    for seq in seqs:
        brutto_list = [amino_brutto.get(letter) for letter in seq]
        brutto_pair = list(zip(*brutto_list))
        brutto = [sum(i) for i in brutto_pair]
        brutto_dict  = dict(zip(elements, brutto))
        result.append(brutto_dict)
    return result
    
