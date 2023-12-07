from collections import Counter

class CamelCards:
    @staticmethod
    def result_comp(lines:list) -> int:
        '''
        Compute final results summing the products of the rank of each hand with the bet.
        '''
        result = 0
        for i,line in enumerate(lines):
            result += ((i+1)*int(line.split(' ')[1]))
        return result
    

    @staticmethod
    def same_score(handL:str,handR:str,cards:list) -> str:
        '''
        This function is used to solve ties between hands, based on value.
        '''
        for i in range(len(handL)):
            if handL[i]==handR[i]:continue
            elif cards.index(handL[i]) > cards.index(handR[i]):return 'L'
            else: return 'R'


    @staticmethod
    def joker(c:Counter,cards:list) -> Counter:
        temp = c['J']
        del c['J']

        max_value = max(c.values())
        max_keys = [k for k, v in c.items() if v == max_value]

        #to solve ties between number of cards compute ranks based on the values
        im = 99
        for key in max_keys:
            i = cards.index(key)
            if i < im:
                im = i

        #sum the number of Js to the card with highest value
        c[cards[im]] += temp
        return c
    
    
    @staticmethod
    def score(hand:str,cards:list,jrule:bool) -> int:
        '''
        This function elaborates the value of the hand:
        5 equal cards = 6
        Poker = 5
        Full = 4
        Tris = 3
        Double couple = 2
        Couple = 1
        High card = 0
        '''

        c = Counter(hand)
        if 'J' in hand and len(c.keys())!=1 and jrule:
            c = CamelCards.joker(c,cards)

        l = len(c.keys())

        if l == 1:return 6

        if l == 2 and 3 in c.values():return 4
        elif l == 2:return 5

        if l == 3: return max(c.values())
        
        if l == 4:return 1
        else: return 0


    @classmethod
    def sorter(cls,arr,L,R,cards,jrule):
        i = j = k = 0
    
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            l_score = cls.score(L[i].split(' ')[0],cards,jrule)
            r_score = cls.score(R[j].split(' ')[0],cards,jrule)

            #solve ties
            if l_score==r_score: high = cls.same_score(L[i].split(' ')[0],R[j].split(' ')[0],cards)
            else: high=''

            if l_score < r_score or high=='L':
                arr[k] = L[i]
                i += 1
            elif l_score > r_score or high=='R':
                arr[k] = R[j]
                j += 1
            k += 1
            
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
    
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return arr
    

    @classmethod
    def mergeSort(cls,arr:list,cards:list,jrule:bool) -> list:
        '''Theta(nlogn)'''
        if len(arr) > 1:

            mid = len(arr) // 2     
                
            # Dividing the array elements
            L = arr[:mid]
            # into 2 halves
            R = arr[mid:]
    
            # Sorting the first half
            cls.mergeSort(L,cards,jrule)
            # Sorting the second half
            cls.mergeSort(R,cards,jrule)

            arr = cls.sorter(arr,L,R,cards,jrule)
        return arr
    
    
    @classmethod
    def winnings_compiler(cls, file:str,jrule:bool) -> int:
        with open(file,'r') as f:
            lines = f.readlines()

            if jrule: cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
            else: cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

            lines = cls.mergeSort(lines,cards,jrule)
            result = cls.result_comp(lines)
        return result
    

if __name__=='__main__':
    solution = CamelCards()
    print('PART 1: ')
    print(CamelCards.winnings_compiler('input7.txt',False))
    print('PART 2: ')
    print(CamelCards.winnings_compiler('input7.txt',True))