9.1
Uncommon words
A sentence is a string of single-space separated words where each word consists only of lowercase letters.A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
 Constraints:
1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
Note:
Use dictionary to solve the problem
For example:
Input	Result
this apple is sweet
this apple is sour

	sweet sour

a=input().split()
b=input().split()
c1,c2,l={},{},[]
for i in a:
    c1[i]=c1.get(i,0)+1
for j in b:
    c2[j]=c2.get(j,0)+1
for w,c in c1.items():
    if(c==1 and w not in b):
        l.append(w)
for w,c in c2.items():
    if(c==1 and w not in a):
        l.append(w)
print(*l)

 

 
 
9.2
Sort Dictionary by Values Summation
Give a dictionary with value lists, sort the keys by summation of values in value list.
 Input : test_dict = {‘Gfg’ : [6, 7, 4], ‘best’ : [7, 6, 5]}
Output : {‘Gfg’: 17, ‘best’: 18}
Explanation : Sorted by sum, and replaced.
 Input : test_dict = {‘Gfg’ : [8,8], ‘best’ : [5,5]}
Output : {‘best’: 10, ‘Gfg’: 16}
Explanation : Sorted by sum, and replaced.
 Sample Input:
2
Gfg 6 7 4
Best 7 6 5
Sample Output
Gfg 17
Best 18
 


For example:
Input
Result
2
Gfg 6 7 4
Best 7 6 5	Gfg 17
Best 18


a=int(input())
d={}
for i in range(a):
    b=input()
    b=b.partition(" ")
    d[b[0]]=b[-1].split(" ")
n=list(d.values())
k=list(d.keys())
for i in range(len(n)):
    s=0
    for j in range(len(n[i])):
        s+=int(n[i][j])
    d.update({k[i]:s})
l=list(d.items())
if(l[0][1]<l[1][1]):
    for k,v in d.items():
        print(k,v)
else:
    j=1
    for k,v in d.items():
        if(j==1):
            k1,v1=k,v
            j+=1
        else:
            print(k,v)
    print(k1,v1)
 

 
 

9.3
Winner of Election
Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.
Examples: 
Input :  votes[] = {"john", "johnny", "jackie",
                    "johnny", "john", "jackie",
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny",
                    "john"};
Output : John
We have four Candidates with name as 'John', 'Johnny', 'jamie', 'jackie'. The candidates John and Johny get maximum votes. Since John is alphabetically smaller, we print it. Use dictionary to solve the above problem
 
Sample Input:
10
John
John
Johny
Jamie
Jamie
Johny
Jack
Johny
Johny
Jackie
 
Sample Output:
Johny
 

For example:
Input	Result
10
John
John
Johny
Jamie
Jamie
Johny
Jack
Johny
Johny
Jackie	Johny

n = int(input())

votes = {}

for _ in range(n):
    candidate = input()
    votes[candidate] = votes.get(candidate, 0) + 1

max_votes = max(votes.values())
max_candidates = [candidate for candidate, count in votes.items() if count == max_votes]

print(min(max_candidates))

 

 
 
9.4
Student Record

Create a student dictionary  for n students with the student name as key and their test mark assignment mark and lab mark as values. Do the following computations and display the result.
1.Identify the student with the  highest average score
2.Identify the student who as the highest Assignment marks
3.Identify the student with the Lowest lab marks
4.Identify the student with the lowest average score
Note:
If more than one student has the same score display all the student names

Sample input:
4
James 67 89 56
Lalith 89 45 45
Ram 89 89 89
Sita 70 70 70
Sample Output:
Ram
James Ram
Lalith
Lalith

n = int(input())
max_average = float('-inf')
min_average = float('inf')
max_assignment = float('-inf')
min_lab = float('inf')
max_average_students = []
max_assignment_students = []
min_lab_students = []
min_average_students = []
for _ in range(n):
    name, test, assignment, lab = input().split()
    test = int(test)
    assignment = int(assignment)
    lab = int(lab)
    average = (test + assignment + lab) / 3
    if average > max_average:
        max_average = average
        max_average_students = [name]
    elif average == max_average:
        max_average_students.append(name)
    if average < min_average:
        min_average = average
        min_average_students = [name]
    elif average == min_average:
        min_average_students.append(name)
    if assignment > max_assignment:
        max_assignment = assignment
        max_assignment_students = [name]
    elif assignment == max_assignment:
        max_assignment_students.append(name)
    if lab < min_lab:
        min_lab = lab
        min_lab_students = [name]
    elif lab == min_lab:
        min_lab_students.append(name)
print(*sorted(max_average_students))
print(*sorted(max_assignment_students))
print(*sorted(min_lab_students))
print(*sorted(min_average_students))


 

 

 

9.5
Scramble Score

In the game of Scrabble™, each letter has points associated with it. The total score of a word is the sum of the scores of its letters. More common letters are worth fewer points while less common letters are worth more points. 
Write a program that computes and displays the Scrabble™ score for a word. Create a dictionary that maps from letters to point values. Then use the dictionary to compute the score.
A Scrabble™ board includes some squares that multiply the value of a letter or the value of an entire word. We will ignore these squares in this exercise.

The points associated with each letter are shown below:
Points Letters
1 A, E, I, L, N, O, R, S, T and U
2 D and G
3 B, C, M and P
4 F, H, V, W and Y
5 K
8 J and X
10 Q and Z

Sample Input
REC
Sample Output
REC is worth 5 points.

letter_scores = {
    'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}
word = input().upper()
score = sum(letter_scores.get(letter, 0) for letter in word)
print(word,"is worth",score,"points.")

 
 
