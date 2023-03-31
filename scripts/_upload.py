import pysftp
import os
import time
from contextlib import contextmanager
import argparse
import builtins

parser = argparse.ArgumentParser(description='argparse')
parser.add_argument('--server', type=str, default='1.1.1.1')
parser.add_argument('--username', type=str, default='root')
args = parser.parse_args()
server = args.server
username = args.username

dry_run = False
noise = True
key = '~/.ssh/id_rsa'

def print_flush(*objects, sep='', end='\n', flush=False):
    return builtins.print(objects, sep, end, flush=True)

builtins.__print__ = print_flush

def log(f):
    def print_log(*args, **kwargs):
        params = ', '.join([str(arg) for arg in args])

        if noise:

            print(f'Running : {f.__name__}({params})')
        # print(f'{f.__code__.co_varnames}')
       
        ret = f(*args, **kwargs)
        # print(f'\t {ret}')

        if noise:
            print(f'Completed : {f.__name__}({params})')

        return ret

    return print_log

@contextmanager
def connection():
    with pysftp.Connection(server, username=username, private_key=key) as sftp:
        yield sftp
         
def upload(sftp_dir, local_dir):
    with connection() as sftp:
        with sftp.cd(sftp_dir):
            # sftp.put_r() proper implementation
            _upload_r(sftp, sftp_dir, local_dir)

    print(f'uploaded {sftp_dir} from {local_dir}')

def _upload_r(sftp, sftp_dir, local_dir, preserve_mtime=True):
    for file in os.listdir(local_dir):
        # rpath = os.path.join(local_dir, file.filename)
        if _is_directory(local_dir + file):
            if not _is_existing(sftp, f'{sftp_dir}{file}'):                
                if dry_run:
                    print(f'mkdir {file}')
                else:
                    sftp.mkdir(f'{sftp_dir}{file}')

            _upload_r(sftp, f'{sftp_dir}{file}/', f'{local_dir}{file}/')
        else:
            # if not _is_existing(sftp, f'{sftp_dir}{file}'):
            if dry_run:
                print(f'replacing {local_dir}{file} with {sftp_dir}{file}')
            else:
                sftp.put(f'{local_dir}{file}', f'{sftp_dir}{file}')

def _delete_r(sftp, sftp_dir):
    for file in sftp.listdir(sftp_dir):
        rpath = os.path.join(sftp_dir, file)
        if _is_directory(rpath):
            print(f'{rpath} is dir')
            _delete_r(sftp, rpath)
        else:
            rpath = os.path.join(sftp_dir, file)
            print(f'{rpath} is file')
            if dry_run:
                pass
                # print(f'removing {rpath}')
            else:
                sftp.remove(rpath)
    if dry_run:
        print(f'removing {sftp_dir}')
    else:
        sftp.rmdir(sftp_dir)
    # filesInRemoteArtifacts = sftp.listdir(path=remoteArtifactPath)
    # for file in filesInRemoteArtifacts:
    #     sftp.remove(os.path.join(remoteArtifactPath, file))

def _is_directory(filepath):
    return os.path.isdir(filepath)

def _is_existing(sftp, filename):
    return sftp.exists(filename)

def _run_os(cmd):
    if dry_run:
        print(cmd)
    else:
        os.system(cmd)

# todo: refactor to fix logging
def log_f(before, after, f, **args):
    print(f'==========\n{before}')
    # f(..args)
    print(f'==========\n{after}')

# 1)
@log
def setup_node(local_dir):
    # clear_local_dir(f'{local_dir}/node_modules')

    _run_os('npm install')
    # _run_os('npm ci')

# 2)
@log
def clear_local_dir(compiled_dir):
    cmd_rm = 'rm -rf'

    _run_os(f'{cmd_rm} {compiled_dir}')

# 3)
@log
def build_site(web_dir):
    cmd_build = f'cd {web_dir}; npm run build'

    # run_os('rm package-lock.json')
    _run_os(cmd_build)

# 4)
@log
def copy_static_dirs(base_dir):
    cmd_cp = f'cp -a {base_dir}/static {base_dir}/web/_site'

    _run_os(cmd_cp)

