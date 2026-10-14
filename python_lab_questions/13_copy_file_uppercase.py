# Copy source.txt to destination.txt in uppercase.
source = open('source.txt', 'r')
content = source.read()
source.close()
destination = open('destination.txt', 'w')
destination.write(content.upper())
destination.close()
print('File copied in uppercase')
