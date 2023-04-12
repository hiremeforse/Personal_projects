
s = [10,20,30,40,50,80]
target = 60

for i in range(len(s)-2):
    second = i + 1
    last = len(s) - 1

    if s[i] + s[second] + s[last] == target:
        print i, second, last
    elif s[i] + s[second] + s[last] <= target:
        second = second + 1
    elif s[i] + s[second] + s[last] >= target:
        last = last - 1


a = [10, 10, 10]
count = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            count = count + 1
print(count)

s = '{{{)'


stack = []

ch = ['{', '[', '(']
rm_ch = ['}', ']', ')']

for i in range((len(s))):
    if i in ch:
        stack.append(ch[i])
    elif i in rm_ch:
        stack.pop(ch[i])
print(stack)


s = [10,30,110,30,23,45,30,68,79,89,40]

x = 30
reverse_pointer = len(s) - 1
for i in range(len(s)):
    if s[i] == x:
        print(i)

x = 30
for i in range(len(s) -1,0,-1):
    if s[i] == x:
        print(i)

s = [10,20,30,40]
index = 0
holder = []

subset = []

for i in range(len(s)-1):
    subset.append(s, index+1, holder + s[i])
    subset.append(s,index+1, holder)
print(subset)





Subset Problem

s = 'mylccooapp'

def
if s[0] == s[1]


LONGEST Palindrome


s = 'abaabcd'

q = s[::-1]

i = ''

for i in range(len(s)):
    for j in range(len(q)):
        if s[i:j] == q[i:j]:
            if len(i) < len(s[str(i:j)]):
                i = s[i:j]

            print(len(i))

s = 'Punitkulkarni'

longest = ''
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if len(longest) < len(s[i:j]):
            longest = s[i:j]
print(longest)


Bubble sort
a = [50,1,4,5,7,4,3,21,6,78]
for i in range(len(a)):
    for j in range(0, len(a) - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)

a = [50,1,4,5,7,4,3,21,6,78]

for i in range(len(a)):
    min_index = i
    for j in range(i+1,len(a)):
        if a[j] < a[min_index]:
            min_index = j
        a[i] , a[min_index] == a[min_index], a[i]

    print(a)


import operator
stats = {'a':1000000, 'b':3000, 'c': 100}
s = max(stats.iteritems(), key=operator.itemgetter(1))[0]
print(s.s)



count = {}
for s in sorted(s):
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

print(count)


k = [10,20,30,40]
last = ''
for i in range(len(k)):break
    for j in range(i+1,len(k)-1):
        product = k[j] * k[j+1]
        last = max(last , product)
    print(last)



Python program to find the maximum for
each and every contiguous subarray of
size k

import sys

p = [90, 2,12,34]

k = 2

maxi = 0
for i in range(len(p)):



global_max = 0
start = 0
diray = {}



    s = 'Punitkulkarni'
   
    longest = ''
    for i in range(len(s)):
   
        for j in range(i+1,len(s)):
            if len(longest) < len(s[i:j]):
                longest = s[i:j]
    print(longest)

    s = 'abcabcafadfkafbaf'
    global_max = 0
    start = 0
    d = {}
   
    for green_end in range(len(s)):
        if s[green_end] in d:
            print(d[s[green_end]] + 1)
        d[s[green_end]] = green_end
        global_max = max(global_max,(green_end - start + 1))
    print(global_max)


    s = 'ababababb'
    d = {}
   
    for i in s:
        if i not in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
   
    print(d)
   
    all_freq = {}
   
    for i in s:
        if i in all_freq:
            all_freq[i] = all_freq[i]+ 1
        else:
            all_freq[i] = 1
    print(all_freq)






  nums = [10,10,10,10,2034,10,10,56,677,67,89]

  nums.sort()



    for i in range(len(nums)):
        last_pointer = len(nums) - 1
        second_last_pointer = len(nums) - 2
        forward_pointer = (i + 1) - 1
          print(second_last_pointer,last_pointer)
   
        target = 40
   
        if nums[i] + nums[forward_pointer] + nums[second_last_pointer] + nums[last_pointer] == target:
            print(nums[i], nums[forward_pointer], nums[second_last_pointer], nums[last_pointer])
            print("nothing found in the array1")
        elif nums[i] + nums[forward_pointer] + nums[second_last_pointer] + nums[last_pointer] > target:
            last_pointer = last_pointer - 1
            second_last_pointer = second_last_pointer - 1
            print("nothing found in the array2")
        elif nums[i] + nums[forward_pointer] + nums[second_last_pointer] + nums[last_pointer] < target:
            i = i + 1
            forward_pointer = forward_pointer + 1
            print("nothing found in the array3")
        else:
            print("nothing found in the array")
   
    import sys
   
    nums = [10,1010,20,30]
   
    for i in range(len(nums)):
        last_pointer = len(nums) - i
        second_last_pointer = len(nums) - 2
        forward_pointer = (i + 1) - 1
          print(second_last_pointer,last_pointer)
   
        target = 40
 
      for i in range(len(nums)):
          if nums[i] + nums[last_pointer] == target:
              print(i,last_pointer)
              sys.exit(0)
          elif nums[i] + last_pointer > target:
              last_pointer = last_pointer - 1
          elif nums[i] + last_pointer < target:
              forward_pointer = forward_pointer + 1


  s = 'aaabbbbaaa'
  previous = s[0]
  count = 0
  output = ''
  for i in range(len(s)-1):
      if s[i] == previous:
          count = count + 1
      else:
          output = output + str(count) + previous
          previous = s[i+1]
          count = 1
      if i == len(s)-1:
          output = output+str(count) + previous
  print(output)

  arr = [1,2,3,4,5]
  val = 0
  for i in range(len(arr)):
      for j in range(i,len(arr)):
          sum = sum + j
      print(sum)


  s = 'mylccccclccf'
  output = ''
 
  for i in range(len(s)-1):
      if i == len(s)-1:
          print("in this")
          output = output + s[i]
 
      if s[i] != s[i+1]:
          output = output + s[i]
 
 
  print(output)

  /// *****  8 8 8 8 8  Count number of char string in the array ******* /////////


  s = 'abbbbc'   output = a4b4c4
  count = 0
  output  = ''
  for i in range(len(s)-1):
      previous = s[i]
      if s[i] == s[i+1]:
          count = count + 1
      else:
          output = output + str(count) + previous
  print(output)



 
  Sliding Window Tchnique
   
    s = [10,20,30,40,50,50]
 
  a = len(s)
  k = 3
  count = 0
  max_sum= 0
  for i in range(a- k + 1):
      count = 0
      for j in range(k):
          count = count + s[i+j]
      max_sum= max(count,max_sum)
  print(max_sum)


  count minimum numbers to make

  n = [1,2,3,100101]
  a = max(n)
  count = 0
  count_number = 0
  for i in range(len(n)-1):
      if n[i] != a:
          count_number = a - n[i]
          count = count + count_number
  print(count)

  s = "()(())"
  count = 0    
  for i in range(len(s)-1):
      for j in range(i,len(s)):
          f s[i] == '(' and s[i+1] == ')':
              count = count + 2
          else:
              if i == "(" s[j+1] === ")":
                  count = count + 2
      return count

  print(count)
                

  s = [10,20,60,50,400]
  k = 2
  gloabl = 0
  for i in range(len(s)-k+1):
      count = 0
      for j in range(k):
          count = count + s[j]
      gloabl = max(gloabl, count)
  print(gloabl)


  nums = [1,2,3]

  mid = len(nums) // 2

  print(len(str(nums[mid:])))


  gas tank and pertrol probelm

  tank = 0
  start = 0
  total = 0
  for idx, (a, b) in enumerate(zip(gas, cost)):
      tank += (a-b)
      if tank < 0:
          tank = 0
          start = idx + 1
      total += (a-b)
  print -1 if total <0 else start


  s = "acb" 
  t = "ahbgdc"
  pointer_s = pointer_t = 0
        
  while pointer_s < len(s) and pointer_t <len(t):
    
      if s[pointer_s] == t[pointer_t]:
          pointer_s += 1
    
      pointer_t+=1
        
          return pointer_s == len(s)




  s = "CCCbAbbBbbC"
  print(s[1:])
  com = []
  for i in range(len(s)):
      if s[i] not in s[i+1:]:
          com.append(s[i])
  print(com)



  a = str(1432219)

  k = 3
  first_half = (a[0])
  print(first_half + a[k+1:])



  nums = [2,7,9,3,1]

  for i in range(2,len(nums)):
      nums[i] = nums[i] + nums[i-2]
      if nums[i]<nums[i-1]:
          nums[i]=nums[i-1]
  print(max(nums))


  nums = [2,0,2,1,1,0]
  sorted_nums = sorted(nums)
  for i in range(len(nums)):
      if nums[i] != sorted_nums[i]:
          nums[i] = sorted_nums[i]
  print(nums)
  s = []
  cnt = []
  emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
  s = []
  count = 0
  for email in emails:
      local = email.split("@")[0]
      domain = email.split('@')[1]

      local = local.replace('+','')
      local = local.replace('.','')

    
      if local+'@'+domain in s:
          print('Already present')  no need to increment if the ids are same
      else:
          s.append(local+'@'+domain)
          count = count + 1
  print(count) 

   




  q = [4,1,2,3]
  bribes = 0
  for i in range(len(q)-1):
      if q[i] > q[i+1]:
          bribes = bribes + q[i] - q[i+1]
      if bribes >= 2:
          print(bribes)
      else:
          print("too chactoic")












  n = [19]
  m = n.split()
  print(m)

  a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]

  ans = 0
  for i in range(len(a)):
      if ans > 0:
          ans = ans + a[i]
      else:
          ans =  a[i]
  print(ans)
    


  a = [-1, 2, 3, -4, -1, 4]

  postive = [] (1)
  negative = [] (1)
  for i in range(len(a)): 0(n)
      if a[i] > 0:
          postive.append(a[i])
      else:
          negative.append(a[i])

  result = [] 
  for  a,b in zip(postive,negative): 
      result.append(a)
      result.append(b)
  print(result)



  a = [100,80,60,70,60,75,85]
  new =[]
  count = 1
  for i in range(len(a)-1):
      if a[i] > a[i+1]:
          new.append(1)
      else:
          count = count + 1
          i = i - 1 
          new.append(count)
  print(new)



  arr = [2,1,4,7,3,2,5]

  next_pointer = 0
  last_pointr = 0
  new = []
  for i in range(len(arr)):
      if arr[i] > next_pointer:
          next_pointer = next_pointer + 1
      else:
          last_pointr = last_pointr + 1
    
      if next_pointer == last_pointr:
          new.append(next_pointer)
          next_pointer = 0
          last_pointr = 0
      print(next_pointer)


  rating = [1,2,3,4]
  e = []
  for i in range(len(rating) - 3 + 1):
      for j in range(i+1,len(rating)):
          for k in range(i+2,len(rating)):
              if rating[i] > rating[j] > rating[k]:
                  e.append((rating[i] , rating[j],rating[k]))
              else:
                  pass
  print(e)



  a = [1, 2, 3, 6, 5, 4]

  a = sorted(a)
  [1, 2, 3, 4, 5, 6]
  for i in range(2,len(a)-1):
      a[i],a[i+1] = a[i+1],a[i]
      if a[i],a[i+1] = a[i+1],a[i]:
          a[i],a[i+1] = a[i+1],a[i]

  print(a)


  dict = {}

  a = ['geeks','kfdakf','geeks']
  count = 0
  dict = {}
  for i in a:
      if i not in dict:
          dict[i] = 1
      else:
          dict[i] = dict[i] + 1
  print(dict)


  strs = ["flower","flow","flight"]

  for i in strs:
      for j in i:
          if j)
    


    arr = [6 ,8 ,0 ,1 ,3]
  arr = [1, 3, 2, 4]
  a = []
  for i in range(len(arr)-1):
      if arr[i+1] > arr[i] or (arr[i+1] >= arr[i]) in arr[i:]:
          a.append(arr[i+1])
      elif arr[i] > arr[i+1] or i == len(arr):
          a.append(-1)
  a.append(-1)
  print(a)


  s ='I am :IronnorI Ma, i'
  s = s.lower()
  a =[]
  for i in range(len(s)):
      if s[i].isalnum():
          a.append(s[i]).lower()
      result = ''.join(a)
  a = result
  b = result[::-1]

  if a == b:
      print("true")
  else:
      print("flase")



  arr = [1, 2, 3, 6, 5, 4]

  arr = sorted(arr)
  print(arr)


  for i in range(2,len(arr),2):
      if arr[i] < arr[i+1]:
          arr[i], arr[i+1] =  arr[i+1],arr[i]
  print(arr)


  s = "cdd"
  p = "dd"
  len_s = 0
  e = []
  count = 0
  for i in range(len(s)):
      for j in range(i+1,len(s)):
          if s[i] == p[i]:
              print(s[i],p[i])
              print("yes")
          else:
              print("no")


  stack = []
  s = '[[][]]'
  dict = {'[':']'}
  for i in range(len(s)):
      if i  == '[':
          stack.append(i)
      else:
          i == dict[stack[-1]]
          stack.pop()
  print(stack)



  s = '[]][]['

  set = ("{", "(", "[")

  d = {"{": "}", "(": ")", "[": "]"}

  stack = []
  for i in s:
      if i in set:
          stack.append(i)
      elif i == d[stack[-1]]:
          stack.pop()
  if len(stack) == 0:
      print("yes")
  else:
      print("no")



  s = "geekk"
  t = "gesek"


    string.replace(oldvalue, newvalue, count)
  for i in s:
      i] != t[i]:
          s = s.replace(t[i],s[i])
  print(s)



  final = 0
  a = 20
  set = (1,2,3,4,5,6,7,8,9,10,15,16,17)
  count = 0
  for i in range(a+1):
      if i and i + 1 and i in set:
          count = count + 1
      final = max(count,final)
  print(final)


  a = 'punit'
  b = a[::-1]
  x = ''
  for i in range(len(a)):
      for j in range(len(a)):
          if a[i:j] == a[i:j][:-1]:
              if x < a[i:j]:
                  x = a[i:j]
  print(x) 



  matrix = [[1,2],[1,3]]
  k = 2


  new_arr = []
  for i in matrix:
      for j in i:
          new_arr.append(j)
    print(new_arr[k-1])
  print(sorted(new_arr)[k-1])




  nums  = [1,3,9]

  max_num = max(nums)



  for i in range(1,max_num+1):
      print(i)



  arr = [1, 10, 13, 34,56,78,100] 
  k = 78

  low = 0 
  high = len(arr) - 1



  arr = [ 2, 3, 4, 10, 40 ]
  x = 10

  l = 0
  r = len(arr) - 1

  while l <= r:

  	mid = (l + r) // 2;
	
  	if arr[mid] == x:
  		print(mid)

  	  If x is greater, ignore left half
  	elif arr[mid] < x:
  		l = mid

  	  If x is smaller, ignore right half
  	else:
  		r = mid


  Longest palindrimic substring

  s = "babad"

  for i in range(len(s), -1, -1):
  	for j in range(len(s) - i, -1, -1):
  		if s[j:j+i] == s[j:j+i][::-1]:
  			print(s[j:j+i])


  a = [0,0,0,0,0,0]

  new_list = []
  last = len(a) - 1
  for i in range(len(a)-2):
  	pointer_two = i + 1

  	if a[i] + a[pointer_two] + a[last] == 0:
  		print(i,pointer_two,last)
  		last = last - 1
  		i = i + 1
  		new_list.append((i,pointer_two,last))
  	elif a[i] + a[pointer_two] + a[last] > 0:
  		last = last - 1
  	elif a[i] + a[pointer_two] + a[last] < 0:
  		i = i + 1
  print(new_list)
	












  @app.route(/paneer= None)
  class Paneer_Serach:
  	paneer = request.args()

  	db = connect_to db


  	panner_list  = [shai paneer,paneer butter masala]

  	  data = select panner form the panner_table where panner = panner 

  	data = select * from the paneer

  	for result in data:
  		if paneer in paneer_list:
  			result = paneer
	
  	retun jsonfiy(result)



  a = [-2,1,4,-5,6,7]
  square = 0 
  new_list = []
  for i in range(len(a)):
  	square = square + a[i] * a[i]
  	new_list.append(square)
  	square = 0
  print(sorted(new_list))

  a = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
  new_a = set(sorted(a))
  print(new_a)
  print(len(new_a))
  b = [2, 1, 8, 3]

  new_list = []

  for num in range(len(b)):
  	if b[num] == a[num]:
  		new_list.append(b[num])
  		new_list.append(b[num])
  	else:
  		b[num] in a
  		new_list.append(b[num])
  		new_list.append(b[num])

  print(new_list)



  nums = [1,3,-1,-3,5,3,6,7]
  k = 3
  listrr = []
  maxx = 0
  new = []
  a = 0
  b = []
  final_list = []
  for i in range(len(nums) - k + 1):
  	for j in range(k):
  		if nums[j] > nums[j+1]:
  			maxi = nums[j]
  		else:
  			maxi = nums[j+1]
  	final_list.append(maxi)
  	maxi = 0
  print(final_list)
		
	

	

		
	
  stack = []

  stack.append(2)

  print(stack)
  print(stack[-1])

  print(stack.pop())

  print(stack.peek())


