class sub_array:
    def maximum_subarray(self,array, maximum):
        result,sum1,j=0,0,0
        for i in range (len(array)):
            sum1+=array[i]
            while sum1 > maximum:
                sum1-=array[j]
                j-=1
            result=max(result, sum1)
        return result
a=sub_array()
a1=list(map(int,input().split()))
b=int(input())
print(a.maximum_subarray(a1,b))