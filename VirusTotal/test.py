from urllib.request import urlopen

#target webpage
url = "https://www.virustotal.com/gui/domain/yangindestek.com/details"

page = urlopen(url)
print("Opened page")
#print(f"Page is stored as {page}")

htmlRaw = page.read()
print("Read page contents")
#print(f"Page contents stored as {htmlRaw}")

htmlDecoded = htmlRaw.decode("utf-8")
print("Page contents decoded as utf-8")
#print(htmlDecoded)

#find paragraph tags, <p ...> </p>
paragraphStart = htmlDecoded.find("<p")
paragraphEnd = htmlDecoded.find("</p>",paragraphStart)
#an index of -1 is returned when the string can't be found
while (paragraphStart > 0):
    print(f"Paragraph found between index {paragraphStart} and {paragraphEnd}")
    print(htmlDecoded[paragraphStart:paragraphEnd])

    #use the index of the end of the last paragraph to find the start of the next paragraph
    paragraphStart = htmlDecoded.find("<p",paragraphEnd)
    if (paragraphStart > 0):
        paragraphEnd = htmlDecoded.find("</p>",paragraphStart)
print("no more paragraphs")
