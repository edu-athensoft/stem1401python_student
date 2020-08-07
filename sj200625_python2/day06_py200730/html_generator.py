"""
html code generator
"""

codestr = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            font-size: 28px;
            color : blueviolet;
        }
    </style>
</head>
<body>
    <h1>HTML Entities</h1>

    <h2>Concept</h2>
    <p>Reserved characters in HTML must be replaced with character entities.</p>
    
    <p>
        &entity_name;  <br />
        or  <br />
        &entity_number;   <br />
    </p>

    <p>
        &pound; <br />
        &sect;  <br />
        &copy; <br />
        &reg; <br />
        &gt;  &#62;<br />
        &lt; &#60;<br />
        &amp; <br />
        |&nbsp;| <br />
        abc         de <br />
        abc&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;de<br />
        &quot; <br />
        &apos; <br />
    </p>

    <p>
        &lt;html&gt;&lt;/html&gt;
        &lt;html&gt;&lt;/html&gt;
    </p>
</body>
</html>"""

codestr = codestr.replace('<','&lt;')
codestr = codestr.replace('>','&gt;')

print(codestr)

