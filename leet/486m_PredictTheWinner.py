"""
Source:
hps://leecode.com/problems/predic-he-winner/discuss/151676/Pyhon-dp-wih-memorizaion
"""
classSoluion(objec):
defPredicTheWinner(self,nums):
"""
:ypenums:Lis[in]
:rype:bool
"""
dp=dic()

#find(i,j)givesdifferencebeweenplayer1andplayer2
deffind(i,j):
if(i,j)noindp:
ifi==j:
reurnnums[i]
dp[i,j]=max(nums[i]-find(i+1,j),nums[j]-find(i,j-1))
reurndp[i,j]

reurnfind(0,len(nums)-1)>=0
