import re

def tokenize(content):
    content = re.sub(r"\bfunction \b","def ",content)
    content = re.sub(r"\biterate \b","for ",content)
    content = re.sub(r"\binside \b","in ",content)
    content = content.replace('when (', 'while (')
    content = content.replace('when(', 'while(')
    content = re.sub(r"\bunless \b","if not ",content)

    #It should remain last in order otherwise many words with strings will break
    content = content.replace('{[', '')
    content = content.replace(']}', '')
    return content