nums = [1,0,-1,0,-2,2]
target = 0

result = []


nums = sorted(nums)

  for i in range(len(nums)-1):
  	first = i
  	second = first + 1
  	last = len(nums) - 1
  	second_last = len(nums) - 2

  	if (nums[first] + nums[second] + nums[last] + nums[second_last]) == target:
  		result.append([nums[first],nums[second],nums[last] ,nums[second_last]])
  		first = i + 1
  		second = second + 1
  		last = last -1 
  		second_last = second_last - 1
  	elif nums[first] + nums[second] + nums[last] + nums[second_last] > target:
  		last  =  last - 1
  		second_last = second - 1
  	elif nums[first] + nums[second] + nums[last] + nums[second_last] < target:
  		first = first + 1
  		second = second + 1
  print(result)



  a = ['ab','bs']
  b = ['av','he']

  s = ' '.join(str(a))
  s =  ','.join(str(a))
  print(s)
  for i in range(len(a)):
  	for j in range(len(b)):
  		if a[i] == b[i]:
  			print("yes")
  		else:
  			print("no")



  a = [1,2,3,4,5,6,8,9,10,11]
  le = len(a)

  b = (le + 1) * (le + 2) // 2

  ans =  b - sum(a)

  print(ans)
 
  dict = {}

  for i in a: 0(n)
  	if i not in dict:
  		dict[i] = 1
  	else:
  		dict[i] = dict[i] + 1
  print(dict)


  for i in range(11): (0(n))
  	if i not in dict: 0(1)
  		print(i)

  		o(n) + o(n) + o(1)
  		n 


  word1 = ["ab", "c"]
  word2 = ["a", "bc"]
  a = str(word1).replace("," ,'')
  a = ''.join(word1)
  print(a)

import operator


  start = [1, 3, 0, 5, 8, 5]
  end = [2, 4, 6, 7, 9, 9]

    [0:7] [1:2] [3:4] [5:9] [5:7] [8:9] 

  zipped = zip(start,end)
  res = sorted(zipped, key = operator.itemgetter(0))
  count = 0
  for i in res:
  	if i[1] > i+1[1]:
  		count = count + 1
  print(count)
	
	  intervals = [[0,30],[5,10],[15,20]]
	  intervals.sort()


	  last_end = -1 

	  for start,end in intervals:
	  	if last_end <= start:
	  		last_end = end
	  	else:
	  		print("Flase")
	  print(True)


  s = ")()())"

  count = 0
  for i in range(len(s)):
  	if s[i] == "(" and s[i + 1] == ")":
  		count = count + 
  print(count)
		


  A Program to check if strings are rotations of each other or not

  https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings

  s = 'abcd'

  substring = []

  for i in range(len(s)):
  	for j in range(i+1,len(s)+1):
  		substring.append(s[i:j])
  print(substring)

  dictionary = [ "man", "go", "mango","i", "like", "sam", "sung", "samsung", "mobile",
  "ice","cream", "icecream", "man", "go", "mango" ]

  a = ''.join(dictionary)
  b = "ilike"

  lenb = len(b)

  if b in a:
  	print("yes")
  else:
  	print("no")




  B = { "i", "like", "sam", "sung", "samsung", "mobile",
  "ice","cream", "icecream", "man", "go", "mango" }
  A = "ilikesamsung"

  l= []

  for i in range(len(A)):
  	for j in range(i+1,len(A)):
  		if A[i:j] in B:
  			l.append((A[i:j]))
  print(l)



  s = [10,20,30,40,50,80]
  target = 60
 
  for i in range(len(s)-2):
      second = i + 1
      last = len(s) - 1
 
      if s[i] + s[second] + s[last] == target:
          print i, second, last
      elif s[i] + s[second] + s[last] <= target:
          second = second + 1
      elif s[i] + s[second] + s[last] >= target:
          last = last - 1

 
  a = [10, 10, 10]
  count = 0
  for i in range(len(a) - 1):
      for j in range(i + 1, len(a)):
          if a[i] > a[j]:
              count = count + 1
  print(count)

