# babynames
Grouping baby names phonetically and ranking

While thinking of names for our first child, my wife and I were curious what the most 
popular boy and girl names were.  I noticed that the officical lists did not group name variants like Sofia and Sophia together.  I wondered what the most popular names would be if all variants were listed together.
I wrote this python code to group the names phonetically.  For example, Christine and Krtistin would be together.  Of course, it only works on given names--Elizabeth and Betsy are in different groups, as are John and Jack.  And etymology is ignored--Ivan and Juan are not considered the same, despite both deriving from the Hebrew equivalent of John.  English phonetic rules are notoriously tricky, not to mention some of the most names aren't English or anglicized.
Think of these as groups of similar sounding given names, not as groups of name variants.  The latter would require some additional web scraping.  Maybe I'll add that soon!

I have the code that makes the groups, as well as a couple csvs to pull from.  I did not include code for extracting csvs from web page; too many locations are hard-coded for that to be worth sharing.
