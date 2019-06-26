api = "AIzaSyCRtAXecCXzA-kNIKtJWWO85R2e4v8FEDA"
file_id=""
i = ""
list1 = []
while i != "q":
    i = input("Enter URL: ")
    list1.append(i)

list1.pop(-1)
#print(list1)
#https://drive.google.com/open?id=1smGR_N5Uxs2-FFHmd_niD699mi56dx3W
for link in list1:
    id_part = link.find("id=")
    id = link[id_part+3:]
    #print(id)
    final_url = f"https://www.googleapis.com/drive/v3/files/{id}?alt=media&key={api}"
    print(f"""
    {final_url}
    """)
