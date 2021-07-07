from pydub import AudioSegment
from pydub.playback import play

f = open('/home/pi/Documents/list_of_music.txt', 'r')
line_first = f.readline().split('\n')
line_first = line_first[0]
lines = f.readlines()
f.close()
f = open("/home/pi/Documents/list_of_music.txt","w")
for line in lines:
    if line != line_first:
        f.write(line)
f.close()
#print(line_first[line_first.index('.') + 1:line_first.index('.') + 4])

print(line_first)
sound = AudioSegment.from_file("/home/pi/Documents/done_zip/"+line_first,
                               format=line_first[-3:])
#sound = AudioSegment.from_file("/home/pi/Documents/Kino.mp3", format="mp3")

play(sound)