s = '{{{)'


  stack = []
 
  ch = ['{', '[', '(']
  rm_ch = ['}', ']', ')']
 
  for i in range((len(s))):
      if i in ch:
          stack.append(ch[i])
      elif i in rm_ch:
          stack.pop(ch[i])
  print(stack)


s = [10,30,110,30,23,45,30,68,79,89,40]

x = 30
  reverse_pointer = len(s) - 1
  for i in range(len(s)):
      if s[i] == x:
          print(i)
 
  x = 30
  for i in range(len(s) -1,0,-1):
      if s[i] == x:
          print(i)
 
  s = [10,20,30,40]
  index = 0
  holder = []
 
  subset = []
 
  for i in range(len(s)-1):
      subset.append(s, index+1, holder + s[i])
      subset.append(s,index+1, holder)
  print(subset)



  Subset Problem

  s = 'mylccooapp'
 
  def
  if s[0] == s[1]


  LONGEST Palindrome

 
  s = 'abaabcd'
 
  q = s[::-1]
 
  i = ''
 
  for i in range(len(s)):
      for j in range(len(q)):
          if s[i:j] == q[i:j]:
              print(s[i:j])
   
  s = 'Punitkulkarni'
 
  longest = ''
  for i in range(len(s)):
      for j in range(i+1,len(s)):
          if len(longest) < len(s[i:j]):
              longest = s[i:j]
  print(longest)


  Bubble sort
  a = [50,1,4,5,7,4,3,21,6,78]
  for i in range(len(a)):
      for j in range(0, len(a) - 1):
          if a[j] > a[j + 1]:
              a[j], a[j + 1] = a[j + 1], a[j]
  print(a)

  a = [50,1,4,5,7,4,3,21,6,78]
 
  for i in range(len(a)):
      min_index = i
      for j in range(i+1,len(a)):
          if a[j] < a[min_index]:
              min_index = j
          a[i] , a[min_index] == a[min_index], a[i]
 
      print(a)
 
 
  import operator
  stats = {'a':1000000, 'b':3000, 'c': 100}
  s = max(stats.iteritems(), key=operator.itemgetter(1))[0]
  print(s.s)



  count = {}
  for s in sorted(s):
    if s in count:
      count[s] += 1
    else:
      count[s] = 1
 
  print(count)


  k = [10,20,30,40]
  last = ''
  for i in range(len(k)):break
      for j in range(i+1,len(k)-1):
          product = k[j] * k[j+1]
          last = max(last , product)
      print(last)



  Python program to find the maximum
  
  
  
  for
  each and every contiguous subarray of
  size k

import sys

  p = [90, 2,12,34]
 
  k = 2
 
  maxi = 0
  for i in range(len(p)):
 
 
 
  global_max = 0
  start = 0
  diray = {}



  s = 'Punitkulkarni'
 
  longest = ''
  for i in range(len(s)):
 
      for j in range(i+1,len(s)):
          if len(longest) < len(s[i:j]):
              longest = s[i:j]
  print(longest)

  s = 'abcabcafadfkafbaf'
  global_max = 0
  start = 0
  d = {}
 
  for green_end in range(len(s)):
      if s[green_end] in d:
          print(d[s[green_end]] + 1)
      d[s[green_end]] = green_end
      global_max = max(global_max,(green_end - start + 1))
  print(global_max)


  s = 'ababababb'
  d = {}
 
  for i in s:
      if i not in d:
          d[i] = d[i]
      else:
          d[i] = 1
 
  print(d)
 
  all_freq = {}
 
  for i in s:
      if i in all_freq:
          all_freq[i] = all_freq[i]+ 1
      else:
          all_freq[i] = 1
  print(all_freq)





 
  nums = [10,10,10,10,2034,10,10,56,677,67,89]
 
  nums.sort()



  for i in range(len(nums)):
      last_pointer = len(nums) - 1
      second_last_pointer = len(nums) - 2
      forward_pointer = (i + 1) - 1
        print(second_last_pointer,last_pointer)
 
      target = 40
 
      if nums[i] + nums[forward_pointer] + nums[second_last_pointer] + nums[last_pointer] == target:
          print(nums[i], nums[forward_pointer], nums[second_last_pointer], nums[last_pointer])
          print("nothing found in the array1")
      elif nums[i] + nums[forward_pointer] + nums[second_last_pointer] + nums[last_pointer] > target:
          last_pointer = last_pointer - 1
          second_last_pointer = second_last_pointer - 1
          print("nothing found in the array2")
      elif nums[i] + nums[forward_pointer] + nums[second_last_pointer] + nums[last_pointer] < target:
          i = i + 1
          forward_pointer = forward_pointer + 1
          print("nothing found in the array3")
      else:
          print("nothing found in the array")
 
  import sys
 
  nums = [10,1010,20,30]
 
  for i in range(len(nums)):
      last_pointer = len(nums) - i
      second_last_pointer = len(nums) - 2
      forward_pointer = (i + 1) - 1
        print(second_last_pointer,last_pointer)
 
      target = 40
 
      for i in range(len(nums)):
          if nums[i] + nums[last_pointer] == target:
              print(i,last_pointer)
              sys.exit(0)
          elif nums[i] + last_pointer > target:
              last_pointer = last_pointer - 1
          elif nums[i] + last_pointer < target:
              forward_pointer = forward_pointer + 1


  s = 'aaabbbbaaa'
  previous = s[0]
  count = 0
  output = ''
  for i in range(len(s)-1):
      if s[i] == previous:
          count = count + 1
      else:
          output = output + str(count) + previous
          previous = s[i+1]
          count = 1
      if i == len(s)-1:
          output = output+str(count) + previous
  print(output)

  arr = [1,2,3,4,5]
  val = 0
  for i in range(len(arr)):
      for j in range(i,len(arr)):
          sum = sum + arr[j]
      print(sum)


  s = 'mylccccclccf'
  output = ''
 
  for i in range(len(s)-1):
      if i == len(s)-1:
          print("in this")
          output = output + s[i]
 
      if s[i] != s[i+1]:
          output = output + s[i]
 
 
  print(output)

  /// *****  8 8 8 8 8  Count number of char string in the array ******* /////////


  s = 'abbbbc'   output = a4b4c4
  count = 0
  output  = ''
  for i in range(len(s)-1):
      previous = s[i]
      if s[i] == s[i+1]:
          count = count + 1
      else:
          output = output + str(count) + previous
  print(output)



 
  Sliding Window Tchnique

  s = [10,20,30,40,50,50]
 
  a = len(s)
  k = 3
  count = 0
  max_sum= 0
  for i in range(a - k + 1):
      count = 0
      for j in range(k):
          count = count + s[i+j]
      max_sum = max(count,max_sum)
  print(max_sum)


  count minimum numbers to make

  n = [1,2,3,100101]
  a = max(n)
  count = 0
  count_number = 0
  for i in range(len(n)-1):
      if n[i] != a:
          count_number = a - n[i]
          count = count + count_number
  print(count)



   Pring all the substrings prgram

  s ='punit'
 
  for i in range(len(s)):
      for j in range(i+1,len(s)+1):
          print(s[i:j])



  s = [1,2,3,4,5,6,7]
 
  k = 5
 
  a = (s[:-k])
 
  b = (s[-k:])
 
  print (b + a)
  Str = "aab"
  count = 0
  for i in range(len(Str)):
      for j in range(i, len(Str), -1):
          if Str[i:j] == Str[i:j][::-1]:
              print("yes")
          else:
              print("no")

  arr = [5, 4, 4, 2, 2, 8]
  a = [i for i in arr if i!= min(arr)]
  print(a)

  arr = [8, 12, 16, 4, 0, 20]
  k = 12
  count = 0
  arr.sort()
  for i in range(len(arr)):
      last_pointer = (len(arr)-1 - i)
      if arr[last_pointer] - arr[i] == k:
          count = count + 1
      elif arr[last_pointer] - arr[i] > k:
          last_pointer = last_pointer - 1
      elif arr[last_pointer] - arr[i] < k:
          last_pointer = i + 1
      elif arr[i] == arr[last_pointer]:
          print("noo matching string")
          break
  print(count)
 
  arr = [10,20,40,50,-1,-3,-5, 60]
 
  for i in range(len(arr)):

 
  s = [10,60,30,0,50]
 
  target = 60
  for i in range(len(s)):
      last_pointer = len(s) - 1
 
      if s[i] + s[last_pointer] == target:
          print(s[i], s[last_pointer])
          i = i + 1
          last_pointer = last_pointer - 1
      elif s[i] + last_pointer == target:
          print(s[i],s[last_pointer])

  arr = [7, 1 ,3 ,5, 2, 4, 6, 7]
  answer = 0
  count = 0
  for i in range(len(arr)-1):
      for j in range(i+1,len(arr)):
          if arr[j] < arr[i]:
              arr[i], arr[j] = arr[j], arr[i]
              count = count + 1
  print(count)

  s = "abcd"
  s2= "bdac"
 
  for first in range(len(s)):
      pointer_one = first
      for j in range(first+1,len(s2)):
          if s2[j] != pointer_one:
              print(s2.replace(s2[j],s[pointer_one]))



  def number(n):
      if n == 1:
          return "yes"
      else:
          return number(n-1) + number(n-2)
 
      n = 10


  que = [10, 12, 11]

  count = 0
  golbal_max = 0
  for i in range(len(que)-1):
      if que[i] < que[i+1]:
          count = count + 1
 
      else:
          count = 0
      golbal_max = max(golbal_max,count)
 
  print(golbal_max)

 
  s = 'i am good'
 
  s = s.split(" ")
  s = s[::-1]
  s = ' '.join(s)
  print(s)



