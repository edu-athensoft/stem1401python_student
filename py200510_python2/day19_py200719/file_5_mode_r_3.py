"""
file mode:  r (t)


Character Sets List (charset=)
Some Basic Ones
charset=big5 - Chinese Traditional (Big5)
charset=euc-kr - Korean (EUC)
charset=iso-8859-1 - Western Alphabet
charset=iso-8859-2 - Central European Alphabet (ISO)
charset=iso-8859-3 - Latin 3 Alphabet (ISO)
charset=iso-8859-4 - Baltic Alphabet (ISO)
charset=iso-8859-5 - Cyrillic Alphabet (ISO)
charset=iso-8859-6 - Arabic Alphabet (ISO)
charset=iso-8859-7 - Greek Alphabet (ISO)
charset=iso-8859-8 - Hebrew Alphabet (ISO)
charset=koi8-r - Cyrillic Alphabet (KOI8-R)
charset=shift-jis - Japanese (Shift-JIS)
charset=x-euc - Japanese (EUC)
charset=utf-8 - Universal Alphabet (UTF-8)
charset=windows-1250 - Central European Alphabet (Windows)
charset=windows-1251 - Cyrillic Alphabet (Windows)
charset=windows-1252 - Western Alphabet (Windows)
charset=windows-1253 - Greek Alphabet (Windows)
charset=windows-1254 - Turkish Alphabet
charset=windows-1255 - Hebrew Alphabet (Windows)
charset=windows-1256 - Arabic Alphabet (Windows)
charset=windows-1257 - Baltic Alphabet (Windows)
charset=windows-1258 - Vietnamese Alphabet (Windows)
charset=windows-874 - Thai (Windows)

"""

print("[info] open file in current directory")
print("[info] opening file5_mode_r.txt ...")

try:
    f = open("file5_mode_r.txt", 'r', encoding="utf-8")
    # f = open("file5_mode_r.txt", 'r', encoding="iso-8859-1")

    # read
    content = f.read()

    # display the content
    print(content)

except FileNotFoundError as fe:
    print(fe)

except Exception as e:
    print(e)

finally:
    f.close()
    print("[info] done.")