# 5)
@log
def clear_ftp_dir(sftp_dir):
    with connection() as sftp:
        with sftp.cd(sftp_dir):
            # sftp.put_r() proper implementation
            _delete_r(sftp, sftp_dir)

# 6) 
@log
def upload_web(compiled_dir):
    ftp_dir = '/var/www/spencers.dev/'
    upload(ftp_dir, f'{compiled_dir}/')

# 7)
@log
def upload_nginx(base_dir):
    # nginx
    ftp_dir = '/etc/nginx/sites-available/'
    nginx_dir = f'{base_dir}/nginx'
    upload(ftp_dir, f'{nginx_dir}/')

def upload_spencersdev(base_dir):
    web_dir = f'{base_dir}/web'
    web_compiled_dir = f'{web_dir}/_site'

    # 1)
    setup_node(web_dir)

    # 2)
    print(f'Clear local compiled site')
    clear_local_dir(web_compiled_dir)
    print(f'Delete compiled directory : {web_compiled_dir}')

    # 3)
    print(f'Building site')
    build_site(web_dir)

    # 4)
    print(f'Copy static dirs')
    copy_static_dirs(base_dir)

    print('Building completed\n==========')

    # 5)
    ftp_dir = '/var/www/spencers.dev/html/'
    clear_ftp_dir(ftp_dir)
    print(f'Cleared directory {ftp_dir}')

    # 6)
    print('==========\nUploading local website to server')
    upload_web(web_compiled_dir)
    print('==========\nUploading completed')

    # 7)
    upload_nginx(base_dir)
    print('==========\nUploaded NGINX configs')
    # service nginx reload
    # systemctl restart nginx
    # sudo ln -s /etc/nginx/sites-available/spencers.dev /etc/nginx/sites-enabled/

# 8)
@log
def upload_puzzle_dirs(base_dir):
    # ftp_dir = '/var/www/puzzle.spencers.dev/'
    ftp_dir = '/var/www/'
    compiled_dir = f'{base_dir}/web_puzzle/puzzle.spencers.dev'
    upload(ftp_dir, f'{compiled_dir}/')

    # ftp_dir = '/var/www/api.spencers.dev/'
    ftp_dir = '/var/www/'
    compiled_dir = f'{base_dir}/web_puzzle/api.spencers.dev'
    upload(ftp_dir, f'{compiled_dir}/')

# 9)
@log
def upload_puzzle_nginx(base_dir):
    # nginx
    ftp_dir = '/etc/nginx/sites-available/'
    nginx_dir = f'{base_dir}/web_puzzle/nginx/puzzle'
    upload(ftp_dir, f'{nginx_dir}/')

# 10)
@log
def upload_webhook_dirs():
    ftp_dir = '/var/www/'
    # ftp_dir = '/var/www/webhooks/'
    compiled_dir = f'{base_dir}/webhooks'
    upload(ftp_dir, f'{compiled_dir}/')

    # supervisord service
    ftp_dir = '/etc/systemd/system/'
    compiled_dir = f'{base_dir}/supervisord'
    upload(ftp_dir, f'{compiled_dir}/')

def upload_puzzle(base_dir):
    # 8)
    print('==========\nUploading puzzle')
    upload_puzzle_dirs(base_dir)
    print('==========\nUploaded puzzle')
    # print('todo : run node servers pm2, logging, metrics')

    # 9)
    upload_puzzle_nginx(base_dir)
    # sudo ln -s /etc/nginx/sites-available/api.spencers.dev /etc/nginx/sites-enabled/
    # sudo ln -s /etc/nginx/sites-available/puzzle.spencers.dev /etc/nginx/sites-enabled/
    # sudo ln -s /etc/nginx/sites-available/test.spencers.dev /etc/nginx/sites-enabled/

    # 10)
    # upload_webhook_dirs()

    # print('==========\nUploaded WEBHOOK DIRS')

    # 10)
    # run servers
    # print('todo : reload nginx, pm2 services, systemd crons')
    # # this should also create a LAST_MODIFIED file with date
    return

if __name__ == '__main__':
    cwd = os.getcwd()

    os.chdir(f'{cwd}/../')
    base_dir = os.getcwd()

    upload_spencersdev(base_dir);
    upload_puzzle(base_dir);