import sys
n = 5
  result = 0
  for i in range(n):
      if i > 1:
          result = i * i
  print(result)
 
 
  s1 = [10,20,30,40,50]
  s2 = ''
 
  k = 3

 
  for i in range(len(s1)-k-1):
      for j in range(k):
          print(s[j])






  n = 2
  fact = 1
  for i in range(1,n):
      fact = fact * i
  print(fact)



  s = "punt"
  rev =''
  for i in reversed(range((len(s)))):
      rev = rev + s[i]
  print(rev)



  n = 6
  fact = 1
  for i in range(1,n):
      fact = fact * i
    print(fact)
 
  s = "ppunit"
  my_dict = {}
  for i in s:
      if i in my_dict:
          my_dict[i] = my_dict[i] + 1
      else:
          my_dict[i] = 1
  print(
  my_dict)

 
  a = ["111", "55555555", "22222"]
  my_len = 0
  global_var = 0
  dumy = ''
  for i in range(len(a)):
      if len(a[i]) > len(dumy):
          dumy = a[i]
  print(sorted(a)[-2])

 
  s = [1,2,3,4,5,6,7,8]
  k = 2
 
  for i in range(len(s)-2):
      for j in range(k):
          sum = i + j
      print(sum)

  Target Sum

  s = [10,20,30,40]
  k = 50
  for i in range(len(s)):
      for j in range(i+1,len(s)):
          if s[i] + s[j] == k:
              print(s[i],s[j])

  def main():
      print("hello world")
 
  if __name__=="__main__":
      main()



s = "{}{}()()()"

set = ("{", "(", "[")

d = {"{": "}", "(": ")", "[": "]"}
 
  stack = []
  for i in s:
      if i in set:
          stack.append(i)
      elif i == d[stack[-1]]:
          stack.pop()
  if len(stack) == 0:
      print("yes")
  else:
      print("no")

  import sys
  import Counter
 
  s = "loveleetcode"
 
  c = Counter(s)
 
  print(c)
 
  d = {}
  for i in s:
      if i not in d:
          d[i] = 1
      else:
          d[i] = d[i] + 1
  print(d)


s = "}][}}(}][))]"

  dict = {"(": ")", "{": "}", "[": "]"}
 
  set = ('(', '{', '[')
 
  stack = []
 
  for i in s:
      if i in set:
          stack.append(i)
      elif stack and i == (dict[stack[-1]]):
          stack.pop()
 
  if len(stack) == 0:
      print "YES"
  else:
      print "NO"


 
  s = 'abc'
 
  x = 'bca'
 
  for i in range((len(s))):
      for j in range(i,len(s)):
          if s[i] == s[j]:
              print("yes")
          else:
              print("no")







  d = 'sahil'
 
  len_d = len(d)
 
 
  for i in range(len(s)-len_d+1):
      i = i + len_d
      if s[i:len_d] == d:
          print("yes")
      else:
          print ("no")



  s = 'geeksforgeeks'
  second_pointer = ''
  dic = {}
  for i in range(len(s)):
      if i not in dic:
          dic[s[i]] = 1
      else:
          dic[s[i]] = dic[s[i]] + 2
  print(dic)



  Longest substring without repating charachters

  s = 'abcabcd'
  maximum = 0
 
  str_list = []
  longest = 0


  str_list = []
  length = 0
 
  for i in s:
      if i in str_list:
          str_list = str_list[str_list.index(i) + 1:]
 
      str_list.append(i)
      length = max(length, len(str_list))
 
  print (length)

 
  s = [10,20,30,30,30]
  a = len(s)
  k = 3
  count = 0
  max_sum= 0
  result = 0
  for i in range(a - k + 1):
      count = 0
      for j in range(k):
          watch = j
          count = count + s[i+j]
      result = max(result, count)
  print(result)




  s = [10,20,30,40,50,60]
  k = 3
  for i in range(len(s) - k + 1):
      count = 0
      first_loop = i
      for j in range(k):
          second_loop = s[j]
          a = s[j]
          count = count + s[i+j]
      maximum = max(count,maximum)
  print(maximum)




   find the index of k the element
  s = 'punitkulkarni'
  k = 'kulkarni'
 
  for i in range(len(s)):
      ans = s[i:]
      if s[i:] == k:
          print(i)
      else:
          print("no")
 
 
  my_dict = {1:'a,','b','c',2 : ['f','g','k']}
 
  for key,value in my_dict.items():
      print(key,value)



  s = [10,20,62,411]
 
  k = 2
  max_count = 0
  for i in range(len(s)-k + 1):
      count = 0
      for j in range(k):
          count = count + s[i:j]
      max_count = (count,max_count)
  print(max_count)




  s = [2, 3, 10, 6, 4, 8, 1]
  max_diff = 0
  ma = 0
  for i in range(len(s)):
      for j in range(i+1,len(s)):
          if s[i] < s[j]:
              max_diff = s[j] - s[i]
          ma = max(max_diff, ma)
  print(ma)
 
  0(n^ 2) ~ 0(n2)



  s = [1,2,3,-2,5]
 
  max_count = 0
  for i in range(len(s)-1):
      count = 0
      for j in range(i+1,len(s)):
          count = s[i] + s[j]
      max_count = max(count,max_count)
  print(max_count)



  s = [-1,-2,-3,-4]
 
  max_so_far = 0
  max_ending_here = 0
 
  for i in range(0, len(s)):
      max_ending_here = max_ending_here + s[i]
      max_ending_here = max_ending_here
 
        if max_so_far is less than max_ending_here
        then update max_so_far
      if (max_so_far < max_ending_here):
          max_so_far = max_ending_here
          max_so_far = max_so_far
 
            check if max_ending_here becomes negative at any point
        then make it 0
      if max_ending_here < 0:
          max_ending_here = 0
 
  print(max_so_far)
 


  s = [74, -72 ,94 ,-53 ,-59, -3 ,-66, 36, -13, 22, 73, 15, -52, 75]
 
 
  max_count = 0
  count = 0
  for i in range(len(s)-1):
      count = 0
      for j in range(i,len(s)):
          count = count + s[i]
      max_count = max(count, max_count)
  print(max_count)



  Kadanes Algorithm


  a = [-2,1,-3,4,-1,2,1,-5,4]
 
  current_sum = 0
  over_all_sum = 0
 
  for i in range(len(a)):
      if current_sum >= 0:
          current_sum = current_sum + a[i]
      else:
          current_sum = a[i]
 
      if current_sum > over_all_sum:
          over_all_sum = current_sum
  print (over_all_sum)



  s = [-2,1,-3,4,-1,2,1,-5,4]
 
  count = 0
  global_max = 0
  for i in range(len(s)):
      count = 0
      for j in range(i,len(s)):
          count = count + s[j]
      global_max = max(count,global_max)
  print(global_max)





  s ='google'
  s2 = s[::-1]
  empty = []
  for i in range(len(s)):
      for j in range(i+1, len(s)+1):
          if s[i:j] == (s[i:j][::-1]):
              empty.append( )
              i = len(s[i:j])
  print(empty)


 
  s = 'aabbaccacc'
 
  s = sorted(s)


  count = 0
  output = ''
  for i in range(len(s)-1):
      previous = s[i]
      if s[i] == s[i+1]:
          count = count + 1
      else:
          output = output + str(count) + str(previous)
  print([output])



  Jump Game

  s = [10,20,30,10,30,40]
 
  s = set(s)
 
  print(s)

  nums = [2,3,1,1,4]
 
      ( 2,0), (3,2), (3,3), (4,4)
 
        2 <  0   3 <  1     3 <  2      4 <  3
 
  nums = [3,2,1,0,4]
 
      (3,0) , (3,2), (3,3), (3,3), (4,8)
        0       1      2      3       4
 
      3 < 0   3 < 1   3 < 2   3 < 3  3 < 4

   
  reachable = 0
  for i in range(len(nums)):
      if reachable < i:
          print(False)
      reachable = max(reachable, nums[i] + i)
 
  print(True)


  s  = [8 ,-2 ,-2, 0, 8 ,0 ,-6 ,-8 ,-6, -1]
  count = 1
  max_count = 0
  for i in range(len(s)):
      count = count * s[i]
      max_count = max(count,max_count)
  print(max_count)

 
  arr = [0 ,2 ,1, 2, 0,67,76,21,445,67,89,0,45,66]
  for i in range(len(arr) - 1):
      for j in range(i,len(arr)):
          if arr[i] > arr[j]:
              arr[i], arr[j] = arr[j], arr[i]
  print(arr)


  a = 1
  b = 2
  c = 3
 
  while True:
      if a + c == b:
          print("1")
      print("0")



  a = [1, 3, 5, 7]
  b = [0, 2, 6, 8, 9]
 
  0 > 1

  le = len(a) - 1
  for i in range(len(b)):
      if a[le] > b[i]:
          a[le], b[i] = b[i], a[le]
          le = le - 1
  print(sorted(a),sorted(b))


  arr = [1 ,4, 45, 6 ,10, 8]
  k = 13
 
  arr = sorted(arr)
 
  last = len(arr) - 1
 
  for i in range(len(arr) - 2):
 
      second = i + 1
      if arr[i] + arr[second] + arr[last] == k:
          print("yes")
      elif arr[i] + arr[second] + arr[last] > k:
          last = last - 1
      elif arr[i] + arr[second] + arr[last] < k:
          second = second + 1




 
  s = 'geek'
  t = 'gesek'
 
 
 
  if s == t:
      print(0)
  count = 0
  for i in range(len(t)-1):
      if s[i] != t[i]:
         t = t.replace(t[i],'')
         count = count + 1
  print(count)



  import statistics
 
 
  d = 3
  expenditure = [10 ,20, 30 ,40, 50]
  count = 0
  for i in range(len(expenditure)-d + 1):
      ((expenditure[i:i+d]) / d * 2) >= expenditure[d:d+1]
      count = count + 1
  print(count)


 
  a = 'OUDFRMYMAW'
 
  b = 'AWHYFCCMQX'
 
 
  result = ''
  for i in range(len(a)):
      if a[i] in b[i+1:]:
          result = result + a[i]
  print(len(result))
 
 
  text1 = "abcde"
  text2 = "ace"
  count = 0
 
  for i in range(len(text2)):
      if text2[i] != text1[i]:
          text1 = text1.replace(text1[i], '')
          count = count + 1
  print(len(text1))




  k = 2
  s = sorted(s)
 
    s = [1 ,5, 3, 4, 2]
 
  count = 0
  for i in reversed(range(len(s))):
      for j in reversed(range(i,len(s))):
          if s[i] - s[j] == k:
              count = count + 1
  print (count)


 
  s = (1,1)
  s = sorted(s)
 
  count = 0
  for i in range(len(s)-1):
      count = count + s[i]
  if count == max(s):
      print("yes")
  else:
      print("no")





 
  gun = 'aba'
 
  mag = 'aba'
 
  mag = sorted(mag)
 
  dict1 = {}
  dict2 = {}
 
 
  for i in gun:
      if i not in dict1:
          dict1[i] = 1
      else:
          dict1[i] = dict1[i] + 1
    print(dict1)
 
  for i in mag:
      if i not in dict2:
          dict2[i] = 1
      else:
          dict2[i] = dict2[i] + 1

 
  for i in dict1:
      if dict1[i] in dict2 and dict1[i] == dict2[i]:
          print("True")
      else:
          print("False")

   
  for key in dict1:
      if dict1.get(key) == dict2.get(key):
          print("True")
      else:
          print("False")









  print(dict2)





  mag = sorted(mag)

  if gun in mag:
      print("True")
  else:
      print("false")

 
  dict1 = {}
 
  for i in range(len(gun))



  arr = [2,4,2,6,1,7,8,9,2,1]
  count = 1
  total = 0
  min_val = 1
  ans = 1
  for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
          total = total + 1
          print(total)
          ans = ans + total
      else:
          ans = ans + min_val
          print(ans)



  s = 'abcdefghijklmnopqrstuvwxyz'
 
  sub_string = 'abcxyzabcdefg'
 
 
  for i in range(len(s)):
      for j in range(i,len(s)):
          if s[i:j] == sub_string:
              print(i,j)



  arr = [4,6,4,5,6,2]
  count = 1
  total = 0
  min_val = 1
  at_least = 1
  count = 1
  total = 1
  min_val = 1
  ans = 1
  emp = []
  for i in range(len(arr) - 1):
      if arr[i] < arr[i + 1]:
          total = total + 1
          emp.append(total)
      elif arr[i] == arr[i + 1]:
          emp.append(total)
      else:
          total = total - 1
          emp.append(total)
  print (emp)



  s = [10,20,30,40,50,50]
  k = 3
  a = len(s)
  count = 0
  max_sum = 0
  for i in range(a - k + 1):
      count = 0
      for j in range(k):
          count = count + s[i+j]
      max_sum = max(count,max_sum)
  print(max_sum)



  Longest consecutive subsequence
 
  a = [1,3,10,4,20,2,8,9]
 
 
  a = sorted(a)
  print(a)
  max_len = 0
  count = 0
  for i in reversed(range(len(a))):
      if (a[i-1]) in a:
          count = count + 1
      max_len = max(count,max_len)
  print(max_len)



  a = 'abcdefxyz'
  b = 'xyz'
  le = len(b)
  le_a = len(a)
 
 
  for i in range(len(a) - le + 1):
      for j in range(i, le_a + 1):
          if a[i:j] == b:
              print(i,j)

 
 
  s = "catsandog"
  wordDict = ["cats", "dog", "sand", "and", "cat"]
 
  for i in range(len(wordDict)):
     if wordDict[i] in s:
         print("yes")



  dict1 = {'a' : 10, 'b' : 20}
 
  dict2 =  {'a' : 10, 'b' : 20}
 
  for key,values in dict1.items():
      if dict1.values == dict2.values():
          print("yes")





 
 
  for key,value in dict1.items():
      print(dict1[key][key])


 
 
  s = set[1, 1, 3]
 
    print(s)
 
  from  statistics import median
 
  nums1 = [1,3]
  nums2 = [2]
  new_num = []
 
  for i in range(len(nums1)):
          new_num.append(nums1[i])
 
  for i in range(len(nums2)):
          new_num.append(nums2[i])
    print len(new_num) / 2
 
  print(median(new_num))

 
  index = len(new_num) // 2
 
  if (len(new_num) % 2):
      print(new_num[index])
  else:
      print(new_num[index] + new_num[index + 1] / 2)



  Python code to implement Fibonacci series

  Function for fibonacci
  def fib(n):
 
  	  Stop condition
  	if (n == 0):
  		return 0
 
  	  Stop condition
  	if (n == 1 or n == 2):
  		return 1
 
  	else:
  		return (fib(n - 1) + fib(n - 2))
 
  fib = fib(5)
  print(fib)

  dict1 = {
  2 : ['A','B','C'],
  3 : ['D','E','F'],
  4 : ['G','H','I'],
  5 : ['J','K','L'],
  6 : ['M','N','O'],
  7 : ['P','Q','R','S'],
  8 : ['T','U','V'],
  9 : ['W','X','Y','Z']
  }
 
  s = ["4444,3333"]




  Time_Complexity
 
  a = [-1, 0, 1, 2, -1, -4]
  target = 0
 
  a = sorted(a)        k1 = 1
 
 
  first_pointer = a[0]               k2 = 2
  last_pointer = len(a) - 1
 
 
  for i in range(len(a)-1):                         k3n = 3
      first_pointer = a[0]
      second_pointer = i + 1
      if a[first_pointer] + a[second_pointer] + a[last_pointer] == target:
          print(a[first_pointer], a[second_pointer], a[last_pointer])
      elif a[first_pointer] + a[second_pointer] + a[last_pointer] >= target:
          last_pointer = last_pointer - i
      elif a[first_pointer] + a[second_pointer] + a[last_pointer] <= target:
          first_pointer = first_pointer + i
          second_pointer = second_pointer + i
      else:
          print("nothing found")
 
 
  tn = k1 + k2 + k3n
 
  ignore_k_Values = 0(n) 

 Robbery
  nums = [1000,100,7,9,3,200]
  for i in range(2,len(nums)):
      print(nums[i])
      nums[i] = nums[i] + nums[i-2]
      if nums[i]<nums[i-1]:
          nums[i]=nums[i-1]
      print (nums[-1])

  nums = [2,3,-2,4]
  result = 0
  for i in range(len(nums)):
     for j in range(i+1,len(nums)):
         result = (nums[i] * nums[j])




  max_pro, min_pro = nums[0], nums[0]
 
    result will store the final max product
  result = max_pro
 
  for i in range(1, len(nums)):
      current = nums[i]
 
      temp_max = max(current, max_pro * current, current * min_pro)
                      3      ,    2 * 3         , 3 * 2  ==  6
                      -2      ,  6 *  - 2        , -2 * 3 == - 2
                      4       ,  6 * 4  ,         , 4 * - 12 = -24
 
      min_pro = min(current, max_pro * current, current * min_pro)
                      3       , 2 * 3         , 2 * 3 ==  3
                      - 2 ,   6 * -2          ,   -2 * - 2 == - 12
 
 
      max_pro = temp_max
 
      result = max(result, max_pro)
                      0 , 6
 
  print(result)



 
  nums = [10, 19, 6, 3, 5]
  count = 0
 
 
  for i in range(len(nums)):
 
      count = 0
      min_index = i
 
      for j in range(i+1,len(nums)):
 
          if nums[min_index] > nums[j]:
              min_index  = j
 
      nums[i], nums[min_index] = nums[min_index], nums[i]
 
 
  print(count)

  nums = [1, 3, 3]
 
 
  for i in range(len(nums)-1):
      if nums[i] == nums[i+1] and nums[i] > 1:
          print(nums[i], nums[i] - 1)
      else:
          print(nums[i+1])




  Product array

  arr = [10, 3, 5, 6, 2]
  product = 1
  em = []
  for i in range(len(arr)):
      product = product * arr[i]
  print(product)
 
 
  for i in range(len(arr)):
      ans = product / arr[i]
      em.append(ans)
  print(em)





