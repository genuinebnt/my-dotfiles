git clone --bare https://github.com/genuinebnt/my-dotfiles.git $HOME/.cfg
function dotconfig {
   /usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME $@
}
mkdir -p ~/.config-backup
dotconfig checkout
if [ $? = 0 ]; then
  echo "Checked out config.";
  else
    echo "Backing up pre-existing dot files.";
    dotconfig checkout 2>&1 | egrep "\s+\." | awk {'print $1'} | xargs -I{} mv {} ~/.config-backup/{}
fi;
dotconfig checkout
dotconfig config status.showUntrackedFiles no
