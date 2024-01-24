def process_easy_to_read_code(filename):
    with open(filename, mode="r") as file:
        line      = file.readline()

        abstract_dict = {
        'ID' : 0,
        'OBJECTIVE': [], 'METHODS': [], 'RESULTS': [], 'CONCLUSIONS': [], 'BACKGROUND': [] 
        }

        if line[0] == '#':
            abstract_dict['ID'].append(line)

        elif line[0] == '\n':
            print("Starting the next abstract processing")

        else:
            words_split = line.splitlines()
            KEYWORD     = words_split[0]
            
            if KEYWORD in abstract_dict.keys():
                abstract_dict[KEYWORD] = words_split[1:]

def preprocess_text_ugly_code(filename):
    f = open(filename, mode="r")
    input_lines = f.readlines()
    
    categories = ['OBJECTIVE', 'METHODS', 'RESULTS', 'CONCLUSIONS', 'BACKGROUND' ]
    abstract_lines = "" # create an empty abstract
    abstract_samples = [] # create an empty list of abstracts
    
    # Loop through each line in target file
    for line in input_lines:
        if line.startswith("###"): # check to see if line is an ID line
        abstract_id = line
        abstract_lines = "" # reset abstract string
        elif line.isspace(): # check to see if line is a new line
        abstract_line_split = abstract_lines.splitlines() # split abstract into separate lines

        # Iterate through each line in abstract and count them at the same time
        for abstract_line_number, abstract_line in enumerate(abstract_line_split):
            line_data = {} # create empty dict to store data from line
            target_text_split = abstract_line.split("\t") # split target label from text
            line_data["target"] = target_text_split[0] # get target label
            line_data["text"] = target_text_split[1].lower() # get target text and lower it
            line_data["line_number"] = abstract_line_number # what number line does the line appear in the abstract?
            line_data["total_lines"] = len(abstract_line_split) - 1 # how many total lines are in the abstract? (start from 0)
            abstract_samples.append(line_data) # add line data to abstract samples list
        
        else: # if the above conditions aren't fulfilled, the line contains a labelled sentence
        abstract_lines += line
    
    return abstract_samples