arr = [2, 6, 3 ,4 ,7, 2, 10, 3 ,2, 1]

arr = sorted(arr)

1 +10 , 2, 2, 2, 3, 3, 4, 6, 7, 10

0 - 11

-7 + 12

- 6 + 12


  print(arr)
 
  k = 10
 
  for i in range(len(arr)):
      pointer_one = i
      last_pointer = len(arr) - 1
 
      if (arr[last_pointer] - k) - (arr[pointer_one] + k) > 0:
          print(arr[last_pointer] - k) - (arr[pointer_one] + k)
      else:
          print(arr[last_pointer] - k) - (arr[pointer_one] + k)
          print("yenu sikila")
          last_pointer = last_pointer - 1






  class rectange(int width,int length):
 
          length, width
 
 
 
 
      def calculate(self):
 
 
 
 
  t = rectange()
  t.calculate(12,30)

 


  class based oopps data base    private table
  xor = 2 elemnent will give  
 
  arr = [1,2,1,2,3,4,3]
 
 
  dict  = {1:1,2:1,3:0,4:1}



  target = 4
 
  arr =
 
 
 
  for i in range(len(arr)):
      if arr[i] in arr[]


  str = "aabbbbcccccccc"
  ma = ''
  max_value = 0
  for i in range(len(str)):
      for j in range(i + 1, len(str)):
          if str[i] == str[j]:
              ma = len(str[i:j])
      max_value = max(ma,max_value)
  print(max_value)




  str1 = 'ABCDGH'
  str2 = 'AEDFHR'
  new_str = ''
  for i in range(len(str1)):
      if str1[i] in str2:
          new_str = new_str + str1[i]
  print(new_str)




  a = [10,20,40,50,60]
  k = 3
 
  for i in range(len(a)-k+1):
      count = 0
      for j in range(k):
          count = count + a[i+j]
      print(count)


  s =[1,-1, -2, 4, 3]
  max_product = 1
  final_pro = 1
  for i in range(len(s)):
      max_product = max_product * s[i]
  final_pro = max(final_pro,max_product)
 
  print(final_pro)


  a = sorted(a)
  k = 5
  b = []
 
  for i in range(len(a)):
      if a[i] < 0:
          b.append(abs(a[i]))
          sorted(b)
  print(b)
  a = [5, -2, 5, -4, 5, -12, 5, 5, 5, 20]
 




  a = [1, 10, 5, 2, 7]
 
  k = 9
  count = 0
  min_len = 0
  mini = 1
  empty = []
 
 
  if k in a:
      print(1)
 
  for i in range(len(a)-1):
      count = 0
      for j in range(i+1,len(a)-2):
          count = count + a[i+j]
          if count > k:
              min_len = len(a[i:j])
              empty.append(min_len)
  print(min(empty))



  b = ['{','}','{']
 
  open = 0
  close = 0
 
  for i in range(len(b)):
      if b[i] == '{':
          open = open + 1
      else:
          close = close + 1
  print(open,close)

  arr = [1, 2, 3, 2, 6, 7]
 
  count = 0
  second_element = arr[1]
  for i in range(len(arr)):
      for j in range(i+1):
          s_max = max(arr[j],0)
  print(s_max)


  nums = [3, 2, 1, 0, 4]
  reachable = 0
 
  for i in range(len(nums)):
      print(nums[i] + 1)
      if reachable < i:
          print('False')
      else:
          reachable = max(reachable, nums[i] + i)
  print('True')


  s = ["act","god"]
 
  s = sorted(s)
  print(s)



 Minimum Platfrom to accure trains


  a = [900, 940, 950, 1100, 1500, 1800]
  d = [910, 1200, 1120, 1130, 1900, 2000]


