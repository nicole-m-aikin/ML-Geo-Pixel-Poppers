# ML-Geo-Pixel-Poppers
This is a github repository for our final project for ML Geo Au 23

ESS 469/569: ML Geo Au 23
Project lead: **Nicole Aikin**, [naikin@uw.edu], [nicole-m-aikin](https://github.com/nicole-m-aikin)
Project helpers: **Jonathan Lindenmann**, [linjon06@uw.edu], [Jon's GitHub](https://github.com/UW-ESS-DS/MLGeo-23_linjon), **Aiman Shamsul**, [aiman188@uw.edu], [AimanHS](https://github.com/AimanHS)
Project GitHub: [nicole-m-aikin/ML-Geo-Pixel-Poppers](https://github.com/nicole-m-aikin/ML-Geo-Pixel-Poppers/)


## Making changes to the repo (the proper way):
**Note:** ***Always*** make sure your local repo is up to date with the original remote repo (**pull** with `git pull https://github.com/nicole-m-aikin/ML-Geo-Pixel-Poppers/`) before you **push** your local changes to the original remote repo. Otherwise you may overwrite other changes.

**Note** that **remote** repositories are somewhere like GitHub, while **local** repositories are on your system. When you **clone** a **remote** repository, you now have a **local** repository that contains a _reference_, or link, to the **remote** repository, allowing you send and receive changes. Please refer to the **Git Cheatsheet** in this repo for a list of useful git commands. 

In order to work on this repository, you want:
- to have your own copy to work on (**forking** and **cloning**)
- to work on individual tasks separately (creating a **branch**)
- to keep your copy up to date with any changes (link the original repo to your copy as a **remote** repo, letting you **fetch** changes)
- to save all your changes in your copy (**committing** changes within a **branch**, then **merging** the **branch** back in with your **main** local branch, and **pushing** to your remote fork.)
- to send your new version back to this original repository, so that all the changes you made can be added and any conflicting changes can be resolved. (**pushing** or **pull requests**)


Here are the steps to do this (do 1-3 once only):

1. Create your own **fork** of this repository.
   This creates a copy of this repository within your own GitHub, so that you can work on it in peace.
   Navigate to the 'fork' button on this repo's GitHub page and choose to fork to your own GitHub.

2. **Clone** your fork to your computer.
   This creates a copy of your forked repository on your computer, so that you can work on it offline and in your local system.
   In a **command line interface** (CLI) on your computer, navigate to the folder you want to have the cloned repo in using the `pwd` and `cd` commands, then enter:

   `git clone yourForkedRepoURL`
  
3. Add [_this_](https://github.com/nicole-m-aikin/ML-Geo-Pixel-Poppers/) (the original) repository as a **remote** repository named `upstream`. 
   Your local repo is a clone of your remote fork, so it is connected to it. The remote fork is called `origin` in your local repo (you can use `origin` in place of the URL). This step creates this connection, naming the original repo `upsteam` so that you can refer to it that way and pull updates from it. This isn't necessary, but here's why you should do it: If you are working on your local repo making changes, but the original repo is updated, you'll want to get your fork/clone up to date with the original before you keep working on it. Rather than having to remember or find the URL of     the original remote repo, you can just **fetch** or **pull** from `upstream`. (Something I learned from ChatGPT, a standard practice to make your    workflow more intuitive.) 

   All you have to do is navigate into the cloned repository with `cd` and `pwd` commands, then:

           git remote add upstream https://github.com/nicole-m-aikin/ML-Geo-Pixel-Poppers

   Now, when someone has update the original repository, you can just
   - `git fetch upstream` to see the changes made, then `merge` them into your local repo yourself
   - `git pull upstream` to `fetch` and `merge` in one fell swoop (make sure you're not getting rid of your own work when doing this).


Now, when you want to change or add something to the project, you can do so locally, then push your changes when you're done with ease. 

4. Create a **branch**.
   Your repository has one **main branch**. If you are making tiny edits, you might not need a new branch, but if you are working on a bigger task or fixing an issue, you should create a **branch** in your local repo for that task, which you can then **merge** back into your local repo. That way, you are keeping each task you are working on isolated until it is complete. 

       `git checkout -b descriptiveNameOfBranch`

Your local repo now has multiple branches. To see your branches and which one is active, use:

        `git branch`

and to switch to a branch, use
    
        `git checkout nameOfTheBranch`

When you are finished working on a branch, you can 'close' it by merging it with the main branch. To do so you need to switch to the main branch, and then merge the extra branch. Or, you can push just the branch you worked on back to the fork.

5. Make and **commit** changes in a branch.
   Any changes you make need to be committed to 'take effect' in git's version history. Git has a **staging area** so that you don't have to lose track of all the changes you are making. This is the idea:

   You edit a file, then **stage** it when finished.
   You create another file, and **stage** it when finished.
   etc.
   You review all your **staged** changes.
   You **commit** those changes to the active branch.
   You are ***done!*** making changes. 

To stage a change, use `git add filepath` for a single file or `git add .` to add all changes.
You can see all your unstaged and staged changes in different ways with a bunch of cool commands; check the cheatsheet.
   
When you are ready, **commit** your changes with a summary message:
   
        `git commit -m "Your commit message here"`

Now your local repository is officially changed. You'll want to **push** these changes back to your fork, and then **push** them back to the original repo.

6. Push Changes to Your Fork:
    You've made a bunch of changes and now you want to send them back to the original repository. 

    Push your changes to your fork on GitHub in any number of ways:

push your entire local repo:
        git push origin
push a specific branch:
        git push origin branchName
push the main branch:
        git push origin main
push the active branch:
        git push origin HEAD


To get the changes from your fork to the original repo, you can **push** them if you are an owner of the original repo (although you should still keep your fork synced up instead of skipping the push to fork), or you can create **pull request** if you are not an owner:

To create a pull request, go to your fork on GitHub and click on the branch you want to push (unless you are pushing the whole repo.)
Click "New Pull Request".
Add a title and description.
The owner can now review the changes you submitted. Nicole, Aiman, and Jon all have owner access and can accept pull requests.

Remember to keep your fork updated with the original repository by periodically fetching changes from the `upstream` and merging them into your local and forked branches.
