import re

def cleantext(text):
    index = text.rfind('References')
    if index != -1:
        text = text[:index + len('References')]

    index = text.rfind('REFERENCES')
    if index != -1:
        text = text[:index + len('REFERENCES')]

    # if the line end up with " -\n", then merge it with the next line
    text = text.replace(' -\n', '')
    text = text.replace('-\n', '')

    # remove all the contents within the brackets
    text = re.sub(r'\([^)]*\)', '', text)

    # use regex to remove all the non-alphanumeric characters, but keep the "," and "." and line break "\n"
    text = re.sub(r'[^a-zA-Z0-9\n\.\,]', ' ', text)


    # remove multiple spaces
    text = re.sub(r' +', ' ', text)

    # if the line does not end with ".", merge with the next line
    lines = text.split('\n')
    merged_lines = []
    for i in range(len(lines) - 1):
        if lines[i] and lines[i][-1] != '.':
            lines[i+1] = lines[i] + ' ' + lines[i+1]
        else:
            merged_lines.append(lines[i])
    merged_lines.append(lines[-1])  # add the last line
    text = '\n'.join(merged_lines)

    # transform the text to all lower case
    text = text.lower()

    # remove the word+".pnum." pattern
    text = re.sub(r'\b\w+\.pnum\.\b', '', text)

    return text

if __name__ == '__main__': 
    with open('data/paper.txt') as f:
        text = f.read()
        f.close()

    text = cleantext(text)

    # save text to file
    with open('output/paper_cleaned.txt', 'w') as f:
        f.write(text)
        f.close()