S = [1,3,0,5,8,5]
F = [2,4,6,7,9,9]


  2 > 3 = 1
  4 > 0  = 1
  6 > 5  = 0
 
 
 
 


  S = [75250, 50074, 43659, 8931, 11273,
  27545, 50879, 77924]
  F =  [112960, 114515, 81825, 93424, 54316,
  35533, 73383, 160252]
  count = 0
 
  for i in range(len(F)-1):
      if S[i] < F[i+1]:
          count = count + 1
      else:
          continue
  print(count)



  SWAP NUMBER TO THEIR INDEX
  s = "aiohn"
 
  s = list(s)
 
  indices = [3, 1, 4, 2, 0]
 
  res = []
  for i in indices:
      res.append(0)
 
  for i in range(len(indices)):
      res[indices[i]] = s[i]
 
  print( ''.join(res))

  s = 'abc'
 
 
  for i in range(len(s)):
      for j in range(i+1,len(s)):
          print(s[i],s[j])


  n = 30
 
  v = []
  sum_sq = 0
  while n not in v:
      v.append(n)
      if n == 1:
          print(True)
      sum_sq = 0
      while (n != 0):
          a = n % 10
          n = n // 10
          sum_sq = sum_sq +  a ** 2
      n = sum_sq
      print(sum_sq)

 
  import collections
 
  s = "aaaa"
 
  ans = 0
  for v in collections.Counter(s).values():
      ans += v // 2 * 2
      if ans % 2 == 0 and v % 2 == 1:
          ans += 1
  print(ans)



  import collections
  s = 'aba'
 
  ans = 0
  for v in collections.Counter(s).values():
      ans = ans + v // 2 * 2
      if ans % 2 == 0 and v % 2 == 1:
          ans += 1
  print(ans)

 
  import collections
 
  s = "abccccdd"
  ans = 0
  for v in collections.Counter(s).itervalues():
      ans += v / 2 * 2
      if ans % 2 == 0 and v % 2 == 1:
          ans += 1




 
  s = 'abacccccccc'
  print(len(s))
  a = s[::-1]
  for i in range(len(s)):
      for j in range(i+1,len(s)+1):
          if s[i:j] == (s[i:j][::-1]):
              if i < len(str(s[i:j])):
                  print(i)


 
 
 
  str1 = 'aab'
  str2 = 'xyz'
 
  dict = {}
 
  for i in str1:
      if i not in dict:
          dict[i] =1
      else:
          dict[i] = dict[i] + 1
  print(dict)
 
 
  dict2 = {}
 
  for i in str2:
      if i not in dict2:
          dict2[i] =1
      else:
          dict2[i] = dict2[i] + 1
  print(dict2)


 
 
  if dict2 == dict:
      print("yes")
  print("no")

  nums = [4,3,2,7,8,2,3,1]
  dict = {}
  for i in nums:
      if i not in dict:
          dict[i] = 1
      else:
          dict[i] = dict[i] + 1
  print(dict.items())
 
 
  for x,y in dict.items():
      print(dict[x] == 2)



  Longest palindromic substring n2 time
 
  class Solution:
      def longestPalindrome(self, s: str) -> str:
          longest = ''
          for i in range(len(s)):
              for j in range(len(s),i,-1):
                  if s[i:j] == s[i:j][::-1]:
                      if len(longest) < len(s[i:j]):
                          longest = s[i:j]
          return longest




  nums = [1,2,3]
  target = 1
 
  last = len(nums)
 
 
  new_list = []
 
  if len(nums) == 1 and nums[0] == target:
      print [0, 0]
 
  if target not in nums:
      print (-1, -1)
 
  for i in range(len(nums)):
      if nums[i] == target:
          new_list.append(i)
          break
 
  count = 0
  for i in reversed(range(len(nums))):
      if nums[i] != target:
          count = count + 1
  new_list.append(count)
 
  print(new_list)





  Maximize sum after K negations


 
  a =[1, 2, -3, 4, 5]
 
  K = 1
 
  a = sorted(a)
  print(a)
 
  count = 0
  for i in range(len(a)):
      if a[i] < 0:
          count = count + 1
          a[i] = a[i] * -1
  print(count)
 
  print(K-count)
  print((sorted(a)))
  print(sum(sorted(a)))




  Minimum number of jumps

 
  arr=[1 ,3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
  count = 0
  m = 1
  for i in range(len(arr)):
      m = i + 1
      for j in range(m):
          m = max(arr[j],m)
          print(m)




  2d matrix
 
  a = [ [1,1,1,0,0,0],
     [1,0,0,0,0,0],
     [1,1,1,1,0,0],
     [1,1,0,0,0,0]
  ]
 
  count = 0
  for i in a:
      for j in i:
          if j == 1:
              count = count + 1
  print(count)



strs = ["flower","flow","flight"]

  s = ""
  idx = 0
  if len(strs) == 0:
      print(s)
  mlen = len(min(strs))
  while True and idx < mlen:
      for l in strs:
          if strs[0][idx] != l[idx]:
              print(s)
      s += strs[0][idx]
      idx += 1
  print s




  a = [['a','b','c'],['a','g','m']]
 
  for i in a:
      if i == 'g':
          print("yes")
      else:
          print("no")

  s = "CCCbAbbBbbC"
    ans = "abc"
  new = []
  for i in range(len(s)):
      if s[i].upper() in s[i+1:] and s[i].upper() == s[i+1].upper():
          pass
      else:
          new.append(s[i])
  a = ' '.join(new)
  print(a)


  count = 0
  s = "()))(("
  s = sorted(s)
  last = len(s) -1
  for i in range(len(s)):
      if s[i] == "(" and s[last] == ')':
          i = i + 1
          last = last - 1
      else:
          count = count + 1
  print(count)




  for i in range(len(s)-1):
      if s[i] == '(' and s[i+1] == ')':
          pass
      else:
          close = close + 1
  print(close)


  S =  "()))(("
  stack = []
  result = 0
  for parenthesis in S:
      if parenthesis == '(':
          stack.append(parenthesis)
      elif stack:
          stack.pop()
      else:
          result +=

  print(result + len(stack))



  txt = "BAABAAABABC"
  pattern = "ABC"
  print(txt[0:len(pattern)])
 
 
  for i in range(len(txt)):
      if txt[i:len(pattern)] == pattern:
          print(i)
      else:
          print("nothing")



s = "acb"
t = "ahbgdc"


  count = 0
  for i in range(len(t)):
      if t[i] in s:
          count = count + 1
  print(count)
  print(len(s))
  pointer_s = 0
  pointer_t = 0
 
  while pointer_s < len(s) and pointer_t <len(t):
 
      if s[pointer_s] == t[pointer_t]:
          pointer_s += 1
 
      pointer_t+=1
 
  print(pointer_s)




  flowerbed = [1,0,0,0,0,0,1]
  n = 2
  for i in range(len(flowerbed)):
      if i + n == 1:
          print(True)
      else:
          print(False)


  intervals = [[1, 4], [3, 6], [2, 8]]
  intervals = sorted(intervals)
  print(intervals)
  intervals.sort(key = lambda x: (x[0], -x[1]))
 
  n = len(intervals)
  end = 0
  for interval in intervals:
  	if interval[1] > end:
  		end = interval[1]
  	else:
  		n -= 1
  print(n)

  intervals.sort(key = lambda intervals: intervals[1])
 
  print(intervals)
 
  print("tttt")
  count = 0
  a = sorted(intervals)
  for i in range(len(a)):
      for j in range(len(a[i])):
          print(a[i][j])



  intervals = [[1,3],[2,6],[8,10],[15,18]]

  intervals = [2,7,4,1,8,1]
  intervals = sorted(intervals)
 
  it = intervals[::-1]
  print(it)
  for i in range(len(it)):
      for j in range(i+1,len(it)):
 

  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
  target = 3
  for i in matrix:
      for j in i:
          if j == target:
              print("yes")


  s = 'abcdefghhgfedecba'
  dict = {}
 
  for i in s:
      if i not in dict:
          dict[i] = 1
      else:
          dict[i] = dict[i] + 1
 
  print(dict.items())
 
  a = []
  for key, value in dict.items():
      a.append(dict[key])
  print(a)
  b = []
  for i in range(len(a)-1):
      b.append(a[i])(Transact-SQL
  s = set(list(b))
  print(s)
 

 
  nums = [1, 2, 3]
  result = [[]]
  for n in nums:
      l = len(result)
      for k in range(l):
          result.append(result[k] + [n])
 
  print(result)


  nums = [1, 2, 3]
  k = 2
 
  low = 0
  high = len(nums) - 1
 
 
  while(low<high):
      mid = high + low // 2
      if nums[mid] == k:
          return k
      elif arr[mid] < k:
          mid = mid - 1
      else:



  a = [-2, -3, 4, -1, -2, 1, 5, -3]
 
  current_sum = 0
  over_all_sum = 0
 
  for i in range(len(a)):
      if current_sum >= 0:
          current_sum = current_sum + a[i]
      else:
          current_sum = a[i]
 
      if current_sum > over_all_sum:
          over_all_sum = current_sum
  print (over_all_sum)

 
  arr = [10, 90, 49, 2, 1, 5, 23]
      if arr:
          arr[i], arr[i + 1] = arr[i + 1], arr[i]
          print(arr[i], arr[i + 1])
          print(arr[0])


 
  nums = [0,0,0,0,0,0]
  target = 0
 
  result = []
 
 
  for i in range(len(nums)-2):
  	first = i
  	second = i + 1
  	last = len(nums) - 1
  	second_last = len(nums) - 2
 
  	if (nums[first] + nums[second] + nums[last] + nums[second_last]) == target:
  		result.append([nums[first],nums[second],nums[last] ,nums[second_last]])
  		first = i + 1
  		second = second + 1
  		last = last -1
  		second_last = second_last - 1
  	elif nums[first] + nums[second] + nums[last] + nums[second_last] > target:
  		last  =  last - 1
  		second = second - 1
  	elif nums[first] + nums[second] + nums[last] + nums[second_last] < target:
  		first = first + 1
  		second = second + 1
  print(result)




  intervals = [[0,30],[5,10],[15,20]]
  intervals.sort()


  last_end = -1

  for start,end in intervals:
  	if last_end <= start:
  		last_end = end
  	else:
  		print("Flase")
  print(True)


a = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

b = 'fcrxzwscanmligyxyvym'




  my_dict = {}
  for i in s:
  	if i in my_dict:
  		my_dict[i] = my_dict[i] + 1
  	else:
  		my_dict[i] = 1

  new_set = []
  ref = []
  for key,values in my_dict.items():
  	new_set.append(values)
  my_set = set(new_set)
  print(my_set)



  S = "aaaabbaa"
  leng = ''
  for i in range(len(S)):
  	for j in range(i+1,len(S)+1):
  		if S[i:j] == S[i:j][::-1]:
  			if len(S[i:j]) > len(leng):
  				leng = S[i:j]
  print(leng)


  Print all Subsequences of a string.


  class Solution:
      def subsets(self, nums: List[int]) -> List[List[int]]:
        
          result = [[]]
          for n in nums:
              l = len(result)
              for k in range(l):
                  result.append(result[k]+[n])
                
          return result
        


  A = ["amazon","apple","facebook","google","leetcode"]
  B = ["e","o"]

  B = ''.join(B)


  for i in A:
  	for j in i:
  		print(j)
  nums = [1,5,5,11]

  print(nums[0:])

  nums = sorted(nums)
        
  total_count = 0
  for i in range(len(nums)):
  	total_count = nums[i] + total_count
  	if total_count == sum(nums[i+1:]):
  		print("Yes")
  	else:
  		print("no")



  n = [1,2,3,4,5,6,7]
  k = 3


  nums = [1,2,3,4,5,6,7]
  k = 3

  print(nums[len(nums) - k:] + nums[:len(nums) - k])

  new = []
  for i in range(12):
  	new.append(str(i))
  print(sorted(new))



  a = [-2,1,-3,4,-1,2,1,-5,4]

  current_sum = 0
  over_all_sum = 0

  for i in range(len(a)):
      if current_sum >= 0:
          current_sum = current_sum + a[i]
      else:
          current_sum = a[i]

      if current_sum > over_all_sum:
          over_all_sum = current_sum
  print (over_all_sum)



  s = 'aba'
  small = 0
  for i in range(len(s),-1):
  	for j in range(len(s) - i, -1,-1):
  		if s[j:j+i]



  nums = [1,1,1]
  k = 2
  d={0:1}
  s=0
  count=0
  for i in nums:
  	s=s+i
	
  	if (s-k) in d:
  		count+=d[s-k]        
		
		
  	if s in d:
  		d[s]+=1
  	else:
  		d[s]=1
  print(count)



  nums = [5,7,7,8,8,10]
  k = 8 

  ans_list = []


  for i in range(len(nums)):
  	first = i
  	last = len(nums) - 1
  	if nums[first] == k or nums[last] == k:
  		ans_list.append(first,last)





  flowerbed = [1,0,0,0,1]
  n = 1


  for i in range(len(flowerbed)-1):
  	if flowerbed[i] == 1 and flowerbed[i+1] == 0:
  		print("yes")
  	else:
  		print("no")


  digits = [1,2,3]

  strs=[str(i) for i in digits]
  print(strs)
  num = int("".join(strs))
  fnum = num + 1
  print(num)

  new = []

  last = digits[-1]
  last = last + 1
  a  = digits[:len(digits) - 1]
  ans = a  + [last]
  print(ans)


  n = 10 

  n =

  numbers = [7,2,11,14]
  target = 9

  for i in range(len(numbers)):
  	fi = i
  	la  = len(numbers) - 1

  	if numbers[fi] + numbers[la] == target:
  		print (fi + 1,la + 1)
  	elif numbers[fi] + numbers[la] > target:
  		la = la - 1
  	elif numbers[fi] + numbers[la] < target:
  		fi = fi + 1


s = "abccccdd"

  leng = ""
  for i in range(len(s), -1, -1):
  	for j in range(len(s) - i, -1, -1):
  		if s[j:j+i] == s[j:j+i][::-1]:
  			print(s[j:j+i])

  nums = [4,1,-1,2,-1,2,3]
  k = 2
    nums = [-1,-1] 
    k = 1
    nums = [-1,-1]
    k = 1
  new = []
  dict = {}
  new = []
  for i in nums:
  	if i not in dict:
  		dict[i] = 1
  	else:
  		dict[i] = dict[i] + 1
          return list(sorted(dict, key=dict.get, reverse=True))[0:k]


  mountain_arr = [1,2,3,4,5,3,1]
  target = 3


  ans = []
  if target in mountain_arr:
  	ans.append(mountain_arr.index(target))
  print (ans)

  arr = [0,2,1,0]
  count = 0
  mini = arr[0]
  for i in xrange(len(arr)):
  	print(i)



  numbers = [4,3,2,3,5,2,1]
  numbers.sort()
  target = max(numbers)
  k = 4

  count = 0
  new = []
  for i in range(len(numbers)):
  	fi = i
  	la  = len(numbers) - 1
  	while(fi<la):
  		if numbers[fi] + numbers[la] == target:
  			new.append((fi,la))
  			count = count + 1
  			la = la - 1
  			fi = fi + 1
  		elif numbers[fi] + numbers[la] > target:
  			la = la - 1
  		elif numbers[fi] + numbers[la] < target:
  			fi = fi + 1
  print(count)



  s  = "bb"
  wordDict = ["a","b","bbb","bbbb"]

  print(len(wordDict))
  count = 0
  for i in range(len(wordDict)):
  	if wordDict[i] in s:
  		s = s.replace(wordDict[i],'')
  	if i == s:
  		print("yes")
  	else:
  		print("no")

  nums = [-1,0,1,2,-1,-4]
  nums = sorted(nums)
  for i in range(len(nums)-2):
  	start = i
  	end = len(nums) - 1
  	second = i + 1
	
  	new = []
  	while(start<end):
  		if (nums[start] + nums[second] + nums[end]) == 0:
  			new.append((nums[start] , nums[second] , nums[end]))
  			start = start + 1
  			end = end - 1
  			second = second + 1
  		elif nums[start]+nums[start]+nums[start] >= 0:
  				end = end - 1
  		elif nums[start]+nums[start]+nums[start] <= 0:
  				start = start + 1
  	print(new)

  nums = [3,4,-1,1]
  new = []
  for i in nums:
  	if i > 0:
  		new.append(i)

  newone = max(new)
  mini = []
  for i in range(1,newone+1):
      if i not in nums:
          mini.append(i)
      else:
          mini.append(newone+1)
  print(min(mini))

         
  nums = [1,1,1,2,2,3]                
  dict = {}

  for i in nums:
  	if i not in dict:
  		dict[i] = 1
  	else:
  		dict[i] = dict[i] + 1
		
  ans = []
  for key,values in dict.items():
      if values <= 2:
          ans.append(key)
  print(len(ans))



  a = [1 ,3 ,4 ,7 ,10, 10, 8, 10]
  x  = 11
  for i in range(len(a)):
      for j in range(i+1,len(a)):
          ans = ans + a[i:j]
      print(ans)
    
            

  

  n = -3 
  x = 2 

  ans = str(x) * n
  ans1 = ans

  result = 1 
  for i in list(ans1):
      result = result * int(i)
  print(result)



    
  s = 'ab((cd))' 
  
  s2 = 'ab)cd' 
  opening = 0
  closing = 0
  for i in s:
      if i  == "(":
          opening = opening +  1
      elif i == ')':
          closing = closing + 1

  if opening == closing:
      print("balanced")
  print("not balanced")
        


s = ')('

set = ('(')

dict = {'(' : ')'}

stack = []



  if s[0] == ')':
      print("not balanced")

  for i in s:
      if i in set:
          stack.append(i)
      elif i == ')' and i == dict[stack[-1]] and len(stack) != 0 :
          stack.pop()
  if len(stack) == 0:
      print("balanced")
  print("not balaced")


  nums1 = [4,1,2]
  nums2 = [1,3,4,2]
  nums1 = [2,4]
  nums2 = [1,2,3,4]
  new = []
  for i in range(len(nums1)):
        print(nums2[nums1[i] - 1])
      if nums1[i] <= (nums2[nums1[i] - 1]):
      	new.append(-1)  
      else:
          new.append(nums2[nums1[i] - 1])
    print(new)
    

  nums = [1,2,3,4,3]
 
  nums[len(nums)-1] 

  ans = []
  global_max = 0
  dict = {}
  for i in range(len(nums)):
  	for j in range(i+1,len(nums)):
  		if nums[i] < nums[j]:
  			dict[nums[i]] = nums[j]
  			ans.append(nums[j])
  		elif nums[i] < nums[j]:
    			ans.append(-1)
  		else:
  			if j == (len(nums) - 1) and nums[j] in dict:
  				ans.append(dict[nums[j]])
   
  		break

  print(ans)


  ans_list = []
  a = [9,9,9,9,9,9,9]
  b = [9,9,9,9]
  s = [str(i) for i in a]
  res1 = int("".join(s))
  q = [str(i) for i in b]
  res2= int("".join(q))
  final_ans = str(res1 + res2)[::-1]
  final_ans2 = list(final_ans)
  final_ans3 = ''.join(final_ans2)
  n = final_ans3.replace('',',')
    
    
  board = ["XOX", "O O", "XOX"]
  for i in range(len(board)-1):
      for j in range(i):
          if board[j][i] != board[j][i+1]:
              print("false")
          else:
              print("no")        
        
        
        
  s = "hello a "

  q = s[::-1].lstrip()
  print(q)
  count = 0
  for i in range(len(q)):
      if q[i] != ' ':
      	count = count + 1
      break
  print(count)
        
        
  arr = [1,2,3,10,4,2,3,5] 

  dict = {}

  for i in arr:
      dict[i] = i
  print(dict)
    
    


  arr = [5,4,3,2,1]  
  arr = [1,2,3]
  arr = [1,2,3,10,4,2,3,5]
  count = 0
  for i in range(len(arr)):
    
  Longest consecutive subsequence  
  sorted_a = sorted(arr)
  count = 0
  ans = 0
  higest_number = max(arr)
  result = 0
  a = 0
  for i in range(max(sorted_a) + 1):
  	if i in sorted_a:
  		count = count + 1
  		result = max(result,count)
  	else:
  		if i not in sorted_a:
  			count = 0
  return result

  b = sorted([2 ,6 ,3 ,4 ,7 ,2, 10, 3, 2, 1])
  print(b)
  k = 5
  first = arr[0]
  last = len(b) -1 

  for i in range(len(b)):
      if ((b[last] - k) - (b[i] + k)) >= 0:
          print((b[last] - k), (b[i] + k))
          break
      else:
          last = last - 1
          i = i + 1

  nums = [2,3,1,1,4]    
  max_reach = 0
  count = 0      
  for i in range(len(nums)):
      for j in range(nums[i]):
          max_reach = max(max_reach,nums[j])
          print(max_reach)
          count = count + 1
          if max_reach < len(nums):
              break
  print(count)



  Merge Intervals 



  result = []
  intervals.sort()
  for interval in intervals:
  	if result == [] or result[-1][1] < interval[0]:
  		result.append(interval)
  	else:
  		result[-1][1] = max(result[-1][1],interval[1])
  return result


  a = [1, 2, 3, -4, -1, 4]
  a = sorted(a)
  last = len(a) -1
  for i in range(len(a)):
      a[i], a[last] = a[last], a[i]
      i = i +qqq 2
  print(a)



  nums = [1,2,3,4,3] * 2
  stack = [] 
  result = [-1 for _ in nums]   giving me all zero's value 
  for i in range(len(nums)-1):
      if nums[i] < nums[i+1]:
          result[i+1] = nums[i+1]
  print(result)
    

  next greater element 
  arr = [11,13,21,3]

  for i in range(0, len(arr)):
  	next = -1
  	for j in range(i+1, len(arr)):
  		if arr[i] < arr[j]:
  			next = arr[j]
  			break
		
  	print(str(arr[i]) + " -- " + str(next))


  sliding window 
  arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
  k = 4
  max_sum = 0
  for i in range(len(arr) - k+ 1):
      current_sum = 0 
      for j in range(k):
          current_sum = current_sum + arr[i+j]
      max_sum = max(max_sum,current_sum)
    
  print(max_sum)
        



  a = [5,4,3,2,1]
  a  = [1,2,3,10,0,7,8,9]
  a = [1,2,3,10,4,2,3,5]
  count = 0
  for i in range(len(a)):
      for j in range(i+1,len(a)):
          if a[i] > a[j]:
              count = count + 1
              break
  print(count)

		
  
  s = 'pwwkew'
  ans_string = []
  max_arr = 0
  for i in s:
      if i in ans_string:
          ans_string = ans_string[ans_string.index(i) + 1:]
      else:
          ans_string.append(i)
      max_arr = max(max_arr,len(ans_string))
  print(max_arr)

    
    
      
  a  = [10,20,30,40,50]
  l = 0
  high = len(a) -1 
  x = 10
  while l <= high :
      mid =  (high - l)  // 2
      if a[mid] == x:
          print(a[mid])
      elif a[mid] > x:
          l = mid + 1
      elif a[mid] < x:
          high = mid -1 
  print("nothing foun")
     
    

   
    
    
        
  list1 = [2, 3, 4]
  list1.append(5)
  list1.extend([7, 15, 16])
  list1.append([10, 11, 12])


  print(list1)



    [2,3,4,5],[7,15,16,[10,11,12]]
    def add(list_):
    	for i in range(len(list_):
    		list_[i] = 2 * list_[i]
    	print(list_) 6, 8,4,8

    list1 = [3, 4, 2, 4] 
    add(list1)
    print(list1) 




  string = "abccdccd"
  a = 'aaaa'
  rev_string =  string[::-1]
  count = 0
  for i in range(0,len(string)): 
  	for j in range(0,len(string)):
       	if string[i:j] == string[j:i]:
           	count = count + 1
  print(count)


  nums = [8,1,2,2,3]

  sor_nums = sorted(nums)

  new = []
  for i in range(len(nums)):
      new.append(sor_nums.index(nums[i]))
  print(new)
     
  class node:
      def __init__(self,data):
          self.data = data
          self.next = None;
 
  class linked_list:
      def __init__(self):
          self.start = None
 
      def insert(self,value):
          newnode = node(value)
          if (self.start == None):
              self.start = newnode
          else:
              temp = self.start
              while temp.next != None:
                  temp = temp.next
              temp.next = newnode
      def view_list(self):
          if self.start == None:
              print("list is empty")
         	else:
              temp = self.start
              while temp:
                  print(temp.data)
                  temp = temp.next
 
 
  mylist = linked_list()
  mylist.insert(10)
  mylist.insert(20)
  mylist.insert(30)
  mylist.insert(40)
  mylist.view_list()


 
  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  for i in range(len(matrix)):
      for j in range(len(matrix) - 1, -1, -1):
          print(matrix[j][i])

  nums = [1,2,3]
  output = set([[]])
 
  for i in nums:
      output += [out + [i] for out in output]
  print output
  nums = [2,3,-2,4]
  max_pro, min_pro = nums[0], nums[0]
 
  908u9 454  bvc vfor i in range(1, len(nums)):
  bh=-    current = nums[i]
 
      temp_max = max(current, max_pro * current, current * min_pro)
 
      min_pro = min(current, max_pro * current, current * min_pro)
 
      max_pro = temp_max
 
      result = max(result, max_pro)
 
  print(result)

  arr = [1,2]
  ans = sorted(arr)
  anns = 0
  ans2 = len(ans)
  i = 0
  for i in range(len(arr)):
      while i < len(arr):
          if ans2[i + 1] == ans2[i]+1:
              count = count + 1
          result = max(count,result)
          i += 1
      count = 0


  class Solution:
      def deepestLeavesSum(self, root: TreeNode) -> int:
 
          d = {}
 
          def dfs(root, depth):
 
              if (not root):
                  return depth
 
              dfs(root.left, depth + 1)
              dfs(root.right, depth + 1)
 
              if depth not in d:
                  d[depth] = []
                  d[depth].append(root.val)
              else:
                  d[depth].append(root.val)
 
          dfs(root, 0)
            print(d)
   
   
    new  = Solution()
    print(new.deepestLeavesSum)
 
    Python program to find the maximum for
    each and every contiguous subarray of
    size k
 
    Method to find the maximum for each
    and every contiguous subarray of s
    of size k
  def printMax(arr, n, k):
  	max = 0
 
  	for i in range(n - k + 1):
  		max = arr[i]
  		for j in range(1, k):
  			if arr[i + j] > max:
  				max = arr[i + j]
  		print(str(max) + " ")
 
    Driver method
  if __name__=="__main__":
  	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  	n = len(arr)
  	k = 3
  	printMax(arr, n, k)
 
    This code is contributed by Shiv Shankar



  nums = [1,3,-1]
 
  k = 3
 
  count = 0
  a = []
  i = 0
  ans = []
  while i < len(nums):
  	a.append(nums[i])
  	count = count + 1
 
  	if count == k or i == len(nums):
  		maxim = max(a)
  		ans.append(maxim)
  		count = 0
  	a = []
  	i += 1
    print(ans)
 
  nums = [9,11]
  k = 3
  new = []
  for i in range(len(nums) - k + 1):
  	curr_max = nums[i]
  	for j in range(k) :
  		if nums[i + j] > curr_max:
  			curr_max = nums[i + j]
  	new.append(curr_max)
  print(new)

A binary search based program to find
the only missing number in a sorted
in a sorted array of distinct elements
within limited range
def search(ar, size):
  	a = 0
  	b = size - 1
  	mid = 0
  	while b > a + 1:
  		mid = (a + b) // 2
  		if (ar[a] - a) != (ar[mid] - mid):
  			b = mid
  		elif (ar[b] - b) != (ar[mid] - mid):
  			a = mid
  	return ar[a] + 1
 
  Driver Code

n = len(a)

print(search(a, n))


  mat = [[1,2,3],
                [4,5,6],
                [7,8,9]]
 
  row=len(mat)
  sum=0
  k=len(mat[0])-1
  for i in range(row):
      sum+=mat[i][i]
      sum+=mat[i][k] if k!=i else 0
      k-=1
  print( sum )

  nums = [1,1,1,1,2,2,2,2]
  k = 2
  n = sorted(nums)
 
  left = 0
  right = len(nums) - 2
 
  li = [n[len(n)-1]]
 
  while left < right:
      if n[left] or n[right] == k:
          li.append((n[left]))
      elif n[left] + n[right] == n[len(nums) - 1]:
          li.append((n[left], n[right]))
          left += 1
          right -= 1
      else:
          return False
      if len(li) == k:
          print li
  print li










 
 
  imoort json
  import request
 
 
 
 
 
  https://jsonplaceholder.typicode.com/posts
 
 
 
  https://jsonplaceholder.typicode.com/posts/1/comments
 
 
 
 
 
 
  ans += a[i



a = [1,1,3,4,3,5,6,6]

left = 0
right = len(a) -1

while left < right:
    if a[right] != 2 and a[left] == 2:
        a[right],a[left] = a[right],a[left]
left += 1
right -= 1
print a


temperatures = [73,74,75,71,69,72,76,73]

stack = [0]
final = [0]*len(temperatures)
for i in range(1,len(temperatures)):
    while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
        j = stack.pop()
        final[j] = i-j
    stack.append(i)
print( final)



select name from tableone left join table2 on table.id = table2.id




















