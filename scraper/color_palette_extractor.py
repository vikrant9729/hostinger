import re

def extract_colors(css):

    colors = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}', css)

    return list(set(colors))