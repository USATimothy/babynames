# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:23:17 2016

@author: Tim Fleck

This takes a .csv file of popular baby names, with names and frequencies for
boys and girls in 4 separate columns.
It then groups similar-sounding names together, and produces a dataframe of the
most popular name groups, or name variants.
"""

import tkinter
from tkinter import filedialog
import pandas
"""
This defines how a name is reduced to a phonetic skeleton.  It is arbitrary;
different reductions would result in different sets of "similar-sounding" names.
"""
def reducename(Name):
    table={'a':'e','d':'t','f':'b','h':'*','i':'e','p':'b','q':'k','v':'b','w':'*','x':'ks','y':'e','z':'s'}
    name=Name.lower()
    #convert to list, to enable slicing and item assignment
    n=len(name)       
    letters=list(name)
    #replace c with k or s
    for i in range(n):
        if letters[i]=='c':
            if i+1==n or not letters[i+1] in ['e','i','y']:
                letters[i]='k'
            else:
                letters[i]='s'
     #replace g with k or j
        if letters[i]=='g':
            if i+1==n or not letters[i+1] in ['e','i','y']:
                letters[i]='k'
            else:
                letters[i]='j'
    #Replace a,i,y with e. Replace many consonants
    for i in range(n):
        if letters[i] in table:
            letters[i]=table[letters[i]]
    #Remove doubles
    for i in range(n):
        if i>0 and letters[i]==letters[i-1]:
            letters[i]='!'
    reduced=''
    #Convert back to string
    for char in letters:
        if char !='!' and char!='*':
            reduced+=char
    #Remove last vowel
    if reduced[-1]=='e':
        return reduced[:-1]
    return reduced

#Open a file dialog so the user can choose the file.
tk=tkinter.Tk()
filepath=filedialog.askopenfilename()
tk.destroy()
#import the file, with assigned column names.
namedf=pandas.read_csv(filepath,header=None,names=['boyname','boyfreq','girlname','girlfreq'])
#Rank the names from 1 to 1000 instead of from 0 to 999.
namedf.index+=1

#separate into boys' and girls' names
boynames=namedf[['boyname','boyfreq']]
girlnames=namedf[['girlname','girlfreq']]

#add a column of reduced names
boynames.loc[:,'reduced']='abc'
for i in range(1,1001):
    boynames.loc[i,'reduced']=reducename(boynames.loc[i,'boyname'])
girlnames.loc[:,'reduced']='abc'
for i in range(1,1001):
    girlnames.loc[i,'reduced']=reducename(girlnames.loc[i,'girlname'])

#Group by the reduced names
bgroup=boynames.groupby('reduced')
#Aggregate each group by the total frequency of all its names
bsummary=bgroup.agg(lambda g: ('/'.join(g.boyname),sum(g.boyfreq)))
#rank the name groups by total frequency
branked=bsummary.sort_values(by='boyfreq',ascending=False)

#Group, aggregate and rank the girls' names.
ggroup=girlnames.groupby('reduced')
gsummary=ggroup.agg(lambda g: ('/'.join(g.girlname),sum(g.girlfreq)))
granked=gsummary.sort_values(by='girlfreq',ascending=False)