import itertools
l,c = map(int,input().split())
chrs = list(input().split())
chrs.sort()
vowels='aeiou'
for i in itertools.combinations(chrs,l):
    vowel_cont = sum(1 for j in i if j in vowels)
    consonant_count = l - vowel_cont

    if vowel_cont >= 1 and consonant_count>=2:
        print(''.join(i))