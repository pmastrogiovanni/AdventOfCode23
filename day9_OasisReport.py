class OasisReport:
    @staticmethod
    def extrapolation(edgevalues:list,backfill:bool) -> int:
        history = 0
        #backwards or forwards extrapolation based on the flag
        for i in range(1,len(edgevalues)):
            if backfill:
                history =  edgevalues[i] - history
            else:
                history = edgevalues[i] + history
        return history
    

    @classmethod
    def prediction(cls,line:str,backfill:bool) -> int:
        nums = [int(num) for num in line.split(' ')]
        #use the flag to save either the last element or the first
        if backfill: side = 0
        else: side = -1
        edgevalues = [nums[side]]
        zeros = 0

        while zeros<len(nums):
            temp = []
            for i in range(len(nums)-1):
                diff = nums[i+1]-nums[i]
                temp.append(diff)
                if diff == 0: zeros += 1

            edgevalues.append(temp[side])
            nums = temp
            if zeros == len(nums):break
            else: zeros = 0

        return cls.extrapolation(edgevalues[::-1],backfill)


    @classmethod
    def report_sum(cls,file:str,backfill = False) -> int:
        with open(file,'r') as f:
            tot_history = 0
            for line in f:
                tot_history += cls.prediction(line.strip(),backfill)
        return tot_history
    


if __name__=='__main__':
    solution = OasisReport()
    #Challenge 1
    print(solution.report_sum('input9.txt'))
    #Challenge 2
    print(solution.report_sum('input9.txt',backfill=True))