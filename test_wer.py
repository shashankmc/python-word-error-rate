import word_error_rate as wer
import sys

if len(sys.argv) != 3:
    raise ValueError('Please provide locations of the ground truth transcript and the generated transcript')

f = open(sys.argv[1], 'r')
r = f.read().split()
f.close()

f = open(sys.argv[2], 'r')
h = f.read().split()
f.close()

print(f"Original:", r)

print(f"Generated:", h)



print("WER: {0:<6.6}%".format( wer.get_word_error_rate(r, h) ) ) 
