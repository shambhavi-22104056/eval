def count(str):
    str=str.lower()
    vowel=set("aeiou")
    count=0
    unique=set()
    for char in str:
                if char in vowel:
                    unique.add(char)
                    
    print(f"Vowels : {count}")
    print("unique vowels :","".join(sorted(unique)))
input="I am a student"
count(input)
    
