# Ask user for file name
file = input('File name: ').strip().lower()
if file[-4:] == '.gif':
    print('image/gif')
elif file[-4:] == '.jpg':
    print('image/jpeg')
elif file[-5:] == '.jpeg':
    print('image/jpeg')
elif file[-4:] == '.png':
    print('image/png')
elif file[-4:] == '.pdf':
    print('application/pdf')
elif file[-4:] == '.txt':
    print('text/plain')
elif file[-4:] == '.zip':
    print('application/zip')
else:
    print('application/octet-stream')
