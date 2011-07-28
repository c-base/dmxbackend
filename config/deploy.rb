set :application, "dmxacl"
set :repository, "git://dev.c-base.org/libart-dmxcontrol/django-backend.git"                          # Your HTTP server, Apache/etc

set :scm, 'git'
# Or: `accurev`, `bzr`, `cvs`, `darcs`, `git`, `mercurial`, `perforce`, `subversion` or `none`

role :web, "baseos.cbrp3.c-base.org"                          # Your HTTP server, Apache/etc

set :use_sudo, false
set :home_path, "/srv/capistranos/dmxacl"
set :deploy_to, "/srv/capistranos/dmxacl"
set :user, "deployer"

namespace :deploy do
    task :restart do
    end
    task :finalize_update do
    end
end


# if you're still using the script/reaper helper you will need
# these http://github.com/rails/irs_process_scripts

# If you are using Passenger mod_rails uncomment this:
# namespace :deploy do
#   task :start do ; end
#   task :stop do ; end
#   task :restart, :roles => :app, :except => { :no_release => true } do
#     run "#{try_sudo} touch #{File.join(current_path,'tmp','restart.txt')}"
#   end
# end
