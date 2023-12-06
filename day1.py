import re

#Challenge 1
def decoder(file:str) -> int:
  sum=0
  for line in open(file,'r'):
      num = re.compile(r'\d').findall(line)
      sum += int(num[0]+num[-1])
  return sum


#Challenge 2
class Decoder2:
    @staticmethod
    def searcher(word_num:dict, line:str ,num:int ,matches={}) -> dict:
        for word in word_num.keys():
            match = list(re.compile(word).finditer(line))

            if match:
                matches[word]=[match[0].start(),match[-1].start()]
            else:
                matches[word]=[9999,-9999]

            if num:
                matches['num'] = [num[0].start(),num[-1].start()]
            return matches


    @staticmethod
    def answer_elaborator(num:int, matches:dict, word_num:dict, answer='') -> str:

        #take the word that has the first lowest index and the one with the highest last index
        min_n = min(matches, key=lambda k: matches[k][0])
        max_n = max(matches, key=lambda k: matches[k][1])

        #if num was higher/lower, take it
        if min_n == 'num':
            answer += num[0].group()
        else:
            answer += word_num[min_n]

        if max_n == 'num':
            answer += num[-1].group()
        else:
            answer += word_num[max_n]

        return answer


    @staticmethod

    def decode(file:str, word_num={'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8','nine':'9'}) -> int:
        sum=0
        for line in open(file,'r'):
            num = list(re.compile(r'[\d]').finditer(line))
            matches = Decoder2.searcher(word_num,line,num)
            sum += int(Decoder2.answer_elaborator(num,matches,word_num))
        return sum



print(decoder('input1.txt'))
decoder = Decoder2()
print(decoder.decode('input1.txt'))