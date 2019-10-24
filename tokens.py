def tokenize(content):
    content = content.replace('function ', 'def ')
    content = content.replace('iterate ', 'for ')
    content = content.replace('inside ', 'in ')
    content = content.replace('when ', 'while ')
    content = content.replace('when(', 'while(')
    content = content.replace('unless ', 'if not ')
    return content
