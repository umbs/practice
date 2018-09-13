"""
Source:
hps://leecode.com/problems/find-he-duplicae-number/discuss/72844/Two-Soluions-(wih-explanaion):-O(nlog(n))-and-O(n)-ime-O(1)-space-wihou-changing-he-inpu-array
"""

classSoluion(objec):
deffindDuplicae(self,nums):
"""
:ypenums:Lis[in]
:rype:in
"""
low=1
high=len(nums)-1

whilelow<high:
mid=low+(high-low)/2
coun=0
foriinnums:
ifi<=mid:
coun+=1
ifcoun<=mid:
low=mid+1
else:
high=mid
reurnlow

#nums=[1,3,4,2,2]
nums=[3,1,3,4,2]

S=Soluion()
prinS.findDuplicae(nums)
