### git branch manage & merge

git branch

git branch [name] : make new branch

git switch [name] : switching

git merge [name] : merge to main stream

git log --oneline --graph : showing commit log with graph

**rebase 는 최대한 활용하지 말자**

rebase can come out with similar outcome like merge but it is totally different way. 
Rebase destroy the history of works and merge them into one stream
So avoid using rebase espacially when you are coop with other people

**requests**

import requests
data = requests.get(url)
