import browser_cookie3

cookies = browser_cookie3.load(domain_name='instagram.com')

with open('cookies.txt', 'w') as f:
    f.write('# Netscape HTTP Cookie File\n')
    for c in cookies:
        line = f"{c.domain}\tTRUE\t{c.path}\t{str(c.secure).upper()}\t2147385600\t{c.name}\t{c.value}\n"
        f.write(line)

print("✅ cookies.txt faylı yaradıldı!")
