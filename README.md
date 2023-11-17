# ML-Geo-Pixel-Poppers
This is a github repository for our final project for ML Geo Au 23

ESS 469/569: ML Geo Au 23
Project lead: [Nicole Aikin, naikin@uw.edu, nicole-m-aikin]:
Project helpers: [Jon Lindenmann, linjon06@uw.edu, linjon]: [Aiman Shamsul,aiman188@uw.edu, AimanHS]
Project GitHub: nicole-m-aikin/ML-Geo-Pixel-Poppers


## Making changes to the repo:

In order to make changes to this repository:
### Do steps 1-4 once:
1. Fork the Repository:
        Go to https://github.com/nicole-m-aikin/ML-Geo-Pixel-Poppers
        Click the "Fork" button in the upper right corner of the repository's page. This creates a copy (fork) of the repository under your GitHub account.

2. Clone Your Fork:

   On your forked repository page, click the green "Code" button and copy the repository URL.
   Open a terminal on your local machine and navigate to the directory where you want to clone the repository.

   Run the following command, replacing <repository_url> with the URL you copied:

            git clone <repository_url>

3. Add a Remote:

  Navigate into the cloned repository with:

            cd <repository_name>

4. Add the original repository as a remote, so you can pull changes from it:

           git remote add upstream <original_repository_url>



6. Create a Branch:

    Create a new branch for your changes:

       git checkout -b feature_branch

7. Make Changes:

    Make the necessary changes to the code using your preferred editor.

8. Commit Changes:

    Stage the changes:

        git add .

9. Commit the changes:

        git commit -m "Your commit message here"

10. Push Changes to Your Fork:

    Push your changes to your fork on GitHub:

        git push origin feature_branch

    Create a Pull Request:
        Visit your fork URL on GitHub and switch to the branch you just pushed.
        Click the "New Pull Request" button.
        Provide a title and description for your pull request, then click "Create Pull Request."
       This sends your committed changes to the owner for review. 

    Collaboration and Merging:
        The owner of the original repository will review your changes.
        If everything looks good, they can merge your changes into the main branch. (Nicole, Aiman, and Jon all have owner access and can          accept pull requests.)

Remember to keep your fork updated with the original repository by periodically fetching changes from the upstream and merging them into your local and forked branches.
        When opening your fork:
                git pull https://github.com/nicole-m-aikin/ML-Geo-Pixel-Poppers
