# GIT

### 수정 중

working tree: 아직 버전관리가 되지 않은 추가/수정 파일

staging area: working tree 에서 사용자가 지정한 파일들을 저장되는 공간(git add)

repository: staging area 에서 지정된 파일들을 저장하여 만들어진 하나의 버전(git commit)

git checkout: HEAD를 조작하는 명령어. HEAD를 브랜치가 아닌 커밋을 가리키도록 할 수 있는데 이러한 상태를 detached라고 한다.
git reset --soft --mixed --hard

git revert: 기존 커밋을 수정/삭제하지 않고 버전을 되돌림. 버전이 2 스텝 이상일 경우 역순으로 차례대로 revert 하지 않으면 conflict 가 발생할 수 있다.

git merge: 서로 다른 두개의 브랜치를 하나의 브랜치로 결합함.
    

#### 3 way merge

- 같은 조상을 가진 두 개의 서로 다른 브랜치가 존재할 때, 서로 중복되는 데이터 영역을 한쪽 혹은 양쪽 브랜치에서 수정하는 경우가 발생할 수 있다.  
두 개의 브랜치를 merge할 때 같은 데이터 영역을 수정한 경우에는 CONFLICT가 발생한다. 하지만 한쪽의 브랜치에서만 데이터를 수정한다면 어떻게 될까?   
 이럴 경우 git은 중복데이터 영역을 BASE와 대조하여 BASE와는 다른 즉, 수정된 branch의 데이터를 merge함으로써 conflict 를 방지하는 자동화 기능을 제공한다.

- before

| branch A | branch B | 2-way-merge |
|:---:|:---:|:---:|
A | A | A 
H | B | CONFLICT
C | T | CONFLICT
H | T | CONFLICT

- after

| branch A | base | branch B | 2-way-merge | 3-way-merge |
|:---:|:---:|:---:|:---:|:---:|
A | A | A | A | A |
H | B | B | CONFLICT | H |
C | C | T | CONFLICT | T |
H | D | T | CONFLICT | CONFLICT |

from [생활코딩](https://opentutorials.org/course/3840/23684)

git stash
git workflow, git flow
git cherrypik



git fsck --unreachable | grep commit | cut -d ' ' -f3 | xargs git log --merges --no-walk --grep=WIP