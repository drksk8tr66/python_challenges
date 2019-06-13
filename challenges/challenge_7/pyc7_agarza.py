lyric_1 = 'bottles of beer on the wall!'
lyric_2 = 'bottles of beer! Take one down! Pass it around!'

all_lyrics = ''

for n in range(99,0,-1):
    
    nstring = str(n)
    lyric = ' '.join([nstring, lyric_1, nstring, lyric_2, nstring, lyric_1])
    
    if n == 99:
        all_lyrics = ''.join([all_lyrics, lyric])
    elif 99 < n > 1:
        all_lyrics = ' '.join([all_lyrics, lyric])
    else:
        lyric_1 = 'bottle of beer on the wall!'
        lyric_2 = 'bottle of beer! Take one down! Pass it around!'
        all_lyrics = ' '.join([all_lyrics, lyric])

print(all_lyrics)