# Credits : @jagrit007 (GitHub)
# https://github.com/jagrit007
print("""Welcome to the Direct Link Generator by @jagrit007
for any issues report to me on Telegram : @notSbeve
Paste as much shareable links as you wish and when you're done just enter q
Make sure you've entered your own API key in main.py
Don't Forget to rename file after Download with extension!!

                                Thanks!""")

api = "PasteHERE"
file_id=""
i = ""
list1 = []
while i != "q":
    i = input("Enter URL: ")
    list1.append(i)

list1.pop(-1)
#print(list1)
for link in list1:
    if link.find("file/d/") != -1:
        id_part = link.find("file/d/")
        id = link[id_part+7:]
        new_id = id.replace("/view?usp=drivesdk", "")
        final_url = f"https://www.googleapis.com/drive/v3/files/{new_id}?alt=media&key={api}"
        print(f"""
        {final_url}
        """)
    elif link.find("&export=download") == -1:
        id_part = link.find("id=")
        id = link[id_part+3:]
        #print(id)
        final_url = f"https://www.googleapis.com/drive/v3/files/{id}?alt=media&key={api}"
        print(f"""
        {final_url}
        """)
    else:
        id_part = link.find("id=")
        id = link[id_part+3:-16]
        final_url = f"https://www.googleapis.com/drive/v3/files/{id}?alt=media&key={api}"
        print(f"""
        {final_url}
        